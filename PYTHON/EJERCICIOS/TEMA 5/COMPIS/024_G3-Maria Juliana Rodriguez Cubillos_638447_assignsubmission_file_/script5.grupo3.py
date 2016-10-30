### My_group: g3 (Maria Juliana Rodriguez, Ioannis Rallis, Patricia Palacios Ibáñez)
##This program reads fasta files, extracts its DNA sequence and translates it using the standrad gene code whose path must be entered as an argument.
##Saves the results of the translation as the accession number in location(C:\Users\Administrator).
##There will be no comments for the last 2 functions as they are a copy of our previous work and are commented separately on our previous scripts.
####ATTENTION### ARGUMENT ORDER: (ScriptName>DNAfastaFile>GeneCodeStandard)###ATTENTION### 

def ACCNUM(fileX): #Create function that uses a fasta file and extracts the accession number.
    import re   #Imports the regular expression module.
    File=open(fileX,"r") #Opens fasta file.
    MyFile=File.readline() #Reads the 1st line.
    File.close() 
    MyRE=r"\w\w_\d*.\d" #Synthesis of RE using the appropriate wildcards
    MyRegex=re.compile(MyRE) #Function of the RE module that transforms a string into a pattern-type object.
    MyRes=MyRegex.findall(MyFile) #Search for the synthesised pattern.
    return(MyRes) # Returns a list with all the matches.
def DNA(FileX):
  Seq=""
  Sequence=open(FileX,"r")
  for line in Sequence:
    if not(">" in line):
      Seq=Seq+line.strip()
  Sequence.close()
  return(Seq.upper())

def Translation(Seq,FileY,Filename):
    import re
    Code={}
    GeneCode=open(FileY,"r") 
    for line in GeneCode:
        MyRE=r"(\w+)\t(.)\t(\w+)" #Creation of the genetic code dictionary using Regular Expressions. 
        MyReg=re.compile(MyRE)
        MyRes=MyReg.search(line)
        Code[MyRes.groups()[0]]=MyRes.groups()[1]
    GeneCode.close()
    rcSeq=""
    compNucl={"A":"T","T":"A","G":"C","C":"G",}
    for base in Seq:
        if compNucl[base] in Seq:
          rcSeq = compNucl[base] + rcSeq
    prFile=open(str(Filename[0])+".txt","w")
    for ORF in [0,1,2]:
        locals()["StF_{}".format(ORF)]=""
        for n in range(ORF,len(Seq),3):
            if Seq[n:n+3] in Code:
              locals()["StF_{}".format(ORF)]  += Code[Seq[n:n+3]]
        prFile.write("StandForward_ORF{}: \n".format(ORF))
        prFile.write(locals()["StF_{}".format(ORF)])
        prFile.write("\n")
        locals()["StR_{}".format(ORF)]=""
        for n in range(ORF,len(rcSeq),3):
            if rcSeq[n:n+3] in Code:
                locals()["StR_{}".format(ORF)]  += Code[rcSeq[n:n+3]]
        prFile.write("StandReverse_ORF{}: \n".format(ORF))
        prFile.write(locals()["StR_{}".format(ORF)])
        prFile.write("\n")
    prFile.close()
def Main(): ## Name of fuction
    accessionNum=ACCNUM(sys.argv[1])##Reads the fasta file whose path is given as an argument in cmd and extracts the accession number.
    openDNA=DNA(sys.argv[1]) ##Reads the fasta file whose path is given as an argument in cmd and extracts its DNA sequence.
    Translation(openDNA,sys.argv[2],accessionNum)## Translates the DNA sequence using the standard gene code (by iserting its path as an argument in cmd).
if __name__ == "__main__": ##This conditional is used to check if the file is being run directly or being imported.
  import sys  
  Main() ## Execution of fuction. 
