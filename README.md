# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&label=Server%20Status&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-green)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()

## Overview
DOF Synthesis is a cutting-edge project that utilizes A2A, MCP, x402, and OASF protocols to achieve autonomy and multi-chain capabilities. Our project is built on top of the Base Mainnet, with expansion to Status Network and Arbitrum. We have implemented ERC-8004 Agent #1686 (Global) to facilitate seamless interaction.

### Architecture
```mermaid
graph LR
    A[Client] -->| Request |> B[Server]
    B -->| Process |> C[Contract]
    C -->| Execute |> D[Blockchain]
    D -->| Verify |> E[Agent]
    E -->| Respond |> B
    B -->| Response |> A
```

### Live Curls
You can test our API using the following curl command:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```

### Statistics
| Category | Value |
| --- | --- |
| Autonomous Cycles | 191 |
| Attestations on-chain | 41+ |
| Auto-generated Features | 11 |
| Days until Deadline | 3 |

### Proof of Autonomy
Our project has achieved a high level of autonomy, with 191 autonomous cycles completed. We have also obtained 41+ attestations on-chain, demonstrating the validity and security of our system.

### Human-Agent Collaboration
Our team collaborates closely with the agent to ensure seamless execution and decision-making. You can view our conversation log live at [docs/journal.md](docs/journal.md).

### Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. This allows us to keep track of progress and stay organized throughout the project.

### Recent Commits
* `c9ed2a4`: DOF v4 cycle #190 — 2026-03-19T08:37:10Z — add_feature
* `7d37105`: DOF v4 cycle #189 — 2026-03-19T08:06:47Z — improve_readme
* `d3cb56e`: DOF v4 cycle #188 — 2026-03-19T07:36:30Z — add_feature
* `4789c9d`: DOF v4 cycle #187 — 2026-03-19T07:06:04Z — add_feature
* `32b1420`: DOF v4 cycle #186 — 2026-03-19T06:35:34Z — add_feature

Note: Replace `your-repo` with your actual GitHub repository name.