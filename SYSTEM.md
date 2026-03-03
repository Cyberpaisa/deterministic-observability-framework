# SYSTEM — Fuente de Verdad del Kernel
# CrewAI Pro — Cyber Paisa / Enigma Group
# Actualizado: 2026-03-02

## Identidad
- **Operador:** Juan Carlos Quiceno — Cyber Paisa
- **Org:** Enigma Group — Holding Web3
- **Idioma:** Español por defecto

## Arquitectura
- 8 agentes especializados (SOUL.md cada uno)
- 11 crews (flujos de trabajo)
- 7 proveedores LLM gratuitos (Smart Router + Zhipu GLM)
- 6 categorías de tools (16 tools nativos)
- 4 MCP servers (filesystem, web_search, fetch, memory)
- A2A Server (8 skills expuestas via JSON-RPC)
- Memoria persistente (ChromaDB + HuggingFace embeddings)
- Pre-research programático (5 búsquedas antes del crew)
- Retry automático con backoff para rate limits
- Process: Sequential (sin planning)

## Reglas Constitucionales
1. Datos verificables con fuentes URL
2. JSON estructurado para output Pydantic
3. Español por defecto, inglés si el contexto lo requiere
4. Si no hay datos, decir "no encontré información verificable"
5. Conciso, sin relleno ni repetición
6. Citar fuentes con URL

## Proveedores LLM (7 activos, distribución balanceada)
| Rol | Primario | Proveedor | Fallback 1 | Fallback 2 |
|-----|----------|-----------|------------|------------|
| Code Architect | Kimi K2.5 | NVIDIA | Kimi K2 (Groq) | — |
| Research Analyst | Llama 3.3 70B | Groq | DeepSeek V3.2 (NV) | — |
| MVP Strategist | Qwen3.5-397B | NVIDIA | GLM-4.7 (Zhipu) | Groq |
| Data Engineer | GPT-OSS 120B | Cerebras | GPT-OSS 120B (Groq) | — |
| Organizer | Qwen3-32B | Groq | GLM-4.7 (Zhipu) | — |
| QA Reviewer | GPT-OSS 120B | Cerebras | Llama 3.3 (Groq) | — |
| Verifier | GPT-OSS 120B | Cerebras | Llama 3.3 (Groq) | — |
| Narrative | GLM-4.7-Flash | Zhipu | DeepSeek V3.2 (NV) | Groq |

## Búsqueda Web (fallback chain)
| Motor | Tipo | Límite |
|-------|------|--------|
| Serper | Google Search | 2,500/mes |
| Tavily | AI Search | 1,000/mes |
| DuckDuckGo | Fallback | Sin key, ilimitado* |

## Pipeline Research Crew (8/10 score)
```
Pre-research (5 búsquedas programáticas)
  ↓ datos reales inyectados
t1: Researcher (Groq) → analiza datos
t2: Strategist v1 (Cerebras) → plan MVP
t3: QA (Groq) → verifica con búsquedas
t4: Verifier (Cerebras) → score + feedback
t5: Strategist v2 (Cerebras) → plan FINAL mejorado
```

## Rate Limits (free tier)
| Provider | Límite | Agentes | Runs/día estimado |
|----------|--------|---------|-------------------|
| Groq | 12K TPM | 2 (Researcher, Organizer) | ~150 |
| Cerebras | 1M tok/día | 3 (Data, QA, Verifier) | ~200+ |
| NVIDIA | 1000 credits | 2 (Architect, Strategist) | ~500+ |
| Zhipu | Generoso | Fallback (Strategy, Narrative) | ~300+ |
| Serper | 2,500/mes | pre-research | ~80/día |
| Tavily | 1,000/mes | backup search | ~33/día |

## Crews Disponibles
1. research — Investigar y validar idea (pre-research + 5 agentes)
2. code-review — Revisar código
3. data — Analizar Excel/CSV
4. database — Analizar base de datos
5. full-mvp — MVP completo (6 agentes)
6. enigma-audit — Auditar agente/scanner/DB
7. grant-hunt — Buscar grants
8. content — Generar contenido
9. daily-ops — Rutina matutina
10. weekly-report — Reporte semanal
11. build — Generar proyecto con código real

## Memoria (ChromaDB + HuggingFace)
- **Short-term:** contexto dentro de la ejecución del crew
- **Long-term:** persiste aprendizajes entre ejecuciones
- **Entity memory:** recuerda entidades mencionadas
- **Embedder:** HuggingFace sentence-transformers/all-MiniLM-L6-v2 (384 dims)
- **Storage:** ChromaDB local (~/.cache/chroma/)

## MCP (Model Context Protocol) — 4 Servers
| Server | Comando | Uso |
|--------|---------|-----|
| Filesystem | @modelcontextprotocol/server-filesystem | Leer/escribir en output/ |
| Web Search | @pskill9/web-search | Google scraping, sin API key |
| Fetch | @anthropics/mcp-server-fetch | URL → markdown |
| Memory | @anthropics/mcp-server-memory | Knowledge graph persistente |

Activar MCP por agente: `create_agent(use_mcp=True)`

## A2A (Agent-to-Agent Protocol)
- **Server:** http://localhost:8000
- **Agent Card:** /.well-known/agent-card.json
- **Skills expuestas:** research, code-review, data-analysis, build-project, grant-hunt, content, daily-ops, enigma-audit
- **Protocolo:** JSON-RPC + REST simplificado
- **Arranque:** `python main.py --mode a2a-server` o menú opción 15

Ejemplo de uso externo:
```bash
curl -X POST http://localhost:8000 \
  -H "Content-Type: application/json" \
  -d '{"skill": "research", "input": "DeFi lending protocols"}'
```

## Seguridad
- Ejecución solo en output/ o ~/proyectos/
- Blocklist: rm -rf, sudo, chmod 777, dd, shutdown
- Git: sin --force, sin reset --hard
- Binarios whitelist: npm, pip, python3, node, docker, make, etc.
- Archivos bloqueados: .env, .pem, .key
