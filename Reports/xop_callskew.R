suppressMessages({ library(Tdata); library(dplyr) })
py <- Tdata:::tdata_py
today <- as.Date("2026-06-08")

sp <- tryCatch(Tdata::getStockPrice("XOP", close = FALSE), error = function(e) NULL)
spot <- tryCatch(as.numeric(sp$price[nrow(sp)]), error = function(e) NA_real_)
if (length(spot)==0 || is.na(spot)) spot <- 169.5
cat(sprintf("XOP spot used: %.2f\n", spot))

exps <- py$getExpirationDates("XOP")
exps <- as.character(unlist(exps))
ed   <- as.Date(exps, format = "%Y%m%d")
dte  <- as.integer(ed - today)
keep <- which(dte >= 14 & dte <= 90)
exps <- exps[keep]; dte <- dte[keep]
ord  <- order(dte); exps <- exps[ord]; dte <- dte[ord]
cat("Tradeable expiries:", paste0(exps," (",dte,"d)", collapse=" | "), "\n\n")

# call-strike ladder around spot
strikes <- seq(floor(spot/5)*5 - 20, ceiling(spot/5)*5 + 30, by = 5)

interp_at_delta <- function(d, iv, target) {
  ok <- is.finite(d) & is.finite(iv) & iv > 0.01 & iv < 3
  d <- d[ok]; iv <- iv[ok]
  if (length(d) < 2) return(NA_real_)
  o <- order(d); d <- d[o]; iv <- iv[o]
  if (target < min(d) || target > max(d)) return(NA_real_)
  approx(d, iv, xout = target)$y
}

rows <- list()
for (i in seq_along(exps)) {
  ex <- exps[i]
  df <- tryCatch(py$getOptValue("XOP", ex, as.list(strikes), "C", force_refresh = TRUE),
                 error = function(e) NULL)
  if (is.null(df) || nrow(df) == 0) { cat(ex, "-> no data\n"); next }
  df <- df[order(df$strike), ]
  d  <- as.numeric(df$delta); iv <- as.numeric(df$impliedvol); k <- as.numeric(df$strike)
  iv_atm <- interp_at_delta(d, iv, 0.50)
  iv_25  <- interp_at_delta(d, iv, 0.25)
  iv_10  <- interp_at_delta(d, iv, 0.10)
  rows[[length(rows)+1]] <- data.frame(
    expiry = ex, DTE = dte[i],
    ATM_IV = round(100*iv_atm,1),
    IV_25dC = round(100*iv_25,1),
    IV_10dC = round(100*iv_10,1),
    skew_25c = round(100*(iv_25 - iv_atm),1),
    skew_10c = round(100*(iv_10 - iv_atm),1),
    n_iv = sum(is.finite(iv) & iv>0.01 & iv<3)
  )
  # raw dump for transparency
  cat(sprintf("--- %s (%dd) ---\n", ex, dte[i]))
  dump <- data.frame(strike=k, delta=round(d,3), iv=round(100*iv,1), mid=round(as.numeric(df$value),2))
  print(dump, row.names = FALSE)
  cat("\n")
}
cat("================ SUMMARY: call skew by chain ================\n")
print(do.call(rbind, rows), row.names = FALSE)
