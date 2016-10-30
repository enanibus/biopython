
MyDNA=input('Type a DNA secuence and then press enter')
l=len(MyDNA)    #Número de nucleotidos  en la secuencia MyDNA insertada
'print(l)'
nºA=MyDNA.count('A')  ##Número de cada base en la secuencia
'print(nºA)'
nºC=MyDNA.count('C')
'print(nºC)'
nºG=MyDNA.count('G')
'print(nºG)'
nºT=MyDNA.count('T')
'print(nºT)'
NA=nºA/l*100       ## % de nucleótidos en la secuencia
print("%A" , NA)
NC=nºC/l*100
print("%C" , NC)
NG=nºG/l*100
print("%G" , NG)
NT=nºT/l*100
print("%T" , NT)

REnz={'EcoRI':'GAATTC','BamHI':'GGATCC','HindIII':'AAGCTT','NotI':'GCGGCCGC'}
Myenzyme="any restriction enzime"
while(Myenzyme!='') :
    Myenzyme=input('Type a restriction enzyme and then press enter  or only press enter to exit')
    if Myenzyme in REnz :

        CutEnz=REnz[Myenzyme] in MyDNA
        print('DNA sequence will be digested', CutEnz)
        if REnz[Myenzyme] in MyDNA :
            t=(MyDNA.find(REnz[Myenzyme]))
            print('The enzyme will  cut in the position', t)

    else:
        print('This enzyme is not contempled')
        
###Generamos un bucle de manera que:
        #Si introducimos el nombre de una enzima contemplada en el diccionario: Nos dirá si corta y en que  posicion
        #Si introducimos el nombre de una enzima NO contemplada en el diccionario: Nos avisará de que  no esta contemplada en nuestro diccionario
        #Si pulsamos solamente 'Enter' cerrará el programa 

