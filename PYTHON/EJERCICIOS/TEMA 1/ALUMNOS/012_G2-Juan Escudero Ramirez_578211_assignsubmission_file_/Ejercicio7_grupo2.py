###My_group: grupo2 (Juan Escudero, Juan Enríquez Traba, Pablo Villoslada)
MyDNA=input("Type DNA sequence and press enter")#Pedimos al usario que introduzca un secuencia de DNA que se guardará como la variable MyDNA.
A=(MyDNA.upper().count("A")/len(MyDNA))*100 #Calculamos el porcentaje de cada nucleótido dividiendo el número de cada nucleótido entre el número total de nucleótidos y                                            
T=(MyDNA.upper().count("T")/len(MyDNA))*100 #multiplicando por 100. Antes de contar el número de nucleotidos introducimos el método str.upper() 
C=(MyDNA.upper().count("C")/len(MyDNA))*100 #por si el usuario introduce la secuencia en minúsucula.
G=(MyDNA.upper().count("G")/len(MyDNA))*100
print("%A=",round(A,2)) #Hacemos que salga en pantalla lo calculado anteriormente y redondeando el resultado a dos difras decimales.
print("%T=",round(T,2))
print("%C=",round(C,2))
print("%G=",round(G,2))
REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC","HindIII":"AAGCTT", "NotI":"GCGGCCGC"} #Definimos nuestro diccionario de enzimas de restricción.
MyEnz=input("type the name of the enzyme and press enter") #Pedimos al usuario que introduzca el nombre de una enzima de restricción que se guardará como la variable MyEnz.
Cleavage=REnz[MyEnz] in MyDNA.upper() #Determinamos si la secuencia de MyEnz está presenta en MyDNA.upper(), por si el usuario introduce la secuencia en minúscula.
print("Cleavage by selected enzyme?",Cleavage) #Hacemos que salga en pantalla lo calculado anteriormente.
Position=MyDNA.upper().find(REnz[MyEnz])#Determinamos en que posición de MyDNA.upper() aparece el primer corte por la enzima de restrición, por si el usuario introduce la secuencia en minúscula.
print("First cleavage site?",Position) #Hacemos que salga en pantalla lo calculado anteriormente.           
