# SMH — Directional Funnel (Applied from JPM Template)

**Snapshot:** 2026-04-24, pre-market 13:25 CET (US open 15:30 CET)
**SMH spot:** $497.13 (live TWS); last 2h bar close $481.90 (2026-04-23)
**1Y range:** $198.98 – $486.36 → **now above 1Y high**
**1Y annualized return:** +138.8%
**Internal scanner (2026-04-23):** LONG TRADE, long 9 / short 2, RS vs ETF **+14.4**, Sector: Technology
**Recent tape:** $443 → $464 → $477 → $497 over 5 sessions (+12%)

---

## 1. ATM IV Landscape (from TWS historical ATM IV, constant moneyness)

| Metric | Value |
|---|---|
| Current ATM IV (interp 30d) | **41.8%** |
| **IV percentile 1Y** | **97.2%** (near top) |
| IV range 1Y (min / max / mean) | 24.9% / 48.3% / 33.5% |
| IV 30d back | 40.5% (already elevated a month ago) |
| IV 180d back | 28.1% |
| Current HV | 36.2% |
| HV percentile 1Y | 77.0% |
| HV 30d back | 37.9% |
| HV 180d back | 22.5% |

**Read:** ATM IV is near the top of its 1Y distribution. Both implied and realized are in the 70-97 percentile bucket — a high-vol regime broadly, but implied is richer than realized (see VRP below).

*Per-expiry ATM IV surface (term structure) needs a live TWS pull at market open — pre-market option snapshots hang.*

---

## 2. IV vs Realized (VRP Check)

**VRP = IV − RV ≈ 41.8% − 36.2% = +5.6 vol pts. POSITIVE.**

Opposite of JPM (which had **negative** VRP −3 to −5 pts). On SMH the market is charging ~5.6 pts above what the ETF is actually delivering day-to-day. Options are a **seller's environment at the ATM**, not a buyer's.

Translation: a directional bull here is paying rich premium for upside that the stock, at current realized pace, wouldn't earn back through gamma.

---

## 3. Term Structure (Expected Shape — requires live pull to confirm)

Component earnings inside each expiry:

| Expiry | DTE | Earnings events inside window |
|---|---|---|
| May 1 | 7 | — (**clean** — before AMD May 5) |
| May 22 | 28 | AMD May 5 + **NVDA May 20** (~2 days before expiry) |
| Jun 18 | 55 | AMD + NVDA + AVGO Jun 3 |
| Aug 21 | 119 | All above + ASML Jul 15 + TSM Jul 16 + INTC Jul 23 |

**Expected shape — opposite of JPM's U-curve:**

- **May 22** should be the **hump**, not the trough — NVDA earnings premium (~20% SMH weight) plus AMD is loaded into ~28-DTE ATM vol.
- **Jun 18** is moderate: the AMD/NVDA events are priced in for weeks before getting burned, but the expiry still carries the full event premium until the events pass. AVGO adds a secondary bump.
- **May 1** is the only clean bucket — but at 7 DTE, theta is devastating for any directional play that needs room.
- **Aug 21** carries multiple summer events but spread over 119 days → annualized vol moderates even with more events.

**Implication:** the JPM play of "target 30–56 DTE because it's the cheapest bucket" **does not translate** — SMH's 29-DTE bucket is the **richest**, not the cheapest.

---

## 4. Skew / Risk Reversal (pending live pull — market open)

**What to pull at 15:30 CET:** `getOptValue` for strikes covering 10d/25d call and 10d/25d put across May 1 / May 22 / Jun 18 / Aug 21. Script ready at `scripts/pull_smh_surface.py`.

**Prior distribution of what I'd expect for SMH:**
- In a post-breakout rally with IVP at 97%, call skew often goes **positive** (calls bid vs ATM) as traders chase upside. This is the XLE pattern, not the JPM pattern.
- Risk reversal in tech ETFs during rally phases: sometimes flips to **positive** (call vol > put vol) when the chase is loud. This is the tell of "everyone already long and paying up for more."

**If that's the actual read (call skew positive, RR ≥ 0):** you are fighting the surface by buying calls — classic late-rally setup where the surface is already priced for the upside.

**If skew prints neutral or negative** (calls cheap vs ATM, RR < 0): that would be unusual here but would flip the structural preference toward long calls / risk reversals.

Flag: **this is the one piece of the funnel that can overturn the vol-seller bias below. Pull and revisit.**

---

## 5. Funnel Grid — JPM vs SMH

| Funnel signal | JPM (2026-04-23) | SMH (2026-04-24) | Directional-bull implication |
|---|---|---|---|
| **IV Rank 1Y** | 52.7% middle | **97.2% top** | Long options expensive in absolute terms |
| **VRP** | −3 to −5 pts | **+5.6 pts** | Surface overpricing realized — **seller's edge**, not buyer's |
| **Term structure** | U-shaped, 30–56 DTE cheapest (no event) | Hump at NVDA (~28 DTE); clean bucket is 7 DTE (too short) or 55 DTE (post-event still pricey) | Cheap-vol bucket does not exist; earnings contaminate 3 of 4 expiries |
| **Call skew** | Negative (calls cheap vs ATM) | **TBD (market open)** — prior: likely positive after 12% rally | If positive → buying calls is buying rich vol on rich skew |
| **Risk reversal** | −3.7 to −5.6 vp (calls cheap vs puts) | **TBD** — prior: near zero or slightly positive | If positive → financing call with short put does NOT help |
| **Earnings / event** | Jul 14, outside May/Jun expiries | NVDA May 20 dominates; only May 1 is clean | Every standard expiry is also an event bet |

**Net:** SMH is the structural **inverse of JPM on the vol surface.** Technically both score LONG TRADE, but JPM's surface supports the thesis; SMH's surface fights it.

---

## 6. Preferred Structures — Bullish Expression on SMH

Given 97% IVP, positive VRP, earnings-loaded term structure:

### ★ If the view is tactical and short (pre-NVDA, before May 20):
- **Stock direct (5–10 shares)** — no IV tax. Scanner score supports continuation.
- **Call spread 2 weeks out (May 8 or May 15), narrow strikes** — if you *must* use options, narrow the spread so theta/IV exposure is minimized. e.g., May 15 $505/$515 — wing the risk, pay cheap cross-strike premium.
- **Avoid May 1** — too short to overcome theta, and the AMD report hits 4 days later (after expiry).

### ★ If the view is to hold through NVDA earnings (May 20):
- **Buy stock outright.** Options are a losing game: you pay event premium, IV crushes post-event, and even if NVDA rips SMH can underperform NVDA by a lot (other components drag).
- **Bull call spread Jun 18 $510/$540** — captures post-event mean reversion in vol while holding delta. The short OTM call collects elevated vol that a pure long call doesn't.
- **Risk reversal (sell put / buy call) Jun 18** — ONLY if skew confirms negative RR at market open. Otherwise this is worse than stock.

### ★ If the goal is to harvest the rich vol (not directional):
- **Short-dated ATM put sale** (May 15 $480 put) — with IV at 97%, selling vol where you don't mind owning the ETF at a 4% pullback is the cleanest expression of "vol is rich, trend is up."
- **Diagonal call spread: sell May 22 $515C / buy Jun 18 $515C** — explicitly harvests NVDA event-vol term structure by short the event-rich expiry and long the post-event one.

### Avoid:
- **Long outright calls at 25d or 10d** — worst of all worlds: top-decile IV, likely elevated call skew, event risk, theta.
- **Long straddles / strangles** — vol is rich; you're selling yourself expensive gamma.
- **Aug 21 bull debit structures** — you pay every component's earnings premium.

---

## 7. Bottom Line

- **SMH technical signal is strong (LONG 9/10, RS +14.4, above 1Y high), but the vol surface says the crowd is already positioned.**
- **IVP 97%, VRP +5.6 pts, NVDA event in 26 days** → this is a "right view, wrong instrument" trap if you default to long calls.
- **Best expressions:** stock direct, OR vol-neutral/vol-short structures (put sale, diagonal, bull call spread) that convert the thesis into a vega-positive or vega-flat carry.
- **Worst expression:** OTM calls in May 22 / Jun 18 — you are paying top-decile vol on a 28-day event bet.
- **Next step:** pull live strike surface at market open to confirm skew/RR — that's the one signal that can upgrade or downgrade the vol-seller bias. Script ready at `scripts/pull_smh_surface.py`.

---

## Appendix — Data Sources

- **TWS `get_volatility_metrics('SMH', lookback_days=252, hist=True, price=True)`** — ATM IV 30d-interp, HV 20d, 1Y percentiles
- **TWS `getValue('SMH')`** — live spot $497.13 @ 2026-04-24 12:48 CET
- **`tdata_py.earnings_utils.getNextEarningsDate`** — NVDA 2026-05-20, AMD 2026-05-05, AVGO 2026-06-03, ASML 2026-07-15, TSM 2026-07-16, INTC 2026-07-23
- **mydb.db `scanner_history`** — LONG TRADE 2026-04-23, long 9, short 2, RS +14.4, price 476.83
- **Pending:** strike-level IV/delta surface — requires live market-hours pull
