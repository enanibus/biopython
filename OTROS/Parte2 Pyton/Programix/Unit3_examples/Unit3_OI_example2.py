#! /usr/bin/python3 
# HPBBM, Unit 3, example 2: reading line by line

# returns a file-object (stored inMyFile) that you can use to access the file.
MyFile=open("aa_frequencies_v2.csv",'r')

# Uses a "for" loop to go over each line in the file
for Line in MyFile:
  print(Line)
# Close the file-object to terminate connection with the file
MyFile.close()