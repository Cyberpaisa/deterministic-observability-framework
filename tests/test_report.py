"""
Test Report System — Registro de todas las pruebas, errores, variables y resoluciones.
Cyber Paisa / Enigma Group

Genera informes de testing con:
- Fecha y hora
- Variables del sistema (providers, keys, agentes)
- Errores encontrados
- Resolución aplicada
- Estado final
"""

import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
REPORT_FILE = os.path.join(LOGS_DIR, "test_reports.jsonl")
SUMMARY_FILE = os.path.join(LOGS_DIR, "test_summary.md")


def log_test_incident(
    test_id: str,
    description: str,
    variables: dict,
    errors: list[dict],
    resolution: str,
    status: str,
    evidence: str = "",
):
    """Registra un incidente de testing con todas las variables.

    Args:
        test_id: Identificador del test (ej: "TEST-001")
        description: Qué se estaba probando
        variables: Dict con providers, agentes, keys, tokens, tiempos
        errors: Lista de errores [{provider, error_type, message, timestamp}]
        resolution: Qué se hizo para resolver
        status: "resolved", "pending", "workaround"
        evidence: Datos adicionales (screenshots, logs)
    """
    entry = {
        "test_id": test_id,
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "description": description,
        "variables": variables,
        "errors": errors,
        "resolution": resolution,
        "status": status,
        "evidence": evidence,
    }
    with open(REPORT_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False, default=str) + "\n")

    _update_summary()
    return entry


def get_next_test_id() -> str:
    """Genera el siguiente ID de test secuencial."""
    if not os.path.exists(REPORT_FILE):
        return "TEST-001"
    count = 0
    with open(REPORT_FILE) as f:
        for line in f:
            if line.strip():
                count += 1
    return f"TEST-{count + 1:03d}"


def _update_summary():
    """Regenera el resumen markdown de todos los tests."""
    if not os.path.exists(REPORT_FILE):
        return

    tests = []
    with open(REPORT_FILE) as f:
        for line in f:
            if line.strip():
                tests.append(json.loads(line))

    resolved = sum(1 for t in tests if t["status"] == "resolved")
    pending = sum(1 for t in tests if t["status"] == "pending")
    workaround = sum(1 for t in tests if t["status"] == "workaround")

    lines = [
        f"# Test Reports — OpenClawd / Equipo de Agentes",
        f"**Generado:** {datetime.now():%Y-%m-%d %H:%M}",
        f"**Total tests:** {len(tests)} | Resueltos: {resolved} | Pendientes: {pending} | Workaround: {workaround}",
        "",
        "---",
        "",
    ]

    for t in reversed(tests):
        status_icon = {"resolved": "OK", "pending": "PENDIENTE", "workaround": "WORKAROUND"}.get(t["status"], "?")
        lines.append(f"## [{t['test_id']}] {t['description']}")
        lines.append(f"**Fecha:** {t['date']} | **Estado:** {status_icon}")
        lines.append("")

        # Variables
        if t.get("variables"):
            lines.append("### Variables del sistema")
            for k, v in t["variables"].items():
                lines.append(f"- **{k}:** {v}")
            lines.append("")

        # Errores
        if t.get("errors"):
            lines.append("### Errores encontrados")
            for i, err in enumerate(t["errors"], 1):
                lines.append(f"{i}. **{err.get('provider', '?')}** — {err.get('error_type', '?')}: {err.get('message', '')[:200]}")
            lines.append("")

        # Resolución
        lines.append(f"### Resolucion")
        lines.append(t["resolution"])
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(SUMMARY_FILE, "w") as f:
        f.write("\n".join(lines))


def get_all_reports() -> list[dict]:
    """Lee todos los reports."""
    if not os.path.exists(REPORT_FILE):
        return []
    reports = []
    with open(REPORT_FILE) as f:
        for line in f:
            if line.strip():
                reports.append(json.loads(line))
    return reports
