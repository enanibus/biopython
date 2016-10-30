DNA=input("Enter your DNA sequence ").upper() #Secuencia de DNA introducida por el usuario, en mayúsculas.
NucPercent={"Adenine":DNA.count("A")*100/len(DNA),"Guanine":DNA.count("G")*100/len(DNA),"Thymine":DNA.count("T")*100/len(DNA),
"Cytosine":DNA.count("C")*100/len(DNA)} #Diccionario con el porcentaje de cada nucleótido en la secuencia de DNA.
print()
print("Percentage of A =",round((NucPercent["Adenine"]),3),"%") #Output que informa al usuario sobre la composición nucleotídica de su secuencia de DNA.
print("Percentage of G =",round((NucPercent["Guanine"]),3),"%")
print("Percentage of T =",round((NucPercent["Thymine"]),3),"%")
print("Percentage of C =",round((NucPercent["Cytosine"]),3),"%")
print()

Enz=input("Enter the name of your enzyme (EcoRI, BamHI, HindIII or NotI) ") #Enzima de restricción seleccionada por el usuario.
REsites={"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT","NotI":"GCGGCCGC"} #Diccionario con cuatro dianas de restricción y sus respectivas enzimas.
Digestion=REsites[Enz] in DNA #Indica si la diana de restricción de la enzima introducida se encuentra en la secuencia de DNA.
print()
Digestion==True and print("Your DNA will be digested by", Enz) or Digestion==False and print("Your DNA will not be digested by", Enz)
#Dos outputs excluyentes que indican al usuario si el DNA será digerido por la enzima de restricción.

Position=DNA.index(REsites[Enz])+1 #Posición de la diana de restricción en la secuencia de DNA.
Digestion==True and print("The cutting site for",Enz,"starts at the nucleotide +"+str(Position),"of your sequence.")
#Output que informa sobre la posición en el DNA del sitio de corte para la enzima de restricción.
