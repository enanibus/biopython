###My Group: Group 4 (Maria Baena, Diego Calzada y Alfonso Cordero)

##The program requires the user to run it in the terminal, call it with python3 and give as an input the sequence to be alayzed

#Function 1: Opening the fasta sequence
def opensequence_Fasta(MyFile):
    File=open(MyFile,"r")  #Object to connect with the file
    Sequence=''
    for Line in File:
        if not('>' in Line): #To introduce only the sequence in the program
            Line=Line.upper().strip() #If the fasta sequence is not in capitals
            Sequence=Sequence+Line#We save the sequence
        else:
            name=Line
            accesion_number=re.compile(r"[NX]M_[0-9]+.[0-9]")
            fastaname="".join(accesion_number.findall(Line))
    print(name)#Telling which fasta name the program is working with
    File.close() #Terminate connection with the file
    return(name,Sequence,fastaname)#The function returns the fasta sequence


#Function 2: Opening the genetic code and saving it to a dictionary
def openAAdiccionary(AAdiccionary):
#Reading the genetic code from the input file, adding to dictionary
    File_code=open(AAdiccionary,'r')  #Object to connect with the file
    GenCode={} #We define the genetic code by adding codon by codon
    for Line in File_code:
        codon=re.compile(r"[TGCA]{3}")#Regular expression with codon's pattern
        MyFields0=codon.findall(Line)
        aa=re.compile(r"\t[A-Z*]\t")#Regular expression to get the amino acid letter as it is between \t in the 'Line' variable   
        MyFields1="".join(aa.findall(Line)).replace("\t","")
        GenCode["".join(MyFields0)]=MyFields1
    File_code.close() #Terminate connection with the file
    return (GenCode)
    

#Function 3: Getting the complementary sequence (not in 5’->3’)
def ComplementSequence(Sequence):
    Complement='' #We create the variable that will contain the complementary sequence
    Complement_dicc={'A':'T','C':'G','G':'C','T':'A'}#Dictionary of complementary bases
    for n in (Sequence):
        Complement=Complement+Complement_dicc.get(n) #For each sequence position we add the corresponding complementary base contained in the dictionary
    return (Complement)#The function returns the complementary sequence

#Function 4: Create the ORFs
def createORFs(seq):
    ORFs=[]#We create a tupla which contains the 3 ORFs
    for k in range(0,3):
        i=k
        ORF=[] #Create the ORF element
        while i+2<len(seq): #For groups of trinucleotides, if there are less than 2 nucleotides after the one considered it is the end of the protein
            triplet=seq[i:i+3] #Assign the amino acid name from the dictionary corresponding to the codon evaluated
            ORF.append(triplet)#Adds each triplet to the list
            i=i+3 #Evaluate the next codon
        ORFs.append(ORF) #Once we've calculated the ORF, we save it in a diccionary
    return (ORFs)#The function returns the three reading frames of the DNA

#Function 5: Translating the ORFs
def translateORF(aadictionary,ORFsequence):
    Proteins=[]#We define the protein dictionary
    for h in ORFsequence:#We use the 3 list in the ORF
        protein=[]#We create a list wich contains the traslation of each aa 
        for n in h:#Translating each codon
            protein.append(aadictionary.get(n))#Translate every nucleotide triple in an aminoacid
        Proteins.append("".join(protein))#We add every reading frame to the variable
    return(Proteins)#The function give us the three reading frames from the protein

        

#Funcion 6: Saving into a file
def savingintoafile(secuence,reverse,PDirect,Preverse,access,nombre):
    if access=="":#In case the sequence does not have an accession number
        Text="".join(re.compile(r"..\|[1-9]+").findall(nombre)).replace("|",";")#my sistema operativo inferior no me deja guardar cosas con | por eso las cambio por :
        MyFile2=open(str(Text)+".txt",'w')
        print("Printing your work in",Text,".txt\n")
    else:#For the case it does
        MyFile2=open(str(access)+".txt",'w')
        print("Printing your work in",access,".txt\n")
        MyFile2.write("Your access number is: "+str(access)+"\n""\n")
    MyFile2.write('Sequence analysis:\n\n')
    MyFile2.write(">Sequence:\n")
    MyFile2.write(secuence+"\n")#It prints the sequence
    MyFile2.write("\n")
    MyFile2.write(">Complementary sequence:\n")
    MyFile2.write(reverse+"\n\n")#It prints the reverse complementary sequence
    for p in (PDirect,Preverse):#It creates a loop to write the 6 posible proteins
        if p==PDirect:#Condicionals to name the 3 ORFS from the direct and reverse sequence and the genetic code used
            MyFile2.write( "> protein direct:\n\n")
        elif p==Preverse:
            MyFile2.write("> protein reverse:\n\n")
        t=1
        for h in (p):#The loop prints the 3 ORFs
            MyFile2.write(">ORF"+str(t)+":\n")
            MyFile2.write(str(h)+"\n\n")
            t=t+1
    MyFile2.close()#We close the open file

#Function 7: Main, compute all
def main():
    Name,Sequence,Accession_Number=opensequence_Fasta(sys.argv[1]) #Getting information from indicated file
    GenCode=openAAdiccionary("GeneticCode_standard.csv") #Defining the genetic code
    complement=ComplementSequence(Sequence)#It calculates the complementary sequence
    rcSeq=complement[::-1]#It computes the inverse to the complementary sequence (5'-3')
    ORF_sequence=createORFs(Sequence)
    ORF_rcSeq=createORFs(rcSeq)#Compute ORFs for each
    Proteins_direct=translateORF(GenCode,ORF_sequence)
    Proteins_reverse=translateORF(GenCode,ORF_rcSeq)#Get protein sequences
    savingintoafile(Sequence,rcSeq,Proteins_direct,Proteins_reverse,Accession_Number,Name)#Invokes a function so as to save data to a file

import sys#So as to use input arguments
import re#So as to use regular expressions
main()


