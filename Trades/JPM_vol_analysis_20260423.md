# JPM Vol Analysis — Directional Bullish Thesis Check

**Snapshot:** 2026-04-23, intraday (source: IBKR TWS live, mydb.Prices EOD 2026-04-20)
**JPM spot:** $313.02
**Next earnings:** 2026-07-14 (confirmed via yfinance)
**Scanner read (internal):** LONG TRADE, composite 10/14 — strong technical setup, Financial sector, RS +1.1 vs ETF

---

## 1. Current IV Landscape (ATM)

From TWS live IV by expiry (interpolated to spot):

| Expiry | DTE | ATM IV (C) | ATM IV (P) | ATM IV (avg) |
|---|---|---|---|---|
| May 1 | 8 | 25.0% | 25.0% | **25.0%** |
| May 22 | 29 | 23.8% | 23.8% | **23.8%** |
| Jun 18 | 56 | 23.9% | 23.9% | **23.9%** |
| Aug 21 | 120 | 25.1% | 25.1% | **25.1%** *(includes Jul 14 earnings)* |

From DB (Prices, 2026-04-20): IV30 = 22.5%, IV180 = 25.3%, IVP = 38.6, IV 1Y percentile = 52.7% (TWS).

**Read:** ATM IV is in the middle of its 1Y range ($IV_{min}$ 17.8% / $IV_{max}$ 36.0% / mean 24.3%). The 23.8–24% mid-curve bucket is essentially "fair" historically — not cheap, not rich.

---

## 2. IV vs Realized Volatility (VRP Check)

From TWS historical volatility (HV percentile 1Y):

| Metric | Value |
|---|---|
| Current HV (20d-ish window) | **26.91%** |
| HV 1Y percentile | **71.8%** (high) |
| DB RV30 (2026-04-20) | 29.21% |
| DB RVP | 78.1 |
| 30d IV | ~23.8% |

**VRP = IV − RV ≈ 23.8% − 27–29% = −3 to −5 vol pts. Negative VRP.**

Translation: options are **underpricing what the stock has actually been doing.** Short-dated gamma is cheap relative to realized. This is the opposite of the typical vol-seller edge — a buyer's environment, not a seller's.

JPM has been realizing 27–29% (close-to-close) over the last month while the surface is pricing ~24%. For a directional bull who wants gamma, this is constructive.

---

## 3. Term Structure — Mid-Curve Is the Sweet Spot

ATM term structure (TWS):

| DTE | ATM IV | Notes |
|---|---|---|
| 8 | 25.0% | small weekend/weekly premium |
| 29 | 23.8% | local low |
| 56 | 23.9% | flat with 29d |
| 120 | 25.1% | **embeds Jul 14 earnings** (~1.2 vol pts event premium) |

The curve is **mildly U-shaped**: cheap in the 30–60 DTE bucket, kinked up on both ends. Key implication:

- **30–60 DTE options are the best-priced bucket** for a directional bull — low ATM, no event noise, VRP negative.
- Any expiry **≥ Jul 17 (86 DTE)** carries earnings premium — you pay for event vol even if you're not trying to trade the event.
- Sub-20 DTE is fine for tactical plays, but theta/gamma cost accelerates.

---

## 4. Skew — The Strongest Signal for This Thesis

Call skew (OTM call IV − ATM IV, % of ATM) and risk reversals (25d call IV − 25d put IV, in vol points):

| Expiry | DTE | 25d Call Skew | 10d Call Skew | 25d Put Skew | 10d Put Skew | **RR 25d** | **RR 10d** |
|---|---|---|---|---|---|---|---|
| May 1 | 8 | **−6.2%** | **−7.6%** | +8.0% | +18.8% | **−3.6 vp** | **−6.6 vp** |
| May 22 | 29 | **−7.5%** | **−9.5%** | +8.0% | +23.7% | **−3.7 vp** | **−7.9 vp** |
| Jun 18 | 56 | **−8.9%** | **−11.7%** | +9.4% | +19.0% | **−4.4 vp** | **−7.4 vp** |
| Aug 21 | 120 | **−10.9%** | **−11.6%** | +11.2% | +14.0% | **−5.6 vp** | **−6.4 vp** |

**Translation — this is the key differentiation from XLE:**

- JPM exhibits **classic negative equity skew**: OTM puts are bid, OTM calls are offered.
- **25d OTM calls trade 3.6–5.6 vol points BELOW 25d OTM puts.** Call vol is structurally cheap.
- Call skew is **negative** (OTM calls cheaper than ATM) across every expiry — OTM calls are not only cheap vs puts, they are also cheap vs ATM itself.
- Put skew at 10d is steep (+14 to +24%) — crash protection is expensive, as always.

Contrast with XLE: XLE had calls at **99th percentile richness** (the market was leaning bullish, pricing the upside). JPM has the opposite: the surface is pricing downside, not upside. A bullish view here is **against the surface consensus** — which is a better setup for a directional long.

---

## 5. Applying the Directional Funnel to JPM

Walking each funnel signal against the JPM surface:

| Funnel signal | JPM reading | Structure implication |
|---|---|---|
| **IV Rank (1Y)** | 52.7% — middle of range | Neutral. Not rich enough to avoid long options, not cheap enough to scream "buy vol" |
| **VRP** | Negative (−3 to −5 vp) | Long options are **underpriced** vs realized → favors option buyer |
| **Term structure** | Mid-curve (30–60 DTE) cheapest, 120d has earnings kick | Target 30–56 DTE for clean expression |
| **Call skew** | Negative (calls cheap vs ATM) | **Outright OTM calls or call spreads are efficient** |
| **Risk reversal** | −3.7 to −5.6 vp (calls cheap vs puts) | **Risk reversals look attractive** — cheap calls + expensive puts to sell |
| **Earnings** | Jul 14 — outside May/Jun expiries | 30–56 DTE structures avoid event risk by construction |

---

## 6. Preferred Structures (Bullish Expression, Ranked)

Given negative VRP, negative call skew, and no earnings before mid-July, the surface says: **buy directional upside efficiently, and consider financing via the put side.**

### ★ Best: OTM Call (30–56 DTE), ATM or slightly OTM
- **Why:** You're paying the cheapest part of the curve (23.8% ATM, 25d call IV ~22%) and negative VRP means realized is outrunning implied. Buy a **May 22 $320 call** or **Jun 18 $320 call** — 25-delta territory where skew is cheapest vs ATM. This is the XLE-playbook reversed: call vol is depressed, not expensive, so "just buy the call" is actually the clean trade.
- **Caveat:** Theta still accrues — size so that a 2% adverse move or 1 week of chop doesn't blow the thesis up.

### ★ Alternative: Bull Call Spread (30–56 DTE)
- **Why:** If you want to cap premium and skew doesn't reward you enough at the long strike, sell a $330 or $335 call against the $320 long. You give up some upside but collect back ~4–6 vol pts of skew on the short OTM call.
- **Less compelling than in XLE**, because JPM's skew is already in the bull's favor — the short OTM call doesn't sell you rich vol, it just caps your payoff.

### ★ Aggressive: Risk Reversal (sell 25d put / buy 25d call)
- **Why:** Risk reversal is −3.7 to −5.6 vp in your favor — you are financing a call buy by selling a vol-rich put. For May 22, that's roughly **sell $295 put / buy $325 call** for near-zero or small net debit.
- **Caveat:** You take the full downside. Given JPM is at $313 and scored LONG TRADE (10/14), conviction seems warranted, but the short put is tail-exposed — scale appropriately. This is the cleanest expression of "call skew is depressed, put skew is elevated, I am bullish."

### Avoid:
- **Long straddle / strangle** — negative VRP helps, but you are paying put-skew for a directional view, not a vol view.
- **Aug or later expiries** — you pay the earnings event premium (~1.2 vp ATM, more on OTM calls) without necessarily trading the event.
- **Calendar spreads selling front vs long back** — term structure is too flat to harvest; and the back-month kink is an earnings artifact, not a genuine structural premium.

---

## 7. Bottom Line

**The vol surface actively supports a bullish thesis on JPM — unlike XLE, you are not fighting the surface.**

- IV is fair at ATM, but OTM calls are **cheap** relative to both ATM and to equivalent-delta puts.
- Realized > implied → long gamma is underpriced.
- Cleanest bucket: **30–56 DTE (May 22 / Jun 18)** — pre-earnings, mid-curve lowest IV, and in the delta band where call skew is most depressed.
- **Preferred**: long OTM call (~25Δ) or risk reversal financed by the put side if you're comfortable with the downside wing.

Combined with the internal scanner signal (LONG TRADE 10/14, positive RS, Financial sector constructive), the surface-level evidence and the technical screen align. This is a "surface not leaning against you" setup — the opposite of chasing where the crowd has already paid.

---

---

## Trade Executed

**Entry date:** 2026-04-24
**Structure:** May 15 2026 $330/$340 Call Debit Spread
**Lots filled:** 2 (initial leg-in)
**Fill price:** $1.30 debit/spread (at mid)
**Total outlay:** ~$262 (2 × $130 + ~$2 commission)
**Net delta:** ~0.24
**Max loss:** $262 | **Max gain:** $1,740 | **Break-even:** $331.30

**Context at entry:** Hedge/balance role against existing bear book (USO short, PSX short, SPY put protection, ESTX50 put protection, QQQ bear spread). Sizing intentionally modest — balancer, not conviction bet.

### Legging plan
- **Reserve for 3rd lot:** ~$140 remaining budget.
- **3rd lot trigger:** daily close above $317 (recent swing high) on above-average volume, OR break of $318–$320 with follow-through next session. No add on gap-ups.

### Pre-committed exits
- **Scale-out:** sell 1 spread at $3.00 (≈130% return, approximates intrinsic at resistance touch $333). Let 2nd run toward short strike $340.
- **Stop (technical):** close both if JPM closes below $310 (breakout pivot fails).
- **Time stop:** if by 2026-05-08 (DTE 7) JPM is still below $320, close residual for whatever remains. OTM theta decay accelerates hard final week.
- **Hedge role caveat:** if bear book pays off (SPX retraces), this spread goes to zero by design. Don't close on first red day — it's doing its job.

### Key levels
- Resistance zone: $334–$337 (52w high close $334.04, intraday $337.25, both single-touch from 2026-01-05)
- Breakout pivot: $317 recent, $320 horizontal
- Breakdown invalidation: < $310

---

## Appendix — Raw Data Sources

- **TWS IBKR API** (`tdata_py.contract.getOptValue`) — per-strike IV/delta for 4 expiries × 15 strikes × 2 rights
- **TWS IBKR API** (`tdata_py.impliedvol.get_volatility_metrics`) — 1Y IV/HV percentiles, lookback 252d
- **TWS IBKR API** (`tdata_py.earnings_utils.getNextEarningsDate`) — earnings date via yfinance
- **mydb.db `Prices`** — snapshot IV30/IV180/IVP/RV30/RVP as of 2026-04-20
- **mydb.db `scanner_history`** — LONG TRADE signal 2026-04-23, composite 10
- **Raw vol surface CSV:** `C:\Users\aldoh\Documents\NewTrading\jpm_vol_surface.csv`
