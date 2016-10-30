#! usr/bin/python
# Exercise Unit 4
# Luis del Peso, oct 2015

# The script:
#   1a. reads the accesion number from a FASTA file provided as the first argument
#   1b. reads the sequence from a FASTA file provided as the first argument
#   2. reads the standard genetic code (extracting it using regular expressions)
#   3. translates sequence in all six frames according to the genetic code
#   4. saves translations into a text file named as the accesion file

### In the code below I used “#” for regular comments 
## and “###” for comments intended just for you as students of this course.

### The objective of this exercise is for you to practise:
### 1. all previous concepts (loops, conditionals, I/O,functions and code modularity,arguments)
### 2. regular expressions


# reads sequence
def ReadFASTA(FileName):
  Seq="" #initializes variable that will store the sequence
  try:### we haven't seen exception handling in class I'll use this example to explain it
    MyFile=open(FileName,"r")###Note that there is another MyFile active, but no interaction because this is a local variable
  except:
    exit("The file "+FileName+" does not exists\n")
  for Line in MyFile:
    if not(">" in Line):## skips the title line of the FASTA format
      Seq=Seq+Line.strip()
    else:
      Acc=GetRefSeqAcc(Line)
  MyFile.close()
  return(Seq,Acc)

def GetRefSeqAcc(TitleLine):
  '''requires re module'''
  MyRE=r'N[MX]_\d+\.\d{1}'
  MyRegex=re.compile(MyRE)
  MyRes=MyRegex.search(TitleLine)
  if MyRes==None:
    return(None)
  return(MyRes.group())

# reads genetic code
def ReadGenCode(FileName):
  '''requires re module'''
  MyRE=r'([ACGT]{3})\t([^BJOUXZ]{1})\t([A-Z]{1}[a-z]{2})'##regular expression with groupings
  MyRegex=re.compile(MyRE)##compiles regular expression
  GenCode={} #initializes dictionary that will store the genetic code
  MyFile=open(FileName,"r")
  for Line in MyFile:
    MyRes=MyRegex.search(Line)##search for regular expression in Line
    Grupo=MyRes.groups() ##each group from the regular expression is an element of "Grupo"
    GenCode[Grupo[0]]=[Grupo[1],Grupo[2]]
  MyFile.close()
  return(GenCode)

# checks and return arguments
def GetArg():
  if len(sys.argv)>1:
    return(sys.argv[1])
  else:
    sys.exit("You must provide the name of the FASTA file to be read as an argument.")

# generates reverse complement
def RevCompl(Seq):
  rcSeq=""#initializes variable that will store the reverse complement of sequence
  Complement={"A":"T","C":"G","G":"C","T":"A"} #dictionary holding complement rule
  for base in Seq:
    rcSeq=Complement[base]+rcSeq##The order of elements generatesthe reverse strand
  return(rcSeq)

# translates sequence and saves results to file
def Translate(Seq,GenCode,Frame):
  Protein=""
  for Position in list(range(Frame,len(Seq),3)):
    if Position<=(len(Seq)-3):
      CurrentCodon=Seq[Position:Position+3]
      Protein=Protein+GenCode[CurrentCodon][0]
  return(Protein)

def Main(): ### contains main body of the script
  inFileName=GetArg()###This is called multiple assignation
  Seq,Acc=ReadFASTA(inFileName) #fetch sequence and accession from file
  if Acc==None:
    sys.exit("The fasta file does not contain the expected accession number\n")#quits if not accesion is found
  MyFile=open(Acc+"_txt","w")
  GenCode=ReadGenCode("GeneticCode_standard.csv")
  CurrentStrand="+" #counter to keep track of frame
  for Strand in [Seq,RevCompl(Seq)]:## use of array without assigment to a variable name
    if CurrentStrand=="+":
      MyFile.write("##### Plus strand #####\n")
    else:
      MyFile.write("##### Minus strand #####\n")
    for Frame in [0,1,2]:##could have used list(range(3)) instead
      MyFile.write("\t## Frame "+str(Frame+1)+"\n")
      MyFile.write(Translate(Strand,GenCode,Frame)+"\n")
    CurrentStrand="-"
  MyFile.close()

if __name__=="__main__":
  import sys ## imports sys module required to get user arguments (among others)
  import re ## imports regular expression module
  Main()###invokes main body