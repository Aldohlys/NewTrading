# Scanner Methodology — TODO

*Opened 2026-04-24 after JPM rotation miss (BAC + JPM surfaced as TOP PICK 10/14 while Technology led the tape at +6.1% RS vs SPY and Financial sat at −2.9%).*

---

## Context & diagnosis

The options-pricing side of the framework is **data-dependent and clean** — IV/HV/VRP/skew all computable, rules map directly to structure choice. Working well.

The **sector + technical side is qualitative** in the current gating system and is where mistakes cluster. Today's example: the sector gate (see `reports/macro_context` SECTOR GATE table) correctly flagged Technology as the leader (+6.1% RS, ADX 36, breadth bullish), but the swing_scanner surfaced two banks (JPM, BAC) because Financial also passed the binary LONG gate. The **ranking information exists but isn't consumed**.

Goal: reduce qualitative guesswork by tightening two things — macro/sector regime definition, and a short list of technical patterns the trader has measured edge on.

---

## Work item 1 — Macro backdrop / sector leadership consumption

**Problem.** Sector gate is binary (LONG / SHORT / BLOCKED). Multiple sectors simultaneously pass LONG despite very different RS vs SPY. The scanner treats them equally.

**Quick-win (low effort, high signal).** RS vs SPY is already computed per sector and displayed in the SECTOR GATE table. Add a ranking overlay consumed by swing_scanner:

- Among LONG-passing sectors, rank by RS vs SPY.
- Flag names from bottom-half sectors as **amber** (watch, not trade), or apply a composite penalty.
- Cap TOP PICK to names from top-3 sectors by RS.

Today's re-rank would have been: Technology (+6.1), Real Estate (+1.3), Consumer Cyclical (−1.5) → TOP PICK only from those three. JPM and BAC (Financial, −2.9) would have been demoted to WATCH.

**Second-order improvement.** Same-sector concentration penalty: if ≥2 names from the same GICS sector land in TOP PICK, flag the cluster as "sector trade, not stock trade" — requires explicit trader affirmation before entering.

**Open question the user flagged.** How wide should the sector gate be? "Still very wide but may have to remain so." Narrowing aggressively risks missing the single great stock in a weak sector (e.g., WMT in a lagging consumer staples). Proposal: keep the gate wide but add the **ranking layer** above it — gate decides *allowed*, ranking decides *preferred*.

**Deliverable.** Modify `swing_scanner/scoring.R` to consume sector RS from macro_context output (via DB cache) and apply ranking multiplier or amber flag. Validate on next 2–3 weeks of picks before making it a hard filter.

---

## Work item 2 — Technical pattern catalog with measured edge

**Problem.** "I have an edge on this technical pattern" is currently qualitative. Need to convert it to a short list of computable, measurable setups.

**Method.**

1. **Winners review.** Query `Trades` table for closed positions with positive PnL. Stratify by percentile (top quartile vs middle vs bottom). Avoid overfitting to the very best trades — they may be tail outliers, not signal.
2. **Pattern extraction.** For each top-quartile winner, pull price history ~60 days before entry date. Look for recurring setups: pullback-to-MA, flag/pennant, breakout-from-base, gap-and-go, etc. **Statistical discipline:** require a pattern to appear in ≥30% of winners AND ≤15% of losers before calling it edge. Otherwise it's selection bias.
3. **Computability check.** For each candidate pattern, write a detection function (price/volume/MA-based). Must be deterministic, not "I know it when I see it."
4. **Backtest.** Run detection across ScannerUniverse, 5-year window. Forward-return distribution at 5/10/20 days. Win rate, mean, R/R, max drawdown per signal.
5. **Comfort filter.** Keep only patterns the trader would actually execute in real time (some may backtest well but violate temperament — e.g., chasing gap-ups). Edge without execution is zero.

**Starting points from prior work.**
- BOT strategy already formalized (see `bot_strategy_checklist.md`): breakout-from-base with Setup/Breakout score, 56% WR 5Y. Treat this as the template.
- BOT deep dive from 2025 identified: asymmetry recognition, progressive exits, sized 1–5 contracts, Fibonacci zones respected. Some of these are exits, not entries — separate them.
- Consider doing the same formalization for **one or two more patterns** (pullback-to-MA in uptrend, retest-of-breakout) rather than trying to catalog everything at once.

**Deliverable.** `strategies/pattern_catalog.md` with N≤3 patterns, each with: detection rule (computable), backtest stats, trader comfort notes. Wire best pattern(s) into swing_scanner as alternative scoring track to BOT.

---

## Order of operations

1. Work item 1 quick-win (sector RS ranking overlay) — days, not weeks. Immediate impact.
2. Observe scanner output for 2–3 weeks with the overlay on. Confirm it catches rotations like today's.
3. Then Work item 2 (pattern catalog) — deeper work, several sessions of DB/backtest.
