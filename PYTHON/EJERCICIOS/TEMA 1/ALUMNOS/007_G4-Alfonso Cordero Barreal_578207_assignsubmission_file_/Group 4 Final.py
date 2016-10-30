###My_group: Group 4 (Maria Baena, Diego Calzada and Alfonso Cordero)

##Introduce the DNA sequence, both for capitals or not

dna_seq=input("Type your DNA sequence and press Enter: ")
DNA_seq= dna_seq.upper()        


##Calculating the base percentages, with two decimals

A=round(100*DNA_seq.count("A")/len(DNA_seq),2)
T=round(100*DNA_seq.count("T")/len(DNA_seq),2)
C=round(100*DNA_seq.count("C")/len(DNA_seq),2)
G=round(100*DNA_seq.count("G")/len(DNA_seq),2)


#Printing the result, all as text (str)

print("Nucleotide composition:")
print ("      - The prercentage of A is "+str(A)+"%")
print ("      - The prercentage of T is "+str(T)+"%")
print ("      - The prercentage of C is "+str(C)+"%")
print ("      - The prercentage of G is "+str(G)+"%")


##Introducing the restriction enzyme, print as text (str)
REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC", "HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
enz=input("Enter the restriction enzime (EcoRI, BamHI, HindIII or NotI): ")
print("     -The number of " +str(enz) + " sites is: "+str(DNA_seq.count(REnz[enz])))
print("     -The first "+str(enz)+" target site is in the position: "+str(DNA_seq.find(REnz[enz])+1))

##Finish the programme making it wait for a final function upon pressing enter
Final_question=input("Press enter to exit the programme:")





