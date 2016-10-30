REnz={"ECORI":"GAATTC", "BAMHI":"GGATCC", "HINDIII":"AAGCTT", "NOTI":"GCGGCCGC"}
MySeq=input("Please  enter a DNA sequence and press enter: ").upper()

if "U" in MySeq:
    print("Caution, the input sequence is RNA. U will be replaced by T") 
    MySeq=MySeq.replace("U","T")

if MySeq.count("A")+MySeq.count("G")+MySeq.count("C")+MySeq.count("T")!=len(MySeq):
    print("This program only accepts DNA sequences")
    exit()

else:
    print("Here are your sequence statistics: ")
    print("The length is,", len(MySeq), "nucleotides")
    for Base in ["A","G","C","T"]:
        print("\t", round((MySeq.upper().count(Base)/len(MySeq))*100,1), "% of", Base)
    diNucl_freq={}
    for Base1 in ["A","C","G","T"]:
        for Base2 in ["A","C","G","T"]:
            diNucl_freq[Base1+Base2]=0
    for Position in list(range(len(MySeq)-1)):
        subSeq=MySeq[Position:Position+2]
        diNucl_freq[subSeq]=diNucl_freq[subSeq]+1
    print ("### Dinucleotide composition ###")
    for diNucl in diNucl_freq.keys():
        print ("\t",round((diNucl_freq[diNucl]/(len(MySeq)-1))*100,1)," % of ", diNucl)

    for Enz in REnz.keys():
        if REnz[Enz] in MySeq:
          print("The enzyme ",Enz," cuts the sequence at position(s): ",end="")
          End_of_Seq=False
          Position=0
          while not(End_of_Seq):
              print(MySeq.find(REnz[Enz],Position)+1,", ",end="")
              Position=(MySeq.find(REnz[Enz],Position))+1
              if MySeq.find(REnz[Enz],Position)<0:
                  End_of_Seq=True
        else:
          print("Sequence does not contain restriction sites for ",Enz)
    print()
                          
