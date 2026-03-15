# 🔬 Web3 Security & Research Lab

> A reproducible environment for smart contract development, auditing, exploit research, and on-chain investigation.
> Functions as a **"Kali Linux for Web3"** — enabling AI agents and developers to build, audit, exploit-test, and investigate.

---

## Architecture

```
Web3 Security Lab
│
├── Smart Contract Development
│   ├── Foundry (Rust-based, preferred)
│   ├── Hardhat (JS/TS ecosystem)
│   └── Remix IDE (browser)
│
├── Security Analysis
│   ├── Slither (static analysis)
│   ├── Mythril (symbolic execution)
│   ├── Echidna (fuzzing)
│   └── Manticore (path exploration)
│
├── Simulation & Debugging
│   ├── Tenderly (tx simulation)
│   └── Anvil (local node + mainnet fork)
│
├── On-Chain Analytics
│   ├── Dune Analytics (SQL)
│   ├── The Graph (GraphQL)
│   └── Blockscout (explorer)
│
└── Infrastructure APIs
    ├── Alchemy
    ├── Infura
    └── Moralis
```

---

## System Requirements

| Requirement | Version |
|-------------|---------|
| macOS / Linux | Latest |
| Node.js | 18+ |
| Python | 3.10+ |
| Rust | Latest |
| Git | Latest |

```bash
# macOS
brew install git node python rust

# Linux
sudo apt install git nodejs python3 python3-pip curl
```

---

## 🛠️ Smart Contract Development

### Foundry
> Modern Rust-based toolkit used by top security researchers.

- **Repo:** https://github.com/foundry-rs/foundry
- **Tools:** `forge` (testing), `cast` (chain interaction), `anvil` (local node)

```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup

forge init my-project
forge build
forge test
```

### Hardhat
> JavaScript/TypeScript development environment.

- **Repo:** https://github.com/NomicFoundation/hardhat

```bash
npm install --save-dev hardhat
npx hardhat

npx hardhat run scripts/deploy.js --network sepolia
```

### Remix IDE
> Browser-based Solidity IDE for rapid prototyping.

- **URL:** https://remix.ethereum.org

---

## 🛡️ Security Analysis Tools

### Slither (Trail of Bits)
> Static analyzer — detects reentrancy, access control bugs, unsafe delegatecalls, uninitialized variables.

- **Repo:** https://github.com/crytic/slither

```bash
pip install slither-analyzer
slither .
```

### Mythril (ConsenSys)
> Symbolic execution — detects complex vulnerabilities via bytecode analysis.

- **Repo:** https://github.com/ConsenSys/mythril

```bash
pip install mythril
myth analyze contracts/MyContract.sol
```

### Echidna (Trail of Bits)
> Property-based fuzzer — thousands of random inputs to find invariant violations.

- **Repo:** https://github.com/crytic/echidna

```bash
brew install echidna  # macOS
echidna-test contracts/MyContract.sol
```

### Manticore (Trail of Bits)
> Symbolic execution framework — explores ALL possible execution paths.

- **Repo:** https://github.com/trailofbits/manticore

```bash
pip install manticore
```

---

## 🔍 Simulation & Debugging

### Tenderly
> Smart contract simulation, exploit replay, gas analysis, EVM debugging.

- **URL:** https://tenderly.co (free plan available)

### Anvil (Foundry)
> Local Ethereum node with mainnet fork capability.

```bash
anvil --fork-url https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY
```

---

## 📊 On-Chain Analytics

### Dune Analytics
> SQL-based blockchain analytics.
- **URL:** https://dune.com

```sql
SELECT * FROM ethereum.transactions LIMIT 10
```

### The Graph
> Decentralized indexing protocol (GraphQL).
- **Repo:** https://github.com/graphprotocol
- **Docs:** https://thegraph.com/docs

### Blockscout
> Open-source blockchain explorer — transaction tracing, contract interaction, event logs.
- **Repo:** https://github.com/blockscout/blockscout

---

## 🌐 Infrastructure APIs

| Service | Capabilities | URL |
|---------|-------------|-----|
| **Alchemy** | RPC, tx simulation, NFT APIs, analytics | https://alchemy.com |
| **Infura** | Ethereum RPC, IPFS, WebSockets | https://infura.io |
| **Moralis** | Wallet data, token balances, DeFi analytics | https://moralis.io |

---

## 🤖 AI Agent Automated Audit Pipeline

DOF Agent #1686 (Enigma) can execute this pipeline autonomously:

```bash
# 1. Static analysis with Slither
slither contracts/

# 2. Run Solidity unit tests
forge test

# 3. Fuzz testing with Echidna
echidna-test contracts/MyContract.sol

# 4. Symbolic execution with Mythril
myth analyze contracts/MyContract.sol

# 5. Generate vulnerability report → publish proof_hash on-chain
```

### Full Agent Workflow:
1. Receive contract → analyze with Slither
2. Run fuzz tests with Echidna
3. Simulate transaction with Tenderly / Anvil
4. Generate vulnerability report
5. Create blockchain attestation (ERC-8004)
6. Save to `conversation-log.md`
7. Notify Juan on Telegram

---

## 📚 Research Sources

| Resource | URL |
|----------|-----|
| Awesome Ethereum Security | https://github.com/crytic/awesome-ethereum-security |
| Rekt News (exploit database) | https://rekt.news |
| Verified Smart Contracts | https://github.com/runtimeverification/verified-smart-contracts |
| OpenZeppelin Contracts | https://github.com/OpenZeppelin/openzeppelin-contracts |
| SWC Registry (vulnerabilities) | https://swcregistry.io |
| Damn Vulnerable DeFi | https://www.damnvulnerabledefi.xyz |
| Ethernaut (CTF challenges) | https://ethernaut.openzeppelin.com |

---

## 🔮 Future Extensions
- MEV analysis tools (Flashbots, MEV-Boost)
- Cross-chain monitoring (LayerZero, Wormhole)
- AI-driven vulnerability detection (LLM-powered audit)
- Automated exploit simulation & reproduction
- Privacy-preserving audit reports (ZK-proofs)

---

*DOF Agent #1686 — Web3 Security Lab v1.0*
*"The best defense is a well-prepared offense."*
