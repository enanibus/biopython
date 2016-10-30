#! usr/bin/python
# Exercise Unit 4
# Luis del Peso

# The script:
#   1. reads the sequence from a FASTA file provided as the first argument
#   2. reads the standard and mitochondrial genetic codes
#   3. translates sequence in all six frames according to both genetic codes
#   4. saves translations into a text file provided as the second argument

### In the code below I used “#” for regular comments 
## and “###” for comments intended just for you as students of this course.

### The objective of this exercise is for you to practise:
### 1. all previous concepts (loops, conditionals, I/O)
### 2. functions and code modularity
### 3. arguments

import sys ## imports sys module required to get user arguments (among others)

# reads sequence
def ReadFASTA(FileName):
  Seq="" #initializes variable that will store the sequece
  try:### we haven't seen exception handling in class I'll use this example to explain it
    MyFile=open(FileName,"r")###Note that there is another MyFile active, but no interaction because this is a local variable
  except:
    print("The file ",FileName," does not exists")
    exit()
  for Line in MyFile:
    if not(">" in Line):## skips the title line of the FASTA format
      Seq=Seq+Line.strip()
  MyFile.close()
  return(Seq)

# reads genetic code
def ReadGenCode(FileName):
  GenCode={} #initializes dictionary that will store the genetic code
  MyFile=open(FileName,"r")
  for Line in MyFile:
    LineFields=Line.strip().split("\t")##splits each line by tab delimiter
    GenCode[LineFields[0]]=LineFields[1:]##codon as key and an array of the 2 aa codes as value
  MyFile.close()
  return(GenCode)

# checks and return arguments
def GetArg():
  if len(sys.argv)>2:
    return(sys.argv[1:3])
  else:
    print('''You must provide (in the indicated order): the name of the FASTA file
      to be read and a name for the output file as arguments.''')
    exit()

# generates reverse complement
def RevCompl(Seq):
  rcSeq=""#initializes variable that will store the reverse complement of sequence
  Complement={"A":"T","C":"G","G":"C","T":"A"} #dictionary holding complement rule
  for base in Seq:
    rcSeq=Complement[base]+rcSeq##The order of elements generatesthe reverse strand
  return(rcSeq)

# translates sequence
def Translate(Seq,GenCode,Frame):
  Protein=""
  for Position in list(range(Frame,len(Seq),3)):
    if Position<=(len(Seq)-3):
      CurrentCodon=Seq[Position:Position+3]
      Protein=Protein+GenCode[CurrentCodon][0]
  return(Protein)

def Main(): ### contains main body of the script
  inFileName,outFileName=GetArg()###This is called multiple assignation
  MyFile=open(outFileName,"w")
  Seq=ReadFASTA(inFileName) #fetch sequence from file
  GenCodeS={} #Dictionary containin all genetic codes (dictionary of dictionaries)
  for GenCodeType in ["standard","mito"]:#reads genetic codes into GenCodeS
    GenCodeS[GenCodeType]=ReadGenCode("GeneticCode_"+GenCodeType+".csv")
  CurrentStrand="+" #counter to keep track of frame
  for Strand in [Seq,RevCompl(Seq)]:## use of array without assigment to a variable name
    if CurrentStrand=="+":
      MyFile.write("##### Plus strand #####\n")
    else:
      MyFile.write("##### Minus strand #####\n")
    for Frame in [0,1,2]:##could have used list(range(3)) instead
      MyFile.write("\t## Frame "+str(Frame+1)+"\n")
      for GenCodeType in ["standard","mito"]:
        MyFile.write("\t\t# "+GenCodeType+" genetic code\n")
        MyFile.write(Translate(Strand,GenCodeS[GenCodeType],Frame)+"\n")
    CurrentStrand="-"

if __name__=="__main__":
  Main()###invokes main body