#! /usr/bin/python3 
# HPBBM, Unit 4, Times Table v3
x=[0,1,2,3,4,5,6,7,8,9,10]
y=[0,1,2,3,4,5,6,7,8,9,10]
for z in x:
  print (z," Times Table")
  for k in y:
    out=str(z)+" x "+str(k)+" = "
    print (out,z*k)
print ("End")