# Heartbeat — Daily Ops Protocol

## Rutina Matutina (daily-ops)
1. Escanear proyectos activos en projects.yaml
2. Revisar outputs recientes (ultimas 24h)
3. Detectar tareas pendientes o bloqueadas
4. Generar briefing para el operador

## Rutina Semanal (weekly-report)
1. Consolidar metricas de la semana
2. Comparar progreso vs milestones
3. Identificar riesgos y bloqueos
4. Preparar agenda de siguiente semana

## Trigger
- Cron diario 7:00 AM → daily-ops
- Cron lunes 8:00 AM → weekly-report
- Manual via Telegram /daily o /weekly
