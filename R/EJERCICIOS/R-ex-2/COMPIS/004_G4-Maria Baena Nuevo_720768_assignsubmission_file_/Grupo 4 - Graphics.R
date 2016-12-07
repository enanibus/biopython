###Group 4 (María Baena, Diego Calzada and Alfonso Cordero)
##1. THE DATA
leuk.dat<- read.table("leukemia.data.txt", row.names = 1)
leuk.dat.m<- data.matrix(leuk.dat)
leuk.class<- factor(scan("leukemia.class.txt", what = ""))
sex <-factor(rep(c("Male", "Female"),19))



##2. BOXPLOT
#Figure 1
#Representing both plots in one canvas
par(mfrow = c(2, 1))
boxplot(leuk.dat.m[2124, ] ~ leuk.class, 
        col = c("orange", "lightblue"), 
        main = "a) Boxplot of PTEN by patient group.",
        ylab = "Gene expression (mRNA)",
        xlab = "Patient groups")


#Scatterplot() is in the 'car' package
library("car")
library("colorspace")


#Symbol size
for.cex <- leuk.dat.m[2600, ] - min(leuk.dat.m[2600, ]) + 1 
the.cex <- 2 * for.cex/max(for.cex)
#Plot
plot(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ]
     , cex = the.cex
     , col = diverge_hcl(2)[leuk.class]
     , pch = c(21, 24)[sex]
     , xlab = "PTEN"
     , ylab = "HK-1"
     , main = "b) HKâˆ’1 vs. PTEN; symbol size proportional to gene 2600"
)


#Legend
lclass <- rep(levels(factor(leuk.class)), rep(2, 2)) 
lsex <- rep(levels(factor(sex)), 2)
text.legend <- paste(lclass, lsex, sep = ", ")


legend(-1, 1, 
       legend = text.legend, 
       pch = c(21, 24)[factor(lsex)],
       col = diverge_hcl(2)[factor(lclass)]
)


#Line
abline(lm(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ]), lty = 2)


#We stop representation of par(c(2, 1))
dev.off()


##3. CONDITIONING PLOTS
#Figure 2
coplot(leuk.dat.m["G1",]~leuk.dat.m["G2124",]|sex, 
       ylab = "HK-1",
       xlab = "PTEN", 
       panel = panel.smooth)


#Figure 3
library("lattice")
xyplot(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ] | sex
       , panel = function(x, y) {
         panel.xyplot(x, y)
         panel.loess(x, y)}
       , xlab = "PTEN"
       , ylab = "HK-1")


#Figure 4
xyplot(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ] | sex
       , panel = function(x, y) {
         panel.xyplot(x, y)
         panel.lmline(x, y)}
       , xlab = "PTEN"
       , ylab = "HK-1")





#Figure 5
library("ggplot2")
dgg <- data.frame(PTEN = leuk.dat.m[2124, ], 
                  HK = leuk.dat.m[1, ],
                  Sex = sex)

#With qplot
qplot(data = dgg, PTEN, HK, facets = ~ Sex, geom = c("point", "smooth")) +
  geom_smooth(method = lm, se = FALSE, col = "darkgrey")

#With ggplot
ggplot(data = dgg, aes(x = PTEN, y = HK)) +
  geom_point(shape = 1) + 
  facet_wrap( ~ Sex) + 
  labs(y = "HK-1") +
  geom_smooth() + 
  geom_smooth(method = lm, se = FALSE, col = "darkgrey")

#4. THE HISTOGRAM OF P-VALUES
p.v.t <- apply(leuk.dat.m, 1, 
               function(x) t.test(x ~ leuk.class)$"p.value")

sorted.p <- sort(p.v.t) 
sorted.adj.p <- p.adjust(sorted.p, method = "fdr")

hist(p.v.t
     , freq = FALSE
     , xlab = "p-value"
     , main = "P-values from t-test"
     , breaks = 50
     , ylim = c(0.3, 14))


abline(h = 1, lty = 2)
axis(2, at = 1)
box()

cut.05 <- sorted.p[sum(sorted.adj.p < 0.05)]
cut.15 <- sorted.p[sum(sorted.adj.p < 0.15)]

abline(v = cut.05, col = "red", lty = 3)
abline(v = cut.15, col = "blue", lty = 4)

legend(0.4, 6,
       legend = c(
         paste("FDR <= 0.05. P <=", round(cut.05, 4)),
         paste("FDR <= 0.15. P <= ", round(cut.15, 4))),
       col = c("red", "blue"),
       cex = 0.75,
       lty = c(3, 4))


##5. THE SCATTERPLOT OF P-VALUES
#We calculate p-values
p.v.t <- apply(leuk.dat.m, 1, function(x) t.test(x ~ leuk.class)$p.value)
p.v.w <- apply(leuk.dat.m, 1, function(x) wilcox.test(x ~ leuk.class)$p.value)


plot(p.v.w ~ p.v.t, 
     ylab = "p-values from Wilcoxon", 
     xlab = "p-values from t-test", 
     cex=0.5)


rug(p.v.t)
rug(p.v.w, side = 2)


sorted.p <- sort(p.v.t) 
sorted.adj.p <- p.adjust(sorted.p, method = "fdr")
cut.15 <- sorted.p[sum(sorted.adj.p < 0.15)]
abline(v = cut.15, col = "blue", lty = 4)
