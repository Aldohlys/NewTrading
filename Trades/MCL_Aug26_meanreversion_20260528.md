# MCL Aug'26 — Mean-Reversion Bounce (Closed)

**Date:** Plan + entry 2026-05-28 → Stopped 2026-05-28 (intraday, ~8.5 h)
**Vehicle:** MCL Aug'26 futures (CLQ26, NYMEX, multiplier \$100/pt)
**Position:** Long 2 lots @ **\$89.16** (avg)
**Result:** **−\$444** — stopped on a flash sell; \$87.15 stop filled \$86.94 (\$0.21/lot slippage)
**Status:** **Closed**
**Framework:** Mean-reversion bounce — **NOT a breakout trade.** See §7.

---

## 1. Thesis

Buying the bounce off a violent washout, betting the de-escalation selloff overshot to the downside on the **back-month** contract. WTI Aug'26 crashed ~\$100 → \$85 in 6 sessions as the Iran-war geopolitical premium fully unwound (the same spike the Jul'26 trade rode up and exited at \$102). Price is now reverting off the \$85 low toward the daily mean.

This is a **counter-trend** trade: Aug is below both its daily 20 EMA (~\$94.8) and 50 EMA (~\$92.0). The edge is reversion to the mean, not trend continuation. Horizon is short (hours to a few days), target is a retrace level, **not** a new high.

---

## 2. Market context (2026-05-28, ~08:00 CET)

### Term structure
- **CLN26 (Jul, front):** \$91.95
- **CLQ26 (Aug, this trade):** \$89.01
- **Jul–Aug spread = \$2.94** backwardation (supply premium still present but draining vs the spike)
- Front 10-day high \$105.21 → now \$91.95; the prompt-month panic has bled off

### Daily trend (Aug)
- Crashed \$100.10 → **\$85.00** (10-day low, 2026-05-27) in 6 sessions
- Now **below 20 EMA (~\$94.8) and 50 EMA (~\$92.0)** → trend freshly flipped down → this is explicitly counter-trend
- (EMAs translated from front-continuous − \$2.94 spread; confirm on the Aug chart in TWS)

### 15-minute structure (the trade timeframe)
- Washout low ~**\$85.8**, higher-lows uptrend back to bounce high ~**\$89.5**
- Fib retracement of the bounce: **0.382 = 88.08 · 0.5 = 87.65 · 0.618 = 87.22**
- **\$88 = natural support** (polarity flip: was the \$87–88 resistance during the base, now support after the breakout above it) + 0.382 fib + 15m MA confluence
- Currently pulling back (~\$88.73 at write time); the live test is whether \$88 holds

---

## 3. Vehicle & sizing

- **MCL** (micro), multiplier **\$100/pt** — not CL (\$1,000/pt). Confirmed.
- 2 lots @ \$89.16, avg cost \$89.16.
- MCL chosen (vs CL) so the structural stop fits the risk budget — same recurring reason as the Jul trade: CL's \$1,000 multiplier blows the cap before the stop reaches a sane technical level.

---

## 4. Risk

**Stop: \$87.15 on both lots** (single flat stop).

- Sits **just below the 0.618 fib (~87.22)** — the structural-failure line for the bounce.
- Max risk = (\$89.16 − \$87.15) × \$100 × 2 = **\$402** (\$201/lot).
- Budget extended from the default ~\$300 to \$400 deliberately: the extra ~\$68 moves the stop *across* the 0.618 instead of leaving it at \$87.50 (above 0.618, where a textbook golden-ratio retrace would tag it out and cost the loss **plus** the upside to \$92). High-value risk — it maps onto the structural line, not vague "room."
- **Dead-zone note:** any stop between \$87.50 and \$87.25 spends risk without clearing the 0.618 — worst of both. Stop is either ≥\$87.50 (cheap, vulnerable) or ≤\$87.20 (clears it). Chose the latter.

**Line in the sand:** the \$85.0–85.8 washout low. The \$87.15 stop exits well above it — by design. If the 0.618 fails, the reversion thesis is broken; no need to wait for a full washout retest, no averaging down.

---

## 5. Targets & exit plan

Mean-reversion target = the daily mean. The 15m reversion off \$85.8 is largely done; the next magnet is the **daily 50 EMA ~\$92**, then the 20 EMA ~\$94.8 (stretch / new-trade territory).

| Target | Level | Reward/lot | R/R |
| ------ | ----- | ---------- | --- |
| Scale (de-risk) | \$90.0 (round, just above \$89.5 bounce high) | \$0.84 | 0.42 |
| Shelf | \$90.5 (15m breakdown point) | \$1.34 | 0.67 |
| **Primary (runner)** | **\$92.0 (daily 50 EMA)** | **\$2.84** | **1.41** |
| Stretch | \$94.0 (daily 20 EMA) | \$4.84 | 2.41 |

**Plan:**
- **Lot 1 (scratch):** sell limit at **\$90.0** — de-risks the position toward free, locks a small gain. Pre-set now, don't decide in the moment.
- **Lot 2 (runner):** target **\$92.0** (the mean). Trail up only after \$88 holds and \$89.5 reclaims.
- Beyond \$92 is **not** this trade — a move that keeps running toward \$94+ is a *new* setup with its own stop, not an extension of this runner (see §7).

---

## 6. Monitoring framework

| Signal | Hold / bullish | Exit / thesis-broken |
| ------ | -------------- | -------------------- |
| **\$88 support (0.382 + polarity flip)** | Holds on the pullback → reversion intact | Decisive 15m close below \$88 → weakening |
| **0.618 (\$87.22)** | Above it → bounce structurally alive | Break below (stop \$87.15) → reversion failed, out |
| **\$85.0–85.8 washout** | — | Below → unconditional exit, no add-backs |
| **Daily 50 EMA (\$92)** | Approaching → take runner profit | Rejection there → don't hope, scale out |
| **Jul–Aug spread (\$2.94)** | Holding/widening → supply premium intact | Collapsing toward flat → premium draining, bearish for the hold |

**Liquidity note:** pre-9:00 CET tape is thin (European markets closed). Don't add legs or chase fills before the open; a low-volume wick can be noise, not signal. Reassess on real volume after 09:00.

---

## 7. Framework discipline (lessons carried from Jul'26)

1. **This is mean-reversion, not BOT breakout.** Stop logic (below 0.618), target (the mean, \$92), and horizon (short) all follow from that. Don't import breakout-trade reasoning.
2. **Don't switch frameworks mid-trade.** If price reclaims \$92 and looks like a genuine trend turn, that is a **new BOT trade** with its own entry/stop/size — not an extension of this bounce runner. → [[feedback-dont-switch-frameworks-midtrade]]
3. **A stop-out ≠ a wrong read.** \$87.15 is a structural-failure stop; if it trips and price then turns back up off \$85–87, that was a deeper-than-0.618 wick, and re-entry on a confirmed reclaim is a clean new trade — not revenge trading.
4. **Hard to exit winners.** Pre-commit the \$90 scratch and \$92 runner limits now; treat 90% of plan as success. → [[feedback-hard-to-exit-winners]]
5. **Verify the contract month.** All prices here are **Aug'26 (CLQ26)**, not the Jul front (\$2.94 higher). Don't quote the front as the position price. → [[feedback-verify-futures-contract-month]]

### Lessons banked (this trade)

6. **No cap-respecting stop survives a washout break.** The flash sell broke \$84.62 — below the \$85.00 line in the sand. Any stop that would have survived sits below \$84.62 (~\$908 risk, 2× cap) *and* would still be underwater at \$86.52. When the unconditional-exit level breaks, the trade is invalidated **by definition** — this is a *correct* stop, not bad luck. The \$87.15-vs-\$87.50 debate is moot: both trigger on a move to \$84.62.

7. **A stop is a trigger, not a guaranteed price — flash sells slip.** \$87.15 stop, \$86.94 fill = \$0.21/lot (\$42) slippage; realized −\$444 vs planned −\$402. In a \$3.62 one-bar air-pocket you fill at-or-worse. Thin tape + micro contract = air-pocket risk; budget slippage into the loss, don't size as if the stop price is the exit.

8. **Don't chase the air-pocket recovery.** Post-stop, price bounced \$84.62 → \$86.52 — tempting re-entry. But that's a **new lower low** in an intact daily downtrend on no interest: the same failed setup, lower. Re-entry is clean only on a confirmed daily reclaim (= a breakout, new trade) or a based bounce with volume — never a 2-bar pop off a flash low. Banking the −\$444 as a correct stop beats revenge-trading it back.

---

## 8. Live log

- **2026-05-28 ~07:30 CET** — Long 2× MCL Aug'26 @ \$89.16. Initial stop \$87.50 (flat, ~\$332).
- **2026-05-28 ~08:00 CET** — Stop moved down to **\$87.15** (clears 0.618 \$87.22; max risk \$402). Lowering a resting stop in thin tape is operationally safe — reduces wick-trigger odds, doesn't chase fills.
- **2026-05-28 ~11:00 CET** — Drifted to \$87.88, below \$88 support / 50 MA on thin volume; held the 0.5/0.618 zone. Stop survived — a \$87.50 stop would have been tagged here, so the \$68 extension to \$87.15 paid off (at this point).
- **2026-05-28 ~15:00 CET** — Recovered: reclaimed 0.382 (88.08), 15m MA curling up on rising volume. Bounce maturing toward the \$92 daily-mean target. Still a 15m up-leg *inside* a daily downtrend → reversion, **not** a breakout.
- **2026-05-28 16:00–16:15 CET (10:00 EST)** — **Flash sell.** Bar O 88.24 → **L 84.62** → C 86.01, vol 714. Broke clean through the \$85.00 washout (unconditional-exit line). **Stopped \$87.15, filled \$86.94** (\$0.21/lot slippage). Flat. **Realized −\$444.** Price recovered to \$86.52 — still below the stop, so the exit was not premature.
