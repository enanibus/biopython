#! /usr/bin/python3 
# HPBBM, Unit 3, example 1: reading line by line

# returns a file-object (stored inMyFile) that you can use to access the file.
MyFile=open("aa_frequencies_v2.csv",'r')

# Uses a "while" loop to go over each line in the file
EoF=False ##boolean variable "End of File"
while not(EoF):
  Line=MyFile.readline().strip()
  if Line=='':
    EoF=True
  else:
    print(Line)
# Close the file-object to terminate connection with the file
MyFile.close()
