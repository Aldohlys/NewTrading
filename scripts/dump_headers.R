x <- readLines("C:/Users/aldoh/Documents/NewTrading/Reports/analyze_UPS_20260512.html", warn = FALSE)
s <- paste(x, collapse = "")
for (anchor in c("Outright put grid", "Vertical spreads")) {
  mm <- regexpr(paste0(anchor, ".+?</table>"), s, perl = TRUE)
  if (mm[1] < 0) { cat(anchor, ": not found\n"); next }
  m <- substr(s, mm[1], mm[1] + attr(mm, "match.length") - 1)
  hdr <- regmatches(m, gregexpr("<th[^>]*>.+?</th>", m, perl = TRUE))[[1]]
  hdr_txt <- gsub("<[^>]+>", "", hdr)
  cat(anchor, "HEADERS:", paste(hdr_txt, collapse = " | "), "\n")
}
