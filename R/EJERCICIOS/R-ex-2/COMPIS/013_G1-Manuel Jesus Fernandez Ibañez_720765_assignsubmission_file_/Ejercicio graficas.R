#EJERCICIO 1

read.table("leukemia.data.txt", header= TRUE)
leuk.dat<-read.table("leukemia.data.txt", header= FALSE)
leuk.dat
leuk.dat.m<-data.matrix(leuk.dat)
leuk.dat.m
scan("leukemia.class.txt", what = "")
leuk.class<-factor(c(scan("leukemia.class.txt", what = "")))
sex<-factor(rep(c("Male", "Female"), times=19))
sex

#EJERCICIO 2
##Ejercicio2.1

boxplot(leuk.dat.m[2124,2:39]~leuk.class,
        ylab="Gene expression(mRNA)", col = c("orange", "lightblue"), 
        main="a) Boxplot of PTEN by patient group")

##Ejercicio2.2
plot(leuk.dat.m[2124,2:39],leuk.dat.m[1,2:39], xlab="HK-1", ylab= "PTEN",
     main="b) HK???1 vs. PTEN; symbol size proportional to gene 2600", 
     pch = c(21, 24)[sex], 
     col = c("blue", "purple")[leuk.class])
lm1<-lm(leuk.dat.m[1,2:39]~leuk.dat.m[2124,2:39])
abline(lm1, lty=2)
lclass <- rep(levels(leuk.class), rep(2, 2))
lsex <- rep(levels(sex), 2) 
text.legend <- paste(lclass, lsex, sep = ", ")
legend(-1, 1, c(text.legend),pch = c(24, 21)[sex],col = c("blue","blue",
                                                          "purple","purple"))

##Ejercicio3

##3.1
coplot(leuk.dat.m[1, 2:39] ~ leuk.dat.m[2124, 2:39]|sex, xlab="PTEN",
       ylab="HK-1", main="Given:sex", panel=panel.smooth)

##3.2
x <- leuk.dat.m[2124, 2:39]
y <- leuk.dat.m[1, 2:39]

library(lattice)
xyplot(leuk.dat.m[1, 2:39] ~ leuk.dat.m[2124, 2:39]|sex, xlab="PTEN",
       ylab="HK-1", main="Given:sex", panel=function(x,y) {panel.xyplot(x,y)
         panel.loess(x,y)})

##3.3
xyplot(leuk.dat.m[1, 2:39] ~ leuk.dat.m[2124, 2:39]|sex, xlab="PTEN",
       ylab="HK-1", main="Given:sex", panel=function(x,y) {panel.xyplot(x,y)
         panel.lmline(x,y)})


##3.4
library(ggplot2)
dgg <- data.frame(PTEN= leuk.dat.m[2124, 2:39], HK=leuk.dat.m[1, 2:39],
                  Sex= sex)
ggplot(data=dgg, aes(PTEN,HK))+ facet_wrap(~Sex) + geom_point() + 
  geom_smooth(method="loess") + geom_smooth(se= FALSE, method= "lm", 
                                            colour="grey") + labs(y="HK-1")




#Ejercicio 4
randomdata <- matrix(rnorm(38 * 1000), ncol = 38)
class <- factor(c(rep("ALL",27 ), rep("AML", 11))) 
pvalues <- apply(randomdata, 1, function(x) t.test(x ~ leuk.class)$p.value)
hist(pvalues, main="P???values from t???test", ylab="Density")

tmp <- t.test(randomdata[1, ] ~leuk.class ) 
tmp




##Ejercicio 5
#5.1
tmp<- wilcox.test(x="vectornumericodelquequeremoshacereltest",...)
#5.2
plot(x="pvalorestestdelatdemanolito",y="pvalorestestwilcox",
                         type = "n", axes = FALSE, ann = FALSE)

#5.3
#aqui no entiendo muy bien lo que hay que hacer en la primera parte de la pregunta
#en la funcion rug podemos elegir el side donde sera proteado,
#siendo este el 3º argumento 1 (abajo)3(arriba)
#4.4
#rug nos es util porque nos permite ver como es la distribucion de valores
#del test, ya sea continua o discreta.
#4.5
points(cex=0.9)

