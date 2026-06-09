# ATR-Move Coefficient — Cross-Asset Validity Envelope

**Date:** 2026-06-09
**Script:** `Strategies/Breakouts/atr_move_envelope.py`
**Question:** The coefficients `C_med≈0.48` / `C_p90≈1.25` in `|N-day move| ≈ C·ATR%·√N` were fit on ~60 US single-names (1–5% ATR, ~10d horizon). Do they generalize to ETFs, commodities, EU/Asian names, FX, and futures — and across horizons N=3→60?

**Method:** ~8y auto-adjusted daily OHLC, 22 instruments. For each, Wilder ATR14/price (median), realized `|N-day move|` median & p90, back out `C = move / (ATR%·√N)`. √N scaling tested via `(move_N/move_1)/√N` (1.0 = random walk, >1 trend, <1 mean-revert). Pure realized test, no options.

---

## Headline

- **Median coefficient is dead-on:** grand mean C_med10 = 0.46, C_med20 = 0.48.
- **p90 ran a touch higher than 1.25** (pooled ~1.30–1.33) → use **1.30** as the broad p90 center; 1.25 was mildly conservative.
- The "normalized shape, vol level lives in ATR%" claim **survives translation** to EUR/JPY/GBP single-names and to ETFs.

## Two coefficients = quantiles, not a per-ticker choice

`0.48·ATR%·√N` = median; `1.25·ATR%·√N` = p90. Both apply to every name simultaneously; the ~2.6× gap is the move-distribution spread (and the positive skew long options harvest). Differentiation across tickers is already in ATR% (the input). Use median for target/R:R; p90 for convexity justification.

## Where it HOLDS (tight)

| Asset class | C_med10 | C_p90·10 | Verdict |
|---|---|---|---|
| US stocks | 0.48 | 1.27 | ✓ on target |
| EU stocks (OR, CA, MT, CRST) | 0.48 | 1.29 | ✓ travels to Europe |
| Equity ETFs (SPY/IWM/QQQ) | 0.53 | 1.34 | ✓ slightly fatter |
| Commodity ETFs (GLD/SLV/USO) | 0.53 | 1.46 | ✓ fatter tails |
| JP stocks (Tokyo) | 0.39 | 1.39 | ~ lower median, wide name dispersion |

**Domain:** equities + equity/commodity ETFs, any region, ATR 1–5%, horizon 3–25 sessions. C_med 0.45–0.55, C_p90 1.25–1.55.

## Three edges of the envelope

**1. Asset class — FX fails, futures wobble**
- **EURUSD: C_med 0.36, C_p90 0.94** — both ~25–30% below equities; thin-tailed + mean-reverting. Heuristic **over-predicts FX strong moves by ~a third.** Recalibrate FX → **0.36 / 0.95**; never size FX convexity off 1.25×.
- **CL=F: C_med 0.41, C_p90 1.13** — low and contaminated by continuous-contract roll. Term-structure work dominates futures sizing anyway.

**2. Horizon — √N breaks past ~25 sessions, both directions**
- 3–20 sessions: clean (scale ratio ~1.0–1.2), coefficients flat.
- **Trending assets exceed √N** at 40–60d (drift/momentum): SPY scale 1.38, QQQ 1.30, NVDA 1.48, JP-3440 1.77, STNG 1.42; NVDA C_med climbs 0.54→0.71. → **add a drift uplift** for indices/momentum names at 2–3 months.
- **Post-parabolic high-ATR names mean-revert below √N**: MP scale → 0.76, C_med → 0.33 at 60d.

**3. ATR% level** — clean 1–5%. Below ~1% (FX, mega-cap staples e.g. PG C_p90 1.16) tails thin; above ~5% (MP) short-horizon fine but long-horizon mean-reverts.

## Bonus: ATR/σ ratio is not ~1.3

Pooled **ATR/σ = 1.13**, ranging **0.86–1.57** by asset (gappy equities ~1.1–1.3; continuous FX/commodity ~1.0; one gap-prone JP name 1.54). Had we derived expected move from `σ√T` instead of ATR, we'd need an asset-specific ATR/σ conversion to return to ATR units — another reason to measure ATR directly.

## The rule to write down

> **0.48 (median) / 1.30 (p90) × ATR% × √N** holds for equities and equity/commodity ETFs (any region, ATR 1–5%), over **3–25 sessions**.
> Outside it: **FX → 0.36 / 0.95**; **futures → ~0.41 / 1.13** (+roll caveat); **horizon >25 sessions** → add drift for trending names, expect mean-reversion for post-parabolic ones; **ATR <1%** → thinner tails.
