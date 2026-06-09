# XLE Vol Analysis — Directional Bullish Thesis Check

Snapshot: 2026-04-21, as of ~19:59 ET (source 1, EOD) XLE spot: $55.89

---

## 1. Current IV Landscape (ATM)

From `cmiv` (source 1, latest EOD snapshot):

| Tenor | IV    |
| ----- | ----- |
| 10d   | 32.2% |
| 20d   | 30.3% |
| 30d   | 29.0% |
| 60d   | 27.5% |
| 90d   | 27.3% |
| 6m    | 27.2% |

Short-dated IV is elevated. The 10d/30d spread is ~320bps — the front is pricing in a lot of near-term movement.

---

## 2. IV vs Realized Volatility (VRP Check)

From `realvol` (source 1, trade date 2026-04-21):

| Window | RV    |
| ------ | ----- |
| 1d     | 17.8% |
| 7d     | 29.4% |
| 14d    | 31.2% |
| 30d    | 30.6% |
| 60d    | 26.5% |

Key read:

- 30d IV ≈ 29.0% vs 30d RV ≈ 30.6% → VRP is essentially flat to slightly negative (IV barely covers realized)
- 7d and 14d RV are running near 29–31%, right in line with where front IV is priced
- The market is not overpricing short-dated vol vs what has actually been happening — energy has been genuinely volatile

This is not a rich vol environment for sellers, but it's also not screaming "cheap calls." IV is roughly fair given recent realized.

---

## 3. Term Structure — Constructive for Your Thesis

From `impliedvol` (source 1), ATM (vol50):

| Expiry | DTE | ATM IV |
| ------ | --- | ------ |
| Apr 24 | 3   | 37.4%  |
| May 1  | 10  | 32.2%  |
| May 8  | 17  | 30.5%  |
| May 15 | 24  | 30.0%  |
| May 22 | 31  | 28.7%  |
| Jun 18 | 58  | 27.5%  |
| Jun 30 | 70  | 27.4%  |
| Jul 17 | 87  | 27.3%  |
| Aug 21 | 122 | 27.2%  |

The curve is steeply downward-sloping in the front (37% at 3 DTE → ~29% at 30 DTE) and then flattens significantly. Your 2–4 week window sits right at the 30–31 DTE bucket (~28.7% ATM IV), where the curve starts to flatten — you're not paying into the steepest part of the inversion. The vol at 30 DTE is a few points below the very front.

---

## 4. Skew — This Is the Key Signal for You

From `skew` (source 1, EOD):

Short-dated (17–31 DTE) skew is aggressively call-heavy:

| Expiry | DTE | 10d Call Skew | 10d Put Skew | 10d Risk Reversal (call − put) | RR Percentile |
| ------ | --- | ------------- | ------------ | ------------------------------ | ------------- |
| May 8  | 17  | +24.9%        | +7.9%        | -16.9% (calls rich)            | 0.28th %ile   |
| May 15 | 24  | +7.8%         | +4.5%        | -3.2% (calls rich)             | 1.19th %ile   |
| May 22 | 31  | +18.9%        | +7.7%        | -11.2% (calls rich)            | 0.38th %ile   |

Translation: The 10d risk reversal percentile for XLE near-term is at the absolute bottom of its historical distribution — meaning calls are extremely rich relative to puts in percentage terms. The market is already pricing a strong asymmetric upward move (or a vol surface distortion from call-buying demand).

25d call skew percentiles are also 92–99th %ile across May expiries — call vol is universally elevated relative to put vol.

---

## 5. What This Means for Your Bullish Thesis

| Factor           | Signal                 | Implication                                                                               |
| ---------------- | ---------------------- | ----------------------------------------------------------------------------------------- |
| 30d IV vs 30d RV | Roughly fair (IV ≈ RV) | Options not obviously mispriced; paying fair price                                        |
| Term structure   | Steep front, flat back | Buy in the 24–31 DTE window to avoid peak theta/gamma cost                                |
| Call skew (10d)  | 97–99th %ile richness  | Calls are significantly more expensive than usual — the bullish bet is priced in via skew |
| Put skew (10d)   | 0–2nd %ile             | Puts are historically very cheap relative to calls                                        |

---

## 6. Bottom Line

The vol surface partially pushes back on expressing a bullish thesis via outright calls:

- The market is already leaning hard upside — call skew is near historically extreme levels. Buying ATM or OTM calls means you are paying into a surface where upside vol is already bid up.
- Realized vol is running close to implied, so there's no obvious "cheap gamma" story.

Better-fitting structures given this setup:

1. Call spreads (buy ATM / sell OTM call): Reduces the cost of elevated call skew. You give up some upside but buy the move at a more reasonable net debit, and you sell the expensive OTM call vol back.

2. Risk reversal (sell put / buy call): Since put skew is at the 0–2nd percentile (puts are historically cheap), you could sell a relatively cheap put to fund the expensive call — but you need to be comfortable with the downside exposure if XLE doesn't rebound.

3. Avoid naked long OTM calls unless conviction is very high — you are paying 97–99th %ile skew on the call side.

The market is already bet on an upside move in XLE. Your thesis isn't "smart money against consensus" right now — it's aligned with where skew is already positioned. If you still want to express it, call spreads give you the best risk-adjusted structure.
