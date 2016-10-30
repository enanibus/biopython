#! /usr/bin/python3 
# HPBBM, Unit 3, example 3: writing to a file

# prompts for user inputs.
DNA=input("Enter a DNA sequence:\n")
SeqName=input("Enter a name for the sequence:\n")

# returns a file-object (stored inMyFile) to access the file.
MyFile=open(SeqName,'w')

# writes sequence to file in FASTA format
outString=">"+SeqName+"\n"+DNA+"\n"
MyFile.write(outString)#Note that, unlike print(), we need "\n"
# Close the file-object to terminate connection with the file
MyFile.close()