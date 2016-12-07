##Ejercicio 1
leuk.dat <- read.table("leukemia.data.txt", row.names = 1)
leuk.dat.m <- data.matrix(leuk.dat) #Lo pasamos a matriz ya que estas son un conjunto de los mismos datos, como los que tenemos, en los data frame las columnas pueden contener distintas variables
leuk.class <- factor(scan("leukemia.class.txt", what = (""))) #Queremos esto para convertir el .txt en un factor
sex <- factor(c("Male", "Female")[rep(1:2, 19)])

##Ejercicio 2
#2.1
boxplot(leuk.dat.m[2124, ] ~ leuk.class, col= c("orange", "light blue"), 
        main = "a) Boxplot of PTEN by patient group.", 
        ylab = "Gene expression (mRNA)", xlab = "Patient groups")
#2.2
for.cex <- leuk.dat.m[2600, ] - min(leuk.dat.m[2600, ]) + 1
the.cex <- 2 * for.cex/max(for.cex)
#Es necesario descargar el paquete colorspace: install.packages("colorspace")
library("colorspace")
plot(leuk.dat.m[2124, ], leuk.dat.m[1, ], pch = c(2 ,1 ), 
     main = "b) HK-1 vs. PTEN; symbol size proportional to gene 2600", 
     ylab = "HK-1", xlab = "PTEN", col = diverge_hcl(2)[leuk.class],
     cex = the.cex, abline(lm(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ]), lty = 2))
lclass <- rep(levels(leuk.class), rep(2, 2))
lsex <- rep(levels(sex), 2)
text.legend <- paste(lclass, lsex, sep = ", ")
legend(-1.5, 0.5, text.legend, pch = c(1, 2), 
       col = c(rep(diverge_hcl(1), 2), rep(diverge_hcl(2, 2),2)))

##Ejercicio 3
#Figura 2
coplot(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ] | sex, ylab = "HK-1",
       xlab = "PTEN", panel = panel.smooth)
#Figura 3
x <- leuk.dat.m[2124, ]
y <- leuk.dat.m[1, ]
library(lattice)
xyplot(y ~ x | sex, ylab = "HK-1",xlab = "PTEN", panel = function(x, y) 
  {panel.xyplot(x, y)
  panel.loess(x, y)})
#Figura 4
xyplot(y ~ x | sex, ylab = "HK-1",xlab = "PTEN", panel = function(x, y) 
  {panel.xyplot(x, y)
  panel.lmline(x, y)})
#Figura 5
#Para correrlo hay que tener instalado ggplot2: install.packages("ggplot2")
dgg <- data.frame(PTEN = leuk.dat.m[2124, ], HK = leuk.dat.m[1, ], Sex = sex)
library(ggplot2)
ggplot(data = dgg, aes(x = PTEN, y = HK)) + geom_point(shape = 1) + facet_wrap( 
  ~Sex) + labs(y = "HK-1") + geom_smooth() + geom_smooth(method = lm, se=FALSE,
                                                         color="darkgray")

##Ejercicio 4
p.v.t <- apply(leuk.dat.m, 1, function(x) t.test(x ~ leuk.class)$p.value)
sorted.p <- sort(p.v.t)
sorted.adj.p <- p.adjust(sorted.p, method = "fdr")
cut.05 <- sorted.p[length(which(sorted.adj.p < 0.05))]
cut.15 <- sorted.p[length(which(sorted.adj.p < 0.15))]
#Para hacer el histrograma de densidades en la funcion hist, invocamos el argumento freq = FALSE
hist(p.v.t, breaks = 50, freq = FALSE, main = "P-values from t-test",
     xlab = "p-value", ylim = c(0.3, 14))
abline(h = 1, v = c(cut.05, cut.15), col = c("black", "red", "blue"), lty = 3,
       lwd = c(2, 1, 1))
axis(side = 2, at = 1)
box()
text.legend2 <- paste(c("FDR <= 0.05. P <=", "FDR <= 0.15. P <="), 
                      c(round(cut.05, 4), round(cut.15, 4)))
legend(0.4, 8, text.legend2, lty = 3, col = c("red", "blue"))

##Ejercicio 5
p.v.w <- apply(leuk.dat.m, 1, function(x) wilcox.test(x ~ leuk.class)$p.value)
plot(x = p.v.t, y = p.v.w, ylab = "p-values from Wilcoxon",
     xlab = "p-values from t-test", cex = 0.5, 
     abline(v = cut.15, col = "blue", lty = 4))
rug(p.v.t, side = 1)
rug(p.v.w, side = 2)