library(dplyr)

f.path="C:/Users/aldoh/Documents/NewTrading/mydb.db"

### mydb belongs to global environment
### it can be retrieved from any function
mydb <- dbPool(drv = RSQLite::SQLite(),dbname = f.path)

portfdb<- tbl(mydb, "U1804173")

replace_date <- function(x) {
  ### replace string by respectively 3rd, 2nd and 1st values
  sub("(\\d{2}).(\\d{2}).(\\d{4})","\\3\\2\\1",x)
}

replace_exp_date <- function(x) {
  d = as.character(as.Date(x))
  sub("(\\d{4}).(\\d{2}).(\\d{2})","\\1\\2\\3",d)
}

dates <- portfdb %>% collect() %>% pull(date) %>% replace_date
mutate(portf,new_date=dates)

new_expdate <- portfdb %>% collect() %>% pull(expdate) %>% replace_exp_date

copy_to(mydb,mutate(portf,new_date=dates,new_expdate=new_expdate,newdate=NULL),overwrite=T,temporary = F,name="U1804173")
