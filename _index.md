# _index — System State
# Auto-updated by Kernel Boot

## Last Session
- **Date:** 2026-03-06
- **Crews executed:** 1

## Last Executions
- `2026-03-02T12:44` | research | success | 40.6s
- `2026-03-02T12:54` | research | success | 48.6s

## System Metrics
- **Total executions:** 2
- **Success rate:** 2/2 (100%)
- **Most used crew:** research (2x)
- **Average time:** 45s

## DOF Status (2026-03-06)
- **Tests:** 719/719 passing (3.9s)
- **LOC:** 27,000+ across 76 Python files
- **Core modules:** 25
- **Z3:** 4/4 theorems verified
- **Governance:** ready (4 HARD + 5 SOFT rules)
- **AST Verifier:** ready
- **Privacy benchmark:** 71% DR, 1% FPR
- **OpenTelemetry:** optional (pip install dof-sdk[otel])
- **EventBus:** in-memory, Redis/Kafka ready

## On-Chain Status
- **Attestations:** 21 on Avalanche C-Chain mainnet
- **Contract:** DOFValidationRegistry at 0x88f6...C052
- **Deployer balance:** ~0.10 AVAX
- **Agents:** #1687 (Apex, 0.85 trust), #1686 (AvaBuilder, 0.85 trust)

## Enigma Status
- **dof_trust_scores:** 24 rows
- **combined_trust_view:** both agents COMPLIANT

## PyPI
- **Package:** dof-sdk 0.2.0
- **Install:** `pip install dof-sdk`

## Last Audit
- **Date:** 2026-03-06
- **Type:** Full 10-round agent cross-transactions
- **Result:** 10/10 rounds completed, GCR 1.0, Z3 4/4
- **Attestations added:** +10 (11 → 21)
- **Enigma scores published:** 10 via token_id
- **Centinela cross-reference:** both agents 0.85 combined trust
