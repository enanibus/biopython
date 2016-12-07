#! usr/bin/python
# Exercise Unit 2
# Luis del Peso, sep2016

# The script asks the user to enter a DNA seq returns the reverse complement

### In the code below I used “#” for regular comments 
## and “###” for comments intended just for you as students of this course.

### The objective of this exercise is for you to practise:
### 1. Conditionals
### 2. Loops
### 3. Lists and dictionaries
### 4. strings as lists

#user input
Sequence=input("Please enter a DNA sequence: \n").upper()###coverts input to upper

#Step 1. Checks if sequence is RNA
if "U" in Sequence:
  print("WARNING: The sequence seems RNA, Uracil replaced by Thymine.")
  Sequence=Sequence.replace("U","T")

#Step 2. Checks sequence for characters other than nucleotides
NonDNA=False ###Boolean type variable to keep track of non DNA characters
for Base in Sequence: ###DNA as a list of characters
  if not(Base in ["A","C","G","T"]):
    NonDNA=True ###A non-DNA (non-RNA) character is found
    break ### avoids testing the remaining of the sequence
if NonDNA:### if Non nucleotides are found, warns user and do not continue
  print("Error: The sequence contained non-nucleotide characters.")
else:### the remaining of the program executed only if NonDNA is False
  #Step 3. Reports sequence stats
  #Step 3.1 Calculates nucleotide composition
  print ("### Nucleotide composition ###")
  for Base in ["A","C","G","T"]: ### more compact that 4 lines of code
    print ("\t",round((Sequence.upper().count(Base)/len(Sequence))*100,1)," % of ", Base)
  #Step 3.2 Calculates dinucleotide composition
  #Initializes a dictionary for all 16 potential dinucleotides
  diNucl_freq={}#Hash storing observed dinucleotide frecuencies
  for Base1 in ["A","C","G","T"]:
    for Base2 in ["A","C","G","T"]:
      diNucl_freq[Base1+Base2]=0
  #Counts dinucleotides
  ### We count overlapping dinucleotides
  for Position in list(range(len(Sequence)-1)):
    subSeq=Sequence[Position:Position+2]
    diNucl_freq[subSeq]=diNucl_freq[subSeq]+1
  #Prints dinucleotide composition
  print ("### Dinucleotide composition ###")
  for diNucl in diNucl_freq.keys():
  #for diNucl in sorted(diNucl_freq.keys()):##uncomment if you want a sorted list
    print ("\t",round((diNucl_freq[diNucl]/(len(Sequence)-1))*100,1)," % of ", diNucl)
  #Step 4. search for restriction sites
  REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC", "HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
  for Enz in REnz.keys():
    if REnz[Enz] in Sequence:
      print("The enzyme ",Enz," cuts the sequence at position(s): ",end="")
      End_of_Seq=False#initializes sentinel###to know when exit "while" loop
      Position=0#This variable indicates the index where to search from
      while not(End_of_Seq):
        print(Sequence.find(REnz[Enz],Position)+1,", ",end="")#para tener como base primera el +1
        Position=(Sequence.find(REnz[Enz],Position))+1
        if Sequence.find(REnz[Enz],Position)<0:
          End_of_Seq=True###you could have used Break instead
    else:
      print("Sequence does not contain restriction sites for ",Enz)
    print()
      
    
    
