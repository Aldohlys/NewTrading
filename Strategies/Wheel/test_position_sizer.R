#!/usr/bin/env Rscript
# ===========================================================================
# Test script for Tdata::sizePosition()
# Reads a CSV file (European format: semicolon-delimited, comma decimal)
# and runs the position sizer for each symbol group.
#
# Usage:
#   Rscript test_position_sizer.R                          # default CSV
#   Rscript test_position_sizer.R my_trades.csv            # custom CSV
#
# CSV columns:
#   symbol  - groups legs into positions
#   strike  - option strike price
#   right   - C or P
#   pos     - signed position (+1 long, -1 short)
#   dte     - days to expiration (per leg)
#   mul     - contract multiplier (100 for US options)
#   sig     - per-leg implied volatility (decimal)
#   spot    - underlying price (same for all legs of a symbol)
#   credit  - net credit received per unit (must be > 0)
#   iv      - annualized IV (decimal)
#   hv      - annualized HV (decimal)
#   ivp     - IV percentile rank (0-100)
#   hvp     - HV percentile rank (0-100)
#   max_loss - risk budget per trade in $ (optional, default 600)
# ===========================================================================

library(Tdata)

# --- Read CSV path from command line or use default ---
args <- commandArgs(trailingOnly = TRUE)
csv_path <- if (length(args) >= 1) {
  args[1]
} else {
  file.path(dirname(sys.frame(1)$ofile %||% "."), "position_sizer_test.csv")
}

if (!file.exists(csv_path)) {
  stop("CSV file not found: ", csv_path)
}

cat("Reading:", csv_path, "\n\n")

# European CSV: semicolon separator, comma decimal
input <- read.csv2(csv_path, stringsAsFactors = FALSE)

# --- Process each symbol ---
symbols <- unique(input$symbol)

for (sym in symbols) {
  rows <- input[input$symbol == sym, ]

  # Legs data frame (per-leg columns)
  legs <- data.frame(
    strike = rows$strike,
    right  = rows$right,
    pos    = as.integer(rows$pos),
    dte    = as.integer(rows$dte),
    mul    = rows$mul,
    sig    = rows$sig
  )

  # Position-level inputs (from first row)
  spot     <- rows$spot[1]
  credit   <- rows$credit[1]
  iv       <- rows$iv[1]
  hv       <- rows$hv[1]
  ivp      <- rows$ivp[1]
  hvp      <- rows$hvp[1]
  max_loss <- if ("max_loss" %in% names(rows)) rows$max_loss[1] else 600

  cat(strrep("=", 70), "\n")
  cat(sprintf("  %s  |  spot=%.2f  credit=%.2f  IV=%.0f%%  HV=%.0f%%  IVP=%.0f  HVP=%.0f\n",
              sym, spot, credit, iv * 100, hv * 100, ivp, hvp))
  cat(strrep("-", 70), "\n")

  # Show legs
  for (i in seq_len(nrow(legs))) {
    l <- legs[i, ]
    cat(sprintf("  Leg %d: %s %s %.0f  pos=%+d  DTE=%d  mul=%d  sig=%.1f%%\n",
                i, l$right, ifelse(l$right == "P", "Put ", "Call"), l$strike,
                l$pos, l$dte, l$mul, l$sig * 100))
  }
  cat("\n")

  # Run sizer
  result <- sizePosition(legs, spot = spot, credit = credit,
                         iv = iv, hv = hv, ivp = ivp, hvp = hvp,
                         max_loss = max_loss)

  if (is.null(result)) {
    cat("  ERROR: sizePosition returned NULL\n\n")
    next
  }

  # Regime
  reg <- result[["regime"]]
  cat(sprintf("  Regime: %s  |  Edge: %s  |  IV/HV: %.2fx  |  VRP: %.1f%%\n",
              reg[["regime"]], reg[["edge_grade"]],
              reg[["iv_hv_ratio"]], reg[["vrp_pct"]]))
  cat(sprintf("  Sizing mult: x%.2f  |  Adjusted vol: %.1f%%\n\n",
              reg[["sizing_multiplier"]], reg[["adjusted_vol"]] * 100))

  # Scenarios table
  cat(sprintf("  %-18s %7s %8s %8s %5s %6s %8s %6s\n",
              "Scenario", "SimVol", "ES95", "ES99", "Lots", "Win%", "E[PnL]", "TP%"))
  cat(sprintf("  %s %s %s %s %s %s %s %s\n",
              strrep("-", 18), strrep("-", 7), strrep("-", 8), strrep("-", 8),
              strrep("-", 5), strrep("-", 6), strrep("-", 8), strrep("-", 6)))

  for (sc_name in c("hv_base", "hv_adjusted", "iv_conservative")) {
    sc <- result[["scenarios"]][[sc_name]]
    label <- switch(sc_name,
      hv_base = "HV base",
      hv_adjusted = "HV adjusted *",
      iv_conservative = "IV conservative"
    )
    cat(sprintf("  %-18s %6.1f%% $%7.0f $%7.0f %5d %5.1f%% $%+7.0f %5.1f%%\n",
                label, sc[["sim_vol"]] * 100, sc[["es95"]], sc[["es99"]],
                sc[["lots_adj"]], sc[["win_rate"]], sc[["mean_pnl"]], sc[["tp_pct"]]))
  }

  # Recommendation
  rec <- result[["recommendation"]]
  cat(sprintf("\n  >> RECOMMENDATION: %d lot(s)  |  ES99/lot: $%.0f  |  Win: %.0f%%\n",
              rec[["lots"]], rec[["es99_per_lot"]], rec[["win_rate"]]))
  if (rec[["conservative_lots"]] != rec[["lots"]]) {
    cat(sprintf("     Conservative: %d lot(s)\n", rec[["conservative_lots"]]))
  }
  cat("\n")
}
