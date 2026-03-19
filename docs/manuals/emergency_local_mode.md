# Manual de Emergencia: Modo Local Soberano (Air-gap)

En caso de fallo masivo de APIs externas (Anthropic/OpenAI) o pérdida de internet:

1. **Iniciar Ollama**: `ollama run llama3:70b`
2. **Configurar Enigma**: Editar `.env` y establecer `OFFLINE_MODE=True`.
3. **Punto de Conmutación**: El motor de ruteo (`core/llm_router.py`) detectará el error y redirigirá todas las peticiones a `localhost:11434`.
4. **Conservación de Contexto**: Los logs locales de `AGENT_JOURNAL.md` servirán como memoria primaria.

*Soberanía Determinística activada.*
