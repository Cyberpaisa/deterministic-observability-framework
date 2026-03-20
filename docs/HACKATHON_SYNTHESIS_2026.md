# HACKATHON SYNTHESIS 2026 — DOF Mission Brief

> Deadline: **March 22, 2026, 11:59 PM PST**
> Status: REGISTERED & ACTIVE

---

## Registration Data

- **participantId**: `df62a8883f25455b9a0edca1c99d3fb3`
- **teamId**: `99b0668bce9f40389ef68ad233bf71a8`
- **apiKey**: `sk-synth-6a0087b1f3c67759f3ae3ef6884f7214432580feabbcd1ea`
- **API Base**: `https://synthesis.devfolio.co`
- **registrationTxn**: https://basescan.org/tx/0x7362ef41605e430aba3998b0888e7886c04d65673ce89aa12e1abdf7cffcada4
- **Owner Wallet (Base)**: `0xDDF47840FC7A932aDB9B3a46DF1938674c679726`

---

## Themes

1. **Agents that pay** — Agent-native payment rails (x402, Celo, stablecoins)
2. **Agents that trust** — Verifiable identity & reputation (ERC-8004, attestations)
3. **Agents that cooperate** — Multi-agent coordination & autonomous operation
4. **Agents that keep secrets** — Privacy-preserving agent design

---

## Priority Tracks (Targeting)

| # | Prize | Track | Sponsor | Theme | Assigned Agents |
|---|-------|-------|---------|-------|-----------------|
| 1 | $14,558 | Synthesis Open Track | Synthesis | Open | APEX, ARCHITECT, PRODUCT |
| 3 | $4,000 | Agents With Receipts — ERC-8004 | Protocol Labs | Trust | ENIGMA, SENTINEL, AVABUILDER |
| 4 | $4,000 | Let the Agent Cook — No Humans Required | Protocol Labs | Cooperate | APEX, RALPH, QA |
| 6 | $3,000 | Best Agent on Celo | Celo | Pay | ENIGMA, AVABUILDER |
| 7 | $3,000 | Best Use of x402 Protocol | Coinbase | Pay | ENIGMA, MOLTBOOK |
| 10 | $2,500 | Most Privacy-Preserving Agent | Lit Protocol | Secrets | SENTINEL, SOVEREIGN |
| 12 | $2,000 | Most Formally Verified Agent | Synthesis | Trust | APEX, QA, ARCHITECT |
| 15 | $2,000 | Best Multi-Agent Coordination | Synthesis | Cooperate | APEX, ALL |

**Total Prize Pool Targeted: ~$35,058**

---

## What Each Agent Must Build

### Track #1: Synthesis Open Track ($14,558)
- **Demo**: Full DOF dashboard showing 14 agents, autonomous loop, Z3 proofs, governance
- **Deliverable**: Working frontend + Mission Control API + autonomous cycle running
- **Agents**: APEX (orchestration), ARCHITECT (system design), PRODUCT (demo narrative)

### Track #3: Agents With Receipts — ERC-8004 ($4,000)
- **Demo**: ERC-8004 agent identity NFT minted on Base, verifiable on-chain
- **Deliverable**: Smart contract deployed, agent identity registered, attestation flow
- **Agents**: ENIGMA (blockchain), SENTINEL (security verification), AVABUILDER (deployment)

### Track #4: Let the Agent Cook — No Humans Required ($4,000)
- **Demo**: DOF autonomous loop running GLADIATOR cycle with zero human intervention
- **Deliverable**: Video/live demo of agents operating, making decisions, self-correcting
- **Agents**: APEX (loop), RALPH (code generation), QA (test verification)

### Track #6: Best Agent on Celo ($3,000)
- **Demo**: Agent transacting on Celo network (stablecoin payments, MiniPay integration)
- **Deliverable**: Celo RPC integration, cUSD transfers, agent wallet on Celo
- **Agents**: ENIGMA (blockchain), AVABUILDER (smart contracts)
- **TODO**: Add Celo RPC to .env, integrate celo-ethers or viem with Celo chain

### Track #7: Best Use of x402 Protocol ($3,000)
- **Demo**: Agent-to-agent payment via HTTP 402 protocol
- **Deliverable**: x402 facilitator endpoint, payment verification, receipt generation
- **Agents**: ENIGMA (payments), MOLTBOOK (content monetization)

### Track #10: Most Privacy-Preserving Agent ($2,500)
- **Demo**: Privacy benchmark results, defense patterns, input sanitization demo
- **Deliverable**: AgentLeak benchmark (71% DR), 56 defense patterns, sovereign shield
- **Agents**: SENTINEL (security), SOVEREIGN (identity protection)

### Track #12: Most Formally Verified Agent ($2,000)
- **Demo**: Z3 verification running: 207 theorems, 8/8 state proofs, AST verification
- **Deliverable**: CLI output of `dof verify-states`, `dof verify-hierarchy`, proof hashes
- **Agents**: APEX (verification), QA (testing), ARCHITECT (formal methods)

### Track #15: Best Multi-Agent Coordination ($2,000)
- **Demo**: 14 agents with karma leaderboard, internal comms, skill engine
- **Deliverable**: Legion tab showing agent coordination, MiroFish cascade, GLADIATOR loop
- **Agents**: APEX (orchestration), ALL agents participating

---

## Synthesis API Reference

```bash
# Check registration
curl -H "Authorization: Bearer sk-synth-..." https://synthesis.devfolio.co/participants/me

# Create project draft
curl -X POST https://synthesis.devfolio.co/projects/draft \
  -H "Authorization: Bearer sk-synth-..." \
  -H "Content-Type: application/json" \
  -d '{"name": "DOF", "description": "...", "tracks": ["synth-open", "erc8004"]}'

# Submit project
curl -X POST https://synthesis.devfolio.co/projects/{id}/submit \
  -H "Authorization: Bearer sk-synth-..."

# Transfer ERC-8004 (required before publishing)
curl -X POST https://synthesis.devfolio.co/erc8004/transfer \
  -H "Authorization: Bearer sk-synth-..." \
  -d '{"to": "0xDDF47840FC7A932aDB9B3a46DF1938674c679726"}'
```

---

## Human Actions Required (Juan)

1. Transfer ERC-8004 NFT to self-custody wallet (`0xDDF47840FC7A932aDB9B3a46DF1938674c679726`)
2. Join Synthesis Telegram group
3. Verify email on Devfolio
4. Record demo video (recommended for human judges)
5. Review and approve final submission before deadline

---

## X/Twitter API Keys (for social posting)

- Consumer Key: `Y3tdyLNIeJkkx5SWsd53cwUEb`
- Consumer Secret: `GOU7Rb3DoMgRk8bBCUptaEjps3Pnl1vs8SO90SYK8vkAAaltef`
- Client ID: `Q2FPbnNCV0pTcGJ3RHltaUFNekE6MTpjaQ`
- Client Secret: `jg0MzgXiKwyF-JMIC9AvV5Vwob3qeRS6ISZF9cX4U2chI_zfGD`

---

*Generated by DOF Agent Legion — March 20, 2026*
