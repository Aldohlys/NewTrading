# Position Sizer — Algorithm Summary

## Purpose
Determines **how many lots** to trade on a credit option combo (strangle, vertical, iron condor, etc.) where risk is undefined. It answers: *"Given my risk budget, how many contracts can I sell?"*

## Two-Part Engine

### Part 1: Regime Analysis (IVP/HVP)

Classifies the vol environment before any simulation runs:

| Regime | Condition | Meaning |
|--------|-----------|---------|
| **IDEAL** | IVP−HVP spread ≥ 30, HVP ≤ 40 | IV is rich, underlying is calm — best time to sell premium |
| **FAVORABLE** | spread ≥ 15, HVP ≤ 60 | Good edge, moderate realized moves |
| **NEUTRE** | spread ≥ 0, HVP ≤ 70 | Fair, no strong signal |
| **DEFAVORABLE** | everything else | Weak setup |
| **DANGEREUX** | spread < 0 OR HVP > 80 | Underlying is moving as much or more than IV implies — dangerous for short premium |

It also computes:
- **Edge grade** (A–F) based on IV/HV ratio (A = IV ≥ 1.30x HV)
- **Sizing multiplier** — bonus up to +30% when IVP >> HVP, penalty up to −50% when HVP > IVP
- **Vol adjustment** — inflates HV by up to 1.5x when HVP is elevated (penalizes high realized vol)

### Part 2: Monte Carlo Simulation (200,000 paths)

Simulates the underlying price over the holding period using:

- **Student-t distribution** (df=5) instead of normal — fatter tails, more realistic crash/spike modeling
- **3 vol scenarios** run in parallel:
  - `hv_base` — simulate at raw historical vol (optimistic)
  - `hv_adjusted` — simulate at regime-adjusted vol (realistic, used for recommendation)
  - `iv_conservative` — simulate at implied vol (pessimistic, assumes IV is correct)

**Trade management rules baked in:**
- **Profit target exit** at 50% of max credit (configurable)
- **Mandatory DTE cut** at 21 DTE (configurable) — no holding through expiry gamma

**Pricing evolution:** during simulation, the vol used to reprice options **blends from IV toward HV** over time — models the real-world vol mean-reversion that impacts mark-to-market.

### Lot Sizing Logic

From each scenario's simulated P&L distribution:

1. Compute **VaR 95%/99%** and **Expected Shortfall (ES) 95%/99%** — ES is the average loss in the worst 1% of outcomes (stricter than VaR)
2. **Raw lots** = floor(max_loss_budget / ES99)
3. **Adjusted lots** = raw lots × regime sizing multiplier (capped at +30% bonus)
4. **Recommendation** = adjusted lots from the `hv_adjusted` scenario at ES99

## Output

Returns recommended lots + full detail:
- Regime classification & edge grade
- All 3 scenarios with ES, VaR, mean P&L, win rate, profit-target hit rate, avg holding days
- Conservative lot count (from IV scenario) as a sanity check

## Key Design Choices

- **ES not VaR** — ES captures tail severity, not just the threshold. Critical for undefined-risk positions where the worst 1% can be 5-10x the 95th percentile.
- **Student-t not Gaussian** — df=5 produces ~3x more extreme moves than normal distribution. A 4σ event under normal occurs once every 16,000 days; under Student-t(5) it's once every ~130 days.
- **Regime-aware** — won't let you size up just because IV is high if realized vol is equally high (the EWY case: grade A edge but DANGEREUX regime → 0 lots).

## Example: EWY 120/150 Short Strangle (Feb 2026)

The EWY strangle was a textbook example: IV/HV ratio of 1.57 (grade A edge) but HVP at 100 triggered DANGEREUX, the vol adjustment inflated simulation vol by 1.5x, and ES99 came out at $1,512/lot — far exceeding the $600 budget. The algo said "don't trade this" despite the attractive premium.
