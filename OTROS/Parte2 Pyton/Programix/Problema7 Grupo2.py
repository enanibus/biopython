###Ejercicio_7_Python_parte_1. Juan Escudero
SEC=input('Type the selected sequence: ')
SEC.count('A')
len(SEC)
A_fr=(SEC.count('A')/len(SEC))*100
C_fr=(SEC.count('C')/len(SEC))*100
G_fr=(SEC.count('G')/len(SEC))*100
T_fr=(SEC.count('T')/len(SEC))*100
print('%G')
print(G_fr)
print('%C')
print(C_fr)
print('%A')
print(A_fr)
print('%T')
print(T_fr)
REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC",
"HindIII":"AAGCTT", "NotI":"GCGGCCGC"}
ENZYME=input('Type the selected enzyme: ')
print ('Cleavage by selected enzyme:')
print(REnz[ENZYME] in SEC)
print ('Position of first cleavage site:')
print (SEC.find(REnz[ENZYME]))
