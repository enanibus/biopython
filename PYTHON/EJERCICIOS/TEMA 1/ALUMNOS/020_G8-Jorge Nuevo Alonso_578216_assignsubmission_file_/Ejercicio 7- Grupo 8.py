#Grupo8: Álvaro Alfayate, Andrea de la Fuente, Carla Guillén y Jorge Nuevo

#Diccionario de Enzimas de Restricción: Asocia la secuencia de corte de cada enzima al nombre de la misma.
REnz={'EcoRI':'GAATTC','BamHI':'GGATCC', 'HindIII':'AAGCTT','NotI':'GCGGCCGC'}

#Input: Pedimos al usuario que introduzca la secuencia de DNA que vamos a analizar con el programa.
DNA=input('Introduce your DNA/RNA sequence ')  #DNA será la variable que contenga la secuencia a analizar.
DNA=DNA.upper() #Por si algún científico decide meter algo en minúsculas...
DNA=DNA.replace('U','T') #Por si deciden meter un RNA, que se transforme y lo cuente igual como si fuera un DNA
#En estos dos pasos, asignamos de nuevo la variable DNA a la modificación. DNA continúa siendo nuestra secuencia a analizar.

#Composition of the DNA sequence (% of each base)
print('A percentage'+' '+str(round(DNA.count('A')/len(DNA)*100,2))+'%')
print('T percentage'+' '+str(round(DNA.count('T')/len(DNA)*100,2))+'%')
print('C percentage'+' '+str(round(DNA.count('C')/len(DNA)*100,2))+'%')
print('G percentage'+' '+str(round(DNA.count('G')/len(DNA)*100,2))+'%')

Enz=input('Introduce Restriction Enzime ') #Enz será la variable correspondiente a nuestra enzima de restricción

#Indicate if the DNA sequence will be digested by the selected enzyme. Indicate the (first) cutting position of the selected restriction enzyme, if applicable.
REnz[Enz] in DNA and print('Your DNA sequence can be cut by '+Enz+'\nFirst nucleotide of the cutting sequence: +'+str((DNA.find(REnz[Enz])+1))) #Si se puede cortar.
#Sumamos +1 para que la posición indicada corresponda al número de nucleótido y no al número de posición de Python (Que empieza por 0)
not(REnz[Enz] in DNA) and print('Your DNA sequence can\'t be cut by '+Enz) #Si no se puede cortar



