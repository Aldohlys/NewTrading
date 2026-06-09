# markethuddle — 2026-04-25

**Source:** External transcript (`markethuddle_20260425_transcript.txt`)
**Transcript:** `markethuddle_20260425_transcript.txt`

## Summary

The episode has two halves. The first is a long interview with **Bohan Jiang** (Falcon X, ex-Goldman G10 FX options trader) by Kevin Muir. The second is **Patrick Ceresna's "Talking Charts"** segment with Kevin.

### Part 1 — Bohan Jiang interview

**Desk mechanics & vol-trader mindset.** Institutional FX options is still a broker-driven, flow-driven OTC market — banks make markets to clients bilaterally, and price discovery happens in the inter-broker (Cantor-style chat-room) market on Bloomberg, with very limited electronic display except for CME's listed currency options (yen, euro, CAD futures-options). The first thing drilled into a new desk trader is *we are not delta traders, we are vol traders*: every position is delta-hedged at inception. Clients either request delta-exchange at trade (hedge funds, RV) or trade "live" (no delta exchange) — in which case the trading team works the hedge in the spot market and adjusts the premium based on the fill. Big complex packages like the JPM option whale are negotiated entirely on vols of each leg vs. a spot/delta ref, not on premiums.

**Theta-gamma P&L framework.** On a daily basis the desk computes theta-gamma — how much theta you paid vs. how much you made trading your gamma around. Conceptually: realized P&L ≈ Σ gamma×(realized vol² − implied vol²), weighted by gamma at each strike. The asymmetry: *theta is highest at the strike, but so is gamma* — you want spot to *move through* your long strike as fast as possible to monetize gamma without paying full theta-at-strike. Corollary: don't want spot to *end* near your long strikes. Bohan calls this the rule that "you want to be long options where spot doesn't end up and short options where it does."

**Retail mistakes.** Number-one mistake: underestimating how fast short-dated options can bleed. Buyers chasing wingy OTM options ("12:50 payoffs / 1000% moves") forget that wings are rich for a reason. ATM is typically the cheapest option on the curve (per unit of gamma) — retail forgets they can express direction with ATM and limit bleed, spending more premium but getting better-priced vol.

**Books.** The "Green Book" — Natenberg, *Option Volatility and Pricing* — handed to all Goldman interns. Bohan also recommends Adam Iqbal's *Volatility: Practical Options Theory* (FX-specific heuristics; Iqbal was Bohan's boss at Goldman running G10 vol, correlation, and exotics), and for the deep end Nassim Taleb's *Dynamic Hedging* and Emmanuel Derman's *The Volatility Smile*.

**Two client archetypes — and why options are not zero-sum.**
1. **RV / vol-focused** clients: reconstruct the vol surface via models, identify dislocations from supply/demand or event mispricing, and trade relative structures (e.g. systematic 105% call buyer creates a kink that an RV book sells against).
2. **Directional** clients: structure asymmetric payoffs from a *real-world* distribution that differs from the *risk-neutral* one. Bohan's binary toy example: stock at 100, can go to 150 or 50. Risk-neutral probability = 50%, so the 100 strike call is worth \$25 to the dealer who can delta-hedge at the risk-neutral measure. A biotech firm believing the true probability is 70/30 (up) values the call at \$35. Both sides can win — the dealer hedges at risk-neutral, the client harvests their real-world edge.

**Crypto-derivatives inefficiencies & the ETH risk-reversal trade (May 2024).** When Bohan moved to crypto (Goldman cash-settled OTC, then Falcon X), the offshore market (Deribit) was structurally inefficient: dealers had balance-sheet/risk limits, early entrants were unsophisticated (would buy back the *same option same tenor* electronically instead of carrying or rolling across tenors), and the vol-RV hedge-fund community wasn't there yet. Skew historically was *for calls* (Bitcoin/ETH calls, dollar puts) because crypto options were used as leverage in bull markets — opposite to S&P (puts richer than calls due to supply/demand for hedges + "grind up, gap down" return distribution), opposite to EUR (USD calls richer in risk-off), opposite to gold (calls richer for catastrophe upside).

The signature trade: in early 2024 the SEC was not responding to ETH ETF filings and two Bloomberg analysts assigned ~20% approval odds. ETH 1M skew was inverted at **7-9 vols** — puts richer than calls — pricing in a high-vol *downside* outcome. Bohan's argument: the modal outcome (no approval) implies vol comes lower and spot sells off slightly; the tail (surprise approval) is the *upside* surprise. The risk reversal expressed this — buy ETH 20-delta calls, sell ETH 20-delta puts, at near zero cost. Within days the SEC surprise-moved on it, spot ripped ~25%, and the trade benefited from both the spot move and the call-vol expansion (risk reversal is both a skew measure and a spot-vol correlation expression).

He notes that since then the market has matured: more sophisticated entrants, more vol-RV participation, tighter pricing in BTC and the top tokens.

**0DTE quoting.** Bohan's desk does not quote a lot of 0DTE. He speculates that the active 0DTE quoters (Citadel-style) rely on heavy electronic infrastructure to manage what is essentially pure gamma + strike-pin / physical-delivery risk on extremely short timescales — manual quoting is infeasible at that cadence.

**Delta hedging — gamma × regime matrix.** The "Holy Grail" is determining the regime (trending vs. mean-reverting) and combining with your own gamma sign:
- Long gamma + trending market → hedge as little as possible, let winners run, get longer as spot moves with you.
- Long gamma + mean-reverting → hedge aggressively, sell high / buy low, earn back theta.
- Short gamma + trending → mirror image (hedge aggressively to flatten).
- Short gamma + mean-reverting → don't over-hedge.

Practical regime signals: variance ratios comparing **intraday realized vol vs. close-to-close realized vol**; **Parkinson** estimator (high-low); **Yang Zhang** estimator (open-high-low-close). The key insight he stresses: *the realized vol you actually trade is unique to you* — it depends on **when** and **how** you delta-hedge, not just the market's realized vol.

**French quant vs. Chicago floor — which vol to mark to.** Bohan's one-liner: *"the French quants sell exotic variance and blow up; the Chicago ones don't."* His substantive position is neither dogma: there are many valid ways to hedge deltas, and you must pick one appropriate to the regime and asset class. The FX-options desk he ran hedged on a **time-based** rule — flat at the WMR fix every four hours — meaning the relevant realized vol *for measuring P&L* is the close-to-fix vol at that cadence, because that's the window at which you actually monetize. If you measure vol close-to-close, you should hedge close-to-close.

**Correlation books.** A correlation product exists wherever you can construct a no-arbitrage triangle. In FX, EUR/USD + GBP/USD + EUR/GBP form one: euro-sterling vol trades cheaper than the legs because the implied correlation is ~80 (eurozone vs. UK move together on monetary policy and rates). For liquid pairs like this you can hedge the implied correlation directly in the inter-broker market. For *illiquid* correlation (dispersion books, pinning dual binaries, exotic cross-asset pairs) you have to live with it — manage the legs and accept the correlation at a level you can stomach. Often the only relief is to pitch a *structure that gives the opposite side of the risk* to a client who wants it, sourced via systematic-community supply.

**Pinning dual-binary example.** If you're pinning both strikes of a dual binary, no one will give you the other side except your original counterparty — you "beg to unwind" or hedge both legs through expiry.

**Index dispersion.** Kevin raises the implied-correlation puzzle in S&P (low realized correlation despite the pod-shop long-short bid and the Korean auto-callable supply). Bohan's answer: scenario analysis only — at the end of the day you're long or short implied correlation at the level you took it, and you delta-hedge through the life of the product.

**Macro positioning (Bohan).** He frames the moment as tricky and price-action-driven — fading the squeeze is hard. Portfolio: barbell between asymmetric long-vol "escalation" trades (long crude, long AGS) and outright risk longs (long S&P). He still likes front-end rates as a trade but says most of it has repriced already; the dominant exercise is position sizing and balance between the two sides.

**Brent 1×2 put spread.** Long Brent benefits from the backwardation (positive roll yield) but vol is extremely high. Bohan likes 1×2 put spreads at zero cost — buy 1 higher-strike put, sell 2 lower-strike puts — chosen on **WTI** with strikes around **June 78 / 71** at zero cost. Selling the cheap side of skew (puts are *low* vol relative to the rich-call/high-vol side in the current crude regime). Max payoff if spot collapses to the lower strike on a deal/Hormuz-reopen scenario, with the asymmetric advantage that you pay no premium. He did the same in last year's "14-day war."

**USDJPY 3M call ladder 157.50 / 158.50 / 159.50.** Buy 1 / sell 1 / sell 1 at zero cost or small credit. **Not** a bullish dollar-yen view — the thesis is that *if* USDJPY grinds higher, intervention/positioning caps depreciation near 160 (the line market and authorities both watch). Payoff is asymmetric for a contained move higher; structure is wrong-way if dollar-yen rips far through 160. He says G10 FX vol has been disappointing because intra-G10 rate differentials rarely sustain large moves — FX is a relative game that tends to mean-revert, except for rare cases like Aussie's commodity terms-of-trade-driven run earlier in the year.

**S&P call spreads, first week of Iran war.** Spot wasn't moving but ATM vol was elevated *and* put skew sat at the **99-100th percentile** over the prior two years. The right expression was selling call spreads — sold ATM vol, but the upper call leg was extremely cheap because the market priced all the skew into the put wing.

**Kevin's subscriber example.** A pod-shop-style trader running rolling Brent 1×1.5 OTM call ratio spreads as a continuous position, claiming the structure realized a **~4 Sharpe**. Bohan echoes that this kind of structural overlay is where pod-shops and desks add real alpha.

**D1 vs. options decision rule.** Bohan: if D1 (delta-one / outright futures or spot) makes sense given the stop and R:R, just use D1. Use options only when there's a vol / skew / structural edge to express.

### Part 2 — Talking Charts (Patrick Ceresna & Kevin Muir)

**Flow-driven regime, JPM whale roll.** Patrick: the last two weeks demonstrated that *flows*, not narrative, drive this market. The **JPM option whale** roll on the month-end was the turn point at the bottom — dealers were short the strike (not long; "pinning" takes happen in the opposite direction), CTAs were net short, and once the position rolled off, the flows pivoted and forced the system to reverse. *Nothing about the underlying narrative changed* (Hormuz still closed, same gluts, same economic problems) — the flip was purely positioning. Kevin agrees on the whale-roll, but on the *follow-through* leg attributes more to *retail* (tax refunds, recently received, flowing into the market) than to CTAs (vol-control is *barely* re-levered). Patrick concedes the marginal-buyer role of CTAs while agreeing retail is in there pushing the bid in the Mag-7 names — retail "comes in where they are most familiar," meaning the sexy names on sale, not utilities or staples.

**2007 Bear Stearns analog.** Patrick raises this as the macro frame: even after the first wave of subprime failures in July 2007, the market brushed it off with a 10-12% correction and rallied to fresh highs in October. The fundamentals didn't *matter* for another six months. He uses this to argue that the market might not "give a shit" about Hormuz / sustained higher oil / second-order economic damage until **September** — not because those problems aren't real, but because the recognition lag is structural.

**Mag-7 and earnings as the single most important event.** Patrick: more important than the Iran resolution. The Mag-7 basket gave back exactly **50%** of prior gains over a 5-month pullback — a textbook half-retracement that ends a correction — and now sits at key overhead resistance into earnings week. If Mag-7 beats and gaps higher Intel/NVDA-style, the **measured-move target on SPX is ~7400-7500 from Liberation Day lows**; without Mag-7 beats, that move can't happen at index level. Going through each name:
- **AAPL**: consolidating sideways 5 months (call it triangle/flat/megaphone, the pattern doesn't matter) — approaching highs right before earnings.
- **MSFT**: most damaged in the SAS-software murder; least likely Mag-7 to retake highs. Even a Fibonacci retrace gets it to **\$480**. Headline risk: MSFT first-time buyouts of senior developers (~7-8% of workforce, AI-driven), shortly mirrored by META; market reaction was *negative* on the day, which Patrick and Kevin found surprising — flagged as a multi-year theme (highest-paying jobs face downsizing, economically disruptive at the macro level even if not stock-specific short-term).
- **META**: flagging formation; ~\$780-800 high retest on a beat.
- **GOOG**: among the strongest through the consolidation; broke out at 61.8% retrace off the midpoint; near 52-week highs; needs only one beat to run.
- **AMZN**: already at 52-week highs *pre-earnings*; structurally one of the strongest.
- **NVDA**: tide turned; approaching previous highs.
- **AMD**: AMD ran hard; non-earnings gap **300 → 350** in one session.
- **INTC** (Mag-7-adjacent): blowout earnings, screaming higher with a gap.

**Narrow rally + 2000 dotcom analog.** Breadth is only **56%** at SPX 52-week highs — Patrick says a healthy reading would be **66-75%**. **XLF** failed in its fib zone (financials not joining); **RTX (defense)** missed and is dragging; the rally is concentrated in the Mag-7 + semis. Patrick floats the parallel to the late-stage dotcom: "only .com stocks were running, everything else was flat" — open question whether this is a parabolic bubble in the "stupid stocks" or genuinely the start of the next bull leg led by tech earnings.

**International confirmation.** **Nikkei** and **Kospi** at 52-week highs — AI/tech-heavy Asian indexes following the same flow despite Korea and Japan being the *most* energy-import-exposed economies to the Middle East conflict. Kevin separately notes structural long-term enthusiasm for Japan ("buy and forget").

**Oil — the \$95 question.** Trump publicly says \$95 oil "isn't that high," and Patrick notes that's not wrong when adjusted for inflation. Jeff Currie (ex-Goldman commodities, now Carlyle) is the most visible bear, calling for \$200 oil on an inventory-draw squeeze that grinds the economy to a halt. Kevin: he suspects oil hits \$200 *before* the economy collapses, but the bears' framework keeps colliding with \$95 spot. He raises a *signaling-mechanism-broken* argument: the administration's "deal is coming" rhetoric is *talking the deferred curve down*, which suppresses the supply response (shale CapEx) that would normally arise from a sustained higher curve. So the more they jawbone, the worse the long-run supply-demand imbalance becomes.

**Oil — Patrick's structural-floor thesis.** Bigger thesis: regardless of whether oil hits \$200, *structural inventory draws are unavoidable* (Morgan Stanley quoted as ~**4.8M bbls/day** — fastest depletion on record). That puts a higher floor on oil (he names ~\$80 as a reasonable downside floor from current \$95) but a much fatter right tail. Long deferred-contract WTI/Brent is asymmetric — backwardation gives positive roll yield, and the COVID-style "nobody cares till everybody cares" risk gives a large right tail. Pulling back off **\$120** has reset the asymmetry, in his view.

**Energy stocks — regime change thesis.** Independent of where oil goes, Patrick believes the *energy-stock* bull market is just getting underway. After a decade-plus of suppressed CapEx and "ESG-taboo" treatment, the war has *structurally* changed attitudes to energy security and CapEx, mainstreaming new build-out and supply diversification. **XOP** just broke out of a 5-year trade range on the monthly chart; that, plus the 50% retracements stocks have done (Eiffel-Tower retrace not playing out), tells him dips should be bought and this is a multi-year theme. Energy stocks don't need oil to \$200 for the sector bull to continue.

**Gasoline.** Despite oil pulling back ~20% off the peak, **gasoline didn't get the memo** — back at 52-week highs ~\$3.30/gallon. Seasonal driving-season tailwind. Question: does it bust \$3.30 to the upside.

**Industrial vs. precious metals.** Industrial metals across the board breaking out: **copper** decoupled from gold and ran (possibly basketed into the semis/data-center theme — copper needed for connectivity); **lithium** breaking out; **aluminum** breaking out despite AA missing earnings; **iron-ore** plays still very good (**RIO** at 52-week highs). The Bloomberg industrial metals index is also breaking out cleanly. **Precious metals** — gold, silver, platinum, palladium, and the miners — are in a corrective absorption phase post the parabolic 2-year run and short-term blow-off. Gold can't beat its 50DMA or its fib zone. Patrick expects this to be the second-quarter theme: more chop, multi-month grinding, sideways absorption. He uses **URA (uranium)** as the analog — a long-term bull that spent 6+ months of corrective chop in the middle. Kevin pushes back marginally on gold miners (blowout earnings, behaving better) — Patrick says no, the pattern is identical and the correlation hasn't broken.

**FX — DXY, yen, euro.** **DXY** stuck in a 96-100 trade range for >1 year, no trend, in the middle of the range. **USDJPY**: extraordinarily weak yen — sat within **one handle of 159.50 for ~33 days**; 160 is the level both authorities and market positioning are watching; intervention has not yet been triggered. Kevin admits he's been wrong on long-dated FX vol: G10 FX is structurally noisy with two-way flow and rate differentials that move together, so directional trends in G10 are rare and quickly mean-revert. **EUR/USD**: bank forecasts in the 1.19-1.22 range based on rate-differential narratives (US softening + ECB potentially hiking); Patrick disagrees and floats a **head-and-shoulders top in EURUSD** driven by Europe's disproportionate oil/food import exposure to the Middle East (the eurozone will eventually have to ease to offset the slowdown). Kevin disagrees: consensus is already bearish EUR, so the sentiment trade is exhausted; he has no strong view.

**Bitcoin.** Bitcoin broke its multi-month trade range to the upside (above the 50DMA, above prior highs) and is *technically* a breakout. But Patrick is unimpressed: relative to the magnitude of the risk-on rally, Bitcoin's move is anemic. It hasn't beaten a fib zone or reclaimed previous lows as overhead resistance. Bitcoin is treated as a *risk-on/risk-off asset, not a safe haven*. Possible move to **~\$85,000** as an oversold relief, but no structural break. **Kevin declines to comment further on Bitcoin.**

**Rates — front-end vs. back-end reaction to next oil spike.** Kevin (writing a piece on this): the front-end (SOFR Dec-26, **transcript renders "sulfur futures"** — ASR error) and **€STR** have been quiet ever since the violent March move. Three cuts got priced out in two weeks then — *taking out cuts* was easy for the front-end to follow oil higher, because the Fed couldn't cut into an oil spike. But *pricing in hikes* is much harder. So the next oil spike, in his view, will get a **much more muted front-end reaction** — his correlation work already shows the relationship breaking down. The complete picture: at \$200 oil he expects a **curve flattening** — front-end still gets pressure, but the back-end *rallies* on recession pricing — which is contrary to most desks' positioning. He notes the bond moves in March were proportionally more violent than the equity moves — what looks like boredom now is just bonds returning to a normalized vol.

**Avis short squeeze.** AVIS ran ~**1000% over two weeks** on the short-squeeze playbook (~**80% short interest**). More orderly than GameStop / AMC (those moved in days; Avis took ~2 weeks) but mechanically identical. Because Avis was ~**17% of the Dow Jones Transports** index, the DJT chart now has a ridiculous spike from **1800 to 2500** — Patrick says this is "permanently scarred" akin to COVID's distortion of the unemployment series. Kevin worries the old **Dow-vs.-DJ-Transports signal** is no longer usable.

**Hertz as the next watch.** **HTZ** has **>50% short interest**; implied vols **doubled** on squeeze speculation. Patrick flags it as a possible next domino, while acknowledging it could be a nothing-burger.

**Reminiscences analog.** Kevin: this kind of single-name corner is not healthy market behavior — markets exist for price discovery and capital formation, not 1000% squeezes. Patrick: corners and squeezes have always existed (Ackman vs. Icahn on Herbalife, etc.) — *Reminiscences of a Stock Operator* — options just amplify the playbook. They agree it's *Reminiscences-like* and don't agree on whether that's healthy.

## Tickers / Assets Mentioned

| Ticker / Asset | Type | Direction / Bias | Context |
|---|---|---|---|
| AA (Alcoa) | Stock | N/A | Missed earnings; aluminum still broke out |
| AAPL (Apple) | Stock | watch | Consolidating sideways 5 months; approaching highs into earnings |
| AGS (Agriculture) | Commodity | long | Part of Bohan's asymmetric "escalation" basket |
| ALUMINUM | Commodity | long | Breaking out per Patrick despite AA's miss |
| AMC | Stock | N/A | Prior short-squeeze precedent that "took its turn" |
| AMD | Stock | long | Non-earnings gap 300 → 350 |
| AMZN (Amazon) | Stock | long | Already at 52-week highs before reporting |
| AUD ("Ozzy") | FX | N/A | Earlier-year run on RBA hikes + commodity terms-of-trade; mean-reverts |
| AVIS (CAR) | Stock | N/A | ~1000% in two weeks; ~80% short interest squeezed |
| BITCOIN (BTC) | Crypto | watch | Broke trade range but underwhelming vs risk-on rally; ~\$85k oversold-relief upside; risk-on/off asset not safe haven |
| BLOOMBERG INDUSTRIAL METALS INDEX | Index | long | Clean breakout |
| BRENT | Future / Commodity | long | Backwardation roll yield + high IV → 1×2 put spreads at zero cost |
| COPPER | Commodity | long | Decoupled from gold; possible AI/data-center basket bid |
| CRUDE / OIL | Commodity | long | Structural inventory draws (~4.8M bbl/day); higher floor ~\$80; ~\$95 spot; deferred contracts attractive |
| DJT (Dow Jones Transports) | Index | N/A | Distorted 1800 → 2500; Avis was ~17% of index |
| DJT (Trump Media) | Stock | N/A | Mentioned only as disambiguation from DJ Transports |
| DXY (US Dollar Index) | FX | neutral | No trend; range 96-100 for >1 year |
| €STR (ESTER) | Rate | N/A | Near-identical pattern to SOFR; quiet after March |
| EUR/GBP | FX | N/A | Implied correlation ~80%; vol cheaper than legs (triangle rule) |
| EUR/USD | FX | N/A | Bank forecasts 1.19-1.22; Patrick floats H&S top from oil-import drag; Kevin disagrees |
| ETH (Ethereum) | Crypto | N/A | Used to illustrate 7-9 vol skew mispricing in May 2024 |
| ETH ETF | ETF | N/A | Bohan's risk-reversal trade context; surprise approval → ~25% spot rip |
| GASOLINE | Future / Commodity | watch | 52w highs ~\$3.30/gal despite 20% oil pullback; summer driving seasonality |
| GBP/USD ("Cable") | FX | N/A | Triangle correlation example |
| GME (GameStop) | Stock | N/A | Cited as analog to Avis squeeze |
| GOLD | Commodity | corrective | Post-blowoff; below 50DMA + fib; multi-month chop expected |
| GOLD MINERS | Sector | corrective | Same pattern as gold per Patrick; Kevin more hopeful |
| GOOG/GOOGL (Google) | Stock | long | Broke out near 52w highs; 61.8% retrace off midpoint; needs 1 beat |
| GS (Goldman Sachs) | Stock | N/A | Speaker's former employer (context only) |
| HERTZ (HTZ) | Stock | watch | >50% SI; IV doubled on squeeze speculation; possible next domino |
| HOOD (Robin Hood) | Stock | N/A | Cited generically as electronic retail brokerage |
| IBIT | ETF | N/A | Prior-approval context for the ETH-ETF debate |
| INTC (Intel) | Stock | long | "Awesome" earnings; screaming higher with gap |
| IRON ORE | Commodity | long | Plays still look very good |
| JPM (JP Morgan) | Stock | N/A | "Option whale" trade — turn point at the bottom (Patrick) |
| KOSPI | Index | long | At 52-week highs; Asia AI/tech bid |
| LITHIUM | Commodity | long | Breaking out |
| LONG BONDS / US 30Y | Rate | neutral | Same trade-range; "watching paint dry"; would *rally* on \$200 oil per Kevin |
| META | Stock | long | Flagging formation; ~\$780-800 high retest if it beats; mirrored MSFT layoffs |
| MSFT (Microsoft) | Stock | watch | Hardest hit in SAS murder; fib target ~\$480; first-time senior-dev buyouts ~7-8% of workforce |
| NIKKEI | Index | long | At 52-week highs |
| NVDA (NVIDIA) | Stock | long | Approaching previous highs |
| PALLADIUM | Commodity | corrective | Same pattern as gold |
| PLATINUM | Commodity | corrective | Same pattern as gold |
| RIO (Rio Tinto) | Stock | long | At 52-week highs |
| RTX (Raytheon) | Stock | N/A | Missed; defense not joining the rally |
| S&P 500 (SPX / SPY / ES) | Index | long (conditional) | Reabsorbed 10% pullback to ATH in ~10 days; ~7400-7500 measured-move target from Liberation Day lows conditional on Mag-7 beats |
| SILVER | Commodity | corrective | Same pattern as gold |
| SMH (Semiconductors) | ETF | long | "Full-on bull face"; rally leadership |
| SOFR / Dec-2026 SOFR FUTURES | Rate | N/A | Quiet after March; muted reaction expected to next oil spike (Kevin); transcript renders "sulfur futures" (ASR error) |
| URA (Uranium) | ETF | N/A | Used as a corrective-absorption analog for gold |
| USD/JPY (Yen) | FX | watch / muted | 33 days within 1 handle of 159.50; 160 intervention ceiling; 3M call ladder 157.50/158.50/159.50 at zero cost |
| WTI | Future / Commodity | long | June 1×2 put spread (~78/71) at zero cost; selling cheap side of skew |
| XLF (Financials) | ETF | N/A | Failed in fib zone; not joining rally |
| XOP (Oil & Gas Producers) | ETF | long | Just broke a 5-year monthly range; dips to be bought; Eiffel-Tower retrace unlikely |

## Notable Trade Ideas / Levels

- **Brent / WTI 1×2 put spreads at zero cost** — buy 1 higher-strike put, sell 2 lower-strike puts; example WTI June ~**78 / 71**; sells the cheap side of skew (put wing is *low* vol in the current crude regime); max payoff = strike distance on a Hormuz-reopen / deal-driven sharp move down; backwardation gives positive carry while waiting (Bohan).
- **USDJPY 3M call ladder 157.50 / 158.50 / 159.50** — buy 1 / sell 1 / sell 1 at zero cost or small credit; thesis is muted realized vol near the **160 intervention ceiling**, not a directional bullish dollar-yen view (Bohan).
- **S&P call spreads** during the early-Iran-war sideways week — sold elevated ATM vol while put skew sat at the **99-100th percentile** vs. the prior two years, making the call leg unusually cheap (Bohan, historical).
- **ETH 1M 20-delta risk reversal (May 2024)** — sell puts / buy calls when 1M downside skew was rich by **7-9 vols** vs the modal "no approval, vol comes off" outcome; trade benefited from both surprise SEC approval (~25% spot move) and call-vol expansion (Bohan, historical example).
- **Brent 1×1.5 OTM call ratio (rolling)** — Kevin's subscriber's structural overlay; claimed **~4 Sharpe** as a rolling position; cited as an example of where pod-shop / desk structures add real alpha.
- **SPX measured move ~7400-7500** from Liberation Day lows, conditional on Mag-7 beats (Patrick).
- **MSFT fib retrace target ~\$480** (Patrick).
- **META high retest ~\$780-800** if it beats (Patrick).
- **Bitcoin upside ~\$85,000** as a possible oversold-relief level; nothing structurally beaten yet (Patrick).
- **USDJPY 160** — intervention ceiling that's holding; ~159.50 has been the magnet for 33 days.
- **EURUSD 1.19-1.22** — bank forecast range cited; Patrick disagrees, floats H&S top.
- **Gasoline ~\$3.30/gallon** — current 52w-high level; break/no-break is the watch.
- **Oil ~\$80 downside floor / ~\$95 spot / pullback off \$120** — Patrick's asymmetry frame.
- **Curve flattening at \$200 oil** — Kevin's expected reaction: front-end pressured, back-end rallies on recession pricing.
- **DJ Transports 1800 → 2500** — Avis-driven distortion (~17% index weight).
- **Avis ~80% short interest / Hertz >50% SI** — Hertz IV doubled on squeeze speculation.
- **Industrial-metals index breakout** + **RIO 52w highs** + **lithium / aluminum breakouts** — broad industrial-metals confirmation.
- **XOP monthly chart** — break of a 5-year range; framed as new structural energy bull market.
