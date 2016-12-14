getwd()
setwd("C:/Users/JET/Documents/BIOQUIMICA/4º/HPBBM/R/EJERCICIOS/R-ex-4/permafrost/")
 files <- dir()
 for (f in files) { 
 	seq <- scan(f, what="")
 	cat("Leido fichero: ", f)
 	cat("\n")
 	cat(seq)
 	cat("\n")
 }
 cat(length(seq))