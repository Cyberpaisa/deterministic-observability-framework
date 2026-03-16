# 🧠 OpenViking Context Manager — Skill para DOF Agent #1686

## 📌 Propósito
Este skill permite a DOF utilizar OpenViking como base de datos de contexto jerárquica, mejorando la memoria a largo plazo y reduciendo el consumo de tokens.

## 🔧 Requisitos
- OpenViking server corriendo (local o remoto)
- Configuración en `~/.openviking/ov.conf`
- Python con `openviking` instalado

## 📥 Instalación del Cliente
```bash
pip install openviking --upgrade

## ⚙️ Configuración Mínima (ov.conf)
```json
{
  "storage": {
    "workspace": "/path/to/openviking_workspace"
  },
  "embedding": {
    "dense": {
      "api_base": "https://api.openai.com/v1",
      "api_key": "sk-...",
      "provider": "openai",
      "dimension": 1536,
      "model": "text-embedding-3-small"
    }
  },
  "vlm": {
    "api_base": "https://api.openai.com/v1",
    "api_key": "sk-...",
    "provider": "openai",
    "model": "gpt-4"
  }
}EOF

