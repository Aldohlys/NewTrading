# calibrate_rr_min.R — Empirical R:R_min from BOT winners
#
# Uses only the Trades table — no external data.
#
# Per-winner R:R = realized return on entry premium:
#   Risk    = avg entry premium per contract (Pos > 0 legs)
#   Reward  = avg exit premium per contract (Pos < 0 legs) − Risk
#   R:R     = Reward / Risk
#
# This is the actual realized risk:reward from the trader's track record.
# The live scanner's BS-forward R:R at structural target with IV+2% is a
# prospective estimate of this realized value (the trader's "expensive but
# still buyable" exit lens). Calibrating R:R_min against realized winners
# anchors the live-scanner threshold to actual delivered edge.
#
# Output: console summary + CSV with per-winner R:R + recommended R:R_min
# at the 25th percentile of winners' realized R:R.

suppressPackageStartupMessages({ library(DBI); library(RSQLite) })

DB_PATH <- "C:/Users/aldoh/Documents/RApplication/data/mydb.db"
OUT_CSV <- "C:/Users/aldoh/Documents/NewTrading/reports/rr_calibration.csv"

con <- dbConnect(SQLite(), DB_PATH)

# Per-Instrument aggregates over all BOT trades.
# Filters: net Pos = 0 (fully closed), at least one open and one close leg,
# only single-leg long-option entries (Pos > 0 first), positive PnL (winners).
df <- dbGetQuery(con, "
WITH legs AS (
  SELECT Instrument, Pos, Prix, TradeDate, PnL
  FROM Trades WHERE Strategy = 'BOT'
),
agg AS (
  SELECT
    Instrument,
    SUM(Pos) AS net_pos,
    MAX(PnL) AS pnl,
    MIN(TradeDate) AS entry_date,
    MAX(TradeDate) AS exit_date,
    SUM(CASE WHEN Pos > 0 THEN Pos ELSE 0 END)            AS contracts_in,
    SUM(CASE WHEN Pos < 0 THEN -Pos ELSE 0 END)           AS contracts_out,
    SUM(CASE WHEN Pos > 0 THEN Pos * Prix ELSE 0 END) /
       NULLIF(SUM(CASE WHEN Pos > 0 THEN Pos ELSE 0 END), 0) AS avg_entry_prix,
    SUM(CASE WHEN Pos < 0 THEN -Pos * Prix ELSE 0 END) /
       NULLIF(SUM(CASE WHEN Pos < 0 THEN -Pos ELSE 0 END), 0) AS avg_exit_prix,
    MAX(CASE WHEN Pos < 0 THEN Prix ELSE NULL END)        AS max_exit_prix,
    MIN(CASE WHEN Pos > 0 THEN Prix ELSE NULL END)        AS min_entry_prix
  FROM legs
  GROUP BY Instrument
)
SELECT Instrument, entry_date, exit_date, pnl, contracts_in, contracts_out,
       ROUND(avg_entry_prix, 4) AS entry_prix,
       ROUND(avg_exit_prix,  4) AS avg_exit_prix,
       ROUND(max_exit_prix,  4) AS max_exit_prix,
       ROUND(min_entry_prix, 4) AS min_entry_prix
FROM agg
WHERE net_pos = 0 AND pnl > 0
  AND avg_entry_prix IS NOT NULL AND avg_exit_prix IS NOT NULL
  AND avg_entry_prix > 0
ORDER BY pnl DESC")

dbDisconnect(con)

cat(sprintf("Closed BOT winners with paired entry/exit: %d\n", nrow(df)))

# ── Filter to single-leg option trades (Instrument format "TICKER ... C|P") ──
# Excludes spreads (multi-leg net=0 by construction for the spread, but the
# Instrument string differs).
single_leg <- grepl("^[A-Z0-9]+ \\d{1,2}[A-Z]{3}\\d{2} [0-9.]+ [CP]$", df$Instrument)
cat(sprintf("Single-leg option winners: %d / %d\n", sum(single_leg), nrow(df)))
df <- df[single_leg, , drop = FALSE]

# ── Compute realized R:R per winner — two anchors ──────────────────────────
# R_R_avg: avg-weighted exit / avg-weighted entry (full realized return)
# R_R_max: max exit price / avg entry — best target the trader hit
#   This second is the closer analog to the live scanner's BS-forward output:
#   "what was the highest expensive-but-still-buyable price reached on this
#   trade?". The scanner attempts to estimate this from structural target +
#   IV+2% before entry; the threshold should reference this empirical max.
df$reward_avg <- round(df$avg_exit_prix - df$entry_prix, 4)
df$R_R_avg    <- round(df$reward_avg / df$entry_prix, 2)
df$reward_max <- round(df$max_exit_prix - df$entry_prix, 4)
df$R_R_max    <- round(df$reward_max / df$entry_prix, 2)
df$days_held <- as.integer(as.Date(df$exit_date, format = "%Y%m%d") -
                           as.Date(df$entry_date, format = "%Y%m%d"))
df <- df[order(-df$R_R_max), ]

# ── Summary + percentiles ───────────────────────────────────────────────────
cat("\n=== Realized R:R distributions ===\n")
cat("R:R_avg (avg-weighted realized):\n");  print(summary(df$R_R_avg))
cat("\nR:R_max (best target hit):\n");      print(summary(df$R_R_max))

qa <- quantile(df$R_R_avg, probs = c(0.05, 0.10, 0.25, 0.50, 0.75, 0.90), na.rm = TRUE)
qm <- quantile(df$R_R_max, probs = c(0.05, 0.10, 0.25, 0.50, 0.75, 0.90), na.rm = TRUE)
cat("\nPercentiles — R:R_avg:\n"); print(round(qa, 2))
cat("\nPercentiles — R:R_max:\n"); print(round(qm, 2))

cat(sprintf("\nWinners covered: %d\n", nrow(df)))
cat(sprintf("\n>>> Recommended R:R_min anchored on R:R_max (25th pctile): %.2f\n",
            qm["25%"]))
cat(sprintf("    (R:R_avg at 25th pctile would be: %.2f — looser, contaminated\n", qa["25%"]))
cat("     by partial losing closes; R:R_max is the cleaner anchor for the\n")
cat("     scanner's BS-forward-at-target prospective R:R.)\n")

# ── Save CSV ────────────────────────────────────────────────────────────────
dir.create(dirname(OUT_CSV), showWarnings = FALSE, recursive = TRUE)
write.csv2(df, OUT_CSV, row.names = FALSE)
cat(sprintf("\nWritten: %s\n", OUT_CSV))
print(head(df[, c("Instrument", "entry_date", "exit_date", "days_held",
                  "entry_prix", "avg_exit_prix", "max_exit_prix",
                  "R_R_avg", "R_R_max", "pnl")], 20))
