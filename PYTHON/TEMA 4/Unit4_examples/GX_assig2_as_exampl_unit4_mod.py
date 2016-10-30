#Grupo_XXXXX
#Script_Unit_2

def AnalizeSeq(Seq,Nt,Dn,Re):
  print('\n  ------DNA COMPOSITION-----\nNucleotide composition')
  for nt in Nt:
    print("        Percentage of ",nt,": ",round((Seq.count(nt)/len(Seq))*100,2)," %")
  print('Dinucleotide composition') 
  for dint in Dn:
    print("        Percentage of ",dint,": ",round((Seq.count(dint)/(len(Seq)-1))*100,2)," %")
  print('\n  ------RESTRICTION ENZYMES-----\n') 
  for enzyme_name in Re:
    if (Seq.count(REnz[enzyme_name]))==0:
      print("The sequence is not digested by ",enzyme_name)
    else:
      position=0
      while(Seq.find(REnz[enzyme_name],position))!=(-1):
        CuttingPosition=Seq.find(REnz[enzyme_name],position)+1 
        print("The sequence is digested by ",enzyme_name," in position ",CuttingPosition)
        position=CuttingPosition+1
  print("\nNote: the cutting positions this program might...")                     


REnz = {"EcoRI":"GAATTC", "BamHI":"GGATCC","HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
NT = ['A','C','G','T']
DINT=['AA','AC','AG','AT','CA','CC','CG','CT','GA','GC','GG','GT','TA','TC','TG','TT']
DNA_input = input("Please introduce a DNA sequence: ")
DNA = DNA_input.upper()

if (DNA.count("U")+DNA.count("T")+DNA.count("A")+DNA.count("G")+DNA.count("C"))!=len(DNA):
  print("\nThis program only accepts DNA sequences, and the introduced one is not DNA")  
elif DNA.count("U")==0:
  print("This is the introduced DNA sequence: ",DNA)
  AnalizeSeq(DNA,NT,DINT,REnz)
else:
  print("\nThe introduced sequence is not DNA but RNA instead")
  DNA=DNA.replace("U","T")
  AnalizeSeq(DNA,NT,DINT,REnz)
print("\nProgram end")
