#! usr/bin/python
# Exercise Unit 4
# Luis del Peso, oct 2016

def GetDNA(FileN):
  Seq=""
  MyFile=open(FileN,"r")
  for Line in MyFile:
    if not(">" in Line):## skips the title line of the FASTA format
      Seq=Seq+Line.strip()
  MyFile.close()
  return(Seq.upper())

def SeqStats(Seq):
  print ("Sequence statistics")
  for Base in ["A","C","G","T"]:
    print ("\t Percent ",Base,":",end="")
    print(round((Seq.count(Base)/len(Seq))*100,1))

def DigestionTF(Seq):
  REnz={"ECORI":"GAATTC", "BAMHI":"GGATCC", "HINDIII":"AAGCTT"}
  for Enzyme in REnz.keys():
    Cut=REnz[Enzyme] in Seq
    print ("Is your DNA digested by the enzyme ",Enzyme,"? ",Cut)
    if Cut:
      DigestionPos(Seq,REnz[Enzyme])

def DigestionPos(Seq,Site):
  print ("The fist cut is at position: ",Seq.find(Site))
  

def Main():
  DNA=GetDNA(sys.argv[1])
  SeqStats(DNA)
  DigestionTF(DNA)

import sys
Main()