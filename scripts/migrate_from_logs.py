import asyncio
import os
import re
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.local_memory import get_local_memory

async def migrate_from_logs():
    print("🔄 Iniciando migración desde logs locales...")
    local = get_local_memory()
    
    log_files = [
        Path("docs/conversation-log.md"),
        Path("AGENT_JOURNAL.md")
    ]
    
    total_migrated = 0
    
    for log_file in log_files:
        if not log_file.exists():
            print(f"⚠️ No se encontró {log_file}")
            continue
            
        print(f"📄 Procesando {log_file}...")
        content = log_file.read_text()
        
        # Regex para formato: [YYYY-MM-DD HH:MM:SS] USER: Content
        # O: **Human:** Content / **Enigma:** Content
        
        # 1. Buscar patrones de [Timestamp] NAME: Content
        matches = re.finditer(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] ([A-Z ]+): (.*?)(?=\s*\[\d{4}|---|\Z)", content, re.DOTALL)
        for m in matches:
            timestamp, name, text = m.groups()
            role = "user" if name.strip() in ["JUAN", "HUMAN", "USER"] else "assistant"
            await local.add_message(role, text.strip(), {"timestamp": timestamp, "source": str(log_file)})
            total_migrated += 1
            
        # 2. Buscar patrones de **Human:** / **Enigma:**
        matches_v2 = re.finditer(r"\*\*([A-Za-z ]+):\*\* (.*?)(?=\n\n|\n\*\*\w+:\*\*|###|\Z)", content, re.DOTALL)
        for m in matches_v2:
            name, text = m.groups()
            role = "user" if name.strip().lower() in ["human", "user"] else "assistant"
            # Evitar duplicados si ya se capturó por el primer regex (heurística simple)
            await local.add_message(role, text.strip(), {"source": str(log_file)})
            total_migrated += 1

        # 3. Buscar patrones de AGENT_JOURNAL específicos
        # ## Learning from user interaction (Telegram) - Timestamp
        # - User Input: ...
        matches_journal = re.finditer(r"## Learning from user interaction \(Telegram\) - (.*?)\n- User Input: (.*?)(?=\n-|\n##|\Z)", content, re.DOTALL)
        for m in matches_journal:
            timestamp, text = m.groups()
            await local.add_message("user", text.strip(), {"timestamp": timestamp, "source": "AGENT_JOURNAL.md"})
            total_migrated += 1

    print(f"🎉 Migración local completada. {total_migrated} entradas procesadas.")

if __name__ == "__main__":
    asyncio.run(migrate_from_logs())
