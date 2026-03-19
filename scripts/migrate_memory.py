import asyncio
import os
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from zep_memory import get_memory
from core.local_memory import get_local_memory

async def migrate():
    print("🔄 Iniciando migración de Zep a SQLite...")
    
    # 1. Instancias
    zep = get_memory()
    local = get_local_memory()
    
    # 2. Recuperar historial de Zep (limit=500 para traer todo)
    try:
        print("📚 Recuperando mensajes de Zep Cloud...")
        messages = await zep.get_recent_messages(limit=500)
        
        if not messages:
            print("⚠️ No se encontraron mensajes en Zep.")
            return

        print(f"✅ Se encontraron {len(messages)} mensajes.")
        
        # 3. Insertar en SQLite
        for msg in messages:
            role = msg.get("role", "unknown")
            content = msg.get("content", "")
            metadata = msg.get("metadata", {})
            
            print(f"   📥 Migrando: [{role}] {content[:50]}...")
            await local.add_message(role, content, metadata)
            
        print(f"🎉 Migración completada con éxito. {len(messages)} mensajes transferidos.")
        
    except Exception as e:
        print(f"❌ Error durante la migración: {e}")

if __name__ == "__main__":
    asyncio.run(migrate())
