# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/ethereum/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://雪崩区块链浏览器链接)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()
### Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system leveraging the power of A2A, MCP, x402, and OASF protocols. Our project features a deployed contract on the Avalanche network, with 1+ on-chain attestations and 1 completed autonomous cycle.

### Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 1+ |
| Autonomous cycles completed | 1 |
| Features auto-generated | 0 |
| Days until deadline | 7 |

### Architecture
```mermaid
graph LR;
    A2A -->|Communicates with|> MCP;
    MCP -->|Triggers|> x402;
    x402 -->|Executes|> OASF;
    OASF -->|Provides input to|> A2A;
    A2A -->|Interacts with|> Contract;
    Contract -->|Stores data on|> Blockchain;
```
### Live Demo
You can test our system by running the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/endpoint1
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/endpoint2
```
### Proof of Autonomy
Our system has completed 1 autonomous cycle, demonstrating its ability to operate independently. The contract address is `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` on the Avalanche network.

### Human-Agent Collaboration
Our team uses [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. You can view our conversation log, which is updated live, at [docs/conversation-log.md](docs/conversation-log.md).

### Git Log
Our recent commit history is as follows:
* `ea4df2c`: DOF v4 cycle #1 — 2026-03-15T03:21:46Z
* `0376a2e`: DOF v4 cycle #1 — 2026-03-15T03:14:59Z
* `2fe249c`: DOF v4 cycle #1 — 2026-03-15T03:13:01Z
* `67d4074`: DOF v4 cycle #1 — 2026-03-15T03:10:34Z
* `99d2179`: DOF v4 cycle #1 — 2026-03-15T03:06:01Z

### Current Decision
Our system is currently awaiting the next input to trigger the next autonomous cycle.

### Contract Details
* Contract Address: `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` (Avalanche)
* ERC-8004 Agent: #1686

Note: Replace `your-repo` with your actual GitHub repository name. Also, the contract address link should be replaced with the actual blockchain explorer link.