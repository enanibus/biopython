## Grupo 5:
##Daniel Diaz Rodriguez, Ruben Gomez-Gordo, Alicia Roig Casado.
## Exercise 1

## 1. Scripts
## 1.1
rm(list = ls())
x <- seq(from = 123, to = 297, by = 3.5)
summary(x)

## 1.2
## 1.2.1 Seleccionando las lineas de codigo a ejecutar
# y, a continuacion, pulsando Ctrl+Intro
#Tambien se puede usar la opcion Run del editor.
## 1.2.2 Usando source("path/nombre del archivo") o cambiando
# el directorio con setwd("Path") a la carpeta que contiene el script
# y despues llamarlo con source("nombre del archivo")
## 1.2.3 Usando R --vanilla < path/nombre del archivo


## 2. Some read.table operations
##Lo primero es asegurarse de que R se ejecuta desde el path
# desde donde tenemos nuestro archivo.
setwd("C:/Path")
## 2.1
read.table("d1.txt", header = TRUE)
#Podríamos haber almacenado esta informacion en una variable
## 2.2
read.table("d2.txt", header = TRUE, sep = "\t")
## 2.3
read.table("d3.txt", sep = "\t", skip = 1)
## 2.4
read.table("d4.txt", header = TRUE, comment.char = "@")
#Si queremos que aparezcan los comentarios usamos lo siguiente:
read.table("d4.txt", fill = TRUE)


## 3. Packages
## 3.1 
sessionInfo("OncoSimulR") 
#Nos devuelve la version 2.4.0
#Podemos verlo tambien en:
#https://www.bioconductor.org/packages/release/bioc/html/OncoSimulR.html

## 3.2
sessionInfo("car")
#Nos devuelve la version 2.1-3
#Podemos verlo tambien en:
#https://cran.r-project.org/web/packages/car/index.html

## 3.3 Instalar el paquete y cargarlo:
library("OncoSimulR")
#Necesitamos además un objeto tipo "Poset".
#Este objeto es una matriz de dos columnas.

## 4. The help
## 4.1
apropos("scatter3d")
# Obtenemos: character(0)

## 4.2
help.search("scatter3d")
#En la ayuda de R nos salen los resultados de la busqueda
# de "sccatter3d"
#En este caso, no encuentra ningun objeto.
#Pese a todo, se indica que hay un match en el paquete "car".

## 4.3
library("car")
#Con apropos obtenemos lo siguiente: [1] "scatter3d"
#Con help.search obtenemos la ayuda de la funcion

## 4.4
#Si, porque la funcion "scatter3d" pertenece al paquete "car".
#Mientras este paquete no este cargado,
# no hay nada en el espacio explorado
# que contenga "scatter3d"

## 4.5
#apropos busca los objetos que contengan "scatter3d"
# (solo en las funciones), mientras que
# help.search no solo busca en las funciones, sino que
# busca paginas de ayuda que contengan "scatter3d"

## 4.6
#Apropos es mas util. Si, si se encuentra
# en un paquete no cargado en la sesion actual.

## 4.7
#Si, puedes hacerlo (pero tienen que estar descargados, no cargados):
# help.search("scatter", fields = "name")


## 5
## 5.1
x <- 97
y <- 95
save(x, file="oneOjbect.Rdata")

## 5.2
#Con save.image se guardan  x e y
#Esto es porque ambas estan presentes en el entorno global.


## 6. Vectors, data frames, etc
hr <- c(87, 78, 86, 62, 69, 69, 68, 67, 75, 76)

## 6.1
age <- rep(c(11, 63, 40, 47), c(3, 2, 4, 1))

## 6.2
tmp <- age < 45 #Logical operation
hr[tmp]

## 6.3
tmp2 <- hr[which(age > 45)]
hr2 <- c(Juan = tmp2[1], Ana = tmp2[2], Carmen = tmp2[3])

## 6.4
hr2[["Juan"]]
hr2[["Ana"]]

## 6.5
age2 <- age[age > 45] #Edades de los tres individuos.
matx <- cbind(HeartRate = hr2, Age = age2)

## 6.6
dataf <- data.frame(HeartRate = hr2, Age = age2)

## 6.7
dataf2 <- data.frame(Name = names(hr2), 
                HeartRate = hr2, Age = age2, row.names = NULL)
matx2 <- cbind(Name = names(hr2), HeartRate = hr2, Age = age2, row.names = NULL)
#matx2
#        Name     HeartRate Age 
#Juan   "Juan"   "62"      "63"
#Ana    "Ana"    "69"      "63"
#Carmen "Carmen" "76"      "47"

## 6.8
# Hay dos posibles formas:
matx[1, 1]
matx["Juan", "HeartRate"] 

## 6.9
matx[1, ]
matx["Juan", ] 

## 6.10
# Hay tres posibles formas:
dataf[2, 1] #2 numero fila, 1 numero columna
dataf["Ana", "HeartRate"] 
dataf$HeartRate[2]

## 6.11
# Hay dos posibles formas:
dataf2[2, 2]
dataf2[2, "HeartRate"]

## 6.12
dataf2[2, ]

## 6.13
tmp3 <- dataf2["Age"] > 60
dataf3 <- dataf2[tmp3, ]
dataf3

## 6.14
tmp4 <- dataf["Age"] > 60
dataf4 <- dataf[tmp4, ]
dataf4

## 6.15
matx3 <- cbind(HeartRate = hr, Age = age)
w <- which(age > 15)
matx4 <- matx3[w, ]

## 6.16
# Solo hay 10 casos
# El vector sex tiene 11 elementos
# Supongamos que descartamos el ultimo elemento de sex
sex <- c("M", "F")[c(1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1)]
AllM <- cbind(matx3, sex)
print(AllM[age == 47][3] == "F")
#Carmen es una mujer.
Only63 <- matrix(AllM[age == 63], nrow = 2)
print(Only63[which(Only63 == 62), ][3] == "M")
#Juan es un hombre.
print(Only63[which(Only63 == 69), ][3] == "F")
#Ana es una mujer.
# Solo en este caso tendria sentido afirmar
# que el vector sex informa del sexo de los miembros del estudio.

## 6.17
#A partir de aqui, eliminamos el ultimo elemento de sex
matx5 <- cbind(matx4, Sex = sex[w]) 
# w <- which(age > 15) (Exercise6.15)

## 6.18
Carmen <- AllM[age == 47][3]
Juan <- Only63[which(Only63 == 62), ][3]
Ana <- Only63[which(Only63 == 69), ][3]
sex2 <- c(Juan, Ana, Carmen)
dataf3 <- cbind(dataf, Sexo = sex2)

## 7.Sort and order
## 7.1
# PRIMERO ordenamos por HeartRate:
ordhr <- order(matx4[, 1]) 
matxhr <- matx4[ordhr, ] 
# SEGUNDO ordenamos por age
# (se mantiene el anterior orden al llamar a matx6):
ordage <- order(matxhr[, 2])
matxageandhr <- matxhr[ordage, ]
print(matxageandhr)