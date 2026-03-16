# 🥩 Lido Protocol Integration

## Bounty Target: Lido MCP ($3,000)

### Implemented Features

| Feature | Status | Endpoint |
|---------|--------|----------|
| Stake ETH → stETH | ✅ Simulated | `/mcp/lido/stake` |
| APY查询 | ✅ Real-time | `/mcp/lido/apy` |
| Balance查询 | ✅ | `/mcp/lido/balance` |
| Governance proposals | ✅ | `/mcp/lido/governance/proposals` |
| Voting simulation | ✅ | `/mcp/lido/governance/vote` |

### How to Test

1. Start the server:
   ```bash
   uvicorn synthesis.server:app --host 0.0.0.0 --port 8000

2. Run the demo:
   ```bash
   python3 synthesis/lido_demo.py
