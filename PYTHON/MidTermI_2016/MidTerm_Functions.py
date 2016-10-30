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

def DigestionPos(Seq):
  REnz={"SALI":"GTCGAC","XBAI":"TCTAGA","BPI1":"GAAGAC","ECORI":"GAATTC","XHOI":"CTCGAG"}
  for Enzyme in REnz.keys():
    Cut=REnz[Enzyme] in Seq
    print ("Is your DNA digested by the enzyme ",Enzyme,"? ",Cut)
    if Cut:
      DigestionPos(Seq,REnz[Enzyme])
  
def DigestionAll(Sequence="",Enzyme="SALI"):
  REnz={"SALI":"GTCGAC","XBAI":"TCTAGA","BPI1":"GAAGAC","ECORI":"GAATTC","XHOI":"CTCGAG"}
  Pos=0
  SiteLocations=[]
  while Pos<len(Sequence):
      Site=Sequence.find(REnz[Enzyme],Pos)
      if Site>0:
          SiteLocations.append(Site)
          Pos=Site+1
      else:
          break
  return(SiteLocations)