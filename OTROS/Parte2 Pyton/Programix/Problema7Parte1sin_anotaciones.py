###Ejercicio_7_Python_parte_1. Juan Escudero
SEC=input('Type the selected sequence: ')
A_fr=(SEC.count('A')/len(SEC))*100
C_fr=(SEC.count('C')/len(SEC))*100
G_fr=(SEC.count('G')/len(SEC))*100
T_fr=(SEC.count('T')/len(SEC))*100
print('%G')
print(round (G_fr, 2))
print('%C')
print(round (C_fr, 2))
print('%A')
print(round (A_fr, 2))
print('%T')
print(round (T_fr, 2))
REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC",
"HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
ENZYME=input('Type the selected enzyme: ')
print ('Cleavage by selected enzyme:')
print(REnz[ENZYME] in SEC)
print ('Position of first cleavage site:')
print (SEC.find(REnz[ENZYME]))
