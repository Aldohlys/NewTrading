# ESTX50 Hedge Management — Roll Sep 5200P → Dec 5700/4600 — EXECUTED

**Status:** ✅ **EXECUTED 2026-06-02** (see §8). Analysis dated 2026-06-01.
**Account:** U1804173
**Old position:** ESTX50 18-SEP-26 5200 P, long 1 lot (GOnet portfolio hedge)
**New position:** ESTX50 18-DEC-26 **5700 / 4600** put spread, long 1 lot
**Spot:** ESTX50 ≈ 6,012 at analysis (2026-06-01) → **6,100 at execution** (2026-06-02)
**Supersedes:** `ESTX50_hedge_management_20260514.md` (wait-and-convert plan — now void, see §2)

> **Note on labels & strikes:** structures are labelled **Option A–D** (Greek letters dropped). §5–§6 evaluate all four; the two deep-wing spreads are **Option C (5,600/4,600)** — the 2026-06-01 analysis baseline — and **Option D (5,700/4,600)** — the structure actually **executed 2026-06-02** after the index rallied to 6,100 (the higher tape thinned the 5,600 cushion at the inflation-grind end, so the long leg was bumped to 5,700). §7 coverage and §8 use **Option D**.

---

## 1. Executive Summary

The May-14 "wait-and-convert" plan (hold the 5,200P, sell a wing into a vol spike) is **dead**: the market rallied instead of selling off, no stress trigger ever fired, and the 5,200P is now 13.5% OTM, –0.12 delta, and **mis-struck for the user's actual objective — a –10% drawdown of the Gonet portfolio**. It also **expires 18-Sep-26**, leaving the book unhedged for Q4.

**Action (executed): roll Sep 5,200P → Dec-26 5,700 / 4,600 put spread (Option D), 823 EUR/lot net debit** (analysis baseline was Option C 5,600/4,600 at ~694; bumped to Option D on the higher execution-day tape).

This single move:

- **Re-strikes** the hedge to pay across the –10%-portfolio band (ESTX50 ~4,940–5,340), where the 5,200 strike pays ~nothing.
- **Extends** continuous coverage through Q4 (Dec-18 expiry).
- **Minimises cost** — the deep 4,600 wing finances most of the longer-dated premium; the net debit is barely more than a same-expiry roll-up, and net carry ≈ –1 to –2 EUR/day.
- Is **condition-independent** (done now at trough vol, no waiting on a spike the grind would deny).

SPY 660P (the USD-side hedge) is **parked** for now — US equity is only 12% of the book — but shares the same 18-Sep expiry and will need the same roll-up-and-out before September.

---

## 2. Why the May-14 plan is void

| May-14 premise                                          | What actually happened                                                                           |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Vol spike would come; sell the 4,700/4,500 wing into it | Market **rallied** 5,929 → 6,012; vol stayed at trough (~24%)                                    |
| Trigger 1: ESTX50 ≤ 5,430 + 4700P-IV ≥ 35%              | Never approached; went the other way                                                             |
| Wing-sale harvests rich premium                         | At trough vol the 4,700 wing is worth ~24 EUR — selling now monetises optionality at its weakest |
| Hold the naked 5,200P                                   | Now –0.12 delta / 13.5% OTM / expires 18-Sep — a thin, expiring tail                             |

**Key reframe:** the wing-sale-timing edge only exists in a *crash* (vol spike). The user's stated base case is a *2022-style inflation grind* with **flat vol** — exactly the regime where there is no spike to wait for, so deferring action gains nothing and just burns carry on an expiring, mis-struck put.

---

## 3. Current position snapshot (2026-06-01)

| Field      | ESTX50 5,200P          | SPY 660P (parked)  |
| ---------- | ---------------------- | ------------------ |
| Expiry     | 2026-09-18             | 2026-09-18         |
| Lots       | 1                      | 1                  |
| Multiplier | 10 EUR/pt              | 100 USD/pt         |
| Avg cost   | 224.13 EUR (2,241 EUR) | 9.67 USD (968 USD) |
| Mark       | 50.5 EUR (506 EUR)     | 5.94 USD (595 USD) |
| unPnL      | **–1,735 EUR**         | **–372 USD**       |
| Delta      | –0.120                 | –0.119             |
| Vega       | 6.70                   | 0.88               |
| Moneyness  | 86.5% (13.5% OTM)      | 87.4% (12.6% OTM)  |
| DTE        | 109                    | 109                |

Forward max additional loss if both expire worthless ≈ 506 EUR + 595 USD ≈ **~1,090 CHF** (sunk loss already booked).

---

## 3b. Position snapshot update (2026-06-02 morning, pre-roll, ESTX50 ≈ 6,100)

Overnight the index rallied +1.5% (6,012 → 6,100). The Sep 5,200P decayed and drifted further OTM — the trigger to re-check the strike (→ Option D) before rolling:

| Field      | ESTX50 5,200P (06-02)    | vs 06-01        |
| ---------- | ------------------------ | --------------- |
| Mark       | ~43.1 EUR (431 EUR)      | –7.4 (was 50.5) |
| unPnL      | **≈ –1,810 EUR**         | –75 EUR         |
| Delta      | –0.10                    | (was –0.12)     |
| Moneyness  | 85.2% (14.8% OTM)        | further OTM     |
| DTE        | 108                      | –1              |

*SPY 660P: US closed overnight CET, mark ≈ unchanged from 06-01; still parked.*

---

## 4. Live OESX quotes (2026-06-01, ESTX50 ≈ 6,012)

**Sep-18-26 (109 DTE):**

| Strike          | bid   | ask   | mid   | delta  |
| --------------- | ----- | ----- | ----- | ------ |
| 5,700           | 117.7 | 119.7 | 118.7 | –0.274 |
| 5,600           | 98.1  | 100.0 | 99.05 | –0.232 |
| 5,500           | 82.1  | 84.0  | 83.05 | –0.195 |
| 5,400           | 69.1  | 70.8  | 69.95 | –0.166 |
| **5,200 (own)** | 49.8  | 51.2  | 50.5  | –0.119 |
| 5,000           | 36.6  | 37.8  | 37.2  | –0.086 |
| 4,700           | 23.8  | 24.7  | 24.25 | –0.053 |

**Dec-18-26 (200 DTE):**

| Strike    | bid   | ask   | mid       | delta  |
| --------- | ----- | ----- | --------- | ------ |
| 5,700     | 189.0 | 192.5 | 190.75    | –0.309 |
| **5,600** | 165.4 | 168.6 | **167.0** | –0.273 |
| 5,500     | 144.7 | 147.7 | 146.2     | –0.241 |
| 5,000     | 76.2  | 78.2  | 77.2      | –0.127 |
| 4,900     | 67.6  | 69.2  | 68.4      | –0.112 |
| 4,800     | 59.8  | 61.2  | 60.5      | –0.099 |
| **4,600** | 46.4  | 47.9  | **47.15** | –0.08  |
| 4,500     | 41.3  | 42.7  | 42.0      | –0.07  |

(IBKR returns null IV on OESX; bid/ask/delta are reliable.)

**Live OESX quotes (2026-06-02 ~09:40 CET, EUREX open, ESTX50 ≈ 6,100)** — the execution-day book; puts cheaper on the higher tape + softer vol:

| Leg                  | bid   | ask   | mid       | delta  |
| -------------------- | ----- | ----- | --------- | ------ |
| Sep-18 5,200P (close)| 42.7  | 43.5  | **43.1**  | –0.10  |
| Dec-18 5,700P (buy)  | 168.8 | 170.6 | **169.7** | –0.28  |
| Dec-18 5,600P        | 147.6 | 149.0 | 148.3     | –0.25  |
| Dec-18 5,500P        | 129.1 | 130.6 | 129.85    | –0.22  |
| Dec-18 4,600P (sell) | 42.6  | 43.4  | **43.0**  | –0.07  |

December-chain check (5,700P): Dec-18 is the **only** December expiry and the most liquid (quarterly spread 1.7 vs Nov-20 2.0 / Jan-15 3.1); term IV flat ~18.5%.

---

## 5. Structures evaluated

Net debit includes closing the Sep 5,200P at +50.5/sh (+505 EUR/lot). Today value = capital tied up per lot.

| Structure                     | Legs (Dec-26)     | Net debit/lot | Caps at        | Net delta |
| ----------------------------- | ----------------- | ------------- | -------------- | --------- |
| Hold (do nothing)             | keep Sep 5,200    | 0             | —              | –0.12     |
| **Option A** Naked            | long 5,600        | ~1,165        | none           | –0.27     |
| **Option B** Near-wing        | 5,600 / 5,000     | ~393          | 5,000 (–16.8%) | –0.15     |
| **Option C** Deep-wing        | 5,600 / 4,600     | ~694          | 4,600 (–23.5%) | –0.19     |
| **Option D** Deep-wing high   | **5,700 / 4,600** | **~931**      | 4,600 (–23.5%) | **–0.23** |

*(Net debits on the 2026-06-01 basis, closing the Sep 5,200P at +50.5. Option D = 5,700/4,600 was executed 2026-06-02 at 823/lot — cheaper on the higher tape; see §8.)*

**Why a deep-wing spread (C / D):** the deep 4,600 wing keeps the cap *below* the 2022 trough analog (~–26%), so the spread is uncapped across essentially the entire grind the user fears, while financing ~half the long-leg cost. It **beats the naked put at every move down to ~–24%** (same long leg, cheaper) and gives back only ~1,000 EUR vs naked even in a full –26% replay. **Option D lifts the long leg to 5,700** — chosen at execution because the overnight rally to 6,100 thinned the 5,600 cushion at the inflation-grind end (restores ~6.6% OTM moneyness; +100 pts of ITM-depth at the inflation –10% point for ~+237 EUR/lot).

---

## 6. Scenario simulation — forward P&L per lot (EUR)

Forward P&L = horizon value − today value (roll cost embedded). September crashes valued MTM at Sep-18 with vol spike (i.e. **monetise into the panic**); year-end scenarios at Dec-18 intrinsic. Hold expires 18-Sep.

| Scenario                       | Hold   | A Naked 5600 | B 5600/5000    | C 5600/4600    | **D 5700/4600** |
| ------------------------------ | ------:| ------------:| --------------:| --------------:| ---------------:|
| Flat 0% / ±5% (year-end)       | –505   | –1,670       | –898           | –1,198         | **–1,436**      |
| Grind +5% (year-end)           | –505   | –1,670       | –898           | –1,198         | **–1,436**      |
| Grind –10% flat-vol (Dec)      | –505   | +220         | +992           | +692           | **+1,454**      |
| **Grind –20% FLAT-VOL (2022)** | –505   | +6,230       | +5,102 *(cap)* | +6,702         | **+7,464**      |
| CRASH Sep –10% (vol spike)     | –505   | +1,777       | +1,147         | +1,467         | **+1,788**      |
| CRASH Sep –15% (vol spike)     | +395   | +3,814       | +2,116         | +2,797         | **+3,329**      |
| CRASH Sep –25% (big spike)     | +6,405 | +9,282       | +4,489 *(cap)* | +6,355         | **+7,113**      |

*(Option D today-value = 1,436 EUR/lot — the extra carry vs C is the cost of the higher 5,700 strike; in return D pays more in every down scenario, materially so in the grind/–10% cases.)*

**Reading:** Hold is a deep-crash lottery that fails the –10% and continuity objectives (0 at a Sep –10%, –505 in every grind, unhedged in Q4). Option B wins only the shallow –10% case and is capped deeper. Option A (naked) owns the crashes but bleeds most if benign. **The deep-wing spreads (C / D) are never the worst in any drawdown, win the 2022 grind, and trail naked only modestly elsewhere** — the all-weather choice. **Option D (5,700)** dominates C in every down scenario (it pays more for ~238 EUR/lot extra carry), at the cost of a slightly larger drag if nothing happens (–1,436 vs –1,198).

The dynamic "B-plus-roll-the-wing-down-in-a-crash" idea is dominated: in a grind it behaves like Option B (no skew trigger → never rolls → capped); in a crash it behaves like the deep-wing spread minus execution slippage. Buying the spread now *is* that roll, executed at the cheapest the 5,000/4,600 vertical will ever be (30 pts at the analysis).

---

## 7. Portfolio coverage — what "–10%" really means

GOnet ≈ **371k CHF**, only **67% equity**:

| Bucket             | CHF     | %   | Hedged by |
| ------------------ | -------:| ---:| --------- |
| EU/CH equity       | 192,400 | 52% | ESTX50    |
| US equity          | 43,900  | 12% | SPY       |
| China equity (FXC) | 14,000  | 4%  | neither   |
| Bonds              | 76,500  | 21% | —         |
| Gold               | 44,200  | 12% | —         |

A **–10% portfolio drawdown = –37,100 CHF**, and because of the 33% defensive ballast it corresponds to an **equity-index move of –11% to –18%**, depending on regime:

| Regime                               | Equity falls | ESTX50 at | SPY at |
| ------------------------------------ | ------------:| ---------:| ------:|
| Crisis risk-off (gold/bonds cushion) | –17.8%       | ~4,944    | ~621   |
| Normal risk-off (gold/bonds flat)    | –14.8%       | ~5,121    | ~643   |
| **Inflation grind (bonds –12%)**     | –11.2%       | ~5,342    | ~671   |

**Coverage at the –10%-portfolio point (1 ESTX50 + 1 SPY):**

| Regime                             | Current (Sep 5200P + SPY660) | **Rolled (Option D 5700/4600 + SPY660)** |
| ---------------------------------- | ----------------------------:| ----------------------------------------:|
| Crisis risk-off                    | 5,400 CHF (14.5%)            | **10,010 CHF (27%)**                     |
| Normal risk-off                    | 2,050 CHF (5.5%)             | **6,590 CHF (18%)**                      |
| Inflation grind                    | **0 CHF (0%)**               | **3,300 CHF (9%)**                       |
| *Any drop completing after 18-Sep* | **0% (expired)**             | Option D still alive to Dec              |

**Three conclusions:**

1. **Roll-up is validated by the portfolio math:** the –10% band lands ESTX50 at 4,940–5,340; the 5,200 strike sits at the bottom edge (pays nothing in the inflation case, 5,342). The executed **5,700 long leg is ITM across the whole band** (ITM by ~361 pts at the inflation point, vs ~261 for 5,600) → lifts inflation-grind coverage 0% → **9%** and normal 5.5% → **18%**. (The 5,600 of Option C would have given 6% / 15% — the 5,700 bump buys ~3 extra coverage points where it's thinnest.)

2. **The inflation grind is structurally the hardest to hedge — but the bond gap is second-order, not the headline.** ~21% of the book is bonds, and in a 2022-type grind they fall *with* equities (an equity put can't touch bond losses). Sized honestly, the gap is small:
   
   | Holding                   | % book    | Duration      | 2022-replay loss (est.)         |
   | ------------------------- | ---------:| ------------- | -------------------------------:|
   | IE00B67T5G21 (Euro bonds) | 9.8%      | intermediate  | ~–4,400 CHF                     |
   | CSBGU0 (US)               | 4.5%      | short         | ~–670 CHF                       |
   | DTLA (US 20+yr)           | 3.9%      | long          | ~–4,000 CHF                     |
   | TRE7 (US)                 | 2.4%      | short/interm. | ~–620 CHF                       |
   | **Bond sleeve**           | **20.6%** |               | **~–9,700 CHF (–2.6% of book)** |
   
   The whole sleeve loses ~–9.7k CHF in a severe replay (~15–16% of an equity-led drawdown; the ~–50k equity loss dominates). **DTLA alone is only 3.9% of the book → ~–4k CHF ≈ –1.1% of the portfolio even in a brutal move** — the larger duration exposure is the Euro-bond ETF (9.8%), not DTLA. (Earlier drafts overstated this by pinning the whole sleeve on DTLA.)
   
   **Why it stays un-actioned (not a free fix):** DTLA's long duration is a *cushion* in the more-likely normal/crisis risk-off regimes — rates fall, DTLA rallies +15–20%, offsetting equity. It only hurts in the inflation-grind regime. Shortening duration would buy ~3–5k CHF of inflation-tail protection by *giving up* that risk-off cushion — a regime bet, not a hedge. Hence flagged, not recommended.

3. **ESTX50 carries the hedge** (EU/CH equity 52% vs US 12%) — focusing here and parking SPY is correct.

**Sizing:** 1 + 1 is the agreed size; this is a **partial convexity hedge (~9–27% of a –10% drawdown with Option D)**, not full insurance — a legitimate "some coverage" posture. Fuller coverage would scale lots linearly; not required.

The thin inflation-grind number was the reason the long leg was taken to **5,700 (Option D)** rather than 5,600 — it deepens the ITM at the ~5,340 point, the one strike tweak the portfolio math argued for. Executed 2026-06-02 (§8).

---

## 8. Execution — DONE (2026-06-02, ESTX50 ≈ 6,100)

**Executed at the EUREX open after an overnight rally (6,012 → 6,100, +1.5%).** Spot drift thinned the 5,600 cushion at the inflation-grind end, so the long leg was bumped to **5,700** (restores ~original 6.6% OTM moneyness; the §7-flagged tweak). December-chain check confirmed Dec-18 is the only December expiry and the most liquid (quarterly, 1.7-pt spread vs Nov 2.0 / Jan 3.1; flat IV ~18.5% so duration is free on a vol basis).

| Leg                          | Action        | Fill (pts)    | EUR/lot  |
| ---------------------------- | ------------- | -------------:| --------:|
| Sep-18-26 5,200 P            | Sold (close)  | **42.7**      | +427     |
| Dec-18-26 5,700/4,600 spread | Bought (open) | **125.0** net | –1,250   |
| **Net roll debit**           |               | **82.3**      | **–823** |

**Resulting position: long Dec-18-26 5,700 / 4,600 put spread**, basis 125.0 pts (1,250 EUR/lot).

- Breakeven 5,575 · Max gain **+9,750 EUR/lot** (≤ 4,600) · Max loss –1,250 (≥ 5,700) · Cap **–24.6%** · Net delta ~–0.21.
- Coverage at the inflation –10%-portfolio point (5,417): ~2,580 CHF intrinsic.
- Closing the old 5,200P realized –1,813 EUR (sunk; forward risk now the 1,250 spread premium).

*Original pre-execution ladder (spot 6,012): close 5,200P @ 50.5, open 5,600/4,600 @ 119.85, net ~694/lot. Superseded by the above on the higher tape + strike bump.*

---

## 9. Post-roll monitoring

| Item                | Source                                                         | Threshold / note                                                                                                                 |
| ------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| ESTX50 spot         | TWS                                                            | ~5,417 = –10% portfolio (inflation regime) → consider monetising into any vol spike; breakeven 5,575                             |
| ESTX50 spot         | TWS                                                            | ≤ 4,600 = spread at max payout (+9,750/lot); below this the cap binds                                                            |
| VSTOXX              | TWS                                                            | ≥ 25 / ≥ 30 — vol spike = window to monetise the spread rather than hold to expiry                                               |
| Dec-18 expiry       | calendar                                                       | manage / re-roll before expiry if H2 risk persists                                                                               |
| SPY 660P — calendar | DB id=61 (~14-Aug)                                             | if calm, roll up+out to Dec (~700/620) so US coverage continues into Q4; don't let it expire unhedged (low urgency, 12% of book) |
| SPY 660P — level    | **TradingView alert: SPY crossing down 705 (–7%), open-ended** | US rolling over / hedge going live → assess roll-up-out before Sep expiry. Monetize only if SPY ≤ 660 **and** VIX ≥ 28           |

---

## 9a. SPY 660P snapshot — 2026-06-05 (09:12 CET, US closed)

Live pull (force_refresh; US shut, so the option line is a frozen closing mark — bid/ask tight, `last` null — but ES confirms a near-flat open, so it's representative):

| Field            | Value                                     | vs 2026-06-01 |
| ---------------- | ----------------------------------------- | ------------- |
| Bid / Ask / Mid  | 5.64 / 5.67 / **\$5.66**                  | was \$5.94    |
| IV               | 23.6%                                     | —             |
| Delta            | **–0.113**                                | was –0.119    |
| unPnL            | **≈ –\$401** (mid 5.66 vs cost 9.67 ×100) | was –\$372    |
| DTE              | **105** (→18-Sep-26)                      | was 109       |

**Underlying:** SPY last close **\$757.09** (06-04, +0.38%); ES front future **7,550** (–0.67% overnight) → SPY opens **~\$755** (≈ –0.3%, minor). SPX cash 7,584 (ratio checks). **Moneyness 660/757 ≈ 12.8% OTM** — essentially unchanged; SPY ~flat over 4 days.

**Trigger check:** SPY \$757 vs ↓705 level alert (~7% away) and vs \$660 monetize floor (not close) → **nothing actionable on price.** Hedge bleeding theta as a deep-OTM tail should (delta only –0.11). **Only live decision = the ~14-Aug calendar roll (id=61):** if SPY still calm, roll the 660P up-and-out to Dec (≈700/620) so US coverage continues into Q4. The –\$401 is sunk insurance premium, not a position to manage.

---

## 10. Alerts updated (2026-06-01)

- **id=52 (SPY-SPREAD)** → **deactivated.** Referenced a SPY 580P bought 25-Mar that was closed and replaced by the 660P (12-May "reopen"). Dead.
- **id=60 (OESX TRIGGER 1)** → **replaced** with the Option-D-roll execution reminder.
- **id=61 (OESX TRIGGER 2)** → **replaced** with the SPY-roll reminder (pre-September).
- **id=62 (OESX TRIGGER 3)** → **replaced** with post-roll monitoring; updated post-fill to the actual 5,700/4,600 levels.
- **Post-execution (2026-06-02):** id=60 marked `[EXECUTED]` and deactivated; id=62 monitor re-pointed to 5,700/4,600 (zone 5,417 / breakeven 5,575 / cap 4,600).

---

## 11. Lessons learned

**Analytical**

1. **"–10% portfolio" ≠ "–10% index."** Gonet is only 67% equity (33% bond+gold ballast), so a –10% *portfolio* drawdown needs equity –11% (inflation, bonds fall too) to –18% (crisis). Always translate a portfolio-level protection target into the index move *through the book's effective beta* before picking a strike.
2. **Size a flagged risk as % of book before calling it material.** The "bond-duration gap" was real but second-order: DTLA is only 3.9% of the book (~–1% pain even at –30%), not the 21% I first implied. Don't conflate a holding's large %-move with its contribution. And check whether the "risk" is a *cushion* in another regime (DTLA's duration helps in a normal risk-off) — a one-regime cost is a regime bet to remove, not a free fix.
3. **Defined objective → defined structure.** Once the goal was a bounded "–10% drawdown" (not open-ended crash insurance), the put *spread* became the right tool; the deep 4,600 wing keeps the cap below the 2022-trough zone so it's uncapped across the grind actually feared, while financing ~half the long leg.
4. **A "roll the wing down in a crash" plan is dominated.** It doesn't fire in a flat-vol grind (no skew trigger) — the very scenario feared — and in a crash the spot-widening of the vertical swamps the skew gain, so it costs more than just buying the deep wing up front. Buying the spread now = that roll at the cheapest the vertical ever trades.

**Execution / mechanics**
5. **Re-check strike vs the *live* spot at execution.** A strike chosen for "–X%" at the analysis spot drifts more OTM if the index rallies before you fill. The overnight 6,012 → 6,100 (+1.5%) thinned the 5,600 cushion at the inflation end → bumped to 5,700 to restore moneyness. Recompute the protection band at the live spot on execution morning.
6. **Exchange-closed option pulls are stale, not live.** With EUREX shut overnight, `getOptValue` returned populated bid/ask but **null `last`/`close`/`uPrice`** — frozen snapshot marks. The tell: they hadn't repriced to the overnight futures move (a delta-vs-spot check exposes it). Only the post-open (~09:00 CET) pull is executable; everything before is indicative.
7. **CFD "cash" (BlackBull) is an overnight *spot proxy*, not the physical print.** Useful at 4am to gauge direction (futures-driven), but it's a back-weighted futures synthetic carrying basis — re-strike to ~0.3% precision only, confirm against the cash open.
8. **OESX/EUREX index-option mechanics.** Quoted in **index points × 10 EUR/point** multiplier (no "shares"). **December has only the quarterly (3rd-Fri Dec-18) expiry** ~6 months out — no December weeklies — and the quarterly is the most liquid (1.7-pt spread vs Nov 2.0 / Jan 3.1); term IV was flat ~18.5%, so rolling out cost nothing on a vol basis.
9. **Good fill = work the combo below mid.** Spread bought at 125.0 vs 126.7 mid; Sep leg sold at the 42.7 bid. Net roll 823 vs ~836 mid estimate.

---

*Document prepared 2026-06-01; executed and finalised 2026-06-02. Supersedes the 2026-05-14 wait-and-convert plan.*
