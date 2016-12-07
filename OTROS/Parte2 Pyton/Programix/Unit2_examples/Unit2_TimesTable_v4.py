#! /usr/bin/python3 
# HPBBM, Unit 4, Times Table v4

z=-1
y=range(10)
while z<10:
  z=z+1
  print (z," Times Table")
  q=input('Press "e" to exit, "s" to skip this number and any other key to continue. ')
  if q=="e":
    break
  elif q=="s":
    continue
  for k in y:
    out=str(z)+" x "+str(k)+" = "
    print (out,z*k)
print ("End")