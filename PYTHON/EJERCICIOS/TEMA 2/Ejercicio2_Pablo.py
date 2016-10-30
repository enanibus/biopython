###My_group: grupo2 (Juan Enriquez, Juan Escudero, Pablo Villoslada)
MyDNA=input("type DNA sequence and press enter ").upper() #Pedimos al usuario que introduzca una secuencia de DNA que se guardará como la variable MyDNA y la ponemos en mayúscula por si el usuario la introduce en minúscula.
REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC","HindIII":"AAGCTT", "NotI":"GCGGCCGC"}#Definimos nuestro diccionario de enzimas de restricción
if "U" in MyDNA: #Introducimos un condicional para detectar si la secuencia es RNA.
    print("Beware, it is a RNA sequence, it will be translated to DNA") #Hacemos que salga en pantalla que es una secuencia de RNA y que será traducida a DNA.
    MyDNA=MyDNA.replace("U","T") #Modificamos la variable MyDNA si el usuario ha introducido una secuencia de RNA.
    print(MyDNA) #Hacemos que salga en pantalla la secuencia de RNA traducida a DNA.
for Base in MyDNA: 
    if not(Base in ["A","T","G","C"]): #Establecemos un condicional para detectar si el usuario ha introducido una seucencia que no es ni DNA ni RNA.
        print("It only accepts DNA sequences") #Hacemos que salga en pantalla que el programa solo acepta secuencias de DNA.
        exit() #Cerramos el programa
print("Nucleotides =",len(MyDNA))#Hacemos que salga en pantalla la longitud de la secuencia.
for Base in ["A","T","C","G"]: #Establecemos un bucle para cada uno de los nucleótidos.
    percentage=(MyDNA.count(Base)/len(MyDNA))*100 #Calculamos el porcentaje de cada nucleótido.
    print("%",Base,"=",round(percentage,2)) #Hacemos que salga en pantalla el porcentaje de cada nucleótido redondeado a dos decimales.
dinucl_freq={} #Definimos un diccionario.
for Base1 in ["A","T","C","G"]:
    for Base2 in ["A","T","C","G"]:
        dinucl_freq[Base1+Base2]=0 #Establecemos un bucle para llenar el diccionario con todos los dinucléoltidos y les asingamos a cada uno el valor 0 para usar el diccionario como contador.
for Position in list(range(len(MyDNA)-1)):
    subseq=MyDNA[Position:Position+2]
    dinucl_freq[subseq]=dinucl_freq[subseq]+1 #Establecemos un bucle para rellenar el diccionario con el número de dinucleótidos.
for dinucl in dinucl_freq: 
    percentage=(dinucl_freq[dinucl]/(len(MyDNA)-1))*100 #Calculamos el porcentaje de cada dinucleótido.
    print("%",dinucl,"=",round(percentage,2)) #Hacemos que salga en pantalla el porcentaje de cada dinucleótido redondeando a dos decimales.
for e in REnz:
    Cut=REnz[e] in MyDNA #Detectamos si cada una de las enzimas corta o no el DNA.
    print("Cleveage by",e,"? ",Cut) #Hacemos que salga en pantalla si cada una de las enzimas corta o no el DNA.
    Position=0
    while Cut: #Establecemos un bucle para detectar cada una de las posiciones en las que corta la enzima y hacemos que salga en pantalla. 
        Position=MyDNA.find(REnz[e],Position)
        print(Position+1)
        Position=Position+1
        if MyDNA.find(REnz[e],Position)<0: Cut=False
        
