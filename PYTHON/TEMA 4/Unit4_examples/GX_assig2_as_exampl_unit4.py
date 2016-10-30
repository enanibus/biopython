#Grupo_XXXXX
#Script_Unit_2

REnz = {"EcoRI":"GAATTC", "BamHI":"GGATCC","HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
NT = ['A','C','G','T']
DINT=['AA','AC','AG','AT','CA','CC','CG','CT','GA','GC','GG','GT','TA','TC','TG','TT']
DNA_input = input("Please introduce a DNA sequence: ")
DNA = DNA_input.upper()

if (DNA.count("U")+DNA.count("T")+DNA.count("A")+DNA.count("G")+DNA.count("C"))!=len(DNA):
	print("\nThis program only accepts DNA sequences, and the introduced one is not DNA")  
elif DNA.count("U")==0:
	print("This is the introduced DNA sequence: ",DNA)
	print('\n  ------DNA COMPOSITION-----\nNucleotide composition')
	for nt in NT:
		print("        Percentage of ",nt,": ",round((DNA.count(nt)/len(DNA))*100,2)," %")
	print('Dinucleotide composition') 
	for dint in DINT: 
		print("        Percentage of ",dint,": ",round((DNA.count(dint)/(len(DNA)-1))*100,2)," %")
	print('\n  ------RESTRICTION ENZYMES-----\n') 
	for enzyme_name in REnz:
		if (DNA.count(REnz[enzyme_name]))==0:
			print("The sequence is not digested by ",enzyme_name)
		else:
			position=0
			while(DNA.find(REnz[enzyme_name],position))!=(-1):
				CuttingPosition=DNA.find(REnz[enzyme_name],position)+1 
				print("The sequence is digested by ",enzyme_name," in position ",CuttingPosition)
				position=CuttingPosition+1
	print("\nNote: the cutting positions this program might have found define the start of the corresponding restriction site, not necessarily where the actual cleavage takes place, which depends on each particular enzyme")			

else:
	print("\nThe introduced sequence is not DNA but RNA instead")
	DNA=DNA.replace("U","T") 
	print("\nThis is the DNA sequence you would have transcribing the RNA sequence introduced: ",DNA) #Prints the sequence once translated to DNA.
	print('\n  ------DNA COMPOSITION-----\nNucleotide composition')
	for nt in NT: 
		print("        Percentage of ",nt,": ",round((DNA.count(nt)/len(DNA))*100,2)," %")
	print('Dinucleotide composition') 
	for dint in DINT:
		print("        Percentage of ",dint,": ",round((DNA.count(dint)/(len(DNA)-1))*100,2)," %") 
	print('\n  ------RESTRICTION ENZYMES-----\n') 
	for enzyme_name in REnz:
		if (DNA.count(REnz[enzyme_name]))==0:
			print("The sequence is not digested by ",enzyme_name)
		else:
			position=0
			while(DNA.find(REnz[enzyme_name],position))!=(-1):
				CuttingPosition=DNA.find(REnz[enzyme_name],position)+1
				print("The sequence is digested by ",enzyme_name," in position ",CuttingPosition)
				position=CuttingPosition+1
	print("\nNote: the cutting positions this program might have found define the start of the corresponding restriction site, not necessarily where the actual cleavage takes place, which depends on each particular enzyme")
				
print("\nProgram end")
