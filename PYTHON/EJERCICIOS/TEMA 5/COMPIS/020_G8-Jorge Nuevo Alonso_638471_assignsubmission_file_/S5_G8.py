##Group 8: Álvaro Alfayate, Andrea de la Fuente, Carla Guillén y Jorge Nuevo.

def ReadFasta(FileName): ##Definimos una función que lea el archivo FASTA elegidoy extraiga la información requerida
    MyFile=open(FileName,'r')
    ReadSeq='' #Una variable vacia que va a almacenar el Fasta leído
    for Line in MyFile: ##Unimos todas las líneas del fasta.
        if '>' in Line:  ##Si es la primera línea definimos esta condición
            #No hacemos un strip para poder separar la primera línea de la secuencia por un \n
            ReadSeq=ReadSeq+Line #Añadimos la primera línea con el \n
        else:
            Line=Line.strip().upper() #Con la secuencia si hacemos strip, para unir toda la secuencia junta.
            ReadSeq=ReadSeq+Line
        MySeq_RE=r'([NX]M_\d+\.\d).+\n([AGCT]+)' #Definimos la expresión regular que nos extrae por un lado el accession number y por otro la secuencia.
        MySeq_Comp=re.compile(MySeq_RE)
    SeqInfo=MySeq_Comp.search(ReadSeq).groups() #Buscamos nuestra expresión regular en la secuencia leída y sacamos los grupos.
    return (SeqInfo) ##SeqInfo es una lista donde el primer elemento es el accesion number y el segundo la secuencia de DNA
    MyFile.close()
    
def CreateDictionary(DicFile): ##Definimos una función que crea diccionarios a partir del archivo que le pasemos.
    MyFile=open(DicFile,'r')
    MyDic_RE=r'([ATGC]{3})\t([^BJUXZ])\t([A-Z][a-z]{2})'  ##Definimos una expresión variable que saca por un lado el codon, por otro los aminoácidos (en ambos códigos)
    MyDic_Comp=re.compile(MyDic_RE)
    Data2=''
    GENCODE={}
    for Line in MyFile: ##Recorremos todas las líneas del archivo y las unimos en Data 2
        Data2=Data2+Line.strip()
    MyRes2=MyDic_Comp.findall(Data2) ##Busca en Data2 todos los elementos que cumplen la secuencia consenso y los almacena en MyRes2 como una lista de listas (2D)
    x=0
    for n in range(0,len(MyRes2)):##Durante la longitud de la lista MyRes2 va a ejecutar este bloque de código.
        GENCODE[MyRes2[x][0]]=MyRes2[x][1:] #Forma un diccionario recorriendo todas las líneas del archivo (que corresponden a la primera dimensión de la lista)
        x+=1 #Avanzamos una posición en la primera dimensión --> A la siguiente línea del archivo de código genético
    return (GENCODE)
    MyFile.close()

def ComplementaryGenerator(SeqName): #Creamos una función que nos devuelve la hebra complementaria de la secuencia de la primera función
    SeqReverse=SeqName[::-1] ##Se invierte la secuencia, de forma que se va a leer la secuencia + en dirección 3'-5'
    SeqComplementary=''  ##Se genera la variable donde se almacenará la secuencia complementaria
    GenCode={'A':'T','C':'G','G':'C','T':'A'} ##Diccionario con los nucleótidos complementarios
    for Nucleotide in SeqReverse: ##Vamos itinerando por cada nucleótido de la secuencia
        ##Se van añadiendo los nucleótidos complementarios 1 a 1 en nuestra variable, generando la secuencia complementaria en dirección 5'-3'.
        SeqComplementary=SeqComplementary+GenCode[Nucleotide]
    return(SeqComplementary) ##Ahora SeqComplementary será la variable resultado de correr esta función.


def TranslateDNA(DNASeq,COMPSEQ,DicFile,ExportName):
    MyFile=open(ExportName+'.txt','w')
    Counter='+' #Declaramos Seq como +. Es un contador de en qué secuencia estamos
    for Seq in (DNASeq,COMPSEQ):
        if Counter=='+': ##Al empezar estamos en la secuencia +
            print('\t\t\t\t\t\t\t\t\t\tPLUS STRAND\n')
            MyFile.write('\t\t\t\t\t\t\t\t\t\tPLUS STRAND\n')
        if Counter=='-': #Para que escriba Minus Strand en este caso
            MyFile.write('\n\t\t\t\t\t\t\t\t\t\tMINUS STRAND\n\n')
            print('\n\t\t\t\t\t\t\t\t\t\tMINUS STRAND\n\n')
        for CodingFrame in range(0,3): #Bucle para leer en las tres pautas de lectura
            ProtSeq=''
            MyFile.write('\n\t\t\t\t\t\t\t\t\t\t Frame '+str(CodingFrame+1)+'\n\n')#Escribe el Frame en el que está (Sumando +1 pues el rango empieza en 0)
            print('\n\t\t\t\t\t\t\t\t\t\t Frame '+str(CodingFrame+1)+'\n\n')
            while True:
                if CodingFrame>(((len(Seq)/3)-1)*3):  ##Esta condición permite correr el código hasta que se alcanza el final de la secuencia.
                    break
                SubSeq=Seq[CodingFrame]+Seq[CodingFrame+1]+Seq[CodingFrame+2] ##Formamos el codón y lo asignamos a SubSeq.
                ProtSeq=ProtSeq+DicFile[SubSeq][0] ##Traducimos el codón actual a código de una letra y lo añadimos a la secuencia traducida que ya estuviera.
                CodingFrame+=3 #Movemos 3 nucleótidos para leer el siguiente codón
            print(ProtSeq)
            MyFile.write(ProtSeq+'\n') #Escribimos la secuencia
        Counter='-' #Cuando terminamos el bloque con SeqName, para la empezar con la reversa Seq será -
    MyFile.close()
    
def Body():
    DNAList=ReadFasta(sys.argv[1]) #Lista que contiene el DNA y el Accession number
    GenCode=CreateDictionary('GeneticCode_standard.csv')
    CompSeq=ComplementaryGenerator(DNAList[1]) #CompSeq contiene ahora la secuencia complementaria correspondente de llamar la función ComplementaryGenerator
    Protein=TranslateDNA(DNAList[1],CompSeq,GenCode,DNAList[0]) ##DNAList[1] contiene la secuencia de DNA extraida y DNAList[0] el Accession Number

if __name__=='__main__':
    import sys
    import re
    if len(sys.argv)<2:
        print('Please, introduce as an argument the file you want to translate.') #Si no nos introduce el argumento con la secuencia, se lo pide.
    if not('.fasta') in sys.argv[1]: #Si introducimos como argumento un archivo que no es fasta te indica que introduzcas un fasta
        print('You have to introduce a fasta sequence')
    else:
        Body()

