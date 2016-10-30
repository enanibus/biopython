#Group 5: Daniel Díaz, Rubén Gómez-Gordo, Alicia Roig


Seq="" #Definimos una variable vacía que almacenará la secuencia de DNA contenida en el fichero.
rcSeq="" #Variable que almacenará la secuencia de la cadena (-) de DNA.
GenCode={} #Diccionario que contendrá cada codón como 'key' y el aminoácido codificado como 'value'.
Complementary={"A":"T","T":"A","C":"G","G":"C"} #Diccionario que contiene cada base asociada a su base complementaria.


#1. Lectura del fichero “Human_HRAS.fasta” y extracción de la secuencia de DNA contenida en él.

MyFile1=open("Human_HRAS.fasta.txt","r") #Abrimos para lectura un fichero que contiene una secuencia de DNA en formato FASTA.
for Line in MyFile1: #Este bucle irá leyendo cada línea del fichero.
  if not ">" in Line: #Con este condicional aseguramos que la línea de cabecera no se incluya en la secuencia. 
    Seq+=Line.strip() #Todas las líneas con secuencia de DNA van a quedar guardadas de manera concatenada dentro de la variable 'Seq'.
MyFile1.close() #Cerramos el fichero.


#2. Lectura del código genético del fichero “GeneticCode_standard.csv”.

MyFile2=open("GeneticCode_standard.csv","r") #Abrimos para lectura el fichero que contiene el código genético.
for Line in MyFile2: #Este bucle irá leyendo cada línea del fichero.
  Line=Line.strip().split("\t") #Convertimos cada línea en una lista con 3 elementos: codón, aa (1 letra), aa (3 letras).
  GenCode[Line[0]]=Line[1] #Guardamos en el diccionario cada codón como "key", y cada aminoácido como "value".
MyFile2.close() #Cerramos el fichero.


#3. Traducción de la secuencia de DNA a proteína, en las 6 posibles pautas de lectura (3 por cadena) y escritura de todas las traducciones en un único fichero.

for Nuc in Seq[::-1]: #Este bucle va a pasar por todos los nucleótidos de la cadena (+) de DNA en sentido 3' -> 5'...
  rcSeq+=Complementary[Nuc] #...y se van a introducir uno a uno los nucleótidos complementarios, obteniendo la cadena (-) de DNA.

MyFile3=open("Protein.txt","w") #Abrimos para escritura un fichero en el que introduciremos los datos de las secuencias proteicas obtenidas.
for Strand in [Seq,rcSeq]: #Primer bucle: el programa pasará por la cadena (+) de DNA y después por la cadena (-).
  for Frame in [0,1,2]: #Segundo bucle: el programa pasará por las 3 posibles pautas de lectura: n=0, n=+1 y n=+2.
    Protein="" #Definimos una variable vacía que almacenará la secuencia de proteína cada vez que el DNA sea traducido.
    for Position in range(Frame,len(Strand),3): #Tercer bucle: el programa avanzará 3 nucleótidos a la derecha cada vez. El origen dependerá de la pauta de lectura.
      CurrentCodon=Strand[Position:Position+3] #Definimos la subsecuencia de 3 nucleótidos equivalente a un codón, que dependerá de los bucles anteriores.
      if len(CurrentCodon)==3: #Con este condicional evitamos que el programa falle al llegar al final, cuando quedan 1 o 2 nucleótidos fuera de la pauta de lectura.
        Protein+=GenCode[CurrentCodon] #Traduce codón a codón y obtiene la secuencia de proteína, almacenándola en su correspondiente variable.
    MyFile3.write(Protein+"\n\n") #Introducimos cada secuencia de proteína en el fichero.
MyFile3.close() #Finalmente cerramos el fichero.



    
