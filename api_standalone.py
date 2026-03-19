import os
import uvicorn
from fastapi import FastAPI
from zep_memory import get_memory

app = FastAPI()
memory = get_memory()

@app.get("/api/status")
async def status():
    return {"pid": os.getpid(), "status": "ok", "memory": "active"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
