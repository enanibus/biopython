##Group 8: Álvaro Alfayate, Andrea de la Fuente, Carla Guillén y Jorge Nuevo.
MyFile=open('Human_HRAS.fasta', 'r')

#Reads the file “Human_HRAS.fasta” (FASTA format sequence) and extracts the DNA sequence from it .
DNAseq=''
for Line in MyFile:
    Line=Line.strip()
    if '>' not in Line: ##Excluimos la primera línea de codigo de la secuencia.
        DNAseq=DNAseq+Line
         
MyFile.close()

#Reads the genetic code from file “GeneticCode_standard.csv” (tab-delimited text file).
MyFile2=open('GeneticCode_standard.csv','r')
CodonList=[]
LetterList=[]
LetterList2=[]
#Vamos a transformar el código genético a un diccionario:
for Line in MyFile2:
    Line=Line.strip()
    Code=Line.split('\t')##Lo separamos en tres columnas. La 0 será el codón, la 1 el código de 1 letra de aas y la 2 el codigo de 3 letras.
    CodonList=CodonList+[Code[0]] 
    LetterList=LetterList+[Code[1]]
    LetterList2=LetterList2+[Code[2]]
MyDic1=dict(zip(CodonList,LetterList)) #Definimos un diccionario para traducir la secuencia al código de una letra de los aminoácidos.
MyDic2=dict(zip(CodonList,LetterList2)) #Definimos un diccionario para traducir la secuencia al código de tres letras de los aminoácidos.
MyFile2.close()

MyFinalFile1=open('HRAS_Translation_1LetterCode.txt','w') #Abrimos un archivo donde se va a importar el RNA traducido a Proteina en código de una letra
MyFinalFile2=open('HRAS_Translation_3LetterCode.txt','w') #Abrimos un archivo donde se va a importar el RNA traducido a Proteina en código de tres letras
StartingPosition=[0,1,2]  ##Definimos una lista con tres posiciones para contar los nucleótidos en las tres posiciones solapantes.
Counter=0   ##Un contador que mide las rondas. Sirve para que a partir de la segunda posición nos imprima Another possible en vez de A possible
MyFinalFile1.write('\t\t\t\t\t\t\t\t SINGLE-LETTER AMINO ACID CODE') ##Introducimos la etiqueta en el archivo para que describa qué código es.
MyFinalFile2.write('\t\t\t\t\t\t\t\t THREE-LETTER AMINO ACID CODE')
# Translates the DNA sequence in all six coding frames according to the corresponding genetic code in 2.
Position=0 ##Esta variable sirve para contar en qué pauta de lectura estamos para luego indicarlo en el archivo
for z in StartingPosition: ##Bucle que va a correr en las tres fases de lectura.
    ProtSeq=''   ##Definimos una variable de texto vacía donde vamos a ir añadiendo los aminoácidos segun se traduzcan
    ProtSeq2='' ##Lo mismo con el codigo de tres letras de los aminoácidos
    while True:
        if z>(((len(DNAseq)/3)-1)*3):  ##Esta condición permite correr el codigo hasta que se alcanza el final de la secuencia.
            break
        subSeq=DNAseq[z]+ DNAseq[z+1]+ DNAseq[z+2] ##Unes las tres letras para formar un codón y la defines como subSeq
        ProtSeq=ProtSeq+MyDic1[subSeq]  ##Añades a la lista de ProtSeq el aminoácido correspondiente a la subSeq (Usando el diccionario)
        ProtSeq2=ProtSeq2+MyDic2[subSeq] ##Lo mismo pero con el codigo de tres letras
        z+=3   ##Sumas +3 para avanzar en la posición 3 nucleótidos.
    Position+=1 #Sumas +1 a la posición pues pasas a la siguiente pauta de lectura
    print('\n\t\t\t\t\t\t\t\t'+str(Position)+' CODING FRAME:\n'+'\t\t\t\t\t\t\t  One-Letter Aminoacid Code:\n'+ProtSeq+'\n'+'\t\t\t\t\t\t\tThree-Letter Aminoacid Code:\n'+ProtSeq2)
    #printeamos la Coding frame en la que estamos y las secuencias traducidas según los diccionarios
    MyFinalFile1.write('\n\t\t\t\t\t\t\t\t\t'+str(Position)+' CODING FRAME:\n'+ProtSeq+'\n') ##Creamos un archivo que lleve los letreros indicadores de las traducciones, asi como cada una de ellas.
    MyFinalFile2.write('\n\t\t\t\t\t\t\t\t\t'+str(Position)+' CODING FRAME:\n'+ProtSeq2+'\n') ##Lo mismo para el código de tres letras de los aminoácidos
    continue  ##Cuando termine de hacer esto para la primera posición, debe volver al principio del bucle for y pasar a la siguiente posición.
    

Position=3  #Ahora la posición parte del 3 pues ya han pasado las tres primeras fases de lectura.
DNAseq=DNAseq[::-1]   ##Se repite el mismo proceso para la secuencia invertida.
for z in StartingPosition:
    ProtSeq=''  ##Redefinimos la variable de texto vacía 
    ProtSeq2='' 
    while True:
        if z>(((len(DNAseq)/3)-1)*3):
            break
        subSeq=DNAseq[z]+ DNAseq[z+1]+ DNAseq[z+2]
        ProtSeq=ProtSeq+MyDic1[subSeq]
        ProtSeq2=ProtSeq2+MyDic2[subSeq]
        z=z+3
    Position+=1
    print('\n\t\t\t\t\t\t\t\t'+str(Position)+' CODING FRAME:\n'+'\t\t\t\t\t\t\t  One-Letter Aminoacid Code:\n'+ProtSeq+'\n'+'\t\t\t\t\t\t\tThree-Letter Aminoacid Code:\n'+ProtSeq2)
    MyFinalFile1.write('\n\t\t\t\t\t\t\t\t\t'+str(Position)+' CODING FRAME:\n'+ProtSeq+'\n')
    MyFinalFile2.write('\n\t\t\t\t\t\t\t\t\t'+str(Position)+' CODING FRAME:\n'+ProtSeq2+'\n')
    continue
#Saves all translations to a single text file
MyFinalFile1.close()
MyFinalFile2.close()
print('\n\nYou have your sequence translated in:\nHRAS_Translation_1LetterCode.txt in Single-letter aminoacid code\nHRAS_Translation_3LetterCode.txt in Three-letter aminoacid code')

  

