import os
import asyncio
from dotenv import load_dotenv
from zep_memory import ZepMemory

load_dotenv()

async def buscar_historial_antiguo():
    # Posibles IDs que pudiste haber usado
    posibles_ids = [
        "dof_agent_1686",  # el actual
        "dof_agent",        # versión simple
        "agent_1686",       # otra variante
        "1686",             # solo el número
        "agente_dof",       # otra posibilidad
        "dof_agent_1",      # con número diferente
    ]
    
    print("🔍 BUSCANDO HISTORIAL ANTIGUO")
    print("=" * 50)
    
    for agent_id in posibles_ids:
        print(f"\n📌 Probando agent_id: {agent_id}")
        print("-" * 30)
        
        try:
            # Crear memoria con este ID
            memory = ZepMemory()
            # Sobrescribir el agent_id
            memory.agent_id = agent_id
            memory.user_id = f"user_{agent_id}"
            memory.thread_id = f"thread_{agent_id}"
            
            # Intentar obtener mensajes
            mensajes = await memory.get_recent_messages(50)
            
            if mensajes:
                print(f"✅ ¡ENCONTRADOS {len(mensajes)} MENSAJES!")
                print(f"\n📅 Primer mensaje (más antiguo):")
                primero = mensajes[-1]
                print(f"   Rol: {primero['role']}")
                print(f"   Contenido: {primero['content'][:100]}...")
                if 'metadata' in primero and 'timestamp' in primero['metadata']:
                    print(f"   Fecha: {primero['metadata']['timestamp']}")
                
                print(f"\n📅 Último mensaje:")
                ultimo = mensajes[0]
                print(f"   Rol: {ultimo['role']}")
                print(f"   Contenido: {ultimo['content'][:100]}...")
                if 'metadata' in ultimo and 'timestamp' in ultimo['metadata']:
                    print(f"   Fecha: {ultimo['metadata']['timestamp']}")
                
                print(f"\n📋 Primeros 5 mensajes:")
                for i, msg in enumerate(mensajes[-5:]):  # últimos 5 (más antiguos)
                    print(f"  {i+1}. [{msg['role']}]: {msg['content'][:50]}...")
                
                # Preguntar si quiere usar este ID
                print(f"\n✨ Si este es tu historial, usa AGENT_ID={agent_id} en .env")
                break
            else:
                print(f"❌ Sin mensajes para {agent_id}")
                
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    asyncio.run(buscar_historial_antiguo())
