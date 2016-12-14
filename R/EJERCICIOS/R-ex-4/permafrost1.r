lengthOfSequence <- function (seq) 
return(nchar(seq))

# frequencyOfT <- function(seq)
# freq = 0
# for (c in seq) {
# 	if (c == 'T') 
# 		freq = freq + 1
# }
# return freq/lengthOfSequence(seq)


getwd()
setwd("C:/Users/JET/Documents/BIOQUIMICA/4º/HPBBM/R/EJERCICIOS/R-ex-4/permafrost/")
 files <- dir()
 for (f in files) { 
 	seq <- scan(f, what="")
 	l <- lengthOfSequence(seq)
 	# fr <- frequencyOfT(seq)
 	cat("Leido fichero: ", f)
 	cat("\n")
 	cat(seq)
 	cat("\n")
 	cat("longitud: ", l)
 	cat("\n")
 	# cat("frecuencia: ", fr)
 	# cat("\n")
 }
 
