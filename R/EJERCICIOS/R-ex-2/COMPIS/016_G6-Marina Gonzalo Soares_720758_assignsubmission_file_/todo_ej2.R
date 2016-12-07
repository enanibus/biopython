## My_Group: Group6 (Alejandro Asensio, Marina Gonzalo, Ma Jose Jimenez, 
## Jaime Quesada)

## 1. The Data
## Creation of a data frame that contains the data from "leukemia.data.txt".

leuk.dat <- read.table("leukemia.data.txt", skip = 2, row.names = 1)

## Conversion of this data frame into a matrix.
leuk.dat.m <- data.matrix(leuk.dat)

## Read of "leukemia.class.txt" and convert it into a factor.
leuk.class <- factor(scan(file = "leukemia.class.txt", what = ""))

## Creation of a factor called sex. It combines Male and Female alternating 
## (starting) with Male.

sex <- factor(rep(c("Male", "Female"), length.out = ncol(leuk.dat.m)))

## ============================================================================

## 2. The boxplot of PTEN and scatterplots with lots of info.
## 2.1 The boxplot

boxplot(leuk.dat.m[2124, ] ~ leuk.class, col = c("orange", "lightblue"), 
        xlab = "Patient groups", ylab = "Gene expression (mRNA)",
        main = "Boxplot of PTEN by patient group")

## 2.2 PTEN, HK-1, a third gene, patient status, and some sex

library(colorspace)
for.cex <- leuk.dat.m[2600, ] - min(leuk.dat.m[2600, ]) + 1
the.cex <- 2 * for.cex/max(for.cex)

plot(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ], ylab = "HK-1", xlab = "PTEN", 
     main = "HK-1 vs. PTEN; symbol size proportional to gene 2600",
     pch = c(21, 24)[sex], col = diverge_hcl(2)[leuk.class], cex = the.cex)

lclass <- rep(levels(leuk.class), rep(2, 2))
lsex <- rep(levels(sex), 2)
text.legend <- paste(lclass, lsex, sep = ", ")

legend(-1, 1, legend = text.legend, pch = rep(c(21, 24), 2), 
       y.intersp = 1.5, text.width = 0.4, 
       col = c(rep(diverge_hcl(2)[1], 2), rep(diverge_hcl(2)[2], 2)))
       
abline(lm(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ]), lty = 2)

## ============================================================================

## 3. Conditioning plots

library(lattice)
coplot(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ] | sex, xlab = "PTEN", 
       ylab = "HK-1", panel = panel.smooth)

xyplot(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ] | sex, panel = function(x, y) {
  panel.xyplot(x, y) 
  panel.loess(x, y)}, ylab = "HK-1", xlab = "PTEN")

xyplot(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ] | sex, panel = function(x, y) {
  panel.xyplot(x, y)
  panel.lmline(x, y)}, ylab = "HK-1", xlab = "PTEN")

library(ggplot2)

dgg <- data.frame("HK.1" = leuk.dat.m[1, ], "PTEN" = leuk.dat.m[2124, ], "Sex" = sex)
ggplot(dgg, aes(PTEN, HK.1)) + labs(y = "HK-1") + facet_wrap (~ Sex) +
  geom_point(shape = 1) + geom_smooth() + geom_smooth(method = lm, col = "darkgrey")

## ============================================================================

## 4. The histogram of p-values

p.v.t <- apply(leuk.dat.m, 1, function(x) t.test(x ~ leuk.class)$p.value)
hist(p.v.t, breaks = 50, freq = FALSE, xlab = "p-value", ylab = "Density", 
     main = "P-values from t-test")
sorted.p <- sort(p.v.t)
sorted.adj.p <- p.adjust(sorted.p, method = "fdr")
cut.05 <- sorted.adj.p[length(which(sorted.adj.p < 0.05))]
cut.015 <- sorted.adj.p[length(which(sorted.adj.p < 0.15))]
abline(h = 1, lty = 2)
abline(v = cut.015, lty = 4, col = "blue")
abline(v = cut.05, lty = 3, col = "red")
axis(2, at = 1)
box()
legend(0.4, 8, legend = c(paste("FDR <= 0.05. P <=", round(cut.05, 4)), 
                          paste("FDR <= 0.15. P <=", round(cut.015, 4))), 
       lty = c(3, 4), lwd = c(1.5, 1.5), col = c("red", "blue"), 
       y.intersp = 1.5, text.width = 0.45)
       
## ============================================================================

## 5. The scatterplot of p-values

p.v.w <- apply(leuk.dat.m, 1, function(x) wilcox.test(x ~ leuk.class)$p.value)
plot(p.v.w ~ p.v.t, cex = 0.4, xlab = "p-values from t-test", 
     ylab = "p-values from Wilcoxon") 
rug(p.v.w, side = 2)
rug(p.v.t, side = 1)
abline(v = cut.015, lty = 4, col = "blue")

