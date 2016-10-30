#! usr/bin/python3
# HPBBM midterm exam 2015 (python)
# Comments have been deliberately omitted

import sys
from Script_Unit4_LPO_v2 import ReadFASTA

def GetNuclFreq(ArraySeq,minLength):
  Freq=[]
  for pos in range(0,minLength):
    Freq.append({})
    for nucl in ["A","C","G","T"]:
      Freq[pos][nucl]=0
  for Seq in ArraySeq:
    for pos in range(0,minLength):
      nucl=Seq[pos:pos+1]
      Freq[pos][nucl]=Freq[pos][nucl]+1
  return(Freq)

def WritesNuclFreq(Freq):
   for nucl in ["A","C","G","T"]:
     print (nucl,end="")
     for pos in range(0,len(Freq)):
       print("\t",Freq[pos][nucl],end="")
     print()
     
def Main(inFiles):
  SeqArray=[]
  minLength=50
  for fileName in inFiles[1:]:
    Seq=ReadFASTA(fileName)
    SeqArray.append(Seq.upper())
    if len(Seq)<minLength:
      minLength=len(Seq)
  NuclFreq=GetNuclFreq(SeqArray,minLength)
  WritesNuclFreq(NuclFreq)

if len(sys.argv)<2:
  sys.exit("You must provide at least the name of one file in fasta format")
else:
  Main(sys.argv)
sys.exit()
    
  