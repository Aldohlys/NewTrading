# XLF Component Breakout Screen — Financials

*Date: 2026-06-08 · Method: BOT gate screen (S1–S6 / BK1–BK4, EMA50 basis, RS vs XLF) + ATR%/pay-for-entry beta filter · yfinance 5y daily*

Same treatment applied to Energy (refiners/XOP) and Healthcare (XLV) — now for **XLF main components**. The beta filter is `reference_atr_move_multiples.md`: a name only qualifies as a *long-option* vehicle if its ATR% is high enough that an OTM call can pay for entry (P(≥6%/10d) high enough). Low-beta names where **selling an OTM call won't pay for the entry** are filtered out and routed to shares / sell-vol instead.

Sector context: **XLF +4.4% / 3m** — financials are leading, so RS-vs-sector is a high bar (the index itself is strong).

## The beta filter first (the gating rule for vehicle, not direction)

Per the validated ATR→move multiples, financials cluster almost entirely in the **MID bucket (~2% ATR, Ppay ~20–32%)**. The decision-relevant consequence:

| ATR% bucket | Ppay (≥6%/10d) | Vehicle | XLF names |
|---|---|---|---|
| **LOW** (<1.7%) | ~6–9% | shares / **SELL** premium — long call structurally loses | **BRK-B (1.42)**, XLF (1.43), V (1.76\*) |
| **MID** (1.7–2.7%) | ~15–32% | **debit spread** / pay-for-entry discipline | C, WFC, SCHW, MS, AXP, BAC, GS, BLK, BK, PGR, SPGI, MA, CB, CME |
| **HIGH** (≥2.7%) | ~45%+ | long OTM calls in sweet spot | **BX (3.05)** |

\* V at 1.76 is technically MID but with Ppay only 14% it behaves low-beta.

**Headline vehicle conclusion:** financials are a **"spread sector," not a "long-call sector."** Unlike NVDA/TSLA (~4% ATR, ~55% payable), no breakout-qualifying financial except Blackstone has the beta to make an outright OTM call structurally pay. The breakout vehicle here is a **debit call vertical**, financed partly by the OTM short leg — which is exactly the mechanism the rule of thumb says works at MID beta and fails at LOW beta.

- **BRK-B is the textbook reject:** 1.42% ATR, 8% payable. Even though it screens S3/BK2 (constructive), selling an OTM call against a long won't pay — route to shares if you want the exposure.

## Gate screen — ranked by setup strength

Cols: `dEMA` = % vs EMA50 · `slope` = 5-bar EMA50 slope% · `rs_sec` = 3m RS vs XLF · `Ppay` = P(≥6%/10d), 5y

| Ticker | px | gates | sig | dEMA | slope | rs_sec | atr% | Ppay | vehicle |
|---|---|---|---|---|---|---|---|---|---|
| **C** | \$133.37 | **S5/BK3** | 🟢 GREEN | +6.9 | +1.40 | **+18.6** | 2.42 | 32 | MID spread |
| BK | \$142.39 | S4/BK2 | grey | +6.8 | +1.50 | +19.8 | 2.03 | 22 | MID spread |
| BAC | \$53.68 | S4/BK2 | grey | +4.2 | +0.72 | +6.7 | 2.23 | 29 | MID spread |
| JPM | \$311.42 | S4/BK2 | grey | +2.6 | +0.29 | +4.0 | 1.98 | 21 | MID spread |
| MS | \$212.15 | S4/BK1 | grey | **+10.0** | **+2.43** | **+28.3** | 2.28 | 30 | MID spread |
| GS | \$1044.82 | S4/BK1 | grey | +9.5 | +2.43 | +21.5 | 2.23 | 28 | MID spread |
| WFC | \$80.96 | S3/BK2 | grey | +2.5 | +0.45 | −0.4 | 2.43 | 32 | MID spread |
| BRK-B | \$486.65 | S3/BK2 | grey | +1.4 | +0.03 | −5.9 | 1.42 | 8 | LOW → shares |
| AXP | \$312.01 | S3/BK0 | grey | −1.0 | −0.40 | −1.1 | 2.26 | 28 | MID spread |
| PGR | \$201.07 | S2/BK1 | grey | +0.7 | −0.14 | −7.2 | 2.03 | 17 | MID spread |
| BX | \$114.13 | S2/BK1 | grey | −4.1 | −0.80 | +0.4 | **3.05** | **45** | HIGH long-call |
| V | \$320.17 | S2/BK0 | grey | 0.0 | −0.08 | −2.4 | 1.76 | 14 | low-MID |
| SPGI | \$417.07 | S2/BK0 | grey | −1.8 | −0.33 | −8.4 | 1.92 | 21 | MID spread |
| CB | \$323.05 | S1/BK1 | grey | +0.1 | −0.31 | −4.8 | 1.80 | 10 | MID spread |
| MA | \$485.16 | S1/BK0 | grey | −2.8 | −0.77 | −10.0 | 1.89 | 15 | MID spread |
| SCHW | \$88.23 | S1/BK0 | grey | −2.8 | −0.69 | −9.4 | 2.51 | 31 | MID spread |
| BLK | \$991.73 | S0/BK1 | grey | −4.1 | −0.72 | −1.3 | 2.06 | 25 | MID spread |
| CME | \$250.48 | S0/BK0 | grey | −11.5 | −2.26 | −22.6 | 1.79 | 11 | MID spread |

*MMC and FI (Fiserv) — Yahoo returned a 404 for both symbols at run time (data-source outage, not a screen failure). Re-run to capture; both are MID-beta and were not expected to lead.*

## Read

**One clean breakout: Citigroup (C) — S5/BK3 GREEN.** The only name firing both a strong setup *and* a live breakout trigger. +6.9% above a rising EMA50, **RS +18.6 vs an already-leading sector** (genuine relative leadership, not just beta), range position 85%, fresh. ATR 2.42% / Ppay 32% → **MID bucket → debit call vertical** is the disciplined vehicle (the short OTM leg pays for part of entry; an outright call is monetizable only ~1 window in 3). This is the financials analogue of the XOP pick.

**Strong trends without a fresh trigger: MS and GS.** Both S4/BK1 — the *best* trends in the group (dEMA +10/+9.5, slope +2.4, RS +28/+21) but no breakout candle firing (BK1 only). These are "already moving," not "breaking out" — adding here is chasing, not a BOT entry. Watch for a consolidation→trigger, or treat as momentum-continuation (different framework — see [[feedback_dont_switch_frameworks_midtrade]]).

**Trigger but milder trend: BK, BAC.** S4/BK2 with a live trigger but more modest leadership (BK RS +19.8 is strong; BAC +6.7 / JPM +4.0 are middling). BK (BNY Mellon) is the second-most-complete after C. JPM is mature/extended (slope nearly flat at +0.29) despite S4.

**Clean avoids — the rule of thumb doing its job:**
- **Payment networks & data compounders (V, MA, SPGI, CME):** doubly disqualified — LOW/low-MID beta (OTM call won't pay) *and* no setup (below EMA, negative slope, negative RS). CME is the worst chart in the group (−11.5% dEMA, RS −22.6).
- **BRK-B:** constructive chart but 1.42% ATR / 8% payable — the canonical "sell-OTM-call-won't-pay" name. Shares only.

**One to watch for vehicle reasons: BX (Blackstone).** The *only* HIGH-beta name (3.05% ATR, 45% payable) — the one financial where outright long calls structurally pay. But no setup right now (S2/BK1, −4.1% below EMA, downtrend). If it turns and triggers, it's the only XLF name that justifies a long call rather than a spread.

## Bottom line

| Action | Name | Vehicle (per ATR rule) |
|---|---|---|
| **Trade candidate** | **C** (S5/BK3 GREEN, RS leader) | debit call vertical (~30–50 DTE) |
| Watch — trend, await trigger | MS, GS, BK, BAC | spread on trigger |
| Watch — vehicle only (needs setup) | BX | long call *if* it breaks |
| Avoid — low beta + no setup | V, MA, SPGI, CME, CB | n/a |
| Avoid — low beta (sell-call won't pay) | BRK-B | shares if wanted |

Next step if you want to act on **C**: workup the debit vertical at ~30 and ~50 DTE (`/analyze C`), pick strikes off the 20d S/R room-to-run, confirm IVP isn't so rich it caps the spread R:R.

## Reproducibility
- Screen script: `Strategies/Breakouts/xlf_screen.py` (mirrors `xlv_screen.py`, folds in beta filter)
- Beta rule: `reference_atr_move_multiples.md` · BOT gates: `Strategies/Breakouts/bot_strategy_checklist.md`
