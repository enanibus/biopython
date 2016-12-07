#! usr/bin/python
# Exercise Unit 3
# Luis del Peso, oct 2016

# The script:
#   1. reads the sequence in file Human_HRAS.fasta
#   2. reads the genetic code in file GeneticCode_standard.csv
#   3. translates sequence in all six frames
#   4. saves translations into a single text file

### In the code below I used “#” for regular comments 
## and “###” for comments intended just for you as students of this course.

### The objective of this exercise is for you to practise:
### 1. all previous concepts
### 2. working with files
### 3. (optional: arguments) we'll see it today

import sys ## imports sys module required to get user arguments (among others)

# reads sequence
Seq="" #initializes variable that will store the sequece
MyFile=open("Human_HRAS.fasta.txt","r")
for Line in MyFile:
  if not(">" in Line):## skips the title line of the FASTA format
    Seq=Seq+Line.strip()
MyFile.close()

print (Seq)
print ('\n\n\n')



# reads genetic code
GenCode={} #initializes dictionary that will store the genetic code
MyFile=open("GeneticCode_standard.csv","r")
for Line in MyFile:
  LineFields=Line.strip().split("\t")##splits each line by tab delimiter, esto acumula variables en una lista LineFields con cada linea de MyFile
  GenCode[LineFields[0]]=LineFields[1:]##codon as key and an array of the 2 aa codes as value, con el [1:] devuelve los dos ulimos elementos de la lista por cada linea.
  ##De la key Linefields[0] cuelga la lista de dos elementos LineFields[1:], que son los dos ultimos valores de la lista LineFields:
  ##Por cada linea, GenCode crea una entrada del estilo: {'TTT':['F','Phe']}
MyFile.close()

print (GenCode)
print ('\n\n\n')

#####WHAAAAAAATTTT
# test if the user provided an output file name as argument and generates one otherwise
OutputFileName="" # holds output file name (and path)
if len(sys.argv)>1:
  OutputFileName=sys.argv[1]
else:
  OutputFileName=sys.argv[0].replace(".py","")+"_output.txt" ##filename from script name
#######################################################


  
print (OutputFileName)
print ('\n\n\n')


# generates reverse complement de la secuencia Seq. Necesitamos el reverso complementario
rcSeq=""#initializes variable that will store the reverse complement of sequence
Complement={"A":"T","C":"G","G":"C","T":"A"} #dictionary holding complement rule
for base in Seq:
  rcSeq=Complement[base]+rcSeq##The order of elements generatesthe reverse strand,
  #mete la base siguiente antes de las demas, asi crea una complementaria mas rapidamente que con el metodo .maketrans y [::-1] (para leerlo de atras adelante)

print (rcSeq)
print ('\n\n\n')


# translates sequence and saves results to file
MyFile=open(OutputFileName,"w")#abre fichero para guardar
CurrentStrand="+" #counter to keep track of frame
for Strand in [Seq,rcSeq]:## use of array without assigment to a variable name
  ##usa 2 bucles, CurrentStrand se ha formado on the flight
  
  if CurrentStrand=="+":
    MyFile.write("##### Plus strand #####\n")
  else:
    MyFile.write("##### Minus strand #####\n")
  for Frame in list(range(3)):##could have used [0,1,2] instead
    MyFile.write("Frame "+str(Frame+1)+"\n")
    Protein=""#initializes variable that will store the protein sequence
    for Position in list(range(Frame,len(Strand),3)):##lista que va a ir de tres en tres ,3)
      if Position<=(len(Strand)-3):
        CurrentCodon=Strand[Position:Position+3]##coja de la string de pos a pos + 3. Empieza en la pos 0 y recorre hacia 0-3-9...,
                                                      ##en la segunda vuelta va a empezar de la 1-4-7-... y en la tercera vuelta 2-5-8-...
        if GenCode[CurrentCodon][0]=="*":##remove this line and next for whole sequence translation, en caso de codon de terminacion deja de acumular, rompe el 
          break
        else:
          Protein=Protein+GenCode[CurrentCodon][0]##el primer codon es CurrentCodon, en la primera vuelta de todos los bucles el 1er aa es ATG.
          #Usa GenCode[CurrentCodon][0] para referirse a solo la pos 0 de la lista a la que se refiere la key Curretcodon en el dicionario de la loista GenCode
          
    MyFile.write(Protein+"\n")
  CurrentStrand="-"##Cuando acaba el condicional-, pasa a negativo y ejecuta el bucle otra vez para la minus con el pimer else y el bucle normal.
MyFile.close()
