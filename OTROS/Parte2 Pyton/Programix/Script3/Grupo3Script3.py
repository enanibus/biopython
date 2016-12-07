###Grupo_3_(Pablo_Villoslada_Juan_Enriquez_Juan_Escudero)_Script_3

###Readfile HumanHRAS.fasta and extracts DNA seq from it###

#Definimos Seq como la str que contendra la secuencia de DNA que abriremos.
Seq=[]
MyFile=open ('Human_HRAS.fasta.txt','r')
# Uses a "for" loop to go over each line in the file
for Line in MyFile: #nombramos Data para crear lista
    Data=Line.strip() #desnudamos Line de todo lo extra a su derecha (\n)
    if not('>' in Line):
        #definimos Seq y hacemos que se le anhadan
        #las lineas de MyFile
        Seq=Seq + [Data]
Seq=('').join (Seq) #Unimos la secuencia
print (Seq)#mostramos la secuencia

MyFile.close() #Close the file-object to terminate connection with the file

print ('\n\n\n\n')

###Reads genetic Code from file
#Dictionary
GenCode={}
MyFile2=open ('GeneticCode_standard.csv')
#llenamos el diccionario del codigo genetico con cada linea de Data2 tomando
#solo las pos 0 y 2, es decir, codon y aa complementario en formato 3 letras
for Line in MyFile2:
    Data2=Line.strip().split('\t')
    GenCode[Data2[0]]=Data2[2]
    print (Data2)
print (GenCode)
print (GenCode.keys())
print (GenCode.values())
print ('\n\n\n')
MyFile2.close() #Close the file-object to terminate connection with the file

rcSeq=[]
Complement_bases={}
Bases=['A','C','T','G']

#construir diccionario con loop
#otra manera es
for Line in Bases:
    Data3=Data3 + Line
   
    print (Line)
    print (Data3)
Complement_bases[Data3[0]]=Data3[1]
print (Complement_bases)
    
    
print (Complement_bases)




##Complement_bases={'A':'T','T':'A','C':'G','G':'C'}
x=0

