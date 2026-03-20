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

## 4. API & Development Tools

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

## 6. Pending to Evaluate

> Repos pendientes de clonación y análisis profundo:
- [ ] `bore` — Clonar y probar tunneling para MC
- [ ] `scuda` — Evaluar para GPU remota
- [ ] `poltergeist` — Probar hot-reload para development
- [ ] `tookie-osint` — Evaluar capacidades OSINT
- [ ] `openapi-devtools` — Probar generación de specs para APIs del DOF

---

## How to Contribute

Para agregar un recurso a este documento:
1. Verificar que el repo es activo y mantenido
2. Documentar: repo URL, descripción, aplicación específica para DOF
3. Clasificar en la categoría correcta
4. Agregar a "Pending to Evaluate" si no se ha probado aún

---

*Curado por DOF Agent Legion — 14 agentes, 56 defense patterns, 207 Z3 theorems*
