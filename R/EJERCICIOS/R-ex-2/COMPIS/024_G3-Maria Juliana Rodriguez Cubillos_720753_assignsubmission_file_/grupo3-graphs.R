##1.THE DATA
leuk.dat <- read.table("~/leukemia.data.txt") # read data from text file  
leuk.dat. <- data.matrix(leuk.dat) #transforms data frame to matrix, else we cannot work further on
leuk.dat.m <- leuk.dat.[,-1]# deletes the 1st colums who has the row names
leuk.class <- factor( scan (file = "~/leukemia.class.txt", what=""))#scans txt files and transforms its content to factor
sex <-factor(c("Male", "Female")) 
##2.BOXPLOT AND SCATTERPLOT
#2.1.
x <- leuk.class; y <- leuk.dat.m[2124,]
boxplot(y ~ x , main = "a)Boxplot of PTEN by patient group",
  xlab = "Patient group", ylab="Gene expression (mRNA)", ylim = c(-1.5,2.1), 
  col=c("orange","lightblue"))  #Creates boxplot
#2.2
install.packages("colorspace")#Installs package
library(colorspace) #Runs it
x1 <- leuk.dat.m[2124, ]; y1 <- leuk.dat.m[1, ]
for.cex <- leuk.dat.m[2124, ] - min(leuk.dat.m[2124, ]) + 1
the.cex <- 2 * for.cex/max(for.cex) # the.cex determines the size of the dots of the plot
lclass <- rep(levels(leuk.class), rep(2, 2))
lsex <- rep(levels(sex),2) 
text.legend <- paste(lclass, lsex, sep = ", ") #text.legend used to create the legend of the plot
plot1 <- plot(x1, y1 , main = "b)HK-1 vs. PTEN; symbol size proportional to gene 2600",
xlab = "PTEN", ylab = "HK-1", xlim = c(-1.7,2.5), ylim = c(-1.7,1.5), col = diverge_hcl(2)[leuk.class],
pch = c(21, 24)[sex], cex = the.cex) #Creates the appropriate plot 
abline(lm(y1~x1), lwd = 1, col= "green")# This is our regression line
legend(-1.5,1, legend=text.legend, col = diverge_hcl(2)[leuk.class], pch = c(24, 21)[sex])#creates the legend of the graphic
#I didn't know how to put the colours of the dots correctly ( ALL->blue, AML->red)
##3.CONDITIONING PLOTS
#LATTICE
library("lattice")# Runs package
xyplot(y1~x1 | sex, xlab = "PTEN", ylab = "HK-1",
       panel = function(x, y){
       panel.xyplot(x, y)
       fit <- lm(y~x)   
       panel.abline(fit)}) #Creates conditioning plot, adds its regression line
xyplot(y1~x1 | sex, xlab = "PTEN", ylab = "HK-1",
       panel = function(x, y){
         panel.xyplot(x, y)
         panel.loess(x,y)})#Creates conditioning plot, adds smoothened line
##GGPLOT
install.packages("ggplot2")
library("ggplot2")
#Creates dataframe which ncludes genes PTEN, HK and the sexes of individuals
dgg<- data.frame(PTEN = leuk.dat.m[2124, ],HK = leuk.dat.m[1, ], Sex = sex)
#Creats a qplot from datafra dgg
qplot(PTEN, HK, data = dgg ,geom = c("point","smooth")) + facet_wrap(~Sex) + geom_smooth(method = "lm")
##4.HISTOGRAM OF P-VALUES
p.v.t <- apply(leuk.dat.m, 1, function(x) t.test(x ~ leuk.class)$p.value)#Calculates  p-values of t-test for all genes comparing the 2 classes
hist(p.v.t, breaks = 50,freq =FALSE, ylim = c(0.3,14),las = 1)# Creates histogram of density
box()
p.v.t.sorted <- sort(p.v.t) #Sorts all p-values
p.v.t.sorted.adj <- p.adjust(p.v.t.sorted, method = "fdr") #Adjusts p-values with the FDR method
pval.05 <- p.v.t.sorted.adj < 0.05  #Indicates which  adjusted p-values are less than 0,05
pval.15 <-p.v.t.sorted.adj < 0.15  #Indicates which  adjusted p-values are less than 0,15
cut.05 <- p.v.t.sorted[695]  # Finds the p-values whose FDR is less than 0,05
cut.15 <- p.v.t.sorted[1117] # Finds the p-values whose FDR is less than 0,15
abline(h = 1, lwd=1, lty =2)
axis(2, at = 1, las = 1)
abline(v=cut.05, lwd = 1, col = "red", lty = 2)#Creates FDR = 0,05 cutoff
abline(v=cut.15, lwd = 1, col = "blue", lty = 2)#Creates FDR = 0,15 cutoff
LEGEND <- paste("FDR <= 0.05. P <=", round(cut.05, 4))
LEGEND1 <- paste("FDR <= 0.05. P <=", round(cut.05, 4))
legend(0.3,10 , legend = LEGEND, col ="red", lty = 2)
legend(0.3,14 ,legend = LEGEND1, col="blue", lty = 2)
##5 SCATTERPLOT OF P-VALUES
#Calculates  p-values of Wilcoxon's test for all genes comparing the 2 classes
p.v.w <- apply(leuk.dat.m, 1, function(x) wilcox.test(x ~ leuk.class)$p.value)
#Creats plot of  (p-values from t-test ~ p-values from Wilcoxon's test)
plot(p.v.w ~ p.v.t, xlab = "p-values from t-test",
     ylab = "p-values from Wilcoxon", pch = 1, cex = 0.7)
rug(p.v.t)
rug(p.v.w, side = 2)
abline(v=cut.15, lwd = 1, col = "blue", lty = 2)
