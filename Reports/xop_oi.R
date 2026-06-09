suppressMessages({ library(Tdata); library(dplyr) })
py <- Tdata:::tdata_py
cm <- reticulate::import("tdata_py.chains_manager", delay_load = TRUE)

exps <- c("20260710","20260717","20260724","20260821")
labs <- c("Jul10 (wk)","Jul17 (MONTHLY)","Jul24 (wk)","Aug21 (MONTHLY)")

for (i in seq_along(exps)) {
  ex <- exps[i]
  df <- tryCatch(cm$get_chain_oi(sym="XOP", expiration=ex, strike_min=155, strike_max=190),
                 error=function(e){cat("ERR",ex,conditionMessage(e),"\n"); NULL})
  if (is.null(df) || nrow(df)==0){ cat(labs[i],"-> no OI\n\n"); next }
  df$strike <- as.numeric(df$strike)
  df$open_interest <- as.numeric(df$open_interest)
  df$avg_volume <- as.numeric(df$avg_volume)
  calls <- df[df$right=="C",] |> arrange(strike)
  cat(sprintf("===== %s  [%s] =====\n", labs[i], ex))
  out <- data.frame(strike=calls$strike, callOI=calls$open_interest, callVol=calls$avg_volume)
  print(out, row.names=FALSE)
  cat(sprintf("  Call OI total (155-190): %s | strikes>0 OI: %d\n\n",
              format(sum(out$callOI,na.rm=TRUE), big.mark=","), sum(out$callOI>0,na.rm=TRUE)))
}
