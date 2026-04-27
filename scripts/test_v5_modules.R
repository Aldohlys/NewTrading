# test_v5_modules.R — Lightweight unit tests for v5 scanner modules
#
# Tests core functions in isolation with synthetic inputs to confirm:
#   - structural_target consensus logic
#   - score_pull stage classification
#   - score_cheap point breakdown
#   - compute_rr_entry vehicle dispatch
#   - classify_entry_state branches
#   - classify_final TOP PICK / WATCH / SKIP routing

suppressPackageStartupMessages({
  library(Tbasics)  # for getOptPrice
})

src_dir <- "C:/Users/aldoh/Documents/RApplication/RStudies/reports/swing_scanner"
source(file.path(src_dir, "scoring.R"))
source(file.path(src_dir, "pull_score.R"))
source(file.path(src_dir, "cheap_score.R"))
source(file.path(src_dir, "setup_chain_rr.R"))
source(file.path(src_dir, "final_classify_v5.R"))

n_pass <- 0; n_fail <- 0
expect <- function(label, condition, detail = "") {
  if (isTRUE(condition)) {
    cat(sprintf("[PASS] %s\n", label))
    n_pass <<- n_pass + 1
  } else {
    cat(sprintf("[FAIL] %s — %s\n", label, detail))
    n_fail <<- n_fail + 1
  }
}

cat("=== Phase D.2 — structural target consensus ===\n")

# AAPL at $187 — three sources should cluster cleanly
hist_close <- c(rep(170, 60), seq(170, 195, length.out = 30), seq(195, 187, length.out = 30))
hist_high  <- hist_close + 1
res <- compute_structural_target(price = 187, hist_close = hist_close, hist_high = hist_high)
expect("compute_structural_target returns spot_target_low",
       !is.na(res$spot_target_low),
       sprintf("got=%s", res$spot_target_low))
expect("compute_structural_target round-number $190 is candidate",
       190 %in% res$source_levels,
       sprintf("source_levels=%s", paste(res$source_levels, collapse=",")))

# .nearest_round_above tiered grid
expect("round-grid: 47 → 50",  .nearest_round_above(47)  == 50)
expect("round-grid: 187 → 190", .nearest_round_above(187) == 190)
expect("round-grid: 487 → 500", .nearest_round_above(487) == 500)
expect("round-grid: 100 mult supersedes: 95 → 100",
       .nearest_round_above(95) == 100)

cat("\n=== Phase B — score_pull stage classification ===\n")
# Synthetic last-row indicators
mk_last <- function(price = 100, ma50 = 95, slope = 1, rs_etf = 1,
                    obv_slope = 1, squeeze = 0.5, vol_dec = 0.9,
                    rsi = 60, rsi_slope = 2, updn = 1.3, rng = 75,
                    vol_surge = 1.5, ret20 = 5) {
  data.frame(
    Close = price, ma50 = ma50, ma50_slope = slope, ret20 = ret20,
    obv_slope = obv_slope, squeeze_ratio = squeeze, vol_decline = vol_dec,
    rsi14 = rsi, rsi_slope = rsi_slope, updn_ratio = updn, rng_pct = rng,
    vol_surge = vol_surge, atr14 = 2, adx10 = 25, dip = 25, din = 15,
    high20 = price + 5, low20 = price - 5, ma20 = ma50 + 1, ma20_slope = 1)
}

last_breakout <- mk_last()
p <- score_pull(last_breakout, price = 100, etf_ret = 0,
                sector_rs_rank = 1, n_long_sectors = 8,
                sector_long_gate = TRUE, sector_short_gate = FALSE,
                trend_passes = FALSE, rs_3m = NA)
expect("early breakout → stage='early'", p$stage == "early",
       sprintf("got=%s", p$stage))
expect("early breakout → pull_score >= 6", p$pull_score >= 6,
       sprintf("got=%d", p$pull_score))
expect("top-3 sector → sector_pts = 3", p$sector_pts == 3L,
       sprintf("got=%d", p$sector_pts))

last_extended <- mk_last(price = 130, ma50 = 100)  # price > ma50*1.15
p_ext <- score_pull(last_extended, price = 130, etf_ret = 0,
                    sector_rs_rank = 4, n_long_sectors = 8,
                    sector_long_gate = TRUE, sector_short_gate = FALSE,
                    trend_passes = FALSE, rs_3m = NA)
expect("extended (price > MA50*1.15) → stage='extended'",
       p_ext$stage == "extended", sprintf("got=%s", p_ext$stage))

cat("\n=== Phase C — score_cheap point breakdown ===\n")
vol_row <- data.frame(
  IVP_2y = 30,    # cheap → 3 pts
  VRP    = -2,    # cheap → 2 pts
  IV30 = 25, IV90 = 27, IV180 = 28,  # contango: 25 vs 27 → -7% → 2 pts
  RV30 = 24,
  skew_25d = 0.01)
c_obj <- score_cheap(vol_row, skew_history = NULL,
                     sector_iv_median = NA,
                     pull_direction = "up")
expect("score_cheap IVP_2y=30 → 3 pts", c_obj$ivp_pt == 3L,
       sprintf("got=%d", c_obj$ivp_pt))
expect("score_cheap VRP=-2 → 2 pts", c_obj$vrp_pt == 2L,
       sprintf("got=%d", c_obj$vrp_pt))
expect("score_cheap term contango → 2 pts", c_obj$term_pt == 2L,
       sprintf("got=%d", c_obj$term_pt))
expect("score_cheap total = 7 → passes", c_obj$cheap_score >= 6 && c_obj$passes,
       sprintf("score=%d passes=%s", c_obj$cheap_score, c_obj$passes))

vol_row_expensive <- data.frame(
  IVP_2y = 85, VRP = 15, IV30 = 35, IV90 = 30, IV180 = 28,
  RV30 = 18, skew_25d = 0.02)
c_exp <- score_cheap(vol_row_expensive, skew_history = NULL,
                     sector_iv_median = NA, pull_direction = "up")
expect("score_cheap expensive IV → fails cutoff", !c_exp$passes,
       sprintf("score=%d", c_exp$cheap_score))

cat("\n=== Phase D.4 — compute_rr_entry vehicle dispatch ===\n")
# Long call: ATM with target spot moving from 100 → 110, +2% IV bump
rr_call <- compute_rr_entry(
  vehicle = "call", strike = 100,
  expiry = format(Sys.Date() + 35, "%Y%m%d"),
  current_price = 100, effective_target = 110, iv_now = 0.30,
  entry_premium = 3.0,
  spread_short_strike = NA, spot_target_high = 115, rr_min = 0.5)
expect("call vehicle → rr is numeric", !is.na(rr_call$rr))
expect("call vehicle → entry_ceiling > entry_floor when target favorable",
       !is.na(rr_call$entry_ceiling) && rr_call$entry_ceiling > rr_call$entry_floor)

# Spread: 100/110 spread, target 110
rr_spread <- compute_rr_entry(
  vehicle = "spread", strike = 100,
  expiry = format(Sys.Date() + 35, "%Y%m%d"),
  current_price = 100, effective_target = 110, iv_now = 0.30,
  entry_premium = 3.5,
  spread_short_strike = 110, spot_target_high = 115, rr_min = 0.5)
expect("spread vehicle → rr returned", !is.na(rr_spread$rr))

# Stock direct
rr_stock <- compute_rr_entry(
  vehicle = "stock", strike = NA, expiry = NA,
  current_price = 100, effective_target = 110,
  iv_now = NA, entry_premium = 5,  # 5 = stop distance
  spread_short_strike = NA, spot_target_high = NA, rr_min = 0.5)
expect("stock vehicle → rr = (110-100)/5 = 2.0",
       abs(rr_stock$rr - 2.0) < 0.01,
       sprintf("got=%s", rr_stock$rr))

cat("\n=== Phase E.1 — classify_entry_state ===\n")
expect("entry_floor < ceiling → IN BAND",
       classify_entry_state(2.0, 3.0, "OK") == "IN BAND")
expect("entry_floor > ceiling → PRICED OUT",
       classify_entry_state(4.0, 3.0, "OK") == "PRICED OUT")
expect("chain FAILED → NO CHAIN",
       classify_entry_state(2.0, 3.0, "FAILED") == "NO CHAIN")

cat("\n=== Phase E.2 — classify_final routing ===\n")
df <- data.frame(
  sym = c("TOP", "WATCH_T", "SKIP_B", "SKIP_C", "SKIP_A"),
  sector = "Tech",
  rich_pass = c(TRUE, TRUE, TRUE, TRUE, FALSE),
  pull_pass = c(TRUE, TRUE, FALSE, TRUE, FALSE),
  cheap_pass = c(TRUE, TRUE, NA, FALSE, NA),
  targets_agreeing = c(2, 1, NA, NA, NA),
  rr = c(2.0, 0.3, NA, NA, NA),
  entry_state = c("IN BAND", "PRICED OUT", NA, NA, NA),
  chain_state = c("structurally bounded", "mixed", NA, NA, NA),
  rank = "", phase_of_drop = "",
  stringsAsFactors = FALSE)
df_classified <- classify_final(df, rr_min = 0.5)
expect("TOP PICK row → rank='TOP PICK'",
       df_classified$rank[df_classified$sym == "TOP"] == "TOP PICK")
expect("WATCH row → rank='WATCH'",
       df_classified$rank[df_classified$sym == "WATCH_T"] == "WATCH")
expect("Phase B drop → rank='SKIP', phase='B'",
       df_classified$rank[df_classified$sym == "SKIP_B"] == "SKIP" &&
       df_classified$phase_of_drop[df_classified$sym == "SKIP_B"] == "B")
expect("Phase C drop → rank='SKIP', phase='C'",
       df_classified$rank[df_classified$sym == "SKIP_C"] == "SKIP" &&
       df_classified$phase_of_drop[df_classified$sym == "SKIP_C"] == "C")
expect("Phase A drop → rank='SKIP', phase='A'",
       df_classified$rank[df_classified$sym == "SKIP_A"] == "SKIP" &&
       df_classified$phase_of_drop[df_classified$sym == "SKIP_A"] == "A")

cat(sprintf("\n=== %d passed, %d failed ===\n", n_pass, n_fail))
if (n_fail > 0) quit(status = 1)
