#! usr/bin/python
# Exercise Unit 3
# Luis del Peso, oct 2016

# The script:
#   1. reads the sequence in file Human_HRAS.fasta
#   2. reads the genetic code in file GeneticCode_standard.csv
#   3. translates sequence in all six frames
#   4. saves translations into a single text file

# In the code below I used # for regular comments
# and ### for comments intended just for you as students of this course.

### The objective of this exercise is for you to practise:
### 1. all previous concepts
### 2. working with files
### 3. (optional: arguments) we'll see it today

import sys ## imports sys module required to get user arguments (among others)

# reads sequence
Seq="" #initializes variable that will store the sequece
MyFile=open("Human_HRAS.fasta","r")
for Line in MyFile:
  if not(">" in Line):## skips the title line of the FASTA format
    Seq=Seq+Line.strip()
MyFile.close()

# reads genetic code
GenCode={} #initializes dictionary that will store the genetic code
MyFile=open("GeneticCode_standard.csv","r")
for Line in MyFile:
  LineFields=Line.strip().split("\t")##splits each line by tab delimiter
  GenCode[LineFields[0]]=LineFields[1:]##codon as key and an array of the 2 aa codes as value
MyFile.close()

# test if the user provided an output file name as argument and generates one otherwise
OutputFileName="" # holds output file name (and path)
if len(sys.argv)>1:
  OutputFileName=sys.argv[1]
else:
  OutputFileName=sys.argv[0].replace(".py","")+"_output.txt" ##filename from script name

# generates reverse complement
rcSeq=""#initializes variable that will store the reverse complement of sequence
Complement={"A":"T","C":"G","G":"C","T":"A"} #dictionary holding complement rule
for base in Seq:
  rcSeq=Complement[base]+rcSeq##The order of elements generatesthe reverse strand

# translates sequence and saves results to file
MyFile=open(OutputFileName,"w")
CurrentStrand="+" #counter to keep track of frame
for Strand in [Seq,rcSeq]:## use of array without assigment to a variable name
  if CurrentStrand=="+":
    MyFile.write("##### Plus strand #####\n")
  else:
    MyFile.write("##### Minus strand #####\n")
  for Frame in list(range(3)):##could have used [0,1,2] instead
    MyFile.write("Frame "+str(Frame+1)+"\n")
    Protein=""#initializes variable that will store the protein sequence
    for Position in list(range(Frame,len(Strand),3)):
      if Position<=(len(Strand)-3):
        CurrentCodon=Strand[Position:Position+3]
        if GenCode[CurrentCodon][0]=="*":##remove this line and next for whole sequence translation
          break
        else:
          Protein=Protein+GenCode[CurrentCodon][0]
    MyFile.write(Protein+"\n")
  CurrentStrand="-"
MyFile.close()
