import os
import asyncio
from datetime import datetime
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from zep_cloud import AsyncZep

# Cargar variables de entorno
load_dotenv()

class ZepMemory:
    """Maneja la memoria persistente usando Zep Cloud v3.18.0"""
    
    def __init__(self):
        api_key = os.getenv("ZEP_API_KEY")
        if not api_key:
            raise ValueError("❌ ZEP_API_KEY no encontrada en .env")
        
        # Inicializar cliente de Zep
        self.client = AsyncZep(api_key=api_key)
        
        # Configuración del agente
        self.agent_id = os.getenv("AGENT_ID", "dof_agent_1686")
        self.user_id = f"user_{self.agent_id}"
        self.thread_id = f"thread_{self.agent_id}"
        
        print(f"🔧 Zep Memory inicializado para agente: {self.agent_id}")
        print(f"📁 Thread ID: {self.thread_id}")
        print(f"👤 User ID: {self.user_id}")
    
    async def ensure_user(self) -> None:
        """Asegura que el usuario existe en Zep"""
        try:
            # Intentar obtener el usuario
            user = await self.client.user.get(self.user_id)
            print(f"✅ Usuario existente: {self.user_id}")
        except Exception:
            # Usuario no existe, lo creamos
            print(f"👤 Creando nuevo usuario: {self.user_id}")
            try:
                await self.client.user.add(
                    user_id=self.user_id,
                    email=f"{self.agent_id}@example.com"
                )
                print(f"✅ Usuario creado: {self.user_id}")
            except Exception as e:
                print(f"❌ Error creando usuario: {e}")
    
    async def ensure_thread(self) -> None:
        """Asegura que el thread existe"""
        try:
            # Intentar obtener el thread
            thread = await self.client.thread.get(self.thread_id)
            print(f"✅ Thread existente: {self.thread_id}")
        except Exception:
            # Thread no existe, lo creamos
            print(f"🔄 Creando nuevo thread: {self.thread_id}")
            try:
                await self.client.thread.create(
                    thread_id=self.thread_id,
                    user_id=self.user_id
                )
                print(f"✅ Thread creado: {self.thread_id}")
            except Exception as e:
                print(f"❌ Error creando thread: {e}")
                raise
    
    async def add_message(self, role: str, content: str, metadata: Optional[Dict] = None) -> None:
        """Añade un mensaje a la memoria usando thread"""
        try:
            # Asegurar que el thread existe
            await self.ensure_thread()
            
            # Preparar metadata
            msg_metadata = metadata or {}
            msg_metadata.update({
                "role": role,
                "timestamp": datetime.now().isoformat()
            })
            
            # Crear el mensaje
            message = {
                "role": role,
                "content": content,
                "metadata": msg_metadata
            }
            
            # Añadir mensaje al thread
            await self.client.thread.add_messages(
                thread_id=self.thread_id,
                messages=[message]
            )
            
            print(f"📝 Mensaje añadido: {role}")
            
        except Exception as e:
            print(f"❌ Error añadiendo mensaje: {e}")
            raise
    
    async def get_recent_messages(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Obtiene los mensajes recientes de la memoria"""
        try:
            # Asegurar que el thread existe
            await self.ensure_thread()
            
            # Obtener el thread completo que contiene los mensajes
            thread = await self.client.thread.get(
                self.thread_id,
                limit=limit
            )
            
            messages = []
            # Extraer mensajes del thread
            if thread and hasattr(thread, 'messages'):
                for msg in thread.messages:
                    messages.append({
                        "role": getattr(msg, 'role', 'unknown'),
                        "content": getattr(msg, 'content', ''),
                        "metadata": getattr(msg, 'metadata', {})
                    })
            
            print(f"📚 Recuperados {len(messages)} mensajes")
            return messages
            
        except Exception as e:
            print(f"❌ Error obteniendo mensajes: {e}")
            return []
    
    async def clear_memory(self) -> None:
        """Limpia la memoria del agente"""
        try:
            await self.client.thread.delete(self.thread_id)
            print(f"🗑️ Memoria limpiada para thread: {self.thread_id}")
        except Exception as e:
            print(f"❌ Error limpiando memoria: {e}")

# Singleton
_memory_instance = None

def get_memory():
    """Obtiene la instancia global de memoria"""
    global _memory_instance
    if _memory_instance is None:
        _memory_instance = ZepMemory()
    return _memory_instance

# Prueba rápida
if __name__ == "__main__":
    async def test():
        memory = ZepMemory()
        await memory.ensure_user()
        await memory.add_message("system", "Iniciando sistema DOF Agent #1686")
        msgs = await memory.get_recent_messages(5)
        print(f"\n✅ Memoria funcionando. Últimos {len(msgs)} mensajes:")
        for msg in msgs:
            print(f"  - {msg['role']}: {msg['content'][:50]}...")

    asyncio.run(test())
