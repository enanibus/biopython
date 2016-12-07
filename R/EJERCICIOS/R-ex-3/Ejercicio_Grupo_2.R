###:
leuk.data <- data.matrix(read.table ("leukemia.data.txt", row.names = 1))      
leuk.class <- factor(scan("leukemia.class.txt", what= ""))
sex <- factor(rep(c("Male", "Female"),19))

###1:
table(sex)
table(sex, leuk.class)
xtabs(~ sex + leuk.class)
mytable <- as.data.frame(xtabs(~ sex + leuk.class))
print(mytable)

###2:
p.v.t <- apply(leuk.data, 1, 
               function(x) t.test(x ~ leuk.class)$p.value)
mean(leuk.data[p.v.t<0.01,3])
median(leuk.data[2, sex=="Male"])

###3:
leuk.data.t <- t(leuk.data)
dim(leuk.data.t)
leuk.data.t[1:5., 1:6]
#3.1:
aggregate(cbind(G1 = leuk.data.t[,1], G2214 =leuk.data.t[,2124], 
          G2600 = leuk.data.t[,2600]), list(type = leuk.class), median)
#3.2:
aggregate(cbind(G1 = leuk.data.t[,1], G2124 =leuk.data.t[,2124], 
          G2600 = leuk.data.t[,2600]), list(type = leuk.class, sex = sex),
          median)
#3.3:
all.median <- aggregate(leuk.data.t, list(type = leuk.class, sex = sex), median)
all.median [,1:10]
dim(all.median)
#3.4:
aggregate(cbind(G1 = leuk.data.t[,1], G2124 =leuk.data.t[,2124], 
          G2600 = leuk.data.t[,2600]), list(type = leuk.class, sex = sex),
          function(x) c(mean = mean(x), sd = sd(x)))
#3.5:
objeto1 <- by(cbind(G1 = leuk.data.t[,1], G2124 =leuk.data.t[,2124], 
              G2600 = leuk.data.t[,2600]), list(type = leuk.class, sex = sex), 
              summary)
objeto1
objeto2 <- aggregate(cbind(G1 = leuk.data.t[,1], G2124 =leuk.data.t[,2124], 
                     G2600 = leuk.data.t[,2600]), 
                     list(type = leuk.class, sex = sex), summary)
objeto2
class(objeto1)
class(objeto2)
  


              
