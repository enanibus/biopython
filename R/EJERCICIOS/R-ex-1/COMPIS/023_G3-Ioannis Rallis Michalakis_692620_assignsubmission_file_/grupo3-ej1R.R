# Grupo 1 (Ioannis Rallis, Patricia Palacios Ibanez, Maria Juliana Rodriguez) 
# Solucion propuesta a el conjunto de ejercicios "Exercises-R-scripts-data-structures-reading"
#
## Ejercicio 1 --> Scripts
#
# 1.1 Creating the script
x<- seq( from = 123, to = 297, by = 3.5) # 1.1.2
summary(x) # 1.1.3
# 1.2 Running the script
#
## 1.2.1 Si escribimos el script desde el editor de texto que aparece en la ventana superior izquierda de la pantalla,
##    basta con poner la barra de texto sobre la línea a editar y oprimir seguidamente las teclas ctrl + enter 
##    al mismo tiempo. De esta manera se ejecutará el script de interés.
##    También podemos colocar File --> Open File y accederemos al repositorio de información del equipo en el que 
##    estemos trabajando.
## 1.2.2 Si por el contario escribimos el script directamente en la consola, cada vez que demos enter para seguir con el 
##    con la siguiente línea de texto se ejecutará la línea anteriormente escrita.
##    No obstante si lo que deseamos es ejecutar un script de R que ya se encuentre listo, podemos hacerlo bajo el
##    comando (ejemplo 1):
source("Script1.R", echo = TRUE)
##    Donde Script1.R corresponde al nombre del fichero que contiene el script con su terminación .R, y echo = TRUE, 	
##    lee y ejecuta todas las líneas que se encuentren dentro del fichero.
## 1.2.3 Si lo hacemos desde el terminal y ya tenemos un fichero de texto con el script escrito, debemos llamar primero
##    al programa R y luego colocar la dirección en la que se encuentra el fichero, junto con el nombre del mismo y 
##    la terminación .RData
#
## Ejercicio 2 --> Some read.table operations
#
#2.1
another.data.set <- read.table ("AnotherDataSet.txt", header = TRUE) # Carga el fichero "AnotherDataSet.txt" en la variable another.dat.set
summary(another.data.set) # Muestra la tabla de forma ordenada, que contenía el fichero de texto cargado
d1<-replace(another.data.set,another.data.set=="23.4", NA) # Reemplaza en la tabla another.data.set, el valor 23.4 por NA 
write.table(d1, file = "d1.txt") # Escribe un nuevo fichero de texto con la tabla modificada d1, bajo el nombre "d1.txt"
#2.2
d2<- read.table ("d1.txt", header = TRUE) # Lee el fichero de texto d1 y lo almacena en la variable d2
d2[2,2]="" # Sustituye el valor que había en la posición [2,2] por un espacio vacío. Fila 2, columna 2.
d2[1,4]="" # Sustituye el valor que había en la posición [1,4] por un espacio vacío. Fila 1, columna 4.
write.table(d2, file = "d2.txt") # Escribe un nuevo fichero de texto con la tabla d2 modificada, bajo el nombre "d2.txt"
#2.3
datos<- read.table("AnotherDataSet.txt") # Lee la tabla "AnotherDataSet.txt" y la almacena en la variable datos.
write.table(datos, file= "d3.txt", col.names = FALSE) # Crea un fichero de texto sin la fila de encabezado
#2.4
d4<-rbind(data.frame(V1 = "@Hello, I created this file", V2 = "", V3 = "", V4 = ""), datos) # Coloca una fila introductoria, con un mensaje, en la tabla. Almacena en d4
d5<-rbind(d4, data.frame(V1 = "@Good bye", V2 = "", V3 = "", V4 = "")) # Coloca una fila final, con un mensaje, en la tabla. Almacena en d5
write.table(d5, file = "d4.txt") # Escribe un fichero de texto con la variable d5 que contiene los dos mensajes introducidos en la tabla
#
## Ejercicio 3--> Packages
#
# Descarga del paquete 'OncoSimulR' de bioconductor
##try http:// if https:// URLs are not supported
source("https://bioconductor.org/biocLite.R")
biocLite("OncoSimulR") # Fue necesario descargar tres paquetes adicionales 'mgcv', 'survival' y 'lme4'. Este último no estaba disponible para R version 3.3.2, se instaló desde cran
# El paquete 'car' lo descargué directamente de la sección de package, la ventana inferior derecha de Rstudio
## 3.1 Version 2.4.0 de OncoSimulR, se puede observar desde dos vias diferentes. La primera de ellas bajo la busqueda del 
##    paquete en la sección de packages en la ventana inferior derecha de Rstudio. La segunda, colocando el comando 
library (OncoSimulR) # Carga el paquete OncoSimulR
sessionInfo()
## 3.2 Version 2.1-3 de car, de la misma manera que el caso anterior, podemos observarlo por dos caminos. El primero bajo 	
##    la búsqueda del paquete, y/o despues de haber cargado la libreria recurrir al comando que nos da información sobre la sesión
library (car)
sessionInfo()
## 3.3 Se requiere como primera medida tener disponibles los paquetes mgcv, lme4, survival y maclapply, para su correctp funcionamiento.
#
## Ejercicio 4--> The help
#4.1 Devuelve character(0)
#4.2 Devuelve ayuda que incuye el uso, los argumentos y ejemplos de la funcion "scatrer3d"
#4.3 En el primer caso devuelve la funcion "scatter3d" y en el segundo la misma ayuda
#4.4 Si,apropos solo busca a los paquetes que estan cargados en la session
#4.5 Si,help.search busca a  los paquetes que estan instalados en el ordenador
#4.6 Si quieres encontrar una funcion que contiene la palabra "scatter" sabiendo que los adecuados paquetes estan cargados
#    es mejor usar "apropos()". Si, esto es posible si esta instalada en el ordenador pero no cargada en la session.
#4.7 Si, help.search busca a  los paquetes que estan instalados en el ordenador
#
## Ejercicio 5 --> Saving objects
#
x <- 95
y <- 97
save(x, file = "oneObject.RData")
# 5.2 Si utilizaramos save.image(), salvariamos ambos los objetos (x,y)
#
## Ejercicio 6 --> Vectors, data frames, etc.
#
hr <- c(87, 78, 86, 62, 69, 69, 68, 67, 75, 76) # Crea la variable hr y le asigna el conjunto de número que está dentor del ()
#6.1
age <-c(rep(11, 3), rep(63, 2), rep(40, 4), 47) # Crea repeticiones del número 11, 3 veces. Repite el 63, 2 veces. Repite el 40, 4 veces y por último pone 47.
#6.2
hr[age<45] # Extrae los hear rates de los individuos que tienen menos de 45 años
#6.3
hrY <- c(hr[age > 45]) # Extrae de hear rates de los individuos con mas de 45 años
hr2 <- c(Juan = hrY[1], Ana = hrY[2], Carmen = hrY[3]) # Asigna a Juan, Ana y Carmen los valores de hrY en la posición 1,2 y 3.
#6.4
hr2["Juan"] # Extrae el valor de hr de Juan
hr2["Ana"] # Extrae el valor de hr de Ana
#6.5
(Mat <- matrix(c(63, 63, 47, 62, 69, 76), nrow = 3, ncol = 2, byrow = FALSE,
               dimnames = list(c("Juan", "Ana", "Carmen"),c("age", "hr")))) # Crea una matriz para Ana, Juan y Carmen; usando como columnas su hry su edad, y sus nombres como las filas.
#6.6
Age <- c(63, 63, 47) 
HR <- c(62, 69, 76)
(Dframe <- data.frame(Age, HR, row.names = c("Juan", "Ana", "Carmen"))) # Agrega valores a la matriz
#6.7
name <- c("Juan", "Ana", "Carmen") 
(Dframe1 <- data.frame(name, Age, HR)) # Eso es imposible usando una matriz, se usa por tanto un data.frame
#6.8
(hrJuan <- Mat[1, 2]) # Extrae el valor de la fila 1, columna 2
#6.9
(ValJuan <- Mat[1,]) # Extrae los valores de la fila 1
#6.10
(hrAna <- Dframe[2, 2]) # Extrae los valores de la fila 2, la columna 2.
#6.11
(hrAna1 <- Dframe1[2, 3]) # Extrae los valores de la fila 2, la columna 3.
#6.12
(valAna <- Dframe1[2,]) # Extrae los valores de la fila 2.
#6.13
(anotherDframe <- Dframe1[Dframe1["Age"] > 60,])  # Extrae los valores de edad mayores a 60 
#6.14
(anotherDframe <- Dframe[Dframe["Age"] > 60,]) # Extrae los valores de edad mayores a 60
#6.15
(OtherMatrix <- subset(cbind(age, hr)[4:10,])) # Crea una matriz con age y hr, de nombre OtherMatrix
#6.16
sex <- c("M", "F")[c(1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1)] 
#Si, si quitamos el ultimo objeto del vector los nombres de las personas que conocemos coinciden con los sexos.
#6.17
sexCor <- c("M", "F")[c(1, 2, 1, 1, 2, 2, 1, 1, 2, 2)] # Crea un conjunto de datos donde signa a M el valor 1 y a F el valor 2. Lo guarda en la variable sexCor.
(Matrix <- subset(rbind(age, hr, sexCor)[, 4:10])) # Añade a Matrix sexCor
#6.18
Sex <- c(sexCor[4:5], sexCor[10]) # Extrae el genero de las personas de la posicion 4,5 y 10.
rbind(Age, HR, Sex) # Le asigna el nombre de cada Fila
#
## Ejercicio 7 --> Sort and order
sort(age) # Implementación de la función sort
order(age)# Implementación de la función order
sort(hr) # Implementación de la función sort
order(hr) # Implementación de la función order
# 7.1
OtherMatrix[order(OtherMatrix[,1]),]