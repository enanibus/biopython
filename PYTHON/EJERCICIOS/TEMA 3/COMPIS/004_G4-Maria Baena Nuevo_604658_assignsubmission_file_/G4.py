###My Group: Group 4 (Maria Baena, Diego Calzada y Alfonso Cordero)

##1. Reading the file "Human_HRAS.fasta" and extracting the DAN sequence

File=open("Human_HRAS.fasta.txt",'r')  #Object to connect with the file
Sequence=[]
for Line in File:
    if not('>' in Line):#To introduce only the sequence in the program
        Line=Line.upper().strip()#if the fasta sequence is not in capitals
        Line=Line.replace("U","T")#if the fasta sequence contains RNA
        Sequence=Sequence+[Line]
    else:
        name=Line
HRAS="".join(Sequence)#This way HRAS is all the sequence without gaps
print(name.strip(),":")
print(HRAS,'\n')
File.close() #Terminate connection with the file

##2 Reading the genetic code from "GeneticCode_standard.csv, adding to dictionary
File_code=open("GeneticCode_standard.csv",'r')  #Object to connect with the file
GenCode={}#We define the genetic code by adding codon by codon
for Line in File_code:
    Line=Line.strip()
    MyFields=Line.split('\t') #For each step MyFileds becomes a list of the codon and amino acid name
    AminoAcidName=MyFields[1] #The position 1 of the list corresponds to the amino acid name
    GenCode[MyFields[0]]=AminoAcidName #Assign the name to a codon in the dictionary
File_code.close() #Terminate connection with the file

##3. Translatethe DNA into the six ORFs

#Create the complementary secuence
rcSeq='' #We create the variable that will contain the complementary sequence
Complement={'A':'T','C':'G','G':'C','T':'A'}#Dictionary of complementary bases
print('Complementary Sequence of HRAS in 3->5:')

for n in (HRAS):
    rcSeq=rcSeq+Complement.get(n) #For each HRAS position we add the corresponding complementary base contained in the dictionary
print(rcSeq)
print("\n")

##Creating the ORFs
ORFs={} #A dictionary will contain the ORFs
for k in range(0,6):
    if k<3: #For the sequence
        seq=HRAS
        i=k
    else: #For the complementary sequence
        seq=rcSeq[::-1]#Revert the complementary sequence from 3-5' to 5'-3', direction in which it will be read for translation
        i=k-3
        
    ORF="" #Create the ORF element
    while i+2<len(seq): #For groups of trinucleotides, if there are less than 2 nucleotides after the one considered it is the end of the protein
        aminoacid=GenCode[seq[i:i+3]] #Assign the amino acid name from the dictionary corresponding to the codon evaluated
        ORF=ORF+aminoacid
        i=i+3 #Evaluate the next codon
        
    ORFs["ORF"+str(k+1)]=ORF #Once we calculate the ORF, we save it in a diccionary
    print('ORF',k+1,': ')
    print(ORF,'\n')

##4. Saving translation to a text file
print("Printing your work in a text called 'SavingFile.txt'...\n")
MyFile=open('SavingFile.txt','w')#Create a file called "SavingFile.txt"
MyFile.write(name)
MyFile.write('Sequence analysis:\n\n')#write in the text the fasta sequences
MyFile.write(">Sequence:\n")
MyFile.write(HRAS+"\n")
MyFile.write("\n")    
MyFile.write(">Complementary Strand(5'->3'):\n")
MyFile.write(rcSeq[::-1]+"\n")
MyFile.write("\n")
        
for g in range(1,7):#It writes the ORF in the txt. 
    MyFile.write('ORF'+str(g)+"\n")
    MyFile.write(ORFs["ORF"+str(g)]+'\n')
    MyFile.write('\n')
    
MyFile.close()
#cheking if the programms are closed
print("Checking if the files are closed...")
if File.closed and File_code.closed and MyFile.closed==True:
    print("\tThe files are closed correctly\n")
else:
    print("\tThe files are not closed correcly\n")
#Final question for keep the programm open
Exit=input("Press enter to finish the programm")
exit()
