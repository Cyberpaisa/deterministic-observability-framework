import os
from dotenv import load_dotenv
from zep_cloud import AsyncZep
import asyncio

load_dotenv()

async def debug_zep():
    api_key = os.getenv("ZEP_API_KEY")
    client = AsyncZep(api_key=api_key)
    
    print("=" * 50)
    print("DEBUG DE ZEP CLOUD v3.18.0")
    print("=" * 50)
    
    # Ver todos los métodos disponibles
    print("\n📋 MÉTODOS DEL CLIENTE:")
    for method in dir(client):
        if not method.startswith('_'):
            print(f"  - {method}")
    
    # Ver si hay algún atributo relacionado con sesiones
    print("\n🔍 BUSCANDO 'session':")
    if hasattr(client, 'session'):
        print("  ✅ ¡Tiene atributo 'session'!")
        print(f"  Métodos de session: {dir(client.session)}")
    else:
        print("  ❌ No tiene atributo 'session'")
    
    # Ver otros posibles nombres
    posibles = ['memory', 'messages', 'conversation', 'chat', 'thread']
    for posible in posibles:
        if hasattr(client, posible):
            print(f"  ✅ Encontrado '{posible}'")
    
    print("\n" + "=" * 50)

asyncio.run(debug_zep())
