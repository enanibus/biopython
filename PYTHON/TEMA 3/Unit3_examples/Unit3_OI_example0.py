#! /usr/bin/python3 
# HPBBM, Unit 3, example 0: reading line by line

# create object to connect with the file
#MyFile=open("aa_frequencies_v1.txt",'r') 
MyFile=open("aa_frequencies_v2.txt",'r') # uncomment to activate
#MyFile=open("aa_frequencies_v2.csv",'r')  # uncomment to activate
MyData=MyFile.readlines() # import file content into MyData
print(MyData)
MyFile.close() # Close the file-object to terminate connection with the file
