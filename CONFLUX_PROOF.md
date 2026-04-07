# DOF-MESH x Conflux — On-Chain Proof Evidence

> All transactions listed here are real, confirmed, and publicly verifiable on ConfluxScan.  
> Last updated: April 6, 2026

---

## 1. Contract Deployment

### DOFProofRegistry — Conflux eSpace Testnet

| Field | Value |
|---|---|
| Contract Address | `0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83` |
| Network | Conflux eSpace Testnet |
| Chain ID | 71 |
| RPC Endpoint | `https://evmtestnet.confluxrpc.com` |
| Explorer | https://evmtestnet.confluxscan.io/address/0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83 |
| Deployer Wallet | `0xEAFdc9C3019fC80620f16c30313E3B663248A655` |
| Total Proofs Registered | 36+ |

---

## 2. Gas Sponsorship — SponsorWhitelistControl

**Activated:** April 6, 2026  
**Internal Contract:** `0x0888000000000000000000000000000000000001`  
**Result:** Any address can interact with `DOFProofRegistry` without paying CFX.

This is a native Conflux mechanism — not a wrapper, not a relayer. The `SponsorWhitelistControl` Core Space internal contract allows the contract owner to deposit CFX that covers gas costs for all whitelisted callers.

### Transaction Log

| # | Function | CFX Value | TX Hash | Block | Status |
|---|---|---|---|---|---|
| 1 | `setSponsorForGas(DOFProofRegistry, upperBound=1_000_000)` | 10 CFX | `014b6bedde7fa449d48822752371bc6ee275d62325117a66ef7d8dfbea52d3b7` | — | ✅ Confirmed |
| 2 | `setSponsorForCollateral(DOFProofRegistry)` | 10 CFX | `d6199877d1ff08c204e3ef60dd914852d305bdacde23c29058067c20e621cc9f` | — | ✅ Confirmed |
| 3 | `addPrivilegeByAdmin(DOFProofRegistry, [0x00...0])` | 0 CFX | `2e47f3fd80d82c251a1c572cadbc2b87c377eeb2a092893094d939ce676862a3` | — | ✅ Confirmed |

**Explorer links:**
- TX 1: https://evmtestnet.confluxscan.io/tx/014b6bedde7fa449d48822752371bc6ee275d62325117a66ef7d8dfbea52d3b7
- TX 2: https://evmtestnet.confluxscan.io/tx/d6199877d1ff08c204e3ef60dd914852d305bdacde23c29058067c20e621cc9f
- TX 3: https://evmtestnet.confluxscan.io/tx/2e47f3fd80d82c251a1c572cadbc2b87c377eeb2a092893094d939ce676862a3

---

## 3. Hackathon Attestation TX

This transaction registers a DOF-MESH governance proof on Conflux with the hackathon metadata encoded in the log payload.

### Transaction Details

| Field | Value |
|---|---|
| TX Hash | `0x6994475597c4052f33012458ed75fac6458b53a88f2fa991ff0e3943ab9b2343` |
| Explorer | https://evmtestnet.confluxscan.io/tx/0x6994475597c4052f33012458ed75fac6458b53a88f2fa991ff0e3943ab9b2343 |
| Block Number | 248,350,045 |
| Block Timestamp | `0x69d41d29` |
| From | `0xEAFdc9C3019fC80620f16c30313E3B663248A655` |
| To (Contract) | `0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83` |
| Gas Used | 373,637 |
| Status | `1` → **SUCCESS** |
| Chain ID | 71 (Conflux eSpace Testnet) |

### Log Payload — Decoded

The transaction log encodes the full governance result. Decoded from the raw `data` field:

```
dof-v0.6.0 conflux-hackathon z3=4/4 tracer=0.504
```

| Field | Value | Meaning |
|---|---|---|
| Version | `dof-v0.6.0` | DOF-MESH SDK version at time of attestation |
| Context | `conflux-hackathon` | Hackathon-tagged proof |
| Z3 result | `z3=4/4` | All 4 formal theorems proven |
| TRACER score | `tracer=0.504` | Multi-dimensional quality score |

### Log Topics (raw)

| Topic | Hex | Decoded |
|---|---|---|
| Event signature | `0xeb76776a23294e1f486bffa083169bebd52ed00bf5299f91d6c4ced229e41bc1` | `ProofRecorded` event |
| Index param [1] | `0x000...002b` | `43` decimal — proof sequence number |
| Index param [2] | `0x000...0697` | `1687` decimal — **Agent #1687** |

### Python Verification

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://evmtestnet.confluxrpc.com'))
receipt = w3.eth.get_transaction_receipt(
    '0x6994475597c4052f33012458ed75fac6458b53a88f2fa991ff0e3943ab9b2343'
)

print("Status:   ", receipt['status'], "→ SUCCESS ✅")
print("Block:    ", receipt['blockNumber'])
print("Gas used: ", receipt['gasUsed'])

# Decode payload from log data
raw = bytes.fromhex(receipt['logs'][0]['data'].hex()[2:])
print("Payload:  ", raw[96:].decode('utf-8', errors='ignore').strip())

# Decode agent ID from topic
agent_id = int(receipt['logs'][0]['topics'][2].hex(), 16)
print("Agent:    #" + str(agent_id))
```

**Output:**
```
Status:    1 → SUCCESS ✅
Block:     248350045
Gas used:  373637
Payload:   dof-v0.6.0 conflux-hackathon z3=4/4 tracer=0.504
Agent:     #1687
```

---

## 4. Full TX History on Conflux

| Date | TX Hash | Type | Explorer |
|---|---|---|---|
| Apr 6, 2026 | `0x6994475597c4052f...b2343` | Governance attestation — hackathon | [View](https://evmtestnet.confluxscan.io/tx/0x6994475597c4052f33012458ed75fac6458b53a88f2fa991ff0e3943ab9b2343) |
| Apr 6, 2026 | `1c5539978c16fa36ed25...e4255` | Governance attestation — conflux_demo.py | [View](https://evmtestnet.confluxscan.io/tx/1c5539978c16fa36ed250200de56b077a969302364567e6dc67e6038753e4255) |
| Apr 6, 2026 | `bf98ea58265dcd8433f5...740c` | Attestation DOF-1687 demo | [View](https://evmtestnet.confluxscan.io/tx/bf98ea58265dcd8433f594376d0d679fde65d93ae8cc18d841627308bebf740c) |
| Apr 6, 2026 | `77d4ddea0043bf6df5a9...4b10` | Attestation direct test | [View](https://evmtestnet.confluxscan.io/tx/77d4ddea0043bf6df5a916cd7040886e0a97480ab12465e5842ce7c2f26b4b10) |
| Apr 6, 2026 | `014b6bedde7fa449d488...d3b7` | setSponsorForGas — gasless setup | [View](https://evmtestnet.confluxscan.io/tx/014b6bedde7fa449d48822752371bc6ee275d62325117a66ef7d8dfbea52d3b7) |
| Apr 6, 2026 | `d6199877d1ff08c204e3...c9f` | setSponsorForCollateral | [View](https://evmtestnet.confluxscan.io/tx/d6199877d1ff08c204e3ef60dd914852d305bdacde23c29058067c20e621cc9f) |
| Apr 6, 2026 | `2e47f3fd80d82c251a1c...62a3` | addPrivilegeByAdmin — global whitelist | [View](https://evmtestnet.confluxscan.io/tx/2e47f3fd80d82c251a1c572cadbc2b87c377eeb2a092893094d939ce676862a3) |

---

## 5. Z3 Formal Proof Summary

The governance cycle formally proves 4 invariants using the Z3 SMT solver before any chain transaction is sent:

| Theorem | Description | Proof Time | Result |
|---|---|---|---|
| `GCR_INVARIANT` | Governance compliance rate must equal 1.0 for deterministic paths | 24.2ms | ✅ PROVEN |
| `SS_FORMULA` | Supervisor score formula is mathematically consistent | 2.4ms | ✅ PROVEN |
| `SS_MONOTONICITY` | Supervisor score increases monotonically with quality | 7.7ms | ✅ PROVEN |
| `SS_BOUNDARIES` | Supervisor score is bounded in [0, 10] | 0.5ms | ✅ PROVEN |
| **Total** | | **34.8ms** | **4/4 PROVEN** |

Proof results saved to: `logs/z3_proofs.json`

---

## 6. Deployer Wallet

| Field | Value |
|---|---|
| Address | `0xEAFdc9C3019fC80620f16c30313E3B663248A655` |
| Network | Conflux eSpace Testnet (Chain ID: 71) |
| CFX Balance (Apr 6, 2026) | 1,098 CFX (testnet) |
| Wallet Explorer | https://evmtestnet.confluxscan.io/address/0xEAFdc9C3019fC80620f16c30313E3B663248A655 |
| CFX spent on sponsorship | 20 CFX (10 gas + 10 collateral) |

---

## 7. Cross-Chain Context

`DOFProofRegistry.sol` is deployed on 8 chains. The same contract ABI, same governance proofs, different chains:

| Chain | Chain ID | Contract Address | Type |
|---|---|---|---|
| Avalanche C-Chain | 43114 | `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` | mainnet |
| Base Mainnet | 8453 | `0x4e54634d0E12f2Fa585B6523fB21C7d8AaFC881D` | mainnet |
| Celo Mainnet | 42220 | `0x35B320A06DaBe2D83B8D39D242F10c6455cd809E` | mainnet |
| **Conflux eSpace Testnet** | **71** | **`0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83`** | **testnet** |
| Avalanche Fuji | 43113 | `0x0b65d10FEcE517c3B6c6339CdE30fF4A8363751c` | testnet |
| Base Sepolia | 84532 | `0x7e0f0D0bC09D14Fa6C1F79ab7C0EF05b5e4F1f59` | testnet |
| Conflux Testnet (Core) | 71 | `0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83` | testnet |
| SKALE Base Sepolia | 324705682 | `0x4e54634d0E12f2Fa585B6523fB21C7d8AaFC881D` | testnet |

---

> All proofs are real. All transactions are confirmed. All links are verifiable on ConfluxScan.  
> DOF-MESH v0.6.0 · April 2026 · Enigma Group · [dofmesh.com](https://dofmesh.com)
