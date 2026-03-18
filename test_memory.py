import asyncio
from zep_memory import get_memory

async def test_memory():
    # Obtener instancia de memoria
    memory = get_memory()
    
    # Asegurar usuario (ya existe)
    await memory.ensure_user()
    
    # Añadir mensajes de prueba
    await memory.add_message("user", "Hola, soy un usuario")
    await memory.add_message("assistant", "Hola, soy el asistente DOF")
    await memory.add_message("user", "¿Cómo estás?")
    
    # Recuperar historial
    historial = await memory.get_recent_messages(5)
    
    print("\n" + "="*50)
    print("📋 HISTORIAL COMPLETO")
    print("="*50)
    for i, msg in enumerate(historial, 1):
        print(f"{i}. [{msg['role']}]: {msg['content']}")
    
    return historial

if __name__ == "__main__":
    asyncio.run(test_memory())
