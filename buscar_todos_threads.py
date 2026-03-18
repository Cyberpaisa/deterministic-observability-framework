import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from zep_cloud import AsyncZep

load_dotenv()

async def listar_todos_threads():
    client = AsyncZep(api_key=os.getenv("ZEP_API_KEY"))
    
    print("🔍 BUSCANDO TODOS LOS THREADS")
    print("=" * 50)
    
    try:
        # Intentar listar todos los threads
        if hasattr(client, 'thread') and hasattr(client.thread, 'list'):
            threads = await client.thread.list()
            print(f"\n📋 Threads encontrados: {len(threads)}")
            
            for thread in threads:
                print(f"\n📌 Thread ID: {thread.id}")
                print(f"   User ID: {getattr(thread, 'user_id', 'N/A')}")
                
                # Obtener mensajes de este thread
                try:
                    # Intentar diferentes métodos para obtener mensajes
                    if hasattr(client.thread, 'get_messages'):
                        mensajes = await client.thread.get_messages(thread.id, limit=5)
                    elif hasattr(client.thread, 'get'):
                        thread_data = await client.thread.get(thread.id)
                        mensajes = getattr(thread_data, 'messages', [])
                    else:
                        mensajes = []
                    
                    if mensajes:
                        print(f"   📨 Mensajes: {len(mensajes)}")
                        for i, msg in enumerate(mensajes[:3]):
                            contenido = msg.get('content', msg) if isinstance(msg, dict) else getattr(msg, 'content', '')
                            print(f"      {i+1}. {contenido[:50]}...")
                    else:
                        print(f"   📭 Sin mensajes")
                        
                except Exception as e:
                    print(f"   ⚠️ Error obteniendo mensajes: {e}")
                    
        else:
            print("❌ No se puede listar threads directamente")
            
            # Si no se puede listar, probar con IDs comunes
            ids_comunes = [
                "thread_dof_agent",
                "thread_dof_agent_1686",
                "thread_agent_1686",
                "thread_1686",
                "session_dof_agent_1686",  # formato antiguo
            ]
            
            for thread_id in ids_comunes:
                print(f"\n📌 Probando thread: {thread_id}")
                try:
                    thread = await client.thread.get(thread_id)
                    print(f"   ✅ Thread encontrado!")
                    if hasattr(thread, 'messages'):
                        print(f"   📨 Mensajes: {len(thread.messages)}")
                except:
                    print(f"   ❌ No existe")
                    
    except Exception as e:
        print(f"❌ Error general: {e}")

asyncio.run(listar_todos_threads())
