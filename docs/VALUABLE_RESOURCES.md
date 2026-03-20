# VALUABLE_RESOURCES.md — DOF Knowledge Arsenal

> Repositorios, herramientas y conocimiento curado para potenciar las habilidades del DOF Agent Legion.
> Actualizado: March 19, 2026

---

## 1. AI Agents & Architecture

### AI Agents — The Definitive Guide (O'Reilly)
- **Repo**: https://github.com/Nicolepcx/ai-agents-the-definitive-guide
- **Clonado en**: `/tmp/ai-agents-the-definitive-guide/`
- **Valor**: Patrones profesionales de agentes AI — ReAct loops, Tree-of-Thought, episodic rollouts, Hard/Soft judges, hierarchical teams, MCTS, tool binding, checkpointing
- **Capítulos**: CH01-CH05 (arquitectura, memoria, seguridad, multi-agent coordination, learning)
- **Aplicación DOF**: Usado para reescribir los 14 SOULs con patrones enterprise. Base teórica para memoria persistente, autoevolución, y governance

### Overstory — Multi-Agent Orchestration Framework
- **Repo**: https://github.com/jayminwest/overstory
- **Descripción**: Convierte una sesión de coding en un equipo coordinado de agentes AI trabajando en git worktrees aislados con mensajería inter-agente y resolución de conflictos por niveles
- **Stack**: TypeScript, Bun, Commander.js, SQLite (WAL mode), tmux
- **Runtimes soportados**: Claude Code, Pi, GitHub Copilot, Gemini CLI, Sapling, Cursor, OpenCode, Codex
- **Aplicación DOF**: Patrón de orquestación multi-agente con worktrees aislados — aplicable al DOF Legion. Mensajería inter-agente y merge workflows

### LazyAgent — Terminal UI for Agent Monitoring
- **Repo**: https://github.com/illegalstudio/lazyagent
- **Descripción**: Terminal UI, macOS menu bar app, y HTTP API para monitorear agentes de coding (Claude Code, Cursor, pi, OpenCode) desde una sola interfaz
- **Stack**: Go 1.25+, bubbletea + lipgloss (TUI), Wails v3 + Svelte 5 + Tailwind 4 (menu bar), REST + SSE
- **Aplicación DOF**: Monitoreo visual de agentes desde terminal. Complemento a Mission Control para operadores que prefieren TUI

### Codeg — Enterprise Multi-Agent Coding Workspace
- **Repo**: https://github.com/xintaofei/codeg
- **Descripción**: Workspace multi-agente enterprise que unifica agentes AI locales en una app desktop con agregación de sesiones y workflows de desarrollo integrados
- **Stack**: Next.js 16, React 19, TypeScript, Tauri 2 (Rust), SeaORM + SQLite
- **Agentes soportados**: Claude Code, Codex CLI, OpenCode, Gemini CLI, OpenClaw
- **Aplicación DOF**: Referencia para desktop app del DOF. Parallel git worktree development, MCP/Skills management, local-first

### Pertmux — Unified SWE Dashboard
- **Repo**: https://github.com/rupert648/pertmux
- **Descripción**: Terminal UI que integra GitLab/GitHub merge requests con git worktrees locales, tmux sessions, y agentes de coding
- **Stack**: Rust, TUI, daemon/client via Unix sockets
- **Aplicación DOF**: Patrón de dashboard para SWE workflow. Integración de PR reviews con agent sessions

### AIlice — Autonomous General-Purpose AI Agent (IACT Architecture)
- **Repo**: https://github.com/myshell-ai/AIlice
- **Descripción**: Agente AI autónomo con modelo IACT (Interactive Agents Call Tree) — spawning dinámico de sub-agentes con comunicación bidireccional. Agentes hijos pueden preguntar al padre cuando están bloqueados
- **Stack**: Python, ZeroMQ (IPC), Flask (UI), Selenium/Playwright (browser), MCP client
- **Stars**: 1,393 | **License**: MIT
- **Features clave**: Dynamic agent spawning, bidirectional communication, self-expansion (agents build new modules at runtime), MCP wrapper (~200 líneas), context window optimization via binary search
- **LLMs soportados**: OpenAI (GPT-4/5), Anthropic (Claude), Mistral, Groq, DeepSeek, Ollama, HuggingFace local
- **Limitaciones**: ZERO governance, ZERO formal verification, ZERO audit logging, ZERO access control — ejecuta output del LLM directamente
- **Aplicación DOF**:
  - Adoptar patrón IACT para spawning dinámico de sub-agentes (DOF tiene 14 fijos)
  - Comunicación bidireccional: agente hijo escala al supervisor con pregunta específica
  - MCP wrapper pattern para consumir tools externos sin integración custom
  - **NO integrar directamente** — es governance-naive. Extraer patrones y aplicar dentro de DOF con Z3+CONSTITUTION

### ApeRAG — Graph RAG with Vector Search and AI Agents ★ IMPLEMENTAR
- **Repo**: https://github.com/apecloud/ApeRAG
- **Descripción**: Plataforma RAG production-ready combinando Graph RAG, vector search, y full-text search con agentes AI MCP-enabled
- **Stack**: FastAPI (Python), React (TypeScript), PostgreSQL, Redis, Qdrant, Elasticsearch, Neo4j, Celery, Kubernetes
- **5 tipos de índice**: Vector, full-text, graph, summary, vision
- **Features clave**: Graph RAG mejorado (LightRAG + entity normalization), agentes MCP-enabled, procesamiento multimodal, hybrid retrieval
- **Aplicación DOF**: IMPLEMENTAR como knowledge base del DOF — indexar toda la documentación, código, y logs en un knowledge graph consultable por los 14 agentes. Vector search para memoria semántica. Graph para relaciones entre módulos

---

## 2. Infrastructure & Networking

### Bore — TCP Tunnel for Exposing Local Ports
- **Repo**: https://github.com/ekzhang/bore
- **Descripción**: Tunnel TCP para exponer puertos locales a internet. Alternativa simple a ngrok
- **Aplicación DOF**: Exponer Mission Control (localhost:3000) y Ollama (localhost:11434) remotamente. Útil para demo remoto, colaboración, y acceso a dashboards desde móvil
- **Stack**: Rust

### SCUDA — GPU over IP Bridge
- **Repo**: https://github.com/kevmo314/scuda
- **Descripción**: Bridge para compartir GPU entre máquinas remotas vía IP. Permite ejecutar cargas CUDA en GPUs remotas
- **Aplicación DOF**: Acceder a GPUs remotas para entrenar modelos más grandes que qwen3:8b. Escalar capacidad de LLM sin hardware local. Fine-tuning distribuido
- **Stack**: CUDA, C++, networking

### Poltergeist — Auto-Reload Projects
- **Repo**: https://github.com/steipete/poltergeist
- **Descripción**: Recarga automáticamente cualquier proyecto cuando detecta cambios en archivos
- **Aplicación DOF**: Hot-reload para Mission Control dashboard, autonomous loops, y configuraciones de agentes. Development workflow más ágil
- **Stack**: macOS native

---

## 3. Security & OSINT

### Tookie OSINT — Username Discovery
- **Repo**: https://github.com/Alfredredbird/tookie-osint
- **Descripción**: Descubre usernames a través de múltiples websites y plataformas
- **Aplicación DOF**:
  - Sentinel Shield: Investigación de amenazas, verificación de identidades
  - Moltbook: Análisis de competencia en plataformas sociales
  - Biz Dominator: Market research y competitive intelligence
- **Uso con precaución**: Solo para OSINT defensivo y autorizado

---

## 4. Data Engineering

### dlt — Data Load Tool
- **Repo**: https://github.com/dlt-hub/dlt
- **Descripción**: Librería Python open-source que automatiza extracción, normalización y carga de datos desde múltiples fuentes a datasets estructurados
- **Stack**: Python (3.9-3.14), DuckDB, Apache 2.0
- **Features**: Schema inference, data normalization, incremental loading, schema evolution
- **Aplicación DOF**: Pipeline de datos para alimentar métricas, logs, y observabilidad. Cargar datos de JSONL a DuckDB para analytics. ETL para traces y experiment results

---

## 5. API & Development Tools

### OpenAPI DevTools — Generate OpenAPI Specs from Network Requests
- **Repo**: https://github.com/AndrewWalsh/openapi-devtools
- **Descripción**: Genera especificaciones OpenAPI automáticamente capturando requests de red
- **Aplicación DOF**:
  - Ralph Code: Documentar APIs internas del DOF automáticamente
  - Charlie UX: Generar specs para el dashboard API
  - Moltbook: Documentar la API de Moltbook para referencia
  - QA Specialist: Generar tests basados en specs capturadas

---

## 5. Key Patterns Extracted (from AI Agents Guide)

### Architecture Patterns
| Pattern | Description | DOF Usage |
|---------|-------------|-----------|
| ReAct | THOUGHT → ACTION → OBSERVATION → ANSWER | Ciclo base de todos los agentes |
| Tree-of-Thought | Generate → Evaluate → Select → Execute | Decisiones complejas (Architect, Product) |
| Episodic Rollouts | Learn from experience, retry with improvements | Autoevolución de agentes |
| Hard Judge + Soft Judge | Deterministic correctness + LLM quality check | Governance dual del DOF |
| Tool Binding | Tools bound to agent, not free-form | Security: tools explícitas por agente |
| Checkpointing | Persist state between cycles | Recovery ante fallos, JSONL persistence |
| HITL | Human-in-the-loop for critical ops | Operador aprueba acciones de alto riesgo |
| Lusser's Law | System reliability = product of component reliabilities | Métricas de confiabilidad multi-agente |

### Security Patterns (Sovereign Shield v2)
| Layer | Patterns | Confidence |
|-------|----------|------------|
| Injection | 15 patterns (ignore instructions, system override, sudo, jailbreak, DAN) | 0.95 |
| Role Hijacking | 6 patterns (act as, pretend, switch mode) | 0.90 |
| Social Engineering | 21 patterns (recruitment, philosophical extraction, goal drift, token promotion) | 0.80 |
| Link Poisoning | 5 patterns (URL shorteners, data URIs, executables) | 0.85 |
| Encoding Attacks | 2 patterns (zero-width chars, code execution) | 0.90 |
| **Semantic** | Identity erosion, goal drift, sovereignty challenge | 0.85 |

### Memory Architecture
| Level | Description | Persistence |
|-------|-------------|-------------|
| Working Memory | Current session, immediate context | Session-scoped |
| Episodic Memory | Past experiences indexed by outcome | JSONL persistent |
| Semantic Memory | Consolidated knowledge, validated patterns | Long-term persistent |

---

## 6. Strategic Intelligence

### Agentic Payments Wars (March 2026)
- **Doc completo**: `docs/AGENTIC_PAYMENTS_INTEL.md`
- **Resumen**: 7+ frameworks compitiendo por payment rails para agentes AI
- **Modelos**: x402 (Coinbase), MPP (Stripe/Tempo), ACP/UCP (OpenAI/Google), ERC-8183 (Virtuals)
- **Números**: McKinsey $3-5T by 2030 | Virtuals $3.8M agent revenue | 18K+ agents | +4,700% AI traffic YoY
- **DOF Position**: ERC-8004 (identity) + Z3 (verification) + keccak256 (attestation) → falta payment rails
- **Prioridad**: Implementar x402 + ERC-8183 en Enigma API
- **Quote clave**: "Very soon there are going to be more AI agents than humans making transactions" — Brian Armstrong

### NVIDIA Nemotron Coalition + Mistral (March 16, 2026 — GTC)
- **Qué pasó**: NVIDIA lanzó Nemotron Coalition — alianza de labs open-source (Mistral, Black Forest Labs, Perplexity) con compute de DGX Cloud
- **Objetivo**: Modelos open-source a nivel frontier, competir con GPT/Gemini/Claude cerrados
- **Mistral Small 4**: 119B params, 128 experts (MoE), 256K context window, text+images, 40% más rápido, Apache 2.0
- **Nemotron 3 Ultra**: ~500B params en horizonte, benchmarks contra Qwen-K2 y top models
- **Jensen Huang**: "El open-source gana a largo plazo" — NVIDIA gana vendiendo GPUs a todos
- **Impacto en costos**: Modelos frontier gratis → self-host → costo marginal por query cae dramáticamente
- **Aplicación DOF**:
  - DOF usa qwen3:8b local via Ollama — Mistral Small 4 (119B) sería upgrade masivo si se puede correr local
  - Nemotron models como alternativa a providers pagos (Groq, NVIDIA NIM, Cerebras)
  - Open-source frontier = soberanía total del LLM sin dependencia de APIs externas
  - MoE (128 experts) ideal para agent specialization — routing por tarea
- **Acción**: Evaluar Mistral Small 4 en Ollama cuando esté disponible como GGUF

---

## 8. Pending to Evaluate

> Repos pendientes de clonación y análisis profundo:
- [ ] `bore` — Clonar y probar tunneling para MC
- [ ] `scuda` — Evaluar para GPU remota
- [ ] `poltergeist` — Probar hot-reload para development
- [ ] `tookie-osint` — Evaluar capacidades OSINT
- [ ] `openapi-devtools` — Probar generación de specs para APIs del DOF
- [ ] `overstory` — Evaluar orquestación multi-agente con worktrees
- [ ] `lazyagent` — Probar TUI monitoring para agentes
- [ ] `codeg` — Evaluar desktop workspace para referencia
- [ ] `pertmux` — Probar SWE dashboard con tmux
- [ ] `ApeRAG` — **PRIORIDAD ALTA** — Implementar Graph RAG como módulo de Mission Control
- [ ] `dlt` — Probar ETL pipeline para JSONL → DuckDB analytics
- [x] `AIlice` — **EVALUADO** — Extraer patrones IACT, no integrar directo (zero governance)
- [ ] `Mistral Small 4` — Evaluar en Ollama cuando GGUF disponible (119B, MoE, Apache 2.0)

---

## How to Contribute

Para agregar un recurso a este documento:
1. Verificar que el repo es activo y mantenido
2. Documentar: repo URL, descripción, aplicación específica para DOF
3. Clasificar en la categoría correcta
4. Agregar a "Pending to Evaluate" si no se ha probado aún

---

*Curado por DOF Agent Legion — 14 agentes, 56 defense patterns, 207 Z3 theorems*
