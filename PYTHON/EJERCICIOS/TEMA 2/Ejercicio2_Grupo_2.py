###My_group: grupo2 (Juan Enriquez, Juan Escudero, Pablo Villoslada)
MyDNA=input("\n Type any DNA sequence and press enter:  ") #Pedimos al usuario que introduzca una secuencia de DNA que se guardará como la variable MyDNA.
Nucleotides=["A","T","G","C","AA","AT","AG","AC","TA","TT","TG","TC","GA","GT","GG","GC","CA","CT","CG","CC"] #Definimos una variable con todos los nucleótidos y los dinucleótidos posibles.
REnz={"EcoRI  ":"GAATTC", "BamHI  ":"GGATCC","HindIII":"AAGCTT", "NotI   ":"GCGGCCGC"} #Definimos nuestro diccionario de enzimas de restricción.
if len(MyDNA)!=MyDNA.upper().count("A")+MyDNA.upper().count("T")+MyDNA.upper().count("G")+MyDNA.upper().count("C")+MyDNA.upper().count("U"): #Establecemos un condicional para detectar si el usuario ha introducio una seucencia que no es ni DNA ni RNA.
    print("\n \t This program only accepts DNA sequences") #Hacemos que salga en pantalla que el programa solo acepta secuencias de DNA.
    exit() #Cerramos el programa
elif "U" or "u" in MyDNA: #Introducimos un condicional para detectar si la secuencia es RNA
    print(" Beware, this is a RNA sequence, it will be translated to DNA: ",end='  ') #Hacemos que salga en pantalla que es una secuencia de RNA y que será traducida a DNA.
    MyDNA_translated=MyDNA.upper().replace("U","T") #Definimos una variable con la secuencia de RNA traducida a DNA.
    print(MyDNA_translated) #Hacemos que salga en pantalla la secuencia de RNA traducida a DNA.
print("\n \t Length (nucleotides) =",len(MyDNA),end='\n \n')#Hacemos que salga en pantalla la longitud de la secuencia.
for n in Nucleotides: #Establecemos un bucle para cada uno de los nucleótidos y dinucleótidos presentes en la variable definida anteriormente.
    percentage=(MyDNA.upper().replace("U","T").count(n)/len(MyDNA))*100 #Calculamos el porcentaje de cada nucleótido y cada dinucleótido teniendo cuidado por si el usuario introduce una secuencia de RNA en vez de DNA o una secuencia en minúsculas.
    print("\t    %",n,"=",round(percentage,2)) #Hacemos que salga en pantalla el porcentaje de cada nucleótido y cada dinucleotido redondeado a dos decimales.
for e in REnz: #Establecemos un bucle para cada una de las enzimas presentes en el diccionario definido anteriormente. 
    Cut=REnz[e] in MyDNA.upper().replace("U","T") #Detectamos si cada una de las enzimas corta o no el DNA teniendo cuidado por si el usuario introduce una secuencia de RNA en vez de DNA o una secuencia en minúsculas. 
    print (' ')
    print("     Cleveage by",e,"? ",Cut) #Hacemos que salga en pantalla si cada una de las enzimas corta o no el DNA.
    if Cut==True: #Establecemos un condicional para continuar solo en el caso de que la enzima corte el DNA.
        Position=MyDNA.upper().replace("U","T").find(REnz[e]) 
        if Position==0:print(Position+1) #Dectectamos si la enzima corta en posición 0, ya que el bucle que viene a continuación se salta el 0, y hacemos que en ese caso salga en pantalla como la posición 1.
        Position=0 #Definimos la variable Position como 0 para poder establecer el bucle que viene a continuación.
        while Position!=-1: #Establecemos un bucle que se repetirá hasta que la variable Position sea -1, es decir, hasta que el DNA no tenga más cortes por la enzima.
            Position=MyDNA.upper().replace("U","T").find(REnz[e],Position+1) #Definimos la variable Position como el punto de corte de la enzima empezando a mirar desde el último punto de corte +1, para evitar que el bucle sea infinito.
            if Position!=-1:print(Position+1) #Hacemos que salga en pantalla la variable Position+1, ya que Python empieza a contar desde 0.

    
    

