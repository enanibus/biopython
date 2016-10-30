###MyGroup_Group 6 (Alejandro Asensio, Marina Gonzalo, MªJose Jimenez y Jaime Quesada)
## ASSIGNMENT 5

##INSTRUCTIONS:
#1-Open the terminal and go to python (or python3).
#2-In the command line, write the name of this file first and then the name of the file that you want to read.
#3-Press enter and the result of the translation will be saved in a document with the accession number of the translated protein as title. 


def GetSequenceandAccessionNumber(File):  #We define a new function, indicating what it does (when going to help)
    """Reads the FileName given and returns two strings: 
        DNA_Seq: Contains DNA sequence
        My_Accession_number: Contains the accession number
    """
    
    DNA_Seq=""
    import re
    MyRE_AccNum = r'[NX]M_(\d+).(\d+)'
    MyAccNum = re.compile(MyRE_AccNum)
    #Regular expression to search the accession number in FileName
    
    FileName = open(File, "r")
    for Line in FileName:
        if '>' in Line:
            My_AccNum = MyAccNum.search(Line)
            My_Accession_Number = My_AccNum.group()
            #Searchs the regular expression in first line of FASTA file and assigns the expression to My_Accession_Number variable
        else:
            DNA_Seq=DNA_Seq+ Line.strip()
            #Assigns all DNA sequence to DNA variable
    FileName.close()
    return(DNA_Seq, My_Accession_Number)

def ReadGeneticCode(): #We define a new function, indicating what it does (when going to help)
    """Reads GeneticCode_standard.csv file and returns a diccionary 
    whose keys are codons and its associated values are the aa encoded 
    by them (one-letter notation).
    """
    
    aa_dic_Triplet_and_Letter = {}
    import re
    MyRE_Codon = r'[ATGC]{3}'
    MyCodon = re.compile(MyRE_Codon)
    MyRE_aa = r'[ARNDCQEGHILKMFPSTWYV*]'
    Myaa = re.compile(MyRE_aa)

    Code = open("GeneticCode_standard.csv", "r")
    for Line in Code:
         ##Searchs the codon and the aa (one-letter notation) in each line and creates a dictionay whose keys are the codons and whose values are the aa 
         My_Codon = MyCodon.search(Line)
         My_aa = Myaa.search(Line,My_Codon.end())
         aa_dic_Triplet_and_Letter[My_Codon.group()] = My_aa.group()   
    Code.close()
    return(aa_dic_Triplet_and_Letter)
    
def ReverseComplement(dna): #We define a new function, indicating what it does (when going to help)
    """Returns the reverse complement sequence
    """
    
    Base_Pairs = {"A":"T", "T":"A", "C":"G", "G":"C"}
    dnarc = ""
    for nucleotide in dna[::-1]:
        dnarc = dnarc + Base_Pairs[nucleotide]
    return(dnarc)

def Frames (dna, dnarc): #We define a new function, indicating what it does (when going to help)
    """Creates a list with the six reading frames
    """
    
    List_of_Frames = []
    for number in range(0,6):
        if number <= 2:
            Frame = dna[number:]
            List_of_Frames.append(Frame)
        elif number <= 5:
            Frame = dnarc[number-3:]
            List_of_Frames.append(Frame)
    return(List_of_Frames)

def Translation (List_of_Frames, aa_dic_Triplet_and_Letter): #We define a new function, indicating what it does (when going to help)
    """Takes the list with the six reading frames and the dictionary where 
    the codon:aa equivalences are store and translates each frame. The result 
    is stored in Protein_dictionary_Letter dictionary and returned)
    """
    
    n = 0
    aa_Letter = []
    codon = ""
    Protein_dictionary_Letter = {1:"", 2:"", 3:"", 4:"", 5:"", 6:""}
    for frame in List_of_Frames:
        n = n+1
        while len(frame) >= 3:
            codon = ""
            codon = frame[0:3]
            frame = frame.split(codon, 1) [1]
            aa_Letter.append(aa_dic_Triplet_and_Letter[codon])
        if len(frame) < 3:
            aa_Letter = "".join(aa_Letter)
            Protein_dictionary_Letter[n] = aa_Letter
            aa_Letter = []
        for element in aa_dic_Triplet_and_Letter: 
            if aa_dic_Triplet_and_Letter[element] == "": 
                aa_dic_Triplet_and_Letter[element] = "NO ORF FOUND"
    return(Protein_dictionary_Letter)

def TranslationFile(My_Accession_Number, Protein_dictionary_Letter): #We define a new function, indicating what it does (when going to help)
    """Creates a new text file whose name is the accession number
    """
    
    File_Name = open(My_Accession_Number + ".txt", "w")
    
    File_Name.write("These are the six possible proteins encoded by your DNA sequence (Standard Genetic Code): \n \n")
    
    for s in range(0,6):
        
        if s <= 2:
            File_Name.write("5'3'Frame " + str(s+1) + ":\n \n\t" + Protein_dictionary_Letter[s+1] + "\n \n")
        elif s <= 5:
            File_Name.write("3'5'Frame " + str(s-2) + ":\n \n\t" + Protein_dictionary_Letter[s+1] + "\n \n")
    File_Name.close()

    
    
    
import sys
DNA, Accession_Number = GetSequenceandAccessionNumber(sys.argv[1])
### Double assignation: DNA = first object returned by GetSequenceandAccessionNumber and Accession number = second object
GeneCodeDictionary = ReadGeneticCode()
DNArc = ReverseComplement(DNA)
Frames =  Frames (DNA, DNArc)
Proteins = Translation (Frames, GeneCodeDictionary)
TranslationFile(Accession_Number, Proteins)
