lengthOfSequence <- function (seq) 
return(nchar(seq))

frequencyOfT <- function(seq) {
vector <- seq
table <- c(vector)
freq <- match("T", table)
cat(class(freq))
cat("\n")
cat("freq: ", freq)
return(freq / lengthOfSequence(seq))
}

getwd()
setwd("permafrost")
 x <- dir()
 for (f in x) { 
 	seq <- scan(f, what="")
 	l <- lengthOfSequence(seq)
 	fr <- frequencyOfT(seq)
 	cat("Leido fichero: ", f)
 	cat("\n")
 	cat(seq)
 	cat("\n")
 	cat("longitud: ", l)
 	cat("\n")
 	cat("frecuencia: ", fr)
 	cat("\n")
 }
 
