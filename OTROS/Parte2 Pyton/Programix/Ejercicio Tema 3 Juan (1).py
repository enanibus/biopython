#Problem1_ExerciseSheet3_Group2 (Juan Enríquez, Juan Escudero, Pablo Villoslada)
SeqHRAS=() #Open an empty string to fill it up later
HRAS=open("Human_HRAS.fasta.txt", "r") #Open text file with the heading and the DNA sequence
for Line in HRAS: #Bucle used to extract just the sequence from the file
    Data=Line.strip() 
    if not(">" in Data): SeqHRAS=SeqHRAS+[Data] #Conditional used to extract just the sequence if the condition is true
HRAS.close() #Close file

GenCode={} #Open an empty dictionary. It will be used to translate the different codons
GeneticCode=open("GeneticCode_standard.csv","r") #Open the file containing the genetic code
for Line in GeneticCode: #Loop used to split each line into the triplet and the coded aminoacid
    Data=Line.strip().split("\t") #Creates a list of 3 values per line.
    Code1[Data[0]]=Data[2] #Fills the dictionary with codons and coded aa. 
    Code2[Data[0]]=Data[1]
GeneticCode.close() #Closes file

reSeq=() #Opens an empty string. We will fill it with the RNA seq.
Complement[] 
for x in [0,1,2]:
    Translate1_1=[]
    Translate1_2=[]
    for aa in list(range(x,len(Sequence)-1)):
        Codons=Sequence[aa:aa+3]
        if Codons in Code1.keys():
            Aminoacides1=Code1[Codons]
            Aminoacides2=Code2[Codons]
        Translate1_1=Translate1_1+[Aminoacides1]
        Translate1_2=Translate1_2+[Aminoacides2]
    Translates=open("Translates.txt","a")
    Translate1_1="".join(Translate1_1)
    Translate1_2="".join(Translate1_2)    
    Translates.write("Translate")
    Translates.write(str(x+1))
    Translates.write("---\n\n")
    Translates.write(Translate1_1)
    Translates.write("\n\n")
    Translates.write(Translate1_2)
    Translates.write("\n\n\n")
    Translates.close()
Original_symbols="ATGC"
Secret_code="TACG"
Trans_table=str.maketrans(Original_symbols,Secret_code)
Sequence=Sequence.translate(Trans_table)
Sequence=Sequence[::-1]
for x in [0,1,2]:
    Translate1_1=[]
    Translate1_2=[]
    for aa in list(range(x,len(Sequence)-1)):
        Codons=Sequence[aa:aa+3]
        if Codons in Code1.keys():
            Aminoacides1=Code1[Codons]
            Aminoacides2=Code2[Codons]
        Translate1_1=Translate1_1+[Aminoacides1]
        Translate1_2=Translate1_2+[Aminoacides2]
        Translates=open("Protein.txt","a")
    Translate1_1="".join(Translate1_1)
    Translate1_2="".join(Translate1_2)    
    Translates.write("Translate")
    Translates.write(str(x+4))
    Translates.write("---\n\n")
    Translates.write(Translate1_1)
    Translates.write("\n\n")
    Translates.write(Translate1_2)
    Translates.write("\n\n\n")
    Translates.close()
print("End, you can see de translates in the file Protein.txt")
input("Press enter if you want to exit")
exit()

                        
    
