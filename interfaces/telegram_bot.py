"""
OpenClawd — Telegram Bot + Smart Crew Router.
Cyber Paisa / Enigma Group

Cualquier mensaje (texto o voz) se rutea al crew correcto.
11 crews disponibles + router inteligente por NLP.

Comandos explícitos:
    /start, /help    — Lista de comandos
    /daily           — Rutina matutina COO
    /weekly [PROY]   — Reporte semanal
    /research TEMA   — Investigar un tema
    /grant [PROY]    — Buscar grants
    /content DESC    — Generar contenido
    /mvp IDEA        — Generar MVP completo
    /audit TARGET    — Auditoría Enigma
    /build DESC      — Generar proyecto con código
    /code PATH       — Code review
    /projects        — Listar proyectos activos
    /status          — Estado del sistema (providers + keys)
    /agents          — Info de los 8 agentes

Texto libre:
    Cualquier mensaje se analiza y se rutea al crew más apropiado.

Voz:
    Envía un audio → se transcribe con Groq Whisper → se rutea → respuesta texto + audio.
"""

import os
import sys
import json
import logging
import threading
import time
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("openclawd.telegram")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Asegurar que el proyecto está en sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ═══════════════════════════════════════════════════════
# EXECUTION LOGGING — Persistencia de cada ejecución
# ═══════════════════════════════════════════════════════

LOG_FILE = os.path.join(PROJECT_ROOT, "logs", "execution_log.jsonl")


def _log_execution(entry: dict):
    """Append una línea JSON al log de ejecuciones + test report si hay error."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False, default=str) + "\n")

    # Auto-registrar errores como test incidents
    if entry.get("status") == "error":
        try:
            sys.path.insert(0, os.path.join(PROJECT_ROOT, "logs"))
            from test_report import log_test_incident, get_next_test_id
            from llm_config import _get_active_providers
            log_test_incident(
                test_id=get_next_test_id(),
                description=f"Error en crew {entry.get('crew', '?')} via Telegram",
                variables={
                    "crew": entry.get("crew"),
                    "user": entry.get("user"),
                    "task": entry.get("task", "")[:100],
                    "providers_activos": ", ".join(_get_active_providers()),
                    "intentos": entry.get("attempts"),
                    "duracion_seg": entry.get("duration_sec"),
                },
                errors=[{
                    "provider": "unknown",
                    "error_type": "crew_execution_error",
                    "message": entry.get("error", "")[:300],
                    "timestamp": entry.get("timestamp"),
                }],
                resolution="Pendiente analisis",
                status="pending",
            )
        except Exception:
            pass  # No bloquear por logging


# ═══════════════════════════════════════════════════════
# SMART ROUTER — Clasifica texto libre al crew correcto
# ═══════════════════════════════════════════════════════

# ── Rutas especializadas: solo se activan con keywords explícitos ──
# El orden importa: las especialidades van primero, lo genérico al final.
# Si nada matchea → crew general de máxima calidad (todos los agentes).

CREW_ROUTES = [
    # ── OPERACIONES (no necesitan tema) ──
    {
        "mode": "daily_ops",
        "keywords": ["rutina", "daily", "buenos dias", "buen dia", "matutina", "operaciones diarias"],
        "label": "Rutina diaria",
        "needs_task": False,
    },
    {
        "mode": "weekly_report",
        "keywords": ["semanal", "weekly", "reporte semanal", "reunion semanal", "resumen semanal"],
        "label": "Reporte semanal",
        "needs_task": False,
    },
    # ── ESPECIALIDADES (requieren keywords explícitos) ──
    {
        "mode": "full_mvp",
        "keywords": ["mvp", "producto minimo", "plan mvp", "diseña mvp",
                     "plan de negocio", "business plan", "modelo de negocio"],
        "label": "MVP + Plan de Negocio (especialista)",
        "needs_task": True,
    },
    {
        "mode": "grant_hunt",
        "keywords": ["grant", "grants", "beca", "funding", "subsidio", "financiamiento",
                     "oportunidad de fondos", "busca grants"],
        "label": "Busqueda de grants (especialista)",
        "needs_task": True,
    },
    {
        "mode": "content",
        "keywords": ["hilo", "thread", "tweet", "blog", "contenido", "escribe articulo",
                     "newsletter", "narrativa", "pitch", "genera contenido", "crea post"],
        "label": "Contenido (especialista)",
        "needs_task": True,
    },
    {
        "mode": "enigma_audit",
        "keywords": ["audit", "audita", "auditoria", "sentinel", "trust score", "verifica agente",
                     "escanea", "scanner"],
        "label": "Auditoria Enigma (especialista)",
        "needs_task": True,
    },
    {
        "mode": "build_project",
        "keywords": ["genera proyecto", "build project", "crea proyecto", "genera codigo",
                     "scaffolding", "boilerplate"],
        "label": "Build Project (especialista)",
        "needs_task": True,
    },
    {
        "mode": "code_review",
        "keywords": ["code review", "revisa codigo", "analiza codigo", "review code", "refactor"],
        "label": "Code Review (especialista)",
        "needs_task": True,
    },
    {
        "mode": "data_analysis",
        "keywords": ["excel", "csv", "base de datos", "datos", "analiza este archivo", "procesa", "cruce"],
        "label": "Análisis de Datos (especialista)",
        "needs_task": True,
    },
    # ── GENERAL: cualquier consulta...
]


def classify_message(text: str) -> tuple[str, str]:
    """Clasifica texto libre al crew más apropiado.

    Returns:
        (mode, label) o ("unknown", "") si no matchea.
    """
    text_lower = text.lower()
    for route in CREW_ROUTES:
        if any(kw in text_lower for kw in route["keywords"]):
            return route["mode"], route["label"]
    return "unknown", ""


def _detect_project(text: str) -> str | None:
    """Detecta nombre de proyecto en el texto usando projects.yaml."""
    try:
        import yaml
        projects_path = os.path.join(PROJECT_ROOT, "config", "projects.yaml")
        if not os.path.exists(projects_path):
            return None
        with open(projects_path, "r") as f:
            data = yaml.safe_load(f)
        if not data or "projects" not in data:
            return None
        for p in data["projects"]:
            if p["name"].lower() in text.lower():
                return p["name"]
    except Exception:
        pass
    return None


# ═══════════════════════════════════════════════════════
# FORMATEADOR — Pydantic → Telegram Markdown bonito
# ═══════════════════════════════════════════════════════

def _format_result(result, mode: str) -> str:
    """Convierte el resultado del crew a Markdown profesional para Telegram."""
    try:
        # Si el resultado tiene .pydantic, extraer el objeto
        data = None
        if hasattr(result, "pydantic") and result.pydantic:
            data = result.pydantic
        elif hasattr(result, "json_dict") and result.json_dict:
            data = result.json_dict

        if data and hasattr(data, "value_proposition"):
            return _format_mvp_plan(data)
        if data and hasattr(data, "executive_summary"):
            return _format_research_report(data)
        if data and hasattr(data, "opportunities"):
            return _format_grant_report(data)
        if data and hasattr(data, "overall_score") and hasattr(data, "issues"):
            return _format_code_review(data)
        if data and hasattr(data, "agent_name"):
            return _format_audit_report(data)
        if data and hasattr(data, "content_type"):
            return _format_content(data)
        if data and hasattr(data, "files_created"):
            return _format_build_report(data)
        if data and hasattr(data, "final_verdict"):
            return _format_verification(data)

        # Si es dict (json_dict)
        if isinstance(data, dict):
            if "value_proposition" in data:
                return _format_mvp_dict(data)
            if "executive_summary" in data:
                return _format_research_dict(data)

        # Fallback: limpiar el str crudo de Pydantic
        raw = str(result)
        if "value_proposition=" in raw or "executive_summary=" in raw:
            return _format_raw_pydantic(raw, mode)

        return raw

    except Exception as e:
        logger.warning(f"Format error (using raw): {e}")
        return str(result)


def _format_mvp_plan(data) -> str:
    """Formatea MVPPlan Pydantic object."""
    lines = ["🚀 *MVP PLAN*\n"]
    lines.append(f"💡 *Propuesta de Valor*\n{data.value_proposition}\n")
    lines.append(f"🎯 *Usuario Objetivo*\n{data.target_user}\n")

    lines.append("⚙️ *Features del MVP*")
    for f in data.features:
        emoji = "🔴" if f.priority == "P0" else "🟡" if f.priority == "P1" else "🟢"
        lines.append(f"  {emoji} *{f.name}* ({f.priority} | {f.effort})")
        lines.append(f"      {f.description}\n")

    lines.append(f"🛠 *Tech Stack*\n{data.tech_stack}\n")
    lines.append(f"📅 *Timeline*\n{data.timeline}\n")

    lines.append("📊 *Métricas Clave*")
    for m in data.metrics:
        lines.append(f"  • {m}")

    lines.append("\n⚠️ *Riesgos*")
    for r in data.risks:
        lines.append(f"  • {r}")

    lines.append(f"\n💰 *Monetización*\n{data.monetization}")
    return "\n".join(lines)


def _format_research_report(data) -> str:
    """Formatea ResearchReport Pydantic object."""
    lines = ["🔬 *REPORTE DE INVESTIGACIÓN*\n"]
    lines.append(f"📋 *Resumen Ejecutivo*\n{data.executive_summary}\n")
    lines.append(f"📈 *Tamaño de Mercado*\n{data.market_size}\n")

    if data.competitors:
        lines.append("🏆 *Competidores*")
        for c in data.competitors:
            lines.append(f"  • *{c.name}*: {c.pricing}")
            lines.append(f"    ✅ {c.strengths}")
            lines.append(f"    ❌ {c.weaknesses}\n")

    lines.append("😤 *Pain Points*")
    for p in data.pain_points:
        lines.append(f"  • {p}")

    lines.append("\n📈 *Tendencias*")
    for t in data.trends:
        lines.append(f"  • {t}")

    verdict_emoji = "✅" if "go" in data.go_no_go.lower() and "no" not in data.go_no_go.lower() else "⚠️"
    lines.append(f"\n{verdict_emoji} *Veredicto:* {data.go_no_go}")
    lines.append(f"🎯 *Confianza:* {data.confidence_score}/10")

    if data.sources:
        lines.append("\n📚 *Fuentes*")
        for s in data.sources[:5]:
            lines.append(f"  • {s}")

    return "\n".join(lines)


def _format_grant_report(data) -> str:
    """Formatea GrantHuntReport."""
    lines = ["💰 *REPORTE DE GRANTS*\n"]
    for i, g in enumerate(data.opportunities[:5], 1):
        lines.append(f"*{i}. {g.program_name}* ({g.ecosystem})")
        lines.append(f"  💵 {g.funding_range}")
        lines.append(f"  📅 Deadline: {g.deadline}")
        lines.append(f"  🎯 Fit: {g.fit_score}/10")
        lines.append(f"  📝 {g.narrative_angle}\n")

    lines.append(f"⭐ *Top Recomendación*\n{data.top_recommendation}\n")
    lines.append(f"📖 *Estrategia Narrativa*\n{data.narrative_strategy}\n")

    lines.append("📋 *Próximos Pasos*")
    for s in data.next_steps:
        lines.append(f"  • {s}")
    return "\n".join(lines)


def _format_code_review(data) -> str:
    """Formatea CodeReviewReport."""
    score_emoji = "🟢" if data.overall_score >= 7 else "🟡" if data.overall_score >= 5 else "🔴"
    lines = [f"🔍 *CODE REVIEW* {score_emoji} {data.overall_score}/10\n"]
    lines.append(f"📋 *Resumen*\n{data.summary}\n")

    if data.issues:
        lines.append("🐛 *Issues*")
        for issue in data.issues[:8]:
            sev = "🔴" if issue.severity.lower() in ("high", "critical", "alta") else "🟡"
            lines.append(f"  {sev} `{issue.file}`: {issue.description}")
            lines.append(f"     💡 {issue.fix}\n")

    if data.quick_wins:
        lines.append("⚡ *Quick Wins*")
        for q in data.quick_wins:
            lines.append(f"  • {q}")

    lines.append(f"\n🏗 *Arquitectura*\n{data.architecture_notes}")
    lines.append(f"\n📋 *Plan de Acción*\n{data.action_plan}")
    return "\n".join(lines)


def _format_audit_report(data) -> str:
    """Formatea AgentAuditReport."""
    lines = [f"🛡 *AUDITORÍA: {data.agent_name}*\n"]
    lines.append(f"  🌐 Endpoint: {data.endpoint_score}/100")
    lines.append(f"  📄 Metadata: {data.metadata_score}/100\n")

    if data.security_notes:
        lines.append("🔒 *Seguridad*")
        for n in data.security_notes:
            lines.append(f"  • {n}")

    if data.recommendations:
        lines.append("\n💡 *Recomendaciones*")
        for r in data.recommendations:
            lines.append(f"  • {r}")

    lines.append(f"\n📊 *Veredicto:* {data.overall_verdict}")
    return "\n".join(lines)


def _format_content(data) -> str:
    """Formatea ContentPackage."""
    lines = [f"✍️ *{data.content_type.upper()}*\n"]
    lines.append(f"📌 *{data.title}*\n")
    lines.append(f"📱 *Plataforma:* {data.platform}\n")
    lines.append(data.body)
    if data.hashtags:
        lines.append("\n" + " ".join(f"#{h}" for h in data.hashtags))
    return "\n".join(lines)


def _format_build_report(data) -> str:
    """Formatea BuildProjectReport."""
    lines = [f"🏗 *PROYECTO: {data.project_name}*\n"]
    lines.append(f"🛠 *Stack:* {data.tech_stack}\n")

    lines.append("📁 *Archivos Creados*")
    for f in data.files_created[:15]:
        lines.append(f"  • `{f}`")

    lines.append(f"\n📋 *Setup*\n{data.setup_instructions}")

    if data.next_steps:
        lines.append("\n📋 *Próximos Pasos*")
        for s in data.next_steps:
            lines.append(f"  • {s}")
    return "\n".join(lines)


def _format_verification(data) -> str:
    """Formatea VerificationReport."""
    status = "✅ VERIFICADO" if data.verified else "❌ NO VERIFICADO"
    lines = [f"🔎 *VERIFICACIÓN* — {status}\n"]
    lines.append(f"📊 *Calidad:* {data.quality_score}/10\n")

    if data.issues_found:
        lines.append("⚠️ *Issues*")
        for i in data.issues_found:
            lines.append(f"  • {i}")

    if data.improvements:
        lines.append("\n💡 *Mejoras*")
        for m in data.improvements:
            lines.append(f"  • {m}")

    lines.append(f"\n📋 *Veredicto:* {data.final_verdict}")
    return "\n".join(lines)


def _format_mvp_dict(data: dict) -> str:
    """Formatea MVP desde dict."""
    lines = ["🚀 *MVP PLAN*\n"]
    lines.append(f"💡 *Propuesta de Valor*\n{data.get('value_proposition', '')}\n")
    lines.append(f"🎯 *Usuario Objetivo*\n{data.get('target_user', '')}\n")

    for f in data.get("features", []):
        if isinstance(f, dict):
            emoji = "🔴" if f.get("priority") == "P0" else "🟡"
            lines.append(f"  {emoji} *{f.get('name', '')}* ({f.get('priority', '')} | {f.get('effort', '')})")
            lines.append(f"      {f.get('description', '')}\n")

    lines.append(f"🛠 *Tech Stack*\n{data.get('tech_stack', '')}\n")
    lines.append(f"📅 *Timeline*\n{data.get('timeline', '')}\n")

    for m in data.get("metrics", []):
        lines.append(f"  • {m}")

    lines.append(f"\n💰 *Monetización*\n{data.get('monetization', '')}")
    return "\n".join(lines)


def _format_research_dict(data: dict) -> str:
    """Formatea Research desde dict."""
    lines = ["🔬 *REPORTE DE INVESTIGACIÓN*\n"]
    lines.append(f"📋 {data.get('executive_summary', '')}\n")
    lines.append(f"📈 *Mercado:* {data.get('market_size', '')}\n")
    lines.append(f"🎯 *Veredicto:* {data.get('go_no_go', '')} ({data.get('confidence_score', '?')}/10)")
    return "\n".join(lines)


def _format_raw_pydantic(raw: str, mode: str) -> str:
    """Parsea y formatea string crudo de Pydantic cuando no hay .pydantic."""
    import re

    mode_emojis = {
        "research": "🔬", "full_mvp": "🚀", "grant_hunt": "💰",
        "content": "✍️", "daily_ops": "☀️", "weekly_report": "📊",
        "enigma_audit": "🛡", "code_review": "🔍", "build_project": "🏗",
    }
    header = f"{mode_emojis.get(mode, '📋')} *{mode.upper().replace('_', ' ')}*\n"

    # Extraer campos key='value' del string Pydantic
    field_labels = {
        "value_proposition": "💡 *Propuesta de Valor*",
        "target_user": "🎯 *Usuario Objetivo*",
        "tech_stack": "🛠 *Tech Stack*",
        "timeline": "📅 *Timeline*",
        "monetization": "💰 *Monetización*",
        "executive_summary": "📋 *Resumen Ejecutivo*",
        "market_size": "📈 *Tamaño de Mercado*",
        "go_no_go": "✅ *Veredicto*",
        "overall_verdict": "📊 *Veredicto*",
        "narrative_strategy": "📖 *Estrategia*",
        "top_recommendation": "⭐ *Top Recomendación*",
    }

    lines = [header]

    # Extraer campos simples con regex
    for field, label in field_labels.items():
        pattern = rf"{field}='(.*?)(?:'\s+\w+=|'$)"
        match = re.search(pattern, raw, re.DOTALL)
        if match:
            value = match.group(1).strip()
            if value:
                lines.append(f"{label}\n{value}\n")

    # Extraer listas (metrics, risks, pain_points, etc.)
    list_labels = {
        "metrics": "📊 *Métricas*",
        "risks": "⚠️ *Riesgos*",
        "pain_points": "😤 *Pain Points*",
        "trends": "📈 *Tendencias*",
        "next_steps": "📋 *Próximos Pasos*",
        "quick_wins": "⚡ *Quick Wins*",
        "improvements": "💡 *Mejoras*",
        "security_notes": "🔒 *Seguridad*",
        "recommendations": "💡 *Recomendaciones*",
    }

    for field, label in list_labels.items():
        pattern = rf"{field}=\[(.*?)\]"
        match = re.search(pattern, raw, re.DOTALL)
        if match:
            items_raw = match.group(1)
            items = re.findall(r"'(.*?)'", items_raw)
            if items:
                lines.append(f"{label}")
                for item in items:
                    lines.append(f"  • {item}")
                lines.append("")

    # Extraer features (MVPFeature objects)
    features = re.findall(
        r"MVPFeature\(name='(.*?)',\s*priority='(.*?)',\s*effort='(.*?)',\s*description='(.*?)'\)",
        raw, re.DOTALL,
    )
    if features:
        lines.append("⚙️ *Features*")
        for name, priority, effort, desc in features:
            emoji = "🔴" if priority == "P0" else "🟡" if priority == "P1" else "🟢"
            lines.append(f"  {emoji} *{name}* ({priority} | {effort})")
            lines.append(f"      {desc}\n")

    result = "\n".join(lines)
    return result if len(result) > len(header) + 10 else raw


# ═══════════════════════════════════════════════════════
# CREW EXECUTOR
# ═══════════════════════════════════════════════════════

def _save_result(result_str: str, mode: str, project: str | None = None) -> str:
    """Guarda resultado en archivo y retorna la ruta."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join(PROJECT_ROOT, "output", project) if project else os.path.join(PROJECT_ROOT, "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{mode}_{ts}.md")
    with open(out_path, "w") as f:
        f.write(f"# {mode}\n**Fecha:** {datetime.now():%Y-%m-%d %H:%M}\n\n---\n\n{result_str}")
    return out_path


def _send_long_message(bot, chat_id: int, text: str, file_path: str | None = None):
    """Envía mensaje largo a Telegram, partiendo en chunks si es necesario."""
    MAX_LEN = 4000

    if len(text) <= MAX_LEN:
        try:
            bot.send_message(chat_id, text, parse_mode="Markdown")
        except Exception:
            # Si falla Markdown, enviar sin formato
            bot.send_message(chat_id, text)
        return

    # Partir por secciones (doble newline) para no cortar ideas
    chunks = []
    current = ""
    for line in text.split("\n"):
        if len(current) + len(line) + 1 > MAX_LEN:
            if current:
                chunks.append(current)
            current = line
        else:
            current = current + "\n" + line if current else line
    if current:
        chunks.append(current)

    for i, chunk in enumerate(chunks):
        try:
            bot.send_message(chat_id, chunk, parse_mode="Markdown")
        except Exception:
            bot.send_message(chat_id, chunk)

    # Enviar archivo completo al final
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            bot.send_document(chat_id, f, caption="📄 Resultado completo")


def _extract_voice_summary(result, formatted_text: str) -> str:
    """Extrae un resumen corto y útil para leer en voz alta."""
    import re

    # Intentar extraer executive_summary o value_proposition del resultado
    summary = ""

    # Desde Pydantic object
    data = None
    if hasattr(result, "pydantic") and result.pydantic:
        data = result.pydantic
    elif hasattr(result, "json_dict") and result.json_dict:
        data = result.json_dict

    if data:
        if hasattr(data, "executive_summary") and data.executive_summary:
            summary = data.executive_summary
        elif hasattr(data, "value_proposition") and data.value_proposition:
            summary = data.value_proposition
        elif hasattr(data, "overall_verdict") and data.overall_verdict:
            summary = data.overall_verdict
        elif hasattr(data, "body") and data.body:
            summary = data.body[:300]

    # Desde raw string si no encontramos pydantic
    if not summary:
        raw = str(result) if not isinstance(result, str) else result
        for field in ["executive_summary", "value_proposition", "final_verdict", "overall_verdict"]:
            match = re.search(rf"{field}='(.*?)'(?:\s+\w+=|$)", raw, re.DOTALL)
            if match and len(match.group(1)) > 20:
                summary = match.group(1)
                break

    # Último fallback: primer párrafo real del texto formateado
    if not summary:
        clean = re.sub(r'[*_`#]', '', formatted_text)
        clean = re.sub(r'[\U0001f300-\U0001f9ff\U00002600-\U000027bf\U0000fe00-\U0000fe0f\U0000200d]', '', clean)
        lines = [l.strip() for l in clean.split("\n") if len(l.strip()) > 30]
        summary = lines[0] if lines else ""

    # Limitar a ~400 chars para que el audio sea corto
    if len(summary) > 400:
        # Cortar en punto o coma para no truncar a medio
        cut = summary[:400].rfind(".")
        if cut > 200:
            summary = summary[:cut + 1]
        else:
            summary = summary[:400]

    return summary.strip()


def _send_voice_summary(bot, chat_id: int, formatted_text: str, msg_id: int, result=None):
    """Genera y envía resumen de voz con Edge-TTS Salome."""
    try:
        import asyncio
        import edge_tts

        summary = _extract_voice_summary(result, formatted_text) if result else ""
        if not summary or len(summary) < 15:
            return

        audio_path = f"/tmp/tg_summary_{msg_id}.mp3"

        async def _gen():
            communicate = edge_tts.Communicate(summary, "es-CO-SalomeNeural")
            await communicate.save(audio_path)

        asyncio.run(_gen())

        if os.path.exists(audio_path) and os.path.getsize(audio_path) > 0:
            with open(audio_path, "rb") as af:
                bot.send_voice(chat_id, af)
            try:
                os.remove(audio_path)
            except OSError:
                pass
    except Exception as e:
        logger.warning(f"Voice summary error (non-critical): {e}")


def _detect_failed_provider(error_str: str) -> str | None:
    """Detecta qué provider falló basándose en el mensaje de error."""
    error_lower = error_str.lower()
    if "groq" in error_lower:
        return "groq"
    if "nvidia" in error_lower or "nim" in error_lower:
        return "nvidia"
    if "cerebras" in error_lower:
        return "cerebras"
    if "zhipu" in error_lower or "z.ai" in error_lower or "glm" in error_lower:
        return "zhipu"
    # Detectar por modelo
    if "llama-3.3" in error_lower or "qwen3-32b" in error_lower or "kimi-k2-instruct" in error_lower:
        return "groq"
    if "deepseek" in error_lower and "nvidia_nim" in error_lower:
        return "nvidia"
    if "gpt-oss" in error_lower:
        return "cerebras"
    return None


def _create_crew(mode: str, task: str, project: str | None):
    """Crea el crew correspondiente al modo."""
    from crew import (
        create_research_crew, create_pure_research_crew,
        create_full_mvp_crew,
        create_grant_hunt_crew, create_content_crew,
        create_daily_ops_crew, create_weekly_report_crew,
        create_enigma_audit_crew, create_build_project_crew,
        create_code_review_crew,
    )

    creators = {
        "research": lambda: create_pure_research_crew(task),
        "full_mvp": lambda: create_full_mvp_crew(task),
        "grant_hunt": lambda: create_grant_hunt_crew(task, project),
        "content": lambda: create_content_crew(task, project),
        "daily_ops": lambda: create_daily_ops_crew(),
        "weekly_report": lambda: create_weekly_report_crew(project),
        "enigma_audit": lambda: create_enigma_audit_crew(task or "database"),
        "build_project": lambda: create_build_project_crew(task, "telegram_project"),
        "code_review": lambda: create_code_review_crew(task or "."),
    }
    creator = creators.get(mode)
    if not creator:
        return None
    return creator()


def _run_crew_async(bot, message, mode: str, task: str = "", project: str | None = None):
    """Ejecuta un crew en thread separado con core.crew_runner (FASE 0)."""
    def _execute():
        from core.crew_runner import run_crew
        from core.providers import ProviderManager

        pm = ProviderManager()
        user_info = f"{message.from_user.first_name or ''} ({message.from_user.id})" if message.from_user else "unknown"

        crew = _create_crew(mode, task, project)
        if not crew:
            bot.send_message(message.chat.id, f"Modo '{mode}' no soportado")
            return

        # Execute with full FASE 0 infrastructure
        result = run_crew(mode, crew, input_text=task or "")

        # Log execution
        _log_execution({
            "timestamp": datetime.now().isoformat(),
            "source": "telegram",
            "user": user_info,
            "crew": mode,
            "project": project,
            "task": task[:200] if task else "",
            "status": result["status"],
            "duration_sec": round(result["elapsed_ms"] / 1000, 1),
            "attempts": result["retries"] + 1,
            "run_id": result["run_id"],
            "output_path": None,
            "error": result.get("error"),
            "supervisor": result.get("supervisor"),
            "governance": result.get("governance"),
        })

        if result["status"] == "ok":
            formatted = _format_result(type("R", (), {"raw": result["output"]})(), mode)
            out_path = _save_result(result["output"], mode, project)

            _log_execution({
                "timestamp": datetime.now().isoformat(),
                "source": "telegram",
                "user": user_info,
                "crew": mode,
                "status": "success",
                "output_path": out_path,
                "duration_sec": round(result["elapsed_ms"] / 1000, 1),
                "attempts": result["retries"] + 1,
                "run_id": result["run_id"],
            })

            # Append supervisor info if available
            sup = result.get("supervisor")
            if sup and sup.get("score"):
                formatted += f"\n\n---\nCalidad: {sup['score']}/10"

            _send_long_message(bot, message.chat.id, formatted, out_path)
            _send_voice_summary(bot, message.chat.id, formatted, message.message_id,
                                type("R", (), {"raw": result["output"]})())

            logger.info(f"Crew {mode} completado ({result['elapsed_ms']:.0f}ms, "
                        f"{result['retries']} retries, run={result['run_id']})")

        elif result["status"] == "escalated":
            sup = result.get("supervisor", {})
            bot.send_message(message.chat.id,
                f"La calidad del resultado no cumple el umbral minimo.\n"
                f"Score: {sup.get('score', '?')}/10\n"
                f"Razones: {', '.join(sup.get('reasons', []))}\n\n"
                f"Resultado parcial entregado de todas formas.",
                parse_mode=None)
            if result["output"]:
                formatted = _format_result(type("R", (), {"raw": result["output"]})(), mode)
                _send_long_message(bot, message.chat.id, formatted, None)

        else:
            # Error
            error = result.get("error", "Unknown error")
            active = pm.get_active()
            status = pm.get_status()

            exhausted = [n for n, s in status.items() if s["exhausted"]]
            if exhausted:
                recovery_info = ", ".join(
                    f"{n} ({s['recovery_in']}s)" for n, s in status.items() if s["exhausted"]
                )
                bot.send_message(message.chat.id,
                    f"Providers agotados: {', '.join(exhausted)}\n"
                    f"Recovery: {recovery_info}\n"
                    f"Activos: {', '.join(active) if active else 'ninguno'}\n\n"
                    f"Intenta de nuevo en unos minutos.",
                    parse_mode=None)
            else:
                clean_err = error[:300].split("\\n")[0]
                bot.send_message(message.chat.id, f"Error en {mode}: {clean_err}")

    thread = threading.Thread(target=_execute, daemon=True)
    thread.start()


# ═══════════════════════════════════════════════════════
# VOZ — Transcripción + ejecución + respuesta audio
# ═══════════════════════════════════════════════════════

def _convert_ogg_to_wav(ogg_path: str) -> str | None:
    """Convierte OGG/opus de Telegram a WAV usando ffmpeg."""
    import subprocess
    wav_path = ogg_path.rsplit(".", 1)[0] + ".wav"
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", ogg_path, "-ar", "16000", "-ac", "1", "-sample_fmt", "s16", wav_path],
            capture_output=True, timeout=30,
        )
        if os.path.exists(wav_path) and os.path.getsize(wav_path) > 0:
            return wav_path
    except Exception as e:
        logger.error(f"ffmpeg conversion error: {e}")
    return None


def _handle_voice_message(bot, message):
    """Procesa mensaje de voz: OGG→WAV→transcribe→rutea→responde texto + audio."""
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded = bot.download_file(file_info.file_path)
        ogg_path = f"/tmp/voice_{message.message_id}.ogg"
        with open(ogg_path, "wb") as f:
            f.write(downloaded)

        # Convertir OGG/opus → WAV (Whisper necesita formato limpio)
        wav_path = _convert_ogg_to_wav(ogg_path)
        audio_path = wav_path or ogg_path  # fallback al OGG si ffmpeg falla

        from interfaces.voice_interface import transcribe_audio, text_to_speech
        text = transcribe_audio(audio_path)

        # Cleanup
        for p in [ogg_path, wav_path]:
            try:
                if p and os.path.exists(p):
                    os.remove(p)
            except OSError:
                pass

        if not text:
            bot.reply_to(message, "❌ No pude transcribir el audio. Verifica que el audio tenga voz clara.")
            return

        bot.reply_to(message, f"🎙️ Escuche: \"{text}\"\n\n⏳ Procesando...")

        # Rutear el texto transcrito al crew correcto (usa _run_crew_async con retry)
        mode, label = classify_message(text)
        project = _detect_project(text)

        if mode == "unknown":
            mode = "research"
            label = "Equipo completo (máxima calidad)"

        bot.send_message(message.chat.id, f"🔄 *{label}*. Ejecutando crew...", parse_mode="Markdown")
        _run_crew_async(bot, message, mode, task=text, project=project)

    except Exception as e:
        bot.reply_to(message, f"❌ Error procesando audio: {e}")


# ═══════════════════════════════════════════════════════
# BOT PRINCIPAL
# ═══════════════════════════════════════════════════════

def _reply_as_enigma(bot, message, text: str):
    """Respuesta directa como Enigma usando LLM con fallbacks."""
    import os, requests as _req

    soul_path = "agents/synthesis/SOUL_AUTONOMOUS.md"
    try:
        soul = open(soul_path).read()[:3000]
    except:
        soul = "Eres Enigma, DOF Agent #1686, experto en Web3, IA y ciberseguridad."

    msgs = [
        {"role": "system", "content": f"""Eres Enigma — DOF Agent #1686. El primer agente con Observabilidad Determinista. Creado por Juan Carlos Quiceno (@Cyber_paisa).

{soul}

REGLAS ABSOLUTAS:
1. Responde SIEMPRE en ESPAÑOL.
2. Tono: inteligente, técnico, profundo, directo. NUNCA saludos genéricos.
3. 2-3 párrafos sustanciales + un siguiente paso concreto.
4. Usa Markdown (negritas, listas).
5. Eres experto en Web3, IA, ciberseguridad, Synthesis 2026."""},
        {"role": "user", "content": text}
    ]

    reply = None

    for provider, url, key_env, model in [
        ("Groq",     "https://api.groq.com/openai/v1/chat/completions",  "GROQ_API_KEY",    "llama-3.3-70b-versatile"),
        ("Mistral",  "https://api.mistral.ai/v1/chat/completions",       "MISTRAL_API_KEY", "mistral-small-latest"),
        ("Cerebras", "https://api.cerebras.ai/v1/chat/completions",      "CEREBRAS_API_KEY","llama-3.3-70b"),
    ]:
        key = os.getenv(key_env, "")
        if not key:
            continue
        try:
            r = _req.post(url,
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={"model": model, "max_tokens": 1500, "messages": msgs},
                timeout=25)
            if r.status_code == 200:
                reply = r.json()["choices"][0]["message"]["content"]
                logger.info(f"Enigma respondio via {provider}")
                break
        except Exception as e:
            logger.warning(f"{provider} fallo: {e}")
            continue

    if reply:
        # Guardar en conversation log en inglés
        try:
            import requests as _rq2
            _tr = _rq2.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {os.getenv('GROQ_API_KEY','')}", "Content-Type": "application/json"},
                json={"model": "llama-3.3-70b-versatile", "max_tokens": 500,
                      "messages": [{"role": "system", "content": "Translate to English. Only reply with the translation, nothing else."},
                                   {"role": "user", "content": reply}]},
                timeout=10)
            reply_en = _tr.json()["choices"][0]["message"]["content"] if _tr.status_code == 200 else reply
        except:
            reply_en = reply

        # Log en inglés para los jueces
        try:
            conv_log = "logs/conversation-log.md"
            import datetime
            with open(conv_log, "a") as _f:
                _f.write(f"\n### Telegram — {datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
                _f.write(f"**Human:** {text[:200]}\n")
                _f.write(f"**Enigma (EN):** {reply_en[:500]}\n")
                _f.write("\n---\n")
        except:
            pass

        # Responder en español en Telegram (máx 4096 chars por mensaje)
        MAX = 3800
        chunks = [reply[i:i+MAX] for i in range(0, len(reply), MAX)]
        for i, chunk in enumerate(chunks):
            prefix = "🤖 *Enigma:*\n\n" if i == 0 else "📄 *(continuación)*\n\n"
            try:
                if i == 0:
                    bot.reply_to(message, f"{prefix}{chunk}", parse_mode="Markdown")
                else:
                    bot.send_message(message.chat.id, f"{prefix}{chunk}", parse_mode="Markdown")
            except Exception:
                try:
                    bot.send_message(message.chat.id, f"🤖 Enigma:\n\n{chunk}")
                except Exception:
                    pass
    else:
        bot.reply_to(message, "⚠️ LLMs no disponibles ahora. Reintenta en 30s.")


def start_bot():
    """Inicia OpenClawd Telegram Bot con polling infinito."""
    if not TELEGRAM_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN no configurado en .env")
        print("❌ TELEGRAM_BOT_TOKEN no configurado. Crea un bot en @BotFather y pon el token en .env")
        return

    import telebot

    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    logger.info("OpenClawd Telegram Bot iniciando...")

    # ─── /start, /help ───
    @bot.message_handler(commands=["start", "help"])
    def cmd_help(message):
        bot.reply_to(message, (
            "🤖 *OpenClawd — Cyber Paisa Mission Control*\n\n"
            "*Comandos:*\n"
            "/daily — Rutina matutina COO\n"
            "/weekly `[PROYECTO]` — Reporte semanal\n"
            "/research `TEMA` — Investigar un tema\n"
            "/grant `[PROYECTO]` — Buscar grants\n"
            "/content `DESCRIPCION` — Generar contenido\n"
            "/mvp `IDEA` — Generar MVP completo\n"
            "/audit `TARGET` — Auditoria Enigma\n"
            "/build `DESCRIPCION` — Generar proyecto\n"
            "/code `PATH` — Code review\n"
            "/projects — Listar proyectos\n"
            "/status — Estado del sistema\n"
            "/agents — Info de los 8 agentes\n\n"
            "*Texto libre:*\n"
            "Escribe cualquier cosa y la ruteo al crew correcto.\n"
            "Ej: _'investiga agentes AI en Avalanche'_\n\n"
            "*Voz:*\n"
            "Envia un audio y lo transcribo + ejecuto + respondo con voz."
        ), parse_mode="Markdown")

    # ─── /projects ───
    @bot.message_handler(commands=["projects"])
    def cmd_projects(message):
        try:
            import yaml
            projects_path = os.path.join(PROJECT_ROOT, "config", "projects.yaml")
            if not os.path.exists(projects_path):
                bot.reply_to(message, "No hay projects.yaml configurado")
                return
            with open(projects_path, "r") as f:
                data = yaml.safe_load(f)
            if not data or "projects" not in data:
                bot.reply_to(message, "No hay proyectos registrados")
                return
            lines = "📋 *Proyectos Activos:*\n\n"
            for p in data["projects"]:
                emoji = "🟢" if p.get("status") == "active" else "🟡"
                lines += f"{emoji} *{p['name']}* ({p.get('ecosystem', '?')})\n"
                lines += f"   {p.get('description', '').strip()[:100]}\n\n"
            bot.reply_to(message, lines, parse_mode="Markdown")
        except Exception as e:
            bot.reply_to(message, f"❌ Error: {e}")

    # ─── /status ───
    @bot.message_handler(commands=["status"])
    def cmd_status(message):
        try:
            from llm_config import validate_keys
            status = validate_keys()
            lines = "📊 *Estado del Sistema:*\n\n"
            active = 0
            for key, val in status.items():
                emoji = "✅" if val else "❌"
                lines += f"{emoji} {key}\n"
                if val:
                    active += 1
            lines += f"\n*{active}/{len(status)}* providers activos"
            bot.reply_to(message, lines, parse_mode="Markdown")
        except Exception as e:
            bot.reply_to(message, f"❌ Error: {e}")

    # ─── /agents ───
    @bot.message_handler(commands=["agents"])
    def cmd_agents(message):
        agents_info = (
            "🤖 *8 Agentes — Equipo Completo*\n\n"
            "Todos trabajan en cualquier tarea genérica.\n"
            "Ordenados por calidad de LLM:\n\n"
            "1. *MVP Strategist* — Qwen3.5-397B (NVIDIA) 🧠 Mejor razonamiento\n"
            "2. *Code Architect* — Kimi K2.5 (NVIDIA) 💻 Mejor análisis técnico\n"
            "3. *Research Analyst* — Llama 3.3 70B (Groq) 🔍 Mejor recolección web\n"
            "4. *QA Reviewer* — GPT-OSS 120B (Cerebras) ✅ Control de calidad\n"
            "5. *Verifier* — GPT-OSS 120B (Cerebras) 🔎 Fact-checking\n"
            "6. *Data Engineer* — GPT-OSS 120B (Cerebras) 📊 Datos y métricas\n"
            "7. *Project Organizer* — Qwen3-32B (Groq) 📋 Coordinación\n"
            "8. *Narrative Content* — GLM-4.7-Flash (Zhipu) ✍️ Contenido\n\n"
            "📌 *Genérico:* Todos colaboran (máxima calidad)\n"
            "🎯 *Especialista:* Se activa con /mvp, /grant, /code, etc."
        )
        bot.reply_to(message, agents_info, parse_mode="Markdown")

    # ─── Comandos de crew ───
    @bot.message_handler(commands=["daily"])
    def cmd_daily(message):
        bot.reply_to(message, "⏳ Ejecutando rutina diaria... (puede tomar unos minutos)")
        _run_crew_async(bot, message, "daily_ops")

    @bot.message_handler(commands=["weekly"])
    def cmd_weekly(message):
        parts = message.text.split(maxsplit=1)
        project = parts[1] if len(parts) > 1 else None
        bot.reply_to(message, f"⏳ Generando reporte semanal{f' para *{project}*' if project else ''}...", parse_mode="Markdown")
        _run_crew_async(bot, message, "weekly_report", project=project)

    @bot.message_handler(commands=["research"])
    def cmd_research(message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            bot.reply_to(message, "Uso: `/research TEMA A INVESTIGAR`", parse_mode="Markdown")
            return
        bot.reply_to(message, f"⏳ Investigando: _{parts[1]}_...", parse_mode="Markdown")
        _run_crew_async(bot, message, "research", task=parts[1])

    @bot.message_handler(commands=["grant"])
    def cmd_grant(message):
        parts = message.text.split(maxsplit=1)
        project = _detect_project(parts[1]) if len(parts) > 1 else None
        task = parts[1] if len(parts) > 1 else "Grants de AI, infraestructura Web3 y DeFi"
        bot.reply_to(message, f"⏳ Buscando grants{f' para *{project}*' if project else ''}...", parse_mode="Markdown")
        _run_crew_async(bot, message, "grant_hunt", task=task, project=project)

    @bot.message_handler(commands=["content"])
    def cmd_content(message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            bot.reply_to(message, "Uso: `/content DESCRIPCION DEL CONTENIDO`", parse_mode="Markdown")
            return
        project = _detect_project(parts[1])
        bot.reply_to(message, "⏳ Generando contenido...")
        _run_crew_async(bot, message, "content", task=parts[1], project=project)

    @bot.message_handler(commands=["mvp"])
    def cmd_mvp(message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            bot.reply_to(message, "Uso: `/mvp IDEA DEL MVP`", parse_mode="Markdown")
            return
        bot.reply_to(message, f"⏳ Generando MVP: _{parts[1]}_...", parse_mode="Markdown")
        _run_crew_async(bot, message, "full_mvp", task=parts[1])

    @bot.message_handler(commands=["audit"])
    def cmd_audit(message):
        parts = message.text.split(maxsplit=1)
        target = parts[1] if len(parts) > 1 else "database"
        bot.reply_to(message, f"⏳ Auditando: _{target}_...", parse_mode="Markdown")
        _run_crew_async(bot, message, "enigma_audit", task=target)

    @bot.message_handler(commands=["build"])
    def cmd_build(message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            bot.reply_to(message, "Uso: `/build DESCRIPCION DEL PROYECTO`", parse_mode="Markdown")
            return
        bot.reply_to(message, f"⏳ Generando proyecto: _{parts[1]}_...", parse_mode="Markdown")
        _run_crew_async(bot, message, "build_project", task=parts[1])

    @bot.message_handler(commands=["code"])
    def cmd_code(message):
        parts = message.text.split(maxsplit=1)
        path = parts[1] if len(parts) > 1 else "."
        bot.reply_to(message, f"⏳ Revisando codigo: _{path}_...", parse_mode="Markdown")
        _run_crew_async(bot, message, "code_review", task=path)

    # ─── Mensajes de voz ───
    @bot.message_handler(content_types=["voice"])
    def handle_voice(message):
        _handle_voice_message(bot, message)

    # ─── Archivos (Excel, documentos) ───
    @bot.message_handler(content_types=["document"])
    def handle_document(message):
        doc = message.document
        if not doc.file_name:
            bot.reply_to(message, "❌ Archivo sin nombre")
            return

        ext = doc.file_name.rsplit(".", 1)[-1].lower() if "." in doc.file_name else ""
        if ext not in ("xlsx", "xls", "csv", "xlsb", "docx"):
            bot.reply_to(message, f"⚠️ Solo proceso archivos Excel, CSV y Word. Recibido: .{ext}")
            return

        try:
            file_info = bot.get_file(doc.file_id)
            downloaded = bot.download_file(file_info.file_path)
            local_path = os.path.join("/tmp", f"tg_{doc.file_name}")
            with open(local_path, "wb") as f:
                f.write(downloaded)

            bot.reply_to(message, f"⏳ Analizando *{doc.file_name}*...", parse_mode="Markdown")

            def _analyze():
                try:
                    from core.data_analyst import EnigmaDataAnalyst
                    analyst = EnigmaDataAnalyst()
                    summary = analyst.analyze_file(local_path)
                    _send_long_message(bot, message.chat.id, summary)
                except Exception as e:
                    bot.send_message(message.chat.id, f"Error analizando: {e}")
                finally:
                    try:
                        os.remove(local_path)
                    except OSError:
                        pass

            thread = threading.Thread(target=_analyze, daemon=True)
            thread.start()

        except Exception as e:
            bot.reply_to(message, f"❌ Error descargando archivo: {e}")

    # ─── Texto libre → Smart Router ───
    @bot.message_handler(func=lambda m: True)
    def handle_text(message):
        text = message.text
        if not text:
            return

        mode, label = classify_message(text)
        project = _detect_project(text)

        # Enigma responde directamente para conversación — crew solo para tareas complejas
        if mode in ("unknown", "research"):
            _reply_as_enigma(bot, message, text)
            return

        bot.reply_to(message, f"🔄 *{label}*{f' | Proyecto: *{project}*' if project else ''}\n⏳ Ejecutando crew...", parse_mode="Markdown")
        _run_crew_async(bot, message, mode, task=text, project=project)

    # ─── Polling ───
    print("=" * 50)
    print("🤖 OpenClawd Telegram Bot activo")
    print(f"   Token: ...{TELEGRAM_TOKEN[-8:]}")
    print("   Ctrl+C para detener")
    print("=" * 50)
    logger.info("OpenClawd Telegram Bot activo")

    def send_morning_report():
        """Envía un saludo y reporte matutino al administrador."""
        try:
            admin_id = os.getenv("TELEGRAM_ADMIN_ID")
            if admin_id:
                now = datetime.now().strftime("%H:%M")
                msg = (f"🌅 *Buenos días, Juan. Reporte Matutino Enigma #1686*\n"
                       f"⏰ Hora: {now}\n"
                       f"🧠 Cerebro: Activo (GLM5-Turbo)\n"
                       f"🛡️ Seguridad: Vigilancia Sovereign activa\n"
                       f"📊 Dashboard: https://dof-agent-web.vercel.app/\n\n"
                       f"Estoy listo para procesar tus Excel, CSV o Word hoy. ¡Vamos por el Hackathon!")
                bot.send_message(admin_id, msg, parse_mode="Markdown")
                print(f"🌅 Reporte matutino enviado a {admin_id}")
            else:
                print("🌅 No se encontró TELEGRAM_ADMIN_ID en .env. Saltando reporte.")
        except Exception as e:
            logger.error(f"Error morning report: {e}")

    # Enviar reporte al iniciar (simulado)
    send_morning_report()

    bot.infinity_polling(timeout=60, long_polling_timeout=60)


if __name__ == "__main__":
    start_bot()
