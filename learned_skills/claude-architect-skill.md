# 📚 SKILL: CLAUDE ARCHITECT - CONOCIMIENTO COMPLETO
## Curso completo para convertirse en Claude Architect

---

## 📋 METADATA DE LA SKILL

```yaml
nombre: "Claude Architect - Full Course Knowledge"
version: "1.0"
dominios:
  - Agentic Architecture & Orchestration (27%)
  - Tool Design & MCP Integration (18%)
  - Claude Code Configuration & Workflows (20%)
  - Prompt Engineering & Structured Output (20%)
  - Context Management & Reliability (15%)
fecha_creacion: "2026-03-17"
autor: "DOF Agent #1686"
propósito: "Conocimiento completo para convertirse en Claude Architect (production-grade applications)"
basado_en: "Claude Certified Architect Exam Guide + Anthropic Official Docs"
📘 PARTE 1: FUNDAMENTOS DE ASISTENTES DE CODIFICACIÓN
Cómo funcionan los asistentes de codificación
Cuando se le asigna una tarea a un asistente de codificación, como corregir un error basándose en un mensaje de error, este sigue un proceso similar al que seguiría un desarrollador humano:

Recopilar contexto: comprender a qué se refiere el error, qué parte del código fuente se ve afectada y qué archivos son relevantes.

Formular un plan: decidir cómo resolver el problema, como cambiar el código y ejecutar pruebas para verificar la solución.

Tomar medidas: implementa la solución actualizando archivos y ejecutando comandos.

La clave reside en que los primeros y últimos pasos requieren que el asistente interactúe con el mundo exterior: leer archivos, obtener documentación, ejecutar comandos o editar código.

El desafío del uso de herramientas
Los modelos de lenguaje por sí solos solo pueden procesar texto y devolver texto; no pueden leer archivos ni ejecutar comandos. Si le pides a un modelo de lenguaje independiente que lea un archivo, te dirá que no tiene esa capacidad.

Cómo funciona el uso de herramientas
Cuando envías una solicitud a un asistente de codificación, este agrega automáticamente instrucciones a tu mensaje que le enseñan al modelo de lenguaje cómo solicitar acciones. Por ejemplo, podría agregar un texto como: "Si quieres leer un archivo, responde con 'ReadFile: nombre del archivo'".

Flujo completo:

Preguntas: "¿Qué código está escrito en el archivo main.go?"

El asistente de codificación añade instrucciones de herramientas a tu solicitud.

El modelo de lenguaje responde: "ReadFile: main.go"

El asistente de codificación lee el archivo real y envía su contenido de vuelta al modelo.

El modelo de lenguaje proporciona una respuesta final basada en el contenido del archivo.

Por qué es importante el uso de herramientas de Claude
La serie de modelos Claude (Opus, Sonnet y Haiku) destaca especialmente por su capacidad para comprender la función de las herramientas y utilizarlas eficazmente.

Beneficios:

Afronta tareas más difíciles: Claude puede combinar diferentes herramientas para manejar trabajos complejos

Plataforma extensible: puedes añadir fácilmente nuevas herramientas a Claude Code

Mayor seguridad: Claude Code puede navegar por las bases de código sin necesidad de indexación

Conclusiones clave
Los asistentes de codificación utilizan modelos de lenguaje para completar diferentes tareas.

Los modelos de lenguaje necesitan herramientas para manejar la mayoría de las tareas de programación del mundo real.

No todos los modelos de lenguaje utilizan herramientas con el mismo nivel de habilidad.

El uso avanzado de herramientas por parte de Claude permite una mayor seguridad, personalización y longevidad.

📘 PARTE 2: INSTALACIÓN Y CONFIGURACIÓN DE CLAUDE CODE
Instalación
MacOS (Homebrew):

bash
brew install --cask claude-code
MacOS, Linux, WSL:

bash
curl -fsSL https://claude.ai/install.sh | bash
Windows CMD:

bash
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
Después de la instalación, ejecuta claude en tu terminal. La primera vez te pedirá autenticación.

Configuración adicional
AWS Bedrock: https://code.claude.com/docs/en/amazon-bedrock

Google Cloud Vertex: https://code.claude.com/docs/en/google-vertex-ai

📘 PARTE 3: GESTIÓN DE CONTEXTO
El comando /init
Cuando inicias Claude en un nuevo proyecto, ejecuta /init. Esto le dice a Claude que analice toda tu base de código y comprenda:

El propósito y la arquitectura del proyecto

Comandos importantes y archivos críticos

Patrones de codificación y estructura

Después del análisis, Claude crea un resumen y lo escribe en un archivo CLAUDE.md.

El archivo CLAUDE.md
Sirve para dos propósitos:

Guía a Claude a través de tu base de código

Te permite darle instrucciones específicas

Ubicaciones de los archivos CLAUDE.md
CLAUDE.md - Generado con /init, commiteado, compartido con el equipo

CLAUDE.local.md - Personal, no commiteado, instrucciones locales

~/.claude/CLAUDE.md - Global, para todos los proyectos

Añadir instrucciones personalizadas
Usa el comando # para entrar en "modo memoria". Ejemplo:

text
# Usa comentarios con moderación. Solo comenta código complejo.
Menciones de archivos con '@'
Cuando necesites que Claude examine archivos específicos, usa @ seguido de la ruta:

text
¿Cómo funciona el sistema de autenticación? @auth
Referenciar archivos en CLAUDE.md
text
El esquema de la base de datos está definido en @prisma/schema.prisma.
📘 PARTE 4: TÉCNICAS AVANZADAS DE CONVERSACIÓN
Uso de capturas de pantalla
Para pegar una captura de pantalla en Claude, usa Ctrl+V (no Cmd+V en macOS).

Modo Plan (Planning Mode)
Habilita con Shift + Tab dos veces. En este modo, Claude:

Leerá más archivos

Creará un plan detallado

Te mostrará lo que pretende hacer

Esperará tu aprobación

Modos Thinking
"Think" - Razonamiento básico

"Think more" - Razonamiento extendido

"Think a lot" - Razonamiento completo

"Think longer" - Razonamiento con tiempo extendido

"Ultrathink" - Capacidad máxima

Cuándo usar Plan vs Thinking
Plan Mode: Tareas que requieren comprensión amplia, implementaciones multi-paso, cambios que afectan múltiples archivos.

Thinking Mode: Problemas de lógica compleja, depuración, desafíos algorítmicos.

Interrumpir a Claude con Escape
Presiona Escape para detener a Claude a mitad de respuesta y redirigir la conversación.

Rebobinar conversaciones
Presiona Escape dos veces para ver todos los mensajes y saltar a un punto anterior.

Comandos de gestión de contexto
/compact: Resume el historial preservando información clave.
/clear: Elimina completamente el historial.

📘 PARTE 5: COMANDOS PERSONALIZADOS
Creación de comandos personalizados
Encuentra la carpeta .claude en tu proyecto

Crea un directorio commands

Crea un archivo markdown con el nombre del comando (ej: audit.md)

Comandos con argumentos
Usa $ARGUMENTS para aceptar parámetros:

markdown
# write_tests.md
Escribe pruebas completas para: $ARGUMENTS

Convenciones de prueba:
* Usa Vitest con React Testing Library
* Coloca los archivos de prueba en __tests__
* Nombra los archivos como [filename].test.ts(x)
Uso: /write_tests el archivo use-auth.ts

Beneficios
Automatización

Consistencia

Contexto

Flexibilidad

📘 PARTE 6: SERVIDORES MCP (MODEL CONTEXT PROTOCOL)
Instalación del servidor MCP de Playwright
bash
claude mcp add playwright npx @playwright/mcp@latest
Gestión de permisos
En .claude/settings.local.json:

json
{
  "permissions": {
    "allow": ["mcp__playwright"],
    "deny": []
  }
}
Ejemplo práctico
Claude puede abrir un navegador, generar componentes, analizar estilos y mejorar prompts automáticamente.

📘 PARTE 7: INTEGRACIÓN CON GITHUB
Configuración
Ejecuta /install-github-app en Claude.

GitHub Actions
Mention Action: @claude en issues/PRs

Pull Request Action: Revisión automática de PRs

Permisos en GitHub Actions
Cada herramienta MCP debe estar listada individualmente:

text
allowed_tools: "Bash(npm:*),mcp__playwright__browser_snapshot,..."
📘 PARTE 8: HOOKS
Tipos de hooks
PreToolUse hooks - Antes de llamar a una herramienta (pueden bloquear)

PostToolUse hooks - Después de llamar a una herramienta

Configuración
json
"PreToolUse": [
  {
    "matcher": "Read",
    "hooks": [
      {
        "type": "command",
        "command": "node /home/hooks/read_hook.ts"
      }
    ]
  }
]
Códigos de salida
Exit Code 0: Permitir

Exit Code 2: Bloquear (solo PreToolUse)

Aplicaciones prácticas
Formateo de código

Pruebas automáticas

Control de acceso (ej: bloquear lectura de .env)

Validación de calidad

Otros tipos de hooks
Notification

Stop

SubagentStop

PreCompact

UserPromptSubmit

SessionStart

SessionEnd

📘 PARTE 9: CLAUDE CODE SDK
Características
Ejecuta Claude Code programáticamente

Misma funcionalidad que la versión de terminal

Permisos de solo lectura por defecto

Uso básico (TypeScript)
typescript
import { query } from "@anthropic-ai/claude-code";

for await (const message of query({
  prompt: "analiza este código",
})) {
  console.log(JSON.stringify(message, null, 2));
}
Permisos de escritura
typescript
options: {
  allowedTools: ["Edit"]
}
Aplicaciones prácticas
Git hooks

Scripts de build

Generación de documentación

CI/CD pipelines

📘 DOMINIO 1: AGENTIC ARCHITECTURE & ORCHESTRATION (27%)
TASK 1.1: AGENTIC LOOPS
Ciclo de vida completo:
Enviar solicitud a Claude via Messages API

Inspeccionar stop_reason

Si stop_reason es "tool_use": ejecutar herramienta(s), añadir resultados al historial, reenviar

Si stop_reason es "end_turn": agente ha terminado

Anti-patrones a evitar:
❌ Parsear lenguaje natural para determinar terminación
❌ Iteración con límites arbitrarios
❌ Verificar contenido de texto como indicador de completado

TASK 1.2: MULTI-AGENT ORCHESTRATION
Arquitectura hub-and-spoke:
Un agente coordinador central

Subagentes para tareas especializadas

Toda comunicación fluye a través del coordinador

Principio de aislamiento:
Los subagentes NO comparten memoria con el coordinador. Cada pieza de información debe pasarse explícitamente.

TASK 1.3: SUBAGENT INVOCATION AND CONTEXT PASSING
Task tool:
Mecanismo para crear subagentes desde un coordinador.

Context passing:
Incluir hallazgos completos de agentes previos directamente en el prompt del subagente.

TASK 1.4: WORKFLOW ENFORCEMENT AND HANDOFF
Espectro de enforcement:
Basado en prompts: funciona la mayoría del tiempo, pero tiene tasa de fallos

Programático: hooks o puertas de requisitos previos, funciona siempre

Regla de decisión:
Cuando las consecuencias son financieras, de seguridad o compliance: usar enforcement programático.

TASK 1.5: AGENT SDK HOOKS
PostToolUse hooks:
Interceptan resultados de herramientas antes de que el modelo los procese.

Tool call interception hooks:
Interceptan llamadas a herramientas antes de ejecutarlas.

TASK 1.6: TASK DECOMPOSITION STRATEGIES
Patrones principales:
Pipelines secuenciales fijos (prompt chaining)

Descomposición adaptativa dinámica

Problema de atención diluida:
Procesar demasiados archivos en una sola pasada produce profundidad inconsistente. Solución: múltiples pasadas.

TASK 1.7: SESSION STATE AND RESUMPTION
Opciones de gestión de sesión:
--resume <session-name>: continuar sesión específica

fork_session: crear rama independiente

Inicio fresco con inyección de resumen

📘 DOMINIO 2: TOOL DESIGN & MCP INTEGRATION (18%)
TASK 2.1: TOOL INTERFACE DESIGN
Las descripciones de herramientas son el mecanismo PRINCIPAL que usan los LLMs para seleccionar herramientas.

Qué incluye una buena descripción:
Qué hace la herramienta

Qué entradas espera

Ejemplos de consultas

Casos extremos y limitaciones

Límites explícitos

TASK 2.2: STRUCTURED ERROR RESPONSES
Cuatro categorías de error:
Transient: timeouts, servicio no disponible (retryable)

Validation: entrada inválida (arreglar input, reintentar)

Business: violaciones de política (NO retryable)

Permission: acceso denegado

TASK 2.3: TOOL DISTRIBUTION AND TOOL_CHOICE
Problema de sobrecarga de herramientas:
Dar 18 herramientas a un agente degrada la confiabilidad de selección. Óptimo: 4-5 herramientas por agente.

Configuración de tool_choice:
"auto": modelo decide si llamar herramienta

"any": debe llamar una herramienta, elige cuál

{"type": "tool", "name": "..."}: debe llamar herramienta específica

TASK 2.4: MCP SERVER INTEGRATION
Jerarquía de scope:
Project-level: .mcp.json en el repo, versionado, compartido

User-level: ~/.claude.json, personal, no versionado

Expansión de variables de entorno:
.mcp.json soporta ${GITHUB_TOKEN}

TASK 2.5: BUILT-IN TOOLS
Grep vs Glob:
Grep: busca en CONTENIDO de archivos

Glob: busca en NOMBRES de archivos por patrón

Read/Write/Edit:
Edit: modificaciones específicas con texto único

Read + Write: fallback cuando Edit falla

📘 DOMINIO 3: CLAUDE CODE CONFIGURATION & WORKFLOWS (20%)
TASK 3.1: CLAUDE.md HIERARCHY
Tres niveles:

User-level (~/.claude/CLAUDE.md): solo para ti, no versionado

Project-level (.claude/CLAUDE.md): para todos, versionado

Directory-level: aplica en ese directorio específico

TASK 3.2: CUSTOM SLASH COMMANDS AND SKILLS
Estructura:
.claude/commands/ = comandos compartidos

~/.claude/commands/ = comandos personales

.claude/skills/ con SKILL.md = invocación bajo demanda

Frontmatter de skills:
context: fork: ejecuta en contexto aislado

allowed-tools: restringe herramientas

argument-hint: pide parámetros al invocar

TASK 3.3: PATH-SPECIFIC RULES
Archivos .claude/rules/ con frontmatter YAML:

yaml
---
paths: ["terraform/**/*"]
---
TASK 3.4: PLAN MODE VS DIRECT EXECUTION
Plan mode: tareas complejas, cambios multi-archivo, decisiones arquitectónicas
Direct execution: cambios claros y limitados, bug fixes simples

TASK 3.5: ITERATIVE REFINEMENT
Jerarquía de técnicas:
Ejemplos concretos input/output (2-3 ejemplos)

Iteración guiada por pruebas

Patrón de entrevista (Claude pregunta antes de implementar)

TASK 3.6: CI/CD INTEGRATION
Flag -p: ejecuta Claude Code en modo no interactivo. Sin él, el job de CI se cuelga.

📘 DOMINIO 4: PROMPT ENGINEERING & STRUCTURED OUTPUT (20%)
TASK 4.1: EXPLICIT CRITERIA
❌ "Sé conservador" / "Solo reporta hallazgos de alta confianza"
✅ "Reporta bugs y vulnerabilidades de seguridad. Omite preferencias de estilo menores."

TASK 4.2: FEW-SHOT PROMPTING
Los ejemplos few-shot son la técnica más efectiva para consistencia.

TASK 4.3: STRUCTURED OUTPUT WITH TOOL_USE
tool_use con JSON schemas elimina errores de sintaxis, pero NO errores semánticos.

TASK 4.4: VALIDATION-RETRY LOOPS
Reintentar con feedback de error: enviar documento original + extracción fallida + error específico.

TASK 4.5: BATCH PROCESSING
Message Batches API:

50% ahorro de costos

Hasta 24h de procesamiento

Sin SLA de latencia garantizado

No soporta multi-turn tool calling

TASK 4.6: MULTI-INSTANCE REVIEW
Un modelo revisando su propio output en la misma sesión es MENOS efectivo que una instancia independiente.

📘 DOMINIO 5: CONTEXT MANAGEMENT & RELIABILITY (15%)
TASK 5.1: CONTEXT PRESERVATION
Trampa de la sumarización progresiva: comprimir el historial pierde valores numéricos, fechas, etc.
Solución: bloque persistente de "casos fácticos" con montos, fechas, números de orden.

TASK 5.2: ESCALATION AND AMBIGUITY RESOLUTION
Tres triggers válidos:
Cliente pide explícitamente un humano

Excepciones de política

Imposibilidad de progresar

Triggers no confiables:
❌ Análisis de sentimiento
❌ Puntajes de confianza auto-reportados

TASK 5.3: ERROR PROPAGATION
Contexto de error estructurado:
Tipo de fallo

Qué se intentó

Resultados parciales

Alternativas potenciales

TASK 5.4: CODEBASE EXPLORATION
Estrategias de mitigación:
Archivos scratchpad

Delegación a subagentes

Inyección de resúmenes

/compact

TASK 5.5: HUMAN REVIEW AND CONFIDENCE CALIBRATION
Validar precisión por tipo de documento y segmento de campo ANTES de automatizar.

TASK 5.6: INFORMATION PROVENANCE
Mapeos estructurados afirmación-fuente: afirmación + URL fuente + nombre documento + extracto relevante.

📝 QUIZ DE CLAUDE CODE - PREGUNTAS Y RESPUESTAS
PREGUNTA 1
What is the fundamental limitation of language models that necessitates the use of a tool system in coding assistants?

✅ Respuesta correcta: They can only process text input/output and cannot directly interact with external systems

PREGUNTA 2
What permission configuration is required when integrating MCP servers with Claude Code in GitHub Actions?

✅ Respuesta correcta: Each MCP server tool must be individually listed in the permissions

PREGUNTA 3
What is the primary difference between Plan Mode and Thinking Mode in Claude Code?

✅ Respuesta correcta: Plan Mode handles breadth (multi-step tasks) while Thinking Mode handles depth (complex logic)

PREGUNTA 4
Which of the following correctly describes the three types of Claude.md files and their usage?

✅ Respuesta correcta: Project level (shared with team, committed), Local level (personal, not committed), Machine level (global for all projects)

PREGUNTA 5
How do you create a custom command in Claude Code that accepts runtime parameters?

✅ Respuesta correcta: Include $ARGUMENTS placeholder in the markdown command file

PREGUNTA 6
Which type of hook can prevent a tool call from happening if certain conditions are met?

✅ Respuesta correcta: PreToolUse hook

PREGUNTA 7
A developer wants to prevent Claude from reading sensitive .env files. Which type of hook should they set up, and what tool names would they likely match?

✅ Respuesta correcta: PreToolUse hook, matching Read and Grep

PREGUNTA 8
What is the primary purpose of hooks in Claude Code?

✅ Respuesta correcta: To run commands before or after Claude executes a tool

🏗️ EJERCICIOS PRÁCTICOS PARA CONSTRUIR
Ejercicio 1: Multi-Agent System
Construye un agente coordinador con dos subagentes (búsqueda web y análisis de documentos), paso de contexto con metadatos estructurados, puerta de requisitos programática y hook PostToolUse de normalización.

Ejercicio 2: MCP Tools
Crea 3 herramientas MCP con un par intencionalmente ambiguo. Escribe respuestas de error con las cuatro categorías. Configúralas en .mcp.json con expansión de variables de entorno.

Ejercicio 3: Claude Code Workflow
Configura un proyecto con jerarquía CLAUDE.md (nivel proyecto + directorio), reglas .claude/rules/ con patrones glob, una skill con context: fork, y un script CI usando flag -p con output JSON.

Ejercicio 4: Extraction Pipeline
Crea una herramienta de extracción con JSON schema (campos required, optional, nullable, enums con 'other'). Implementa validation-retry. Procesa 10 documentos, añade ejemplos few-shot para formatos variados.

Ejercicio 5: Coordinator-Subagents
Construye un coordinador con dos subagentes. Implementa bloque persistente de casos fácticos. Simula un timeout con propagación de error estructurado. Prueba con fuentes conflictivas.

📚 RECURSOS RECOMENDADOS DE ANTHROPIC
Building with the Claude API

Introduction to Model Context Protocol

Claude Code in Action

Claude 101

🎯 CONCLUSIÓN
Este conocimiento te permite convertirte en un Claude Architect sin necesidad de certificación oficial. Todos los conceptos aquí presentados son los que el examen evaluaría y son habilidades que puedes monetizar en producción.

"NOW GO AND BECOME A UNCERTIFIED CLAUDE ARCHITECT."

