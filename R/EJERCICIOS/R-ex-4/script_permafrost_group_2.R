#Exercise 4: Permafrost and stop codons programming practice
#Group 2
## install.packages("stringr") ## Install the package if you do not have it
library(stringr)
#To work inside the directory that contains the required data:
#getwd()
#setwd("permafrost")
###1:
#Assign all the sequences to a variable "files": 
files <- dir()
#sapply is used to scan all these sequences contained in "files":
sequences <- sapply(files, function(x) scan(x, what = ""))
#Establish the three stop codons:
stopCodons <- c("TAA", "TAG", "TGA")
#Define functionS that returns the sequences filtered by the stop codons
#containing and non_containing all three of above:
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
#Define the variables that contain the data reported:
procaryote <- fyes(stopCodons, sequences)
non_procaryote <- fno(stopCodons, sequences)
#Now the lenght of each sequence is obtained:
l.procaryote <- sapply(procaryote, function(x) nchar(x))
l.non_procaryote <- sapply(non_procaryote, function(x) nchar(x))
##Calculation of the "T" frequency in each type of sequence:
Tfreq_procaryote <- str_count(procaryote, "T")/nchar(procaryote)
Tfreq_non_procaryote <- str_count(non_procaryote, "T")/nchar(non_procaryote)
###3:
#Summaries of the lenght of the sequences:
summary(l.procaryote)
summary(l.non_procaryote)
#Summaries of the reported data for the "T" frequencies:
summary(Tfreq_procaryote)
summary(Tfreq_non_procaryote)
