#! /usr/bin/python3 
# HPBBM, Unit 4, Times Table v1

x=95946
y=list (range(100000))
for z in y:
  out=str(x)+" x "+str(z)+" = "
  print (out, x**z)
print ("End")
