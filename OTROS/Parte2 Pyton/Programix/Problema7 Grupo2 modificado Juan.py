###Ejercicio_7_Python_parte_1. Juan Escudero
#Indico que se introduzca la secuencia, ese string sera asignado a la variable SECUENCIA
SEC=input('Type the selected sequence: ')
#obtener el % de cada nucleotido, numero de N entre total de nucleotidos
A_fr=(SEC.count('A')/len(SEC))*100
C_fr=(SEC.count('C')/len(SEC))*100
G_fr=(SEC.count('G')/len(SEC))*100
T_fr=(SEC.count('T')/len(SEC))*100
#ordeno que imprima los valores obtenidos redondeados debajo de cada identificador (otra manera?)
print('%G')
print(round (G_fr, 2))
print('%C')
print(round (C_fr, 2))
print('%A')
print(round (A_fr, 2))
print('%T')
print(round (T_fr, 2))
#Defino el diccionario de RE.
REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC",
"HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
#Indico que se introduzca la enzima, ese string sera asignado a la variable ENZYME
ENZYME=input('Type the selected enzyme: ')
#introduzco la enzima, tiene que ser una de las que esta en el diccionario.
#Refiero la enzima introducida al hash, ahora la enzima introducida se refiere a unapequena sec de nu
#Sera el DNA digerido por la enzima? imprimo la solucion
print ('Cleavage by selected enzyme:')
print(REnz[ENZYME] in SEC)
#busca la primera posicion de corte imprimo la solucion
print ('Position of first cleavage site:')
print (SEC.find(REnz[ENZYME]))
