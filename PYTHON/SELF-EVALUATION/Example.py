#! usr/bin/python3
# code for self-evaluation test Oct. 2016
# Comments have been deliberately omitted
# The code might contain some errors

def SeqStats(Seq,Base):
  print ("\t Percent ",Base,":",end="")
  tmp=round((Seq.upper().count(Base)/len(Seq))*100,1)
  print (tmp

def DigestionTF(Seq,EnzDic,Enz)
return(EnzDic[Enz.upper()] in Seq)

def DigestionPos(Seq,EnzDic,Enz):
  return(Seq.upper().find(EnzDic[Enz.upper()]))

def Main():
  REnz={"ECORI":"GAATTC", "BAMHI":"GGATCC", "HINDIII":"AAGCTT"}
  DNA=input("Please enter a DNA sequence: ")
  print ("Sequence statistics")
  for Nucl in ["A","C","G","T"]:
    SeqStats(DNA,Nucl)
  nR=input("Please enter an enzyme (EcoRI, BamHI, HindIII or NotI): ")
  print ("Is your DNA digested by the enzyme ",nR,"?")
  print(DigestionTF(DNA,REnz,nR))
  print ("The enzyme cuts the DNA at position (-1=no digestion):",end="")
  print(DigestionPos(DNA,REnz,nR))

Main()
