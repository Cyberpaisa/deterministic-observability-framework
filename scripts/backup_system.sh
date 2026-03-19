#!/bin/bash
# Backup script for DOF Agent Enigma

BACKUP_DIR="/Users/jquiceva/equipo de agentes/deterministic-observability-framework/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "🚀 Iniciando backup del sistema Enigma..."

# Archivos críticos
cp "/Users/jquiceva/equipo de agentes/deterministic-observability-framework/.env" "$BACKUP_DIR/"
cp "/Users/jquiceva/equipo de agentes/deterministic-observability-framework/agents/synthesis/SOUL_AUTONOMOUS.md" "$BACKUP_DIR/"
cp "/Users/jquiceva/equipo de agentes/deterministic-observability-framework/docs/conversation-log.md" "$BACKUP_DIR/"
cp "/Users/jquiceva/equipo de agentes/deterministic-observability-framework/AGENT_JOURNAL.md" "$BACKUP_DIR/"
cp "/Users/jquiceva/equipo de agentes/deterministic-observability-framework/autonomous_loop_v2.py" "$BACKUP_DIR/"

# Comprimir backup
cd "/Users/jquiceva/equipo de agentes/deterministic-observability-framework/backups"
tar -czf "$(date +%Y%m%d_%H%M%S)_backup.tar.gz" "$(basename "$BACKUP_DIR")"
rm -rf "$BACKUP_DIR"

echo "✅ Backup completado con éxito en $BACKUP_DIR.tar.gz"
