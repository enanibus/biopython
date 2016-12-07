#1 Scripts
#1.1 Creating the script

rm(list=ls())
x <- seq (from=123, to=297, by=3.5)
print(summary(x))

#1.2 Running the script

#To execute the line of source code where the cursor currently resides you+
#press the Ctrl+Enter key or To run the entire document press the+
# Ctrl+Shift+Enter keys 
#read.table("nombredelarchivo.extension")
#Type the name of the script, including its file name extension, at+
# the command prompt



#2 Some readable operations

read.table("d1.txt", header= TRUE)
read.table("d2.txt", header= TRUE, sep= "\t")
read.table("d3.txt", sep= "\t")
read.table("d4.txt", skip= 1, nrows= 6, sep= "\t")



#3 Packages

#Mirando la columna version del paquete instalado (version 2.4.0)
#De nuevo, mirando la columna versión del paquete instalado (versión 2.1-3)
#Activar paquete, typear la funcion e introducir los argumentos como fp



#4 The help 

#4.1 character(0)
#4.2 obtenemos una página de ayuda para usar la función scatter3d
#4.3 Obtenemos "scatter3d" como output
#4.4 Porque scatter3d está dentro del paquete car
#4.5 apropos en los paquetes cargados, te buscas las funciones que tengan en+
# su nombre lo que tipees. help.search este o no instalado te lo busca.+
# Por tanto, apropos es mas facil para encontrar solo las funciones de +
# paquetes intalados(conoces) y help.search cuando estas perdido
#4.6 apropos; No, puedes saltarte funciones que usen scatter pero no+
# lo tienen en su nombre
#4.7 Sí, con la función fields="name", dentro de help.search; en este caso+
# habría que typear help.search("scatter", fields="name")

#5 Savingobjects
#5.1
x<-97
y<-95
save(x, file="oneObject.RData")

#5.2 save.image() is just a short-cut to "save my current environment", It is what+
# also happens with q("yes"). 



#6 Vectors,dataframes,etc

hr <- c(87, 78, 86, 62, 69, 69, 68, 67, 75, 76)
#6.1
age <- (c(rep( 11, 3), rep( 63, 2), rep( 40, 4), rep( 47, 1)))
#6.2
hr[age<45]
#6.3
hr2 <- c(Juan = 62, Ana= 69, Carmen = 76)
#6.4
hr2["Juan"]
hr2["Ana"]
#6.5 creamos una matriz(we use their names as a row names)
datos<-matrix(c(62,63,69,63,76,47), nrow=3, byrow=T)
colnames(datos)<-c("hr", "age")
rownames(datos)<-c("Juan", "Ana", "Carmen")
datos
#6.6 data frames
datos2<-data.frame(datos)
datos2
#6.7 yes I could (we can use their names as another column)
nombres<-c("Juan", "Ana", "Carmen")
datos3<-cbind(datos2,nombres)
datos3
#6.8
datos["Juan", "hr"]
#6.9
datos["Juan",]
#6.10
datos2["Ana","hr"]
#6.11
datos3["Ana","hr"]
#6.12
datos3["Ana",]
#6.13
datos3[which(datos3$age>60),]
#6.14
datos2[which(datos3$age>60),]
#6.15
matriz_total<-cbind(hr,age)
matriz_total[(age>15),]
#6.16 sí corresponde el sexo femenino con el nombre de Carmen pero+
# hay un dato de más 
#6.17
sex <- c("M", "F")[c(1, 2, 1, 1, 2, 2, 1, 1, 2, 2)]
matriz_total_2<-cbind(hr, age, sex)
matriz_total_2[(age>15),]



#7 El enunciado del ejercicio no correspondia con el ejemplo del ejercicio:
#Hemos ordenado la matriz de las dos formas: enunciado y ejemplo
#7.1
matriz_total_3<-cbind(hr,age=sort(age))
matriz_total_3[(age>15),]
#7.1.1
matriz_total_3<-cbind(hr=sort(hr),age=sort(age))
matriz_total_3[(age>15),]
