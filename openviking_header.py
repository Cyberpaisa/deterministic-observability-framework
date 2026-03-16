# OpenViking Memory Integration (local mode, no embeddings needed)
try:
    import requests
    VIKING_URL = "http://localhost:1933"
    # Test connection
    r = requests.get(f"{VIKING_URL}/health")
    if r.status_code == 200:
        VIKING_ACTIVE = True
        print("✅ OpenViking server connected (local mode)")
    else:
        VIKING_ACTIVE = False
        print("⚠️ OpenViking server unreachable")
except Exception as e:
    VIKING_ACTIVE = False
    print(f"⚠️ OpenViking not available: {e}")

