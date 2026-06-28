# breakeven.md  

## 1. Unit Economics (per **active user / month**)

| Cost Component | Assumption (per user) | Unit Cost | Monthly Cost (USD) |
|----------------|-----------------------|-----------|--------------------|
| **Compute** | 0.10 vCPU‑hour (cloud inference for terrain matching & IMU fusion) | $0.010 / vCPU‑h (AWS t3.micro spot) | **$0.01** |
| **Storage** | 5 GB of terrain tiles / flight logs retained 30 days | $0.023 / GB (S3 Standard) | **$0.12** |
| **Bandwidth** | 5 GB outbound (telemetry + map tiles) | $0.09 / GB (AWS Data Transfer) | **$0.45** |
| **Total Variable Cost** |  |  | **$0.58 / user‑mo** |

> *Variable cost excludes fixed overhead (dev salaries, office, SaaS tooling, etc.).*  

---

## 2. Pricing Tiers  

| Tier | Monthly Price | Core Features | Max Flights / Mo | Max Area* | SLA / Support |
|------|---------------|---------------|------------------|-----------|---------------|
| **Basic** | **$9** | • Terrain‑match (offline map) <br>• 5 km² area limit <br>• 10 flight‑sessions <br>• Email support (48 h) | 10 | 5 km² | Email (48 h) |
| **Pro** | **$29** | • Real‑time IMU‑fusion <br>• 25 km² area limit <br>• 50 flight‑sessions <br>• API access <br>• Slack community | 50 | 25 km² | Email (24 h) |
| **Enterprise** | **$99** | • Unlimited area & flights <br>• Dedicated edge‑module (on‑prem) <br>• Custom integration <br>• 99.9 % SLA <br>• Phone & priority support | Unlimited | Unlimited | Phone (4 h) |

\*Area limits are *average* per‑month footprint; larger projects can request temporary extensions on Pro/Enterprise.

---

## 3. Customer‑Acquisition Cost (CAC)

| Channel | Typical Spend per Lead | Conversion Rate | CAC (USD) |
|---------|------------------------|-----------------|-----------|
| Digital ads (LinkedIn, Google) | $30 | 5 % | $600 |
| Drone‑industry trade shows | $500 (booth + travel) | 30 % (qualified demos) | $1,667 |
| Partner referrals (OEMs) | $0 (revenue share) | 10 % | $200‑$300 |

**Pragmatic CAC range:** **$200 – $500** (mix of referrals + low‑cost digital).  

---

## 4. Lifetime Value (LTV)

*Assumptions*  

- Average subscription length = **24 months** (2 years) – typical churn for B2B SaaS in the UAV sector.  
- Mix of tiers (30 % Basic, 50 % Pro, 20 % Enterprise) → **Weighted ARPU** = (0.30×$9) + (0.50×$29) + (0.20×$99) = **$30.30** per month.  

**LTV** = ARPU × months = **$30.30 × 24 ≈ $727**  

(Variable cost per user over 24 mo = $0.58 × 24 ≈ $14 → net contribution ≈ $713)

---

## 5. Break‑Even Users Count  

### Fixed Monthly Overhead (estimated)

| Item | Monthly Cost |
|------|--------------|
| 2 senior devs (remote) | $12,000 |
| 1 DevSecOps engineer | $6,000 |
| Cloud infra (reserved, monitoring) | $2,000 |
| SaaS tools (CI/CD, analytics) | $1,000 |
| General & admin | $1,000 |
| **Total Fixed** | **$22,000** |

*(If the team is bootstrapped, a leaner $5k fixed cost can be used – see note below.)*  

### Contribution Margin per User  

Revenue per user (average) = **$30.30**  
Variable cost per user = **$0.58**  

**Contribution margin** = $30.30 – $0.58 = **$29.72**  

### Break‑Even Users  

- **With $22k fixed**: 22,000 / 29.72 ≈ **741 users**  
- **With $5k fixed (early‑stage)**: 5,000 / 29.72 ≈ **168 users**  

*We’ll target the lean $5k baseline for the first 6 months, then scale to the $22k baseline as the team expands.*

---

## 6. Path to **$10 K MRR**

| Scenario | # Users | Tier Mix | Monthly Revenue |
|----------|--------|----------|-----------------|
| **All Pro** | 345 | 100 % Pro ($29) | 345 × $29 = **$10,005** |
| **Mixed** | 120 Basic + 150 Pro + 5 Enterprise | 120 × $9 + 150 × $29 + 5 × $99 = **$10,020** |
| **Enterprise‑focused** | 101 Enterprise | 100 % Enterprise ($99) | 101 × $99 = **$9,999** |

**Fastest realistic route:** Acquire **~350 Pro‑tier** customers via drone‑operator SaaS marketplaces and OEM partnerships.  

*Revenue‑only break‑even (ignoring fixed costs) occurs at 9 × $9 + 29 × $29 + 99 × $99 ≈ 10 K, but the contribution‑margin break‑even (see section 5) requires ~741 users under full‑cost assumptions.*

---

## 7. Quick‑Start KPI Dashboard (to monitor)

| KPI | Target (Month 1) | Target (Month 6) |
|-----|------------------|------------------|
| Active Users | 150 | 800 |
| CAC (average) | $350 | $300 (referral‑heavy) |
| Churn (monthly) | 5 % | ≤3 % |
| Gross Margin % | 98 % (variable cost tiny) | 98 % |
| MRR | $4,350 (150 × $29) | $23,400 (800 × $29) |
| LTV:CAC Ratio | ≥2.0 | ≥3.0 |

---  

**Takeaway:** With a modest variable cost of **$0.58 / user‑mo**, a well‑priced tiered model, and a CAC under **$500**, terrain‑lock can reach **$10 K MRR** with roughly **350 Pro customers** or a mixed‑tier portfolio. Scaling to the full‑cost break‑even of **~740 users** will unlock profitability and fund the next wave of features (edge‑module, multi‑sensor fusion).