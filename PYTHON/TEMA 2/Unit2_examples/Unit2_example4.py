#! /usr/bin/python3 
# HPBBM, Unit 4, example 4

x=input("Enter a number: ")
y=int(x)
if y < 0 :
  print ("First Condition true")
  print ("It is negative")
elif y > 0:
  print ("Second condition true")
  print ("It is positive")
else:
  print ("1st and 2nd conditions false")
  print ("It is zero")
print ("End") 