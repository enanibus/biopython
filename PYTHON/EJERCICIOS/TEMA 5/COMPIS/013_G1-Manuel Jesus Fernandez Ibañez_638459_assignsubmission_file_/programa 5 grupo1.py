
def GetAnaccesionnumber(Filename1): 
    File1=open(Filename1,"r") 
    Data1=File1.readline() #obtenemos la primera línea del archivo, que es la que contiene el accession number.
    File1.close() 
    RE1=r"[NX]M.\d+.\d" #Definimos una expresión regular para el accession number.
    Regex1=re.compile(RE1) #Compilamos e
    Result1=Regex1.findall(Data1) #Buscamos la expresión regular. 
    return(Result1[0]) #Hacemos que la función nos devuelva el accesion number.

def GetDNA(Filename2): # para extraer la secuencia del DNA.
    File2=open(Filename2,"r") 
    Sequence="" # 
    for Line in tmpFile2: 
        if not (">" in Line): Sequence=Sequence+Line.strip()
    File2.close() #Cerramos el archivo.
    return(Sequence) #Hacemos que la función nos retorne la secuencia de DNA.

def GetCode(): #Definimos una función para extaer el código genético.
    File3=open("GeneticCode_standard.csv","r") 
    Code={} 
    RE3=r"([ATGC]{3})\t(.)\t([A-Z][a-z]{2})" #Definimos una exprsión regular para el código genetico.
    Regex3=re.compile(RE3) #Compilamos esa expresión regular.
    for Line in tmpFile3: 
        Data3=Line.strip()
        Result=Regex3.search(Data3)
        Code[Result.groups()[0]]=Result.groups()[1:]
    File3.close() 
    return(Code) #Hacemos que la función nos devuelva el código genético.

def Getrc(Seq): 
    rcSequence=""
    Complement={"A":"T","C":"G","G":"C","T":"A"}
    for Base in Seq:
        rcSequence=Complement[Base]+rcSequence
    return(rcSequence) 

def Gettranslates(DNA,Code,Outputname): #Definimos una función para escribir un archivo con los 6 translates.
    rcDNA=Getrc(DNA) 
    MyFile=open(Outputname+".txt","w") #Abrimos un archivo cuyo nombre será el accesion number.
    CurrentStrand="+"
    for Strand in [DNA,rcDNA]: #Establecemos un bucle para que saque los translates tanto de nuestro DNA como del reverso complementario.
        if CurrentStrand=="+": MyFile.write("PLUS STRAND\n\n\n")
        else: MyFile.write("MINUS STRAND\n\n\n")
        for x in [0,1,2]: 
            Translate1="" 
            Translate2=""
            for aa in list(range(x,len(Strand),3)): #Establecemos un bucle para ir sacando los codones y los aa a los que pertenece.
                Codons=Strand[aa:aa+3]
                if Codons in Code.keys():
                    Aminoacides1=Code[Codons][0]
                    Aminoacides2=Code[Codons][1]
                Translate1=Translate1+Aminoacides1 #Guardamos los aa en las strings definidas anteriormente. 
                Translate2=Translate2+Aminoacides2
            MyFile.write("Frame"+str(x+1)+"\n\n"+Translate1+"\n"+Translate2+"\n\n\n\n") #Escribirmos los translates en el archivo.
        CurrentStrand="-" 
    MyFile.close() #Cerramos el archivo.

def Main(): #Definimos una función principal.
    MyAcNumber=GetAnaccesionnumber(sys.argv[1]) #Sacar el accesion number.
    MyDNA=GetDNA(sys.argv[1]) #Sacamos la secuencia de DNA.
    MyCode=GetCode() 
    Gettranslates(MyDNA,MyCode,MyAcNumber) 

if __name__=="__main__": #Establecemos un condicional para que esta parte del código solo se ejecute si el script es el principal.
    import re 
    import sys 
    Main()





    
