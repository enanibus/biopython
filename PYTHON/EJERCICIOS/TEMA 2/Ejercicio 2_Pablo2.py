MyDNA=input("type DNA sequence and press enter ")
Nucleotides=["A","T","G","C","AA","AT","AG","AC","TA","TT","TG","TC","GA","GT","GG","GC","CA","CT","CG","CC"]
REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC","HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
if len(MyDNA)!=MyDNA.upper().count("A")+MyDNA.upper().count("T")+MyDNA.upper().count("G")+MyDNA.upper().count("C")+MyDNA.upper().count("U"):
    print("It only accepts DNA sequences")
    exit()
elif "U" in MyDNA:
    print("Beware, it is a RNA sequence, it will be translated to DNA")
    MyDNA_translated=MyDNA.upper().replace("U","T")
    print(MyDNA_translated)
print("Nucleotides =",len(MyDNA))
for n in Nucleotides:
    percentage=(MyDNA.upper().replace("U","T").count(n)/len(MyDNA))*100
    print("%",n,"=",round(percentage,2))
for e in REnz:
    Cut=REnz[e] in MyDNA.upper().replace("U","T")
    print("Cleveage by",e,"? ",Cut)
    if Cut==True:
        Position=MyDNA.upper().replace("U","T").find(REnz[e])
        if Position==0:print(Position+1)
        Position=0
        while Position!=-1:
            Position=MyDNA.upper().replace("U","T").find(REnz[e],Position+1)
            if Position!=-1:print(Position+1)

    
    

