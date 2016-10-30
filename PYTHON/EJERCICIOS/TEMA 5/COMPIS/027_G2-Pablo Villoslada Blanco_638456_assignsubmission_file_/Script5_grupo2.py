###My_group: grupo2 (Juan Enríquez, Juan Escudero, Pablo Villoslada)

def GetAcNumber(Filename1): #Definimos una función para extraer el accession number.
    tmpFile1=open(Filename1,"r") #Abrimos el archivo cuyo nombre nos dará el usuario por línea de comando.
    Data1=tmpFile1.readline() #Sacamos la primera línea del archivo, que es la que contiene el accession number.
    tmpFile1.close() #Cerramos el archivo.
    tmpRE1=r"[NX]M.\d+.\d" #Definimos una expresión regular para el accession number.
    tmpRegex1=re.compile(tmpRE1) #Compilamos esa expresión regular.
    Result1=tmpRegex1.findall(Data1) #Buscamos la expresión regular. 
    return(Result1[0]) #Hacemos que la función nos devuelva el accesion number.

def GetDNA(Filename2): #Definimos una función para extraer la secuencia del DNA.
    tmpFile2=open(Filename2,"r") #Abrimos el archivo cuyo nombre nos dará el usuario por línea de comando.
    Sequence="" #Definmos un string que nos permitirá ir guandando cada una de las líneas que contiene el archivo. 
    for Line in tmpFile2: #Establecemos un bucle para sacar la secuencia de DNA.
        if not (">" in Line): Sequence=Sequence+Line.strip()
    tmpFile2.close() #Cerramos el archivo.
    return(Sequence) #Hacemos que la función nos retorne la secuencia de DNA.

def GetCode(): #Definimos una función para extaer el código genético.
    tmpFile3=open("GeneticCode_standard.csv","r") #Abrimos el archivo que contiene el código genético
    Code={} #Definimos un diccionario para ir guardando el codigo genético.
    tmpRE3=r"([ATGC]{3})\t(.)\t([A-Z][a-z]{2})" #Definimos una exprsión regular para el código genetico.
    tmpRegex3=re.compile(tmpRE3) #Compilamos esa expresión regular.
    for Line in tmpFile3: #Establecemos un bucle para ir sacando el codigo genético utilizando la expresión regular anterior.
        Data3=Line.strip()
        Result=tmpRegex3.search(Data3)
        Code[Result.groups()[0]]=Result.groups()[1:]
    tmpFile3.close() #Cerramos el archivo.
    return(Code) #Hacemos que la función nos devuelva el código genético.

def Getrc(Seq): #Definimos una función para sacar el reverso complementario.
    rcSequence=""
    Complement={"A":"T","C":"G","G":"C","T":"A"}
    for Base in Seq:
        rcSequence=Complement[Base]+rcSequence
    return(rcSequence) #Hacemos que la función nos retorne la secuencia del reverso complementario.

def Gettranslates(DNA,tmpCode,Outputname): #Definimos una función para escribir un archivo con los 6 translates.
    rcDNA=Getrc(DNA) #Sacamos el reverso complementario de nuestro DNA.
    MyFile=open(Outputname + '.txt',"w") #Abrimos un archivo cuyo nombre será el accesion number.
    CurrentStrand="+"
    for Strand in [DNA,rcDNA]: #Establecemos un bucle para que saque los translates tanto de nuestro DNA como del reverso complementario.
        if CurrentStrand=="+": MyFile.write("PLUS STRAND\n\n\n")
        else: MyFile.write("MINUS STRAND\n\n\n")
        for x in [0,1,2]: #Establecemos un bucle para que saque las 3 pautas de lectura.
            Translate1="" #Definimos dos strings para ir guardando los translates.
            Translate2=""
            for aa in list(range(x,len(Strand),3)): #Establecemos un bucle para ir sacando los codones y los aa a los que pertenece.
                Codons=Strand[aa:aa+3]
                if Codons in tmpCode.keys():
                    Aminoacides1=tmpCode[Codons][0]
                    Aminoacides2=tmpCode[Codons][1]
                Translate1=Translate1+Aminoacides1 #Guardamos los aa en las strings definidas anteriormente. 
                Translate2=Translate2+Aminoacides2
            MyFile.write("Frame"+str(x+1)+"\n\n"+Translate1+"\n"+Translate2+"\n\n\n\n") #Escribirmos los translates en el archivo.
        CurrentStrand="-" 
    MyFile.close() #Cerramos el archivo.

def Main(): #Definimos una función principal.
    MyAcNumber=GetAcNumber(sys.argv[1]) #Sacamos nuestro accesion number.
    MyDNA=GetDNA(sys.argv[1]) #Sacamos nuestra secuencia de DNA.
    MyCode=GetCode() #Sacamos nuesto código.
    Gettranslates(MyDNA,MyCode,MyAcNumber) #Escribimos un archivo con nuestros 6 translates.

if __name__=="__main__": #Establecemos un condicional para que esta parte del código solo se ejecute si el script es el principal.
    import re #importamos nuevas funciones que nos permitirán trabajar con expresiones regulares.
    import sys #Importamos nuevas funciones que permitirán que el usuario nos de los nombres de los archivos por línea de comando.
    Main() #Ejecutamos la función principal.

#Para funcionar el programa necesita que se aporte el archivo que contenga la secuencia por línea de comandos.





    
