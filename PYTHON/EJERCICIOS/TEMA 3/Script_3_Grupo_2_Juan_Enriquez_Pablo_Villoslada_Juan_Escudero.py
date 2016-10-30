###My_group: grupo 2 (Juan Enríquez, Juan Escudero, Pablo Villoslada)
HRAS=open("Human_HRAS.fasta.txt","r") #Abrimos el archivo con la secuencia de HRAS.
Sequence=[] #Definimos una lista que nos permitirá ir añadiendo las distintas líneas que contiene el archivo para luego juntarlas.
for Line in HRAS: #Establecemos un bucle para sacar las distintas líneas que contiene el archivo.
    Data=Line.strip()
    if not(">" in Data): Sequence=Sequence+[Data]
HRAS.close() #Cerramos el archivo.
Sequence="".join(Sequence) #Unimos la lista para obtener la secuencia de HRAS.
GeneticCode=open("GeneticCode_standard.csv","r") #Abrimos el archivo con el codigo genético.
Code1={} #Definimos dos diccionarios que nos permtirán guardar el código genético, uno para el código de tres letras y otro para el de una.
Code2={}
for Line in GeneticCode: #Establecemos un bucle para sacar el codigo genético.
    Data=Line.strip().split("\t")
    Code1[Data[0]]=Data[2]
    Code2[Data[0]]=Data[1]
GeneticCode.close() #Cerramos el archivo.
for x in [0,1,2]: #Establecemos un bucle para sacar los 3 primeros translates.
    Translate1_1=[] #Definimos dos listas que nos permitirán sacar los translates, uno para el código de tres letras y otro para el de una.
    Translate1_2=[]
    for aa in list(range(x,len(Sequence)-1)): #Establecemos un bucle para ir sacando los disintos codones.
        Codons=Sequence[aa:aa+3]
        if Codons in Code1.keys():
            Aminoacides1=Code1[Codons] #Buscamos en el diccionario los codones y los aminoácidos a los que pertenecen.
            Aminoacides2=Code2[Codons]
        Translate1_1=Translate1_1+[Aminoacides1] #Añadimos los aminoácidos a los tranlates.
        Translate1_2=Translate1_2+[Aminoacides2]
    Translates=open("Translates.txt","a") #Abrimos un archivo para ir grabando los translates.
    Translate1_1="".join(Translate1_1) #Unimoslas listas para obtener los tranlates.
    Translate1_2="".join(Translate1_2)    
    Translates.write("Translate")
    Translates.write(str(x+1))
    Translates.write("---\n\n")
    Translates.write(Translate1_1)
    Translates.write("\n\n")
    Translates.write(Translate1_2)
    Translates.write("\n\n\n")
    Translates.close() #Cerramos el archivo.
Original_symbols="ATGC" #Calculamos el reverso complementario para sacar los otros 3 translates.
Secret_code="TACG"
Trans_table=str.maketrans(Original_symbols,Secret_code)
Sequence=Sequence.translate(Trans_table)
Sequence=Sequence[::-1]
for x in [0,1,2]: #Procedemos de la misma forma que en los 3 primeros translates.
    Translate1_1=[]
    Translate1_2=[]
    for aa in list(range(x,len(Sequence)-1)):
        Codons=Sequence[aa:aa+3]
        if Codons in Code1.keys():
            Aminoacides1=Code1[Codons]
            Aminoacides2=Code2[Codons]
        Translate1_1=Translate1_1+[Aminoacides1]
        Translate1_2=Translate1_2+[Aminoacides2]
        Translates=open("Translates.txt","a")
    Translate1_1="".join(Translate1_1)
    Translate1_2="".join(Translate1_2)    
    Translates.write("Translate")
    Translates.write(str(x+4))
    Translates.write("---\n\n")
    Translates.write(Translate1_1)
    Translates.write("\n\n")
    Translates.write(Translate1_2)
    Translates.write("\n\n\n")
    Translates.close()
print("End of the program, you can see de translates in the file Translates.txt") #Informamos al usuario de que el programa ha terminado de ejecutarse y de que puede leer los translates en el archivo creado.
input("Press enter if you want to exit") #Pedimos al usuario que presione enter para salir del programa.
exit() #Salimos del programa.



    
    
