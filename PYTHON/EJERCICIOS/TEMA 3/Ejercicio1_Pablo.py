HRAS=open("Human_HRAS.fasta.txt","r")
Sequence=[]
for Line in HRAS:
    Data=Line.strip()
    if not(">" in Data): Sequence=Sequence+[Data]
HRAS.close()
Sequence="".join(Sequence)
GeneticCode=open("GeneticCode_standard.csv","r")
Code1={}
Code2={}
for Line in GeneticCode:
    Data=Line.strip().split("\t")
    Code1[Data[0]]=Data[2]
    Code2[Data[0]]=Data[1]
GeneticCode.close()
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
        Translates=open("Translates.txt","a")
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
print("End, you can see de translates in the file Translates.txt")
input("Press enter if you want to exit")
exit()



    
    
