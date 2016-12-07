###1:
leuk.data <- data.matrix(read.table ("leukemia.data.txt", row.names = 1))      
leuk.class <- factor(scan("leukemia.class.txt", what= ""))
sex <- factor(rep(c("Male", "Female"),19))

###2:
#2.1:
boxplot (leuk.data[2124,] ~ leuk.class, col=c("orange","lightblue"),
         main = "a) Boxplot of PTEN by patient group.",
         xlab = "Patient groups",
         ylab = "Gene expression (mRNA)")
#2.2:
library(colorspace)
for.cex <- leuk.data[2600,] - min(leuk.data[2600,]) + 1
the.cex <- 2 * for.cex/max(for.cex)
plot (leuk.data[1,] ~ leuk.data[2124,], pch = c(21, 24)[sex],
      col = diverge_hcl(2)[leuk.class], cex = the.cex,
      main = "b) HK-1 vs. PTEN; symbol size proportional to gene 2600.",      
      xlab = "PTEN", ylab = "HK-1")
lclass <- rep(levels(leuk.class), c(2,2))
lsex <- rep(levels(sex), 2)
text.legend <- paste(lclass, lsex, sep = ", ")
legend (-1, 1, legend = text.legend,
        pch = rep(c(21, 24), 2), col = rep(diverge_hcl(2), c(2,2)))
lm1 <- lm(leuk.data[1,]~leuk.data[2124,])
abline(lm1, lty = 2)

###3:
#3.1:
coplot (leuk.data[1,] ~ leuk.data [2124,] | sex, panel = panel.smooth,
        xlab = "PTEN", ylab = "HK-1")
#3.2:
library(lattice)
xyplot (leuk.data[1,] ~ leuk.data [2124,] | sex, xlab = "PTEN", ylab = "HK-1",
        panel = function (x, y) {
          panel.xyplot(x, y)
          panel.loess(x, y)})
#3.3:
xyplot (leuk.data[1,] ~ leuk.data [2124,] | sex, xlab = "PTEN", ylab = "HK-1",
        panel = function (x, y) {
          panel.xyplot(x, y)
          panel.lmline(x, y)})

#3.4:
library (ggplot2)
dgg <- data.frame (PTEN = leuk.data[2124,], HK = leuk.data [1,], Sex = sex)
ggplot(data = dgg, aes(PTEN, HK)) + facet_wrap(~Sex) + 
  geom_point() + geom_smooth(method = "loess") + 
  geom_smooth(method = "lm", se = FALSE, colour = "grey") + labs(y = "HK-1")

###4:
p.v.t <- apply (leuk.data, 1,
                function(x) t.test(x ~ leuk.class)$p.value)
sorted.p <- sort(p.v.t)
sorted.adj.p <- p.adjust(sorted.p, method = "fdr")
cut.05 <- sorted.p [sum(sorted.adj.p < 0.05)]
cut.15 <- sorted.p [sum(sorted.adj.p < 0.15)]
hist(p.v.t, breaks = 50, freq = FALSE, main = "P-values from t-test",
     xlab = "p-value", ylim = c(0.3, 14))
box()
abline(h=1, lty = 2)
abline(v=cut.05, lty = 3, col = "red")
abline(v=cut.15, lty = 4, col = "blue")
text.legend.05 <- paste("FDR <= 0.05. P <=", round(cut.05, 4))
text.legend.15 <- paste("FDR <= 0.15. P <=", round(cut.15, 4))
legend(0.4, 8, c(text.legend.05, text.legend.15), lty = c(3, 4), 
       col = c ("red", "blue"))

###5:
p.v.w <- apply (leuk.data, 1,
                function(x) wilcox.test(x ~ leuk.class)$p.value)
plot(p.v.w ~ p.v.t, xlab = "p-values from t-test", 
     ylab = "p-values from Wilcoxon", cex = 0.5)
rug(p.v.t)
rug(p.v.w, side = 2)
abline(v=cut.15, lty = 4, col = "blue")
         
             


        




