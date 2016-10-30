#! usr/bin/python
# Exercise Unit 4
# Luis del Peso, sep 2016

def SeqStats(Seq,Base):
  print ("\t Percent ",Base,":",end="")
  tmp=round((Seq.upper().count(Base)/len(Seq))*100,1)
  print (tmp)

def DigestionTF(Seq,EnzDic,Enz):
  return(EnzDic[Enz.upper()] in Seq)

def DigestionPos(Seq,EnzDic,Enz):
  return(Seq.find(EnzDic[Enz.upper()]))

def Main():
  REnz={"ECORI":"GAATTC", "BAMHI":"GGATCC", "HINDIII":"AAGCTT"}
  DNA=input("Please enter a DNA sequence: ").upper()
  print ("Sequence statistics")
  for Nucl in ["A","C","G","T"]:
    SeqStats(DNA,Nucl)
  nR=input("Please enter an enzyme (EcoRI, BamHI, HindIII or NotI): ")
  print ("Is your DNA digested by the enzyme ",nR,"?")
  print(DigestionTF(DNA,REnz,nR))
  print ("The enzyme cuts the DNA at position (-1=no digestion):",end="")
  print(DigestionPos(DNA,REnz,nR))

if __name__=='__main__':
  Main()