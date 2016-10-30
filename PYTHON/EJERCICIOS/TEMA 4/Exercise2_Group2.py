###My_group: grupo2 (Juan Enríquez, Juan Escudero, Pablo Villoslada)
def GetDNA(Filename1): #Definimos una función para extraer la secuencia del DNA.
    tmpFile1=open(Filename1,"r") #Abrimos el archivo cuyo nombre nos dará el usuario por línea de comando.
    Sequence="" #Definmos un string que nos permitirá ir guandando cada una de las líneas que contiene el archivo. 
    for Line in tmpFile1: #Establecemos un bucle para sacar la secuencia de DNA.
        if not (">" in Line): Sequence=Sequence+Line.strip()
    tmpFile1.close() #Cerramos el archivo.
    return(Sequence) #Hacemos que la función nos retorne la secuencia de DNA.
def GetCode(Filename2): #Definimos una función para extraer el código.
    tmpFile2=open(Filename2,"r") #Abrimos el archivo cuyo nombre nos dará el usuario por línea de comando.
    Code={} #Definimos un diccionario que nos permitirá ir guardando el código.
    for Line in tmpFile2:
        Data=Line.strip().split("\t")
        Code[Data[0]]=Data[1:]
    tmpFile2.close() #Cerramos el archivo.
    return(Code) #Hacemos que la función nos retorne la secuencia de DNA.
def Getrc(Seq): #Definimos una función para sacar el reverso complementario.
    rcSequence=""
    Complement={"A":"T","C":"G","G":"C","T":"A"}
    for Base in Seq:
        rcSequence=Complement[Base]+rcSequence
    return(rcSequence) #Hacemos que la función nos retorne la secuencia del reverso complementario.
def Gettranslates(DNA,tmpCode,Outputname): #Definimos una función para escribir un archivo con los 6 translates.
    rcDNA=Getrc(DNA) #Sacamos el reverso complementario de nuestro DNA.
    MyFile=open(Outputname,"w") #Abrimos un archivo cuyo nombre nos dará el usuario por línea de comando.
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
    MyDNA=GetDNA(sys.argv[1]) #Sacamos nuestra secuencia de DNA.
    MyCode=GetCode(sys.argv[2]) #Sacamos nuesto código.
    Gettranslates(MyDNA,MyCode,sys.argv[3]) #Escribimos un archivo con nuestros 6 translates.
if __name__=="__main__": #Establecemos un condicional para que esta parte del código solo se ejecute si el script es el principal.
    import sys #Importamos nuevas funciones que permitirán que el usuario nos de los nombres de los archivos por línea de comando.
    Main() #Ejecutamos la función principal.

    
    
    
        
        
        

