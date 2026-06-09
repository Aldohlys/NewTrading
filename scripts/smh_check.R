suppressPackageStartupMessages(library(Tdata))
hist <- tryCatch(quantmod::getSymbols("SMH", src = "yahoo",
                                      from = as.character(Sys.Date() - 200),
                                      to = as.character(Sys.Date() + 1),
                                      auto.assign = FALSE),
                 error = function(e) { cat("yahoo err:", e$message, "\n"); NULL })
if (!is.null(hist)) {
  closes <- as.numeric(quantmod::Cl(hist))
  ma50   <- mean(tail(closes, 50))
  spot   <- tail(closes, 1)
  cat("SMH spot:", round(spot, 2), "\n")
  cat("SMH MA50:", round(ma50, 2), "\n")
  cat("Pct above MA50:", round((spot / ma50 - 1) * 100, 1), "%\n")
  cat("Extended trigger (>15%):", spot > ma50 * 1.15, "\n")
}
res <- tryCatch(Tdata::getVolMetrics("SMH"),
                error = function(e) { cat("getVolMetrics err:", e$message, "\n"); NULL })
if (!is.null(res) && nrow(res) > 0) {
  cat("\nFresh vol:\n")
  print(res[, c("sym", "iv30", "ivp", "ivp_2y", "rv30", "vrp")])
}
