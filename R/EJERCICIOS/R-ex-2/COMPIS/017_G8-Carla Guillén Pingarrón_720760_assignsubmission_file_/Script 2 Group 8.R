#GRUPO 8. Andrea de la Fuente, Carla Guillén, Jorge Nuevo, Álvaro Alfayate

# EJERCICIO 1 ----------------------------------------------------------------

leuk.dat <- read.table("leukemia.data.txt", row.names = 1)
leuk.dat.m <- data.matrix(leuk.dat)
leuk.class <- factor (scan ("leukemia.class.txt", what = "") )
sex <- factor ( c ("Male", "Female") [rep(c(1, 2), 19) ] )


# EJERCICIO 2 ------------------------------------------------------------------

##2.1.
row2124 <- leuk.dat.m[2124, ]
boxplot(row2124 ~ leuk.class, col = c("orange", "lightblue"),
        main = "a) Boxplot of PTEN by patient group", 
        xlab = "Patient groups", ylab = "Gene expression (mRNA)")
       )
        
#Important: You have to know that the first colour will be associated with
        # the first level of class, in this case, ALL.
##2.2.
install.packages("colorspace") ## In case ou don't have it installed
library("colorspace")

for.cex <- leuk.dat.m [ 2600, ] - min ( leuk.dat.m [2600, ] )  + 1
# for.cex will contain the difference between our value and the minus value
# of the row. We will add + 1 in order to remove all zero values.
the.cex <- 2*for.cex/max(for.cex) 
#the.cex will contain the relative amount of our cex. We have choose 2
# because one unit more or less will be seeing as the double/half of the size.
#If we put 3 or 4 the difference between two patients will be bigger.

HK1 <- leuk.dat.m [1, ]
PTEN <- leuk.dat.m [2124, ]

plot( HK1 ~ PTEN, xlab = "PTEN", ylab = "HK-1", 
      main = 'b) HK-1 vs. PTEN. Symbol size proportional to gene 2600',
      pch = c(21, 24)[sex], cex = the.cex, 
      col = diverge_hcl(2)[leuk.class] )

#Be careful: The first pch (21) of the vector will be assign to the first level
# of sex vector: that's female and not male.


lclass <- rep (levels (leuk.class), rep (2, 2))
lsex <- rep ( levels(sex), 2)
text.legend <- paste(lclass, lsex, sep = ", ")
abline( lm (HK1~ PTEN ), lty = 2)

legend( -1, 1, legend = text.legend, pch = c(21, 24)[sex],
       col = diverge_hcl(2) [rep(1:length(levels(leuk.class)), each=2)])

#Another option could be:
legend (-1, 1, text.legend, 
        pch= c (21, 24) [ (sex) ], col = diverge_hcl(2)
        [ factor ( c ( rep ('ALL', 2), rep ('AML', 2) ) ) ] )

# EJERCICIO 3 -----------------------------------------------------------------

##3.1.

coplot( HK1 ~ PTEN | sex, panel = panel.smooth, xlab = "PTEN",
        ,ylab = "HK-1") 

##3.2.

library(lattice)
xyplot(HK1 ~ PTEN | sex, xlab = "PTEN", ylab = "HK-1", panel = function(x, y) 
  {
  panel.xyplot (x, y)
  panel.loess (x, y)
  } )

##3.3.

xyplot(HK1 ~ PTEN| sex, xlab = "PTEN", ylab = "HK-1", panel = function(x, y) 
  {
  panel.xyplot(x, y)
  panel.lmline(x, y)
  } )


##3.4.

install.packages("ggplot2") 
library(ggplot2)

dgg <- data.frame(PTEN = leuk.dat.m[2124, ],
                  HK = leuk.dat.m[1, ],
                  Sex = sex)

ggplot(dgg, aes(x = PTEN, y = HK)) + labs(y = "HK-1") + geom_point(shape = 
  1) + geom_smooth(method = lm, se = FALSE, col = "grey") + geom_smooth() +
  facet_wrap( ~ Sex)


#EJERCICIO 4 ------------------------------------------------------------------


p.v.t <- apply (leuk.dat.m, 1, 
               function(x) t.test(x ~ leuk.class)$p.value)
#We compute the p-value of each class of patient using a T-test
sorted.p <- sort(p.v.t) 
sorted.adj.p <- p.adjust(sorted.p, method = "fdr")
#FDR adjusted p-values. 
cut.05 <- sorted.p[length (which(sorted.adj.p < 0.05 )) ]
# We want to now which p.values have a FDR < 0.05. 
# Lenght of this condition will be the position of the last p-value 
# This is where we want to set our line
cut.15 <- sorted.p[length(which(sorted.adj.p<0.15))]
# We want to now which p.values have a FDR < 0.15. 
# Lenght of this condition will be the position of the last p-value 
# This is where we want to set our line

hist(sorted.p, breaks=50, freq=FALSE, ylim=c(0.3,14),
     xlab="p-value", main="P-values from t-test") 
# By putting freq = FALSE we made a density histogram.
box() # We frame the histogram.

abline( h=1, lty=2) #We made an horizontal line in y=1
abline(v=cut.05, col="red", lty=3) 
#We make a vertical line in x. This line delimite the p-values with FDR < 0.05
abline(v=cut.15, col="blue", lty=4)

legend.05=paste("FDR <= 0.05. P <=", round(cut.05, 4))
# We create the legend by joining the text. The p-values
# are rounded to 4 decimals.
legend.15=paste("FDR <= 0.15. P <=", round(cut.15, 4))

legend(0.4, 8, legend =c(legend.05, legend.15),
       lty = c(3,4), col = c("red", "blue"))  

# EJERCICIO 5 -----------------------------------------------------------------

p.w.t <-apply(leuk.dat.m, 1,
              function(x) wilcox.test (x ~ leuk.class)$p.value)

## non-parametric test like the Wilcoxon paired signed rank test
plot(p.w.t ~ p.v.t, cex = 0.6, xlab= "p-values from t-test", 
     ylab="p-values from Wilcoxon")
rug(p.v.t, side = 1)
rug(p.w.t, side = 2)
abline(v=cut.15, lty=4, col="blue") 











