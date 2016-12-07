###Grupo 5
###Daniel Diaz Rodriguez, Ruben Gomez-Gordo, Alicia Roig Casado.
### 1. The data.

leuk.dat <- read.table("leukemia.data.txt", row.names = 1)
leuk.dat.m <- data.matrix(leuk.dat)
leuk.class <- factor(scan("leukemia.class.txt", what = ""))
sex <- factor(rep(c("M", "F"), length(leuk.class)/2))
#En los siguientes gráficos podríamos conseguir que las etiquetas fueran
#"Male" y/o "Female" sustituyendo en sex los valores "M" y "F".

### 2. The boxplot of PTEN and scatterplots with lots of info.
## 2.1 The boxplot.

par(mfrow = c(2, 1))

boxplot(leuk.dat.m[2124, ] ~ leuk.class, xlab = "Patient groups", 
        ylab = "Gene expression (mRNA)", col = c("orange", "lightblue"),
        main = "Boxplot of PTEN by patient group")

## 2.2 PTEN, HK-1, a third gene, patient status, and some sex
## (this is a lot of stuff!!).

for.cex <- leuk.dat.m[2600, ] - min(leuk.dat.m[2600, ]) + 1
the.cex <- 2 * for.cex/max(for.cex)

#Necesitamos evitar que haya números negativos o nulos en el argumento "cex".
#Por eso, realizamos todas estas operaciones, que garantizan un tamaño
#de punto adecuado (no demasiado grande, pero tampoco inexistente).

lclass <- rep(levels(leuk.class), rep(2, 2))
lsex <- rep(levels(sex), 2)
text.legend <- paste(lclass, lsex, sep = ", ")
library("colorspace")

plot(leuk.dat.m[2124, ], leuk.dat.m[1, ], xlab = "PTEN", ylab = "HK-1",
     main = " HK-1 vs. PTEN; symbol size proportional to gene 2600",
     pch = c(21, 24)[sex], cex = the.cex, col = diverge_hcl(2)[leuk.class])
legend(-1, 1, legend = text.legend, 
       col = diverge_hcl(2)[factor(lclass)], pch = c(21, 24)[factor(lsex)])
Hk1.PTEN <- lm(leuk.dat.m[1, ] ~ leuk.dat.m[2124, ])

#La función lm() devuelve los parámetro necesarios (pendiente y ordenada
# en el origen) para pintar la recta de regresión.

abline(Hk1.PTEN, lty = 3)

### 3.  Conditioning plots.

par(mfrow = c(1, 1))

#Al contrario que con los dos gráficos anteriores, a partir de ahora queremos
#que solo haya un gráfico por página. 

dgg <- data.frame(PTEN = leuk.dat.m[2124, ],
                  HK = leuk.dat.m[1, ],
                  Sex = sex)
coplot(HK ~ PTEN | sex, dgg,  panel = panel.smooth)

#El segundo valor de la función coplot() (dgg) corresponde al 
#argumento "data" que se explica en la ayuda de esta función.

library("lattice")
xyplot(HK ~ PTEN | sex, dgg, panel = function(x, y) {
  panel.xyplot(x, y)
  panel.loess(x, y)
  }
)
xyplot(HK ~ PTEN | sex, dgg, panel = function(x, y) {
  panel.xyplot(x, y)
  panel.lmline(x, y)
  }
)
library("ggplot2")
ggplot(aes(PTEN, HK), data = dgg) + facet_wrap( ~ Sex) + 
  labs(y = "HK-1", x = "PTEN") + geom_point(shape = 1) + 
  geom_smooth(method = "loess", se = FALSE)

#Tal y como se indica en los ejercicios, sólo se ha representado la línea
#curva del gráfico, no el resto de líneas.

### 4.  The histogram of p-values.

p.v.t <- apply(leuk.dat.m, 1,
                 function(x) t.test(x ~ leuk.class)$p.value)
sorted.adj.p <- p.adjust(sort(pvalues), method = "fdr")
hist(p.v.t, breaks = 50, freq = FALSE, main = "P-values from t-test",
     las = 1, xlab = "p-values")

#El argumento freq = FALSE permite representar densidades.

box()

#En los enunciados, las indicaciones sobre la línea roja y la azul están
#colocadas al revés respecto a su posición en el gráfico adjunto.

cut.05 <- sort(p.v.t)[length(sorted.adj.p[sorted.adj.p < 0.05])]
cut.015 <- sort(p.v.t)[length(sorted.adj.p[sorted.adj.p < 0.15])]
abline(v = cut.05, col = "red", lty = 4)
abline(v = cut.015, col = "blue", lty = 3)
abline(h = 1, col = "black", lty = 2)
axis(2, at = 1, las = 1)

#El argumento "las" permite cambiar la posición de los números de cada eje.

text.legend.2 <- c(paste("FDR <= 0.05. P <=", round(cut.05, 4)), 
                   paste("FDR <= 0.015. P <=", round(cut.015, 4)))
legend(0.2, 6, legend = text.legend.2, col = c("red", "blue"), lty = c(4, 3))

### 5.  The scatterplot of p-values.

p.v.t2 <- apply(leuk.dat.m, 1,
                 function(x) wilcox.test(x ~ leuk.class)$p.value)
plot(p.v.t2 ~ p.v.t, xlab = "p-values from the t-test",
     ylab = "p???values from Wilcoxon", cex = 0.6)
abline(v = 0.15, col = "blue", lty = 4)
rug(p.v.t2, side = 2)
rug(p.v.t)

#Invocamos dos veces a la función rug() para conseguir marcas en los dos ejes.
#El argumento "side" permite colocar una de estas series de marcas en el eje Y.