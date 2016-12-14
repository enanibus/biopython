files <- dir()
sequences <- sapply (files, function(x) scan(x, what = ""))
stopCodons <- c("TAA", "TAG", "TGA")

fyes <- function(pattern, seq) {
  list <- sapply (pattern, function(x) grep(x, seq))
  unlist <- unique(unlist(list))
  return(seq[unlist])
}

fno <-function(pattern, seq) {
  list <- sapply (pattern, function(x) grep(x, seq, invert = TRUE))
  unlist <- unique(unlist(list))
  return(seq[unlist])
}

procaryote <- fyes(stopCodons, sequences)
non_procaryote <- fno(stopCodons, sequences)

l.procaryote <- sapply (procaryote, function(x) nchar(x))
l.non_procaryote <- sapply (non_procaryote, function(x) nchar(x))
summary(l.procaryote)
summary(l.non_procaryote)

library(stringr)
T.procaryote <- str_count(procaryote, "T")/nchar(procaryote)
T.non_procaryote <- str_count(non_procaryote, "T")/nchar(non_procaryote)
summary(T.procaryote)
summary(T.non_procaryote)