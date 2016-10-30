

MyFile=open('Human_HRAS.fasta.txt','r') #abrimos el archivo
DNA=""
for Line in MyFile: # usamos "for" para hacer un loop y leer linea por linea del archivo
 Line=MyFile.readline().strip()
 DNA=DNA+Line
 print(Line)
 
MyFile.close() # usamos este método para terminar la conexión con el archivo


MyFile=open('GeneticCode_standard.csv','r')
codigo_genetico={}
for Line in MyFile:
 codigo_genetico[Line[1:4]]=Line[5:6] 
 'print(Line)'

MyFile.close()
'print(codigo_genetico)'

MyFile=open('salida.txt','w')

longitud=len(DNA)


print(DNA, " secuencia de DNA empezando por la izquierda")

for Desplazamiento in range (0,3) : #hacemos un bucle para que nos vaya cogiendo letras de 3 en 3 

    inicial= Desplazamiento
    final= inicial+3
    
    secuencia_aa="" # para que haya separacion entre tripletes
    while final<=longitud:
        secuencia_aa=secuencia_aa+codigo_genetico[DNA[inicial:final]] + " "
    
    
        inicial=inicial+3
        final=final+3
    print(secuencia_aa, "  fase de triplete empezando por la izquierda desplazado ", Desplazamiento)

    MyFile.write ("secuencia_aa") # utilizamos este método para guardar las secuencias que nos interesa en un archivo de texto aparte
        
DNA_reverso=DNA[::-1] # de esta forma hacemos que el programa lea de derecha a izquierda
DNA=DNA_reverso
print(DNA, " secuencia de DNA empezando por la derecha")

for Desplazamiento in range (0,3) : #hacemos un bucle para que nos vaya cogiendo letras de 3 en 3 

    inicial= Desplazamiento
    final= inicial+3
    
    secuencia_aa="" # para que haya separacion entre tripletes
    while final<=longitud:
        secuencia_aa=secuencia_aa+codigo_genetico[DNA[inicial:final]] + " " 
        inicial=inicial+3
        final=final+3
    print(secuencia_aa, "  fase de triplete empezando por la derecha desplazado ", Desplazamiento)

    MyFile.write (secuencia_aa)
        
MyFile.close()

