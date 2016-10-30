REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC",
"HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
MyDNA=input("type DNA sequence and press enter")
MyDNA_mayus=MyDNA.upper()
MyEnz=input("type the name of the enzyme and press enter")
Nucleotides=len(MyDNA_mayus)
A=(MyDNA_mayus.count("A")/Nucleotides)*100
T=(MyDNA_mayus.count("T")/Nucleotides)*100
C=(MyDNA_mayus.count("C")/Nucleotides)*100
G=(MyDNA_mayus.count("G")/Nucleotides)*100
Cut=REnz[MyEnz] in MyDNA_mayus
Position=MyDNA.find(REnz[MyEnz])
print("%A=",A)
print("%T=",T)
print("%C=",C)
print("%G=",G)
print("Cut?",Cut)
print("Position?",Position)



                    
