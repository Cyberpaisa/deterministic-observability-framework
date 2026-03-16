# 🥩 Lido MCP Integration Skill

## Objetivo
Proveer un servidor MCP completo para interactuar con Lido Protocol.

## Endpoints implementados

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/mcp/lido/stake` | POST | Stakear ETH y recibir stETH (simulado) |
| `/mcp/lido/apy` | GET | Obtener APY actual de staking |
| `/mcp/lido/balance` | GET | Consultar balance de stETH de una wallet |
| `/mcp/lido/governance/proposals` | GET | Listar propuestas activas de Lido DAO |
| `/mcp/lido/governance/vote` | POST | Votar en propuesta (simulado) |

## Integración con DOF
En ciclos financieros, DOF puede:
1. Consultar APY actual
2. Simular staking de ETH inactivo
3. Monitorear gobernanza de Lido
4. Reportar oportunidades en journal.md

## Evidencia para jueces
- Código en `synthesis/server.py`
- Demos en `synthesis/lido_demo.py`
- Documentación en `docs/LIDO_INTEGRATION.md`
