#! usr/bin/python
# Exercise Unit 1
# Luis del Peso, sep 2016

# The program ask the user to enter a DNA sequence and restriction enzyme (only works with selected enzymes) via standard input and returns sequence stats, and whether the enzyme cuts and position

### In the code below I used “#” for regular comments (those you would include to make your code readable) and “###” for comments intended just for you as students of this course.
# REnz is a dictionary of restriction enzymes sites. key= enzyme name, value=restriction site sequence.
REnz={"ECORI":"GAATTC", "BAMHI":"GGATCC", "HINDIII":"AAGCTT", "NOTI":"GCGGCCGC"}### Note that I use capital letters for the keys, then I can transform user's input and employ it as key in line 35

#user input
DNA=input("Please enter a DNA sequence: ")
### Note that we could generate a new variable containin the capitalized form of DNA, e.g. uDNA=DNA.upper(). This way we won't have to keep repeating "DNA.upper()" below.

#calculates and prints sequence stats
print ("Sequence statistics")
print ("\t Percent A: ",end="") ###Note that using end="", we overide the default behavior of adding new line in print
tmp=round((DNA.upper().count('A')/len(DNA))*100,1)###Note that we perform several calculations in a single line.
print (tmp)
print ("\t Percent C: ",end="")###Note the use of "\t", "\" is a escape code that tells python to interpret the following character as "special". In this case the "t" is undestood as "tab"
tmp=round((DNA.upper().count('C')/len(DNA))*100,1)###Note that we re-use this variable, this way we save memory and keep code clean
print (tmp)
print ("\t Percent G: ",end="")
tmp=round((DNA.upper().count('G')/len(DNA))*100,1)
print (tmp)
print ("\t Percent T: ",end="")
tmp=round((DNA.upper().count('T')/len(DNA))*100,1)
print (tmp)
### Of course we could have done:
### print ("\t Percent T: ",round((DNA.upper().count('T')/len(DNA))*100,1))
### However, the code becomes less readable

#user input
nR=input("Please enter an enzyme (EcoRI, BamHI, HindIII or NotI): ")###Note that if you do not enter some value, you'll get an error below, but there is no easy way to solve it without using conditionals or "try" (we'll see it soon)

#Is sequence digested?
print ("Is your DNA digested by the enzyme ",end="")
print (nR,end="")###Note that it prints the enzyme name as you entered it although we convert it to caps to use it as the dictionary key (line 39)
print (" ?")
print ((REnz[nR.upper()] in DNA.upper())) ###note that I included the comparison within the backets, this way I avoid creating a variable to store it

### A way to compress the above four lines into one:
### print ("Is your DNA digested by the enzyme ",nR," ?", ((REnz[nR.upper()] in DNA)))
### but again it gets a little hairy

#indicates cut site
print ("The enzyme cuts the DNA at position (-1 indicates no digestion): ",end="")
print (DNA.upper().find(REnz[nR.upper()]))


###############################
## More on formating strings ##
###############################
#There is a method to format strings in various ways
#See the documentation at:
#https://docs.python.org/2/library/string.html#format-string-syntax
#Example:
print("\n\nThis is an example of the use of .format() method")
print("\t Percent T: {0:.1f}".format(tmp))

