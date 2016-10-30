# Problema 7, grupo 7

DNA=input("Introduzca su secuencia de DNA:")

Enzima=input("Introduzca su enzima de restriccion:")

numeroA=DNA.upper().count("A") #Contaje del numero de cada acido nucleico en la secuencia de DNA
numeroC=DNA.upper().count("C")
numeroG=DNA.upper().count("G")
numeroT=DNA.upper().count("T")
porcentajeA=(numeroA/(numeroA+numeroC+numeroG+numeroT))*100 #Calculo del porcentaje de cada acido nucleico en la secuencia de DNA
porcentajeC=(numeroC/(numeroA+numeroC+numeroG+numeroT))*100
porcentajeG=(numeroG/(numeroA+numeroC+numeroG+numeroT))*100
porcentajeT=(numeroT/(numeroA+numeroC+numeroG+numeroT))*100
print("%A:")
print(porcentajeA)
print("%C:")
print(porcentajeC)
print("%G:")
print(porcentajeG)
print("%T:")
print(porcentajeT)

EnzimaRestriccion={"EcoRI":"GAATTC", "BamHI":"GGATCC", "HindIII":"AAGCTT", "NotI":"GCGGCCGC"} #Diccionario con el nombre de las enzimas de restriccion y sus secuencias de corte
print("¿Sera digerida esta secuencia de DNA por dicha enzima?:")
print(EnzimaRestriccion [Enzima] in DNA) #Busqueda en la secuencia de DNA de las secuencias de corte de las enzimas de restriccion

if (EnzimaRestriccion [Enzima] in DNA): #Solo te da el punto de corte cuando la secuencia de DNA es digerida por la enzima de restriccion
    print("Primer punto de corte de la enzima de restriccion:")
    print(DNA.find(EnzimaRestriccion[Enzima])) #Busqueda del punto de corte de la enzima de restriccion en la secuencia de DNA


