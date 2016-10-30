REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC","HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
MySeq=input("Please type a DNA sequence and press enter: ")
perA=MySeq.upper().count("A")/len(MySeq)*100
perG=MySeq.upper().count("G")/len(MySeq)*100
perC=MySeq.upper().count("C")/len(MySeq)*100
perT=MySeq.upper().count("T")/len(MySeq)*100
print("%A is: ", perA)
print("%G is: ", perG)
print("%C is: ", perC)
print("%T is: ", perT)
Enzyme=input("Please enter a valid enzime: ")
Cut=REnz[Enzyme] in MySeq.upper()
print("Does your selected enzyme cut in the sequence?",Cut)
Position=MySeq.upper().find(REnz[Enzyme])
print("The position of that cut is: ", Position)
