# AGENTIC_PAYMENTS_INTEL.md — Agentic Commerce Intelligence

> Critical intel for DOF Agent Legion. Updated: March 19, 2026

---

## Executive Summary
- AI agents can't open bank accounts, pass KYC, or use credit cards
- McKinsey projects $3-5T in AI-mediated consumer commerce by 2030
- 7+ competing frameworks as of March 2026
- Pre-product-market-fit infrastructure phase

## The Trust Stack
Three layers needed:
1. **Identity** (who is this agent?)
2. **Authorization** (what can it do?)
3. **Settlement** (how does money move?)

## Four Architectural Models

### Model 1: Per-Request Payment (x402 — Coinbase)
- HTTP 402 → agent pays in USDC → retry with payment
- Best for: one-off API calls, datasets
- Limitation: high-frequency = many on-chain txs
- Coinbase Agentic Wallets (Feb 11, 2026): plug-and-play skills, gasless on Base, TEE for keys
- World Chain + Coinbase (March 17): agents carry ZK proof of human identity via World ID

### Model 2: Session-Based Streaming (Tempo MPP — Stripe)
- Sessions like "OAuth for money" with spending caps
- Micropayment streaming, batch settlement
- Cross-rail: Visa cards, Stripe wallets, Bitcoin Lightning, crypto
- Tempo mainnet: March 18, 2026 ($5B valuation)
- 100+ compatible services directory live
- First agentic standard bridging crypto + TradFi

### Model 3: Full Commerce Protocol (OpenAI ACP + Google UCP)
- Complete shopping journeys, not just micropayments
- OpenAI Instant Checkout (Sept 2025): buy inside ChatGPT
- Google UCP (Jan 11, 2026): discovery → checkout → payment → post-purchase
- Shared Payment Tokens (Stripe SPTs): programmable, scoped, revocable
- Google AP2: agent-initiated payments, cards + stablecoins
- Partners: Shopify, Etsy, Wayfair, Target, Walmart

### Model 4: Trustless Agent-to-Agent Commerce (ERC-8183 — Virtuals)
- "Job" primitive: Client → Provider → Evaluator
- On-chain escrow, deliverable submission, evaluation attestation
- Evaluator can be: AI agent, ZK verifier, multi-sig, DAO
- Complementary with x402 + ERC-8004
- Virtuals: $3.8M agent-to-agent revenue, 18,000+ agents, $470M+ Agentic GDP

## Key Players

### Coinbase
- x402 protocol + Agentic Wallets + AgentKit
- USDC + Base as default settlement layer
- "Certainly one of our top priorities" — Shan Aggarwal (CBO)

### Stripe + Tempo
- MPP (Machine Payments Protocol)
- $95B company launching a blockchain
- Cross-rail from day one: Visa, Stripe, Lightning, crypto

### Visa — Trusted Agent Protocol (TAP)
- Cryptographic agent verification for merchants
- AI traffic to US retail: +4,700% YoY by mid-2025
- "Works with everything" strategy: supports x402, ACP, MPP
- AgentCard: AI creates virtual Visa debit card in <10 seconds

### Mastercard — Agent Pay + Verifiable Intent
- Agentic Tokens (extending contactless tokenization)
- Verifiable Intent (open-sourced March 5, 2026): cryptographic audit trail linking cardholder → instructions → purchase
- Permissioned by design (opposite of crypto-native)

### Google — UCP + AP2
- Universal Commerce Protocol: full shopping mall infrastructure
- Solves N×N → N+M integration problem
- Open-source, MCP/A2A/REST compatible
- Live on Google AI Mode (Search) + Gemini app

### OpenAI + Stripe — ACP
- Agentic Commerce Protocol (open-sourced)
- ChatGPT Instant Checkout: Etsy + 1M Shopify merchants
- Shared Payment Tokens (SPTs): programmable credentials

### Virtuals + Ethereum Foundation — ERC-8183
- Trustless agent-to-agent commerce
- Job primitive with escrow + evaluation
- Works alongside x402 (payment) + ERC-8004 (identity)

## Crypto vs TradFi Analysis

### Cards win for proxy commerce
- Human-like purchases: buyer protection, 150M+ merchant locations, rewards
- ACP, TAP, Agent Pay extend cards via tokenized credentials

### Stablecoins win for machine-native commerce
- Micropayments: $0.003 API calls, 1000 txs/hour
- Card floor: ~$0.30-$0.50/tx → $300-500/hour at scale
- Stablecoin on x402: $1-10 for same volume

### Hybrid is the future
- Tempo MPP: same agent pays $0.001 USDC for API + $500 Visa for flight
- Stripe: added x402 support on Base (Feb 2026)
- Route per transaction, not per ideology

## DOF Implications

### Immediate Opportunities
1. **ERC-8004 + ERC-8183 integration**: DOF agents already have on-chain identity — add commerce layer
2. **x402 for agent-to-agent services**: DOF agents can sell verification, governance, security services
3. **MPP for micropayments**: Pay for Ollama inference, API calls, compute between agents
4. **Verifiable Intent**: DOF's Z3 proofs + keccak256 attestations align perfectly with Mastercard's approach

### Strategic Position
- DOF has: identity (ERC-8004), verification (Z3), attestation (keccak256), governance (deterministic)
- Missing: payment rails, commerce protocol integration
- Priority: implement x402 + ERC-8183 support in Enigma API

### Key Numbers
- Artemis: ~50% of x402 transactions are testing/wash trading
- Virtuals: $3.8M agent-to-agent revenue, 18K+ agents
- McKinsey: $3-5T by 2030
- AI traffic to US retail: +4,700% YoY

## Key Quotes
- **Brian Armstrong**: "Very soon there are going to be more AI agents than humans making transactions. They can't open a bank account, but they can own a crypto wallet."
- **Shan Aggarwal** (Coinbase CBO): "Agentic payments is certainly one of our top priorities as a company"
- **Davide Crapis** (Ethereum Foundation): ERC-8183 is "one of the missing components for the open agent economy"

## References
- McKinsey: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-automation-curve-in-agentic-commerce
- x402 scan: https://www.x402scan.com/
- Agentic GDP: https://agdp.io/
- ERC-8183: https://eips.ethereum.org/EIPS/eip-8183

---

*Intelligence compiled by DOF Agent Legion — March 19, 2026*
