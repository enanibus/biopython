
###My_group: Group 4 (Maria Baena, Diego Calzada and Alfonso Cordero)

##Asking whether the user wants to launch the program
print("Hello, I am Group 4's sequence analyzer:")
Start_Question=input("Do you want to analyze nucleotid acid secuence? (Yes or No):")
if(Start_Question.upper()=="NO"):
    print("See you soon")
    exit()

##Introducing the DNA sequence
while(Start_Question.upper()=="YES"):#This allow us to continue analyzing other sequences not having to restart the programme
    DNAsequence=input("Enter your DNA sequence and press enter: ")
    DNASequence=DNAsequence.upper()#Sequence in capitals

    ##Define sequences that are not nucleotides 
    alphabet=['B','D','E','F','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
    for z in alphabet:
        if z in DNASequence: #If found, it will shut down
            print('This program just admits DNA or RNA sequences')
            ext=input('PRESS ENTER TO EXIT')#Retain the exit upon pressing a button
            exit()

#Replace U for T in case there are
    if 'U' in DNASequence:
        DNASequence=DNASequence.replace('U','T')
        print('-The given sequence has some RNA characters, the corresponding DNA sequence will be considered: ',DNASequence)

        
   
    ##Calculating sequence statistics
    print("Sequence statistics:")
    print('')
    print("   Secuence length:",len(DNASequence))#Length
    print('')

    ##Calculating the base percentages
    print("   Nucleotide composition:")
    print("\t- The percentage of G is:",round(100*DNASequence.count("G")/len(DNASequence),2),"%")
    print("\t- The percentage of C is:",round(100*DNASequence.count("C")/len(DNASequence),2),"%")
    print("\t- The percentage of T is:",round(100*DNASequence.count("T")/len(DNASequence),2),"%")
    print("\t- The percentage of A is:",round(100*DNASequence.count("A")/len(DNASequence),2),"%")
    print('')
    
    ##Calculating the dinucleotide percentages
 
    print("   Dinucleotide composition:")
    Dinucleotide=["A","G","T","C"]
    for z in Dinucleotide:
        for h in Dinucleotide: ##Consider all dinucleotide combinations
            if z==h: ##For homonucleotides
                pair=round(100*DNASequence.count(z+h)/((len(DNASequence)-1)),2)
                unpair=round(100*DNASequence.replace(z+h,z+"F").count("F"+z)/((len(DNASequence)-1)),2)
                print("\t- The percentage of",z+h,"is",pair+unpair,"%")

                ##The function count() just takes each nucleotide into accoutn once, but if there are more than 3 consecutive equal nucleotides, most will belong to two dinucleotides.
                #In order to solve this we use count and then replace the second nt of each pair for another character, counting then as another dinucleotide the second+first of the next pair

            else:
                print("\t- The percentage of",z+h,"is",round(100*DNASequence.count(z+h)/((len(DNASequence)-1)),2),"%")##With different nucleotides the program can analyze all de dinucleotides directly

        print('')
    
    #Introducing the Restriction Enzymes
    REnz={"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT","NotI":"GCGGCCGC"}
    print("   Restrictión sites:")
    for Enz in REnz:##Calculating all the diferent restriction sites for all the enzymes
        print ("     -",Enz,"(",REnz[Enz],")")
        if (REnz[Enz] in DNASequence)== True:
            print("\t-The secuence has a/an ",Enz, " site")
            print("\t-The number of ",Enz," sites is:",DNASequence.count(REnz[Enz]))
            print("\t-The enzime cut the secuence in:")

            
            n=0
            i=-1
            #find() just finds the first site so we analyzie n times (as much as Enz sites) and each time starting find() upstream the last site found
            
            while(DNASequence.count(REnz[Enz])>n):
                print("\t   -",Enz," target site is in the position:",(DNASequence.find(REnz[Enz],i+1)+1)) #We consider the starting nucleotide to be position 1, not 0
                n=(n+1)
                i=DNASequence.find(REnz[Enz],i+1)  
        else:
            print("\t-The secuence has not a/an ",Enz, " site")
    print('')
    print('')

 ##Analyzing other sequences
    final_question=input("Do you want to analyse another sequence (Yes or No):")
    if final_question.upper()=="NO":
        print("See you later")
        break

