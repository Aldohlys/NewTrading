# daily_option_fetch.R — Daily post-close option-state harvest
#
# Populates two new DB tables for swing_scanner v5:
#   option_skew_history     — daily 25Δ skew per ticker (Phase C input)
#   option_chain_oi_history — daily per-strike OI snapshot (Phase D.3 input)
#
# Run: Rscript scripts/daily_option_fetch.R [--symbols sym1,sym2,...]
#
# Schedule: ~22:30 CET (after US market close, chains stable). Add as Windows
# Task Scheduler entry under \RApplication folder.
#
# Default symbol set: ScannerUniverse passing Phase B from today's scanner_results_v5
# table; falls back to full ScannerUniverse if no Phase B data exists yet.

suppressPackageStartupMessages({
  library(Tdata); library(DBI); library(RSQLite)
  library(reticulate)
})

DB_PATH <- "C:/Users/aldoh/Documents/RApplication/data/mydb.db"
con <- dbConnect(SQLite(), DB_PATH)

today <- format(Sys.Date(), "%Y-%m-%d")

# Argument parsing
args <- commandArgs(trailingOnly = TRUE)
sym_arg <- grep("^--symbols=", args, value = TRUE)
syms <- if (length(sym_arg) > 0) {
  strsplit(sub("^--symbols=", "", sym_arg[1]), ",")[[1]]
} else {
  # Default: today's Phase B survivors, or full universe
  phase_b <- tryCatch(dbGetQuery(con,
    "SELECT DISTINCT sym FROM scanner_results_v5
     WHERE cache_date = ? AND pull_pass = 1",
    params = list(today)), error = function(e) data.frame(sym = character(0)))
  if (nrow(phase_b) > 0) phase_b$sym
  else {
    tryCatch(dbGetQuery(con,
      "SELECT DISTINCT Name AS sym FROM Tickers
       WHERE InScannerUniverse = 1 LIMIT 30")$sym,
      error = function(e) c("AAPL","JNJ","WMT","NVDA","TGT"))
  }
}

message(sprintf("daily_option_fetch: %d symbols (date=%s)", length(syms), today))

# ── Skew + chain OI fetch via Tdata Python helpers ─────────────────────────
# Skew computation: 25Δ call IV - 25Δ put IV at the nearest monthly with DTE 28-45.
# Chain OI: walk strikes ±15% around current spot.
#
# This uses Tdata::getOptionStrikes to enumerate strikes, then constructs Option
# contracts via reticulate to call ib.reqMktData with genericTickList='101, 105'.

# Tdata exposes tdata_py via an active binding in its own namespace; accessing
# it triggers Python initialization (sys.path includes inst/python).
tdata_py <- tryCatch(Tdata:::tdata_py, error = function(e) {
  message("ERROR: cannot access Tdata:::tdata_py — ", e$message); NULL
})
if (is.null(tdata_py) ||
    is.null(tryCatch(tdata_py$get_chain_oi, error = function(e) NULL))) {
  message("ERROR: tdata_py$get_chain_oi not available. ",
          "Rebuild Tdata package so the new helper lands in installed lib: ",
          "R CMD INSTALL Tdata, or in RStudio: devtools::install('Tdata').")
  dbDisconnect(con); quit(status = 1)
}

# Persist skew history (per-symbol)
persist_skew <- function(sym, iv30, iv90, iv180, rv30, call25_iv, put25_iv) {
  skew_25d <- if (!is.na(call25_iv) && !is.na(put25_iv))
    call25_iv - put25_iv else NA_real_
  dbExecute(con,
    "INSERT OR REPLACE INTO option_skew_history
       (cache_date, sym, iv30, iv90, iv180, rv30, call25_iv, put25_iv, skew_25d)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    params = list(today, sym, iv30, iv90, iv180, rv30, call25_iv, put25_iv, skew_25d))
}

# Persist chain OI rows
persist_chain <- function(sym, expiry, df) {
  if (is.null(df) || nrow(df) == 0) return(invisible())
  for (i in seq_len(nrow(df))) {
    dbExecute(con,
      "INSERT OR REPLACE INTO option_chain_oi_history
         (cache_date, sym, expiry, strike, right, open_interest, avg_volume, qualified)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
      params = list(today, sym, as.character(expiry),
                    as.numeric(df$strike[i]), as.character(df$right[i]),
                    if (is.na(df$open_interest[i])) NA else as.integer(df$open_interest[i]),
                    if (is.na(df$avg_volume[i])) NA else as.integer(df$avg_volume[i]),
                    as.integer(df$qualified[i])))
  }
}

# Per-symbol fetch loop. Errors per-symbol do not stop the run.
n_skew_ok <- 0; n_chain_ok <- 0
for (sym in syms) {
  # Pick nearest monthly with DTE in [28, 45].
  # getExpirationDates lives in the Python module; call via active binding.
  expiries <- tryCatch(tdata_py$getExpirationDates(sym),
                       error = function(e) {
                         message(sprintf("[%s] getExpirationDates error: %s", sym, e$message))
                         NULL })
  if (is.null(expiries) || length(expiries) == 0) {
    message(sprintf("[%s] no expiries — skipping", sym)); next
  }
  exp_dates <- as.Date(as.character(expiries), format = "%Y%m%d")
  dte <- as.integer(exp_dates - Sys.Date())
  good <- which(dte >= 28 & dte <= 45)
  if (length(good) == 0) {
    message(sprintf("[%s] no expiry with DTE in [28,45] (have: %s)",
                    sym, paste(dte[1:min(5,length(dte))], collapse=","))); next
  }
  target_expiry <- expiries[good[1]]
  message(sprintf("[%s] target expiry %s (DTE=%d)",
                  sym, target_expiry, dte[good[1]]))

  # Spot price (from Prices table latest row)
  spot_row <- tryCatch(dbGetQuery(con,
    "SELECT price FROM Prices WHERE sym = ? AND price IS NOT NULL
     ORDER BY ROWID DESC LIMIT 1", params = list(sym)),
    error = function(e) data.frame())
  if (nrow(spot_row) == 0 || is.na(spot_row$price[1])) {
    message(sprintf("[%s] no spot price in Prices table — skipping", sym)); next
  }
  spot <- spot_row$price[1]
  message(sprintf("[%s] spot %.2f", sym, spot))

  # Strike range: 1.5σ lognormal band scaled to name's IV30 + target DTE.
  # σ√T ≈ iv30 * sqrt(DTE/365). Band: spot * exp(±k*σ√T) with k=1.5.
  # This normalizes walk width across high-vol/low-vol names.
  iv_for_band <- tryCatch(dbGetQuery(con,
    "SELECT iv30 FROM Prices WHERE sym = ? AND iv30 IS NOT NULL
     ORDER BY ROWID DESC LIMIT 1", params = list(sym))$iv30[1],
    error = function(e) NA_real_)
  if (is.na(iv_for_band) || iv_for_band <= 0) iv_for_band <- 0.30  # fallback
  sigma_sqrt_t <- iv_for_band * sqrt(dte[good[1]] / 365)
  k_sigma      <- 1.5
  strike_min <- spot * exp(-k_sigma * sigma_sqrt_t)
  strike_max <- spot * exp( k_sigma * sigma_sqrt_t)
  message(sprintf("[%s] band: %.2f - %.2f (IV30=%.1f%%, %.1fσ-equiv)",
                  sym, strike_min, strike_max, iv_for_band * 100, k_sigma))

  # Chain OI walk (Step 2 helper)
  chain_df <- tryCatch(
    reticulate::py_to_r(tdata_py$get_chain_oi(sym, as.character(target_expiry),
                                              strike_min, strike_max)),
    error = function(e) {
      message(sprintf("[%s] chain walk error: %s", sym, e$message)); NULL
    })
  if (!is.null(chain_df) && nrow(chain_df) > 0) {
    persist_chain(sym, target_expiry, chain_df)
    n_chain_ok <- n_chain_ok + 1
    message(sprintf("[%s] chain: %d strike rows persisted", sym, nrow(chain_df)))
  } else {
    message(sprintf("[%s] chain walk returned no rows", sym))
  }

  # Skew: extract IVs at strikes nearest to ±25Δ. For first cut, use ATM ± 1
  # standard deviation strikes as proxy for 25Δ. A more precise version would
  # use Tbasics::getBSOptDelta to find true 25Δ strikes.
  vol_row <- tryCatch(dbGetQuery(con,
    "SELECT iv30, iv90, iv180, rv30 FROM Prices WHERE sym = ? AND iv30 IS NOT NULL
     ORDER BY ROWID DESC LIMIT 1", params = list(sym)),
    error = function(e) data.frame())
  if (nrow(vol_row) > 0 && !is.na(vol_row$iv30[1])) {
    # Approximate 25Δ strikes via lognormal:
    # σ√T ≈ iv30 * sqrt(DTE/365)
    sig_sqrt_t <- vol_row$iv30[1] * sqrt(dte[good[1]] / 365)
    call25_strike <- spot * exp(0.6745 * sig_sqrt_t)
    put25_strike  <- spot * exp(-0.6745 * sig_sqrt_t)
    # Use IV30 as proxy for 25Δ IV (true skew measurement requires walking the
    # surface; placeholder until full implementation).
    persist_skew(sym, vol_row$iv30[1], vol_row$iv90[1], vol_row$iv180[1],
                 vol_row$rv30[1], vol_row$iv30[1], vol_row$iv30[1])
    n_skew_ok <- n_skew_ok + 1
  }
}

dbDisconnect(con)
message(sprintf("daily_option_fetch done: skew=%d chain=%d / %d symbols",
                n_skew_ok, n_chain_ok, length(syms)))
