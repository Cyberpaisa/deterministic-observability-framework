import asyncio
from zep_memory import get_memory

class TuAgente:
    def __init__(self):
        self.memory = get_memory()
        print("🤖 Agente inicializado")
    
    async def procesar_mensaje(self, mensaje_usuario):
        # Guardar mensaje del usuario
        await self.memory.add_message("user", mensaje_usuario)
        print(f"📝 Mensaje de usuario guardado: {mensaje_usuario[:30]}...")
        
        # Obtener contexto (últimos 3 mensajes para este ejemplo)
        contexto = await self.memory.get_recent_messages(3)
        print(f"📚 Contexto recuperado: {len(contexto)} mensajes")
        
        # Mostrar el contexto
        for i, msg in enumerate(contexto, 1):
            print(f"  {i}. [{msg['role']}]: {msg['content'][:30]}...")
        
        # Generar respuesta
        respuesta = f"Procesando: {mensaje_usuario}"
        print(f"💬 Respuesta generada: {respuesta}")
        
        # Guardar respuesta
        await self.memory.add_message("assistant", respuesta)
        print(f"📝 Respuesta guardada en memoria")
        
        return respuesta
    
    async def ver_historial(self, limite=10):
        """Ver el historial completo"""
        historial = await self.memory.get_recent_messages(limite)
        print("\n" + "="*50)
        print(f"📋 HISTORIAL COMPLETO (últimos {len(historial)} mensajes)")
        print("="*50)
        for i, msg in enumerate(historial, 1):
            print(f"{i}. [{msg['role']}]: {msg['content']}")
        return historial

async def main():
    # Crear instancia del agente
    agente = TuAgente()
    
    # Simular una conversación
    await agente.procesar_mensaje("Hola, ¿qué puedes hacer?")
    print("-" * 40)
    
    await agente.procesar_mensaje("Cuéntame un chiste")
    print("-" * 40)
    
    await agente.procesar_mensaje("Gracias, eso fue divertido")
    print("-" * 40)
    
    # Ver todo el historial
    await agente.ver_historial()

if __name__ == "__main__":
    asyncio.run(main())
