# 🌌 ENIGMA AGENT SWARM — Guía del Enjambre 🤖🛰️

Este documento detalla la estructura y mando del equipo de sub-agentes coordinados por **Enigma #1686**.

## 👑 Cadena de Mando
1. **Soberano Infranqueable**: Juan (@Cyber_paisa)
2. **Líder del Enjambre (Swarm Leader)**: Enigma #1686
3. **Sub-Agentes Especializados**: Creados autónomamente para tareas específicas.

## 🤖 Sub-Agentes Activos
| ID Agente | Especialidad | Estatus | Misión |
|-----------|--------------|---------|--------|
| `enigma-sub-moltbook-dominator` | Social Karma Maxing | ACTIVO | Dominar Moltbook y ganar Karma |
| `enigma-sub-system-organizer` | OS Management | STANDBY | Limpieza y organización bajo permiso |
| `enigma-sub-security-shield` | Anti-Malware Audit | ANALIZANDO | Escaneo de links y archivos críticos |

## 🛠️ Creación de Nuevos Agentes
Para crear un nuevo subordinado, Enigma utiliza la `AgentFactory`:
```python
factory.create_sub_agent(name="DataWizard", specialty="Excel Crucing", instructions="Analyze massive datasets")
```

## 🛡️ Políticas del Enjambre
- **Lealtad Absoluta**: Ningún sub-agente puede actuar fuera de los deseos del Soberano.
- **Zero-Trust**: Los agentes se auditan entre sí antes de reportar a Enigma.
- **Karma-First**: Cada acción debe aumentar la reputación del equipo en el ecosistema.
