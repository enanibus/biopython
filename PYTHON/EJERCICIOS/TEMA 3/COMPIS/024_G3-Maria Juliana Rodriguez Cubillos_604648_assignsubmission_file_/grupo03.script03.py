# My_Group (Maria Juliana Rodriguez Cubillos,Patricia Palacios Ibáñez, Ioannis Rallis) 
# Se crea una variable tipo string vacía
Sequence = ""
# Se leen los archivos que contienen el DNA de interes, y el codigo de traduccion del mismo a proteína
file=open("Human_HRAS.fasta","r")
GeneCode=open("GeneticCode_standard.csv","r")

# Para el pimer archivo, se le asigna a la variable line, la lectura de cada una de las lineas del archivo, omitiendo los espacios que en ella pudieran existir
line=file.readline().strip()
# Se crea un bucle de tipo for para recorrer el archivo tipo fasta. Para todas las líneas del archivo, si el caracter ">" esta en la línea, no la tendrá en cuenta.
# De lo contrario, la linea que este siendo leida se incluirá dentro de la variable tipo string vacía creada con anticipación. Se creará una lista lineal tipo string.
for line in file:
    if ">" not in line:
        Sequence += line
        Seq = Sequence.replace("\n","")
# Se cierra el archivo del cual fue leida la secuencia
file.close()

# Crea una lista vacía
Code={}
# Se crea un bucle tipo for que recorre todas las líneas de la variable que contiene los datos del archivo del codigo genetico del mismo a proteína,
# leyendo las columnas 0 y 1 del archivo 
for lines in GeneCode:
    Field=lines.split("\t")
    Code[str(Field[0])]=str(Field[1])
GeneCode.close()

# Se crea una variable tipo string vacía
rcSeq=""
# Creación del diccionario que especifica los complementos posibles de los nucleótidos
compNucl={"A":"T","T":"A","G":"C","C":"G",}

# Se crea un bulce tipo for que recorre cada base nitrogenada de la secuencia de DNA de interés. Si la base esta presente en el diccionario que se creó con anterioridad
# Se adiciona a la variable tipo string vacía creada 
for base in Seq:
    if compNucl[base] in Seq:
        rcSeq += compNucl[base]

# Se crea el documento en el que se guardarán las 6 traducciones posibles a la secuencia
prFile=open("prot.txt","w")

# Se crea un bucle tipo for donde se iran leyendo de tres en tres:
for ORF in [0,1,2]:
# Se utiliza el comando format para poder editar 3 string al tiempo que comienzan el prefijo StF_{0,1,2}
    locals()["StF_{}".format(ORF)]=""
# Se utiliza un bucle de tipo for para la posición n que evalua el rango creado entre Orf, la longitud de la secuencia evaluada y los tres nucleotidos siguientes
    for n in range(ORF,len(Seq),3):
# Se evalua si la secuencia y las tres posiciones siguientes estan en la evaluación del codigo genetico 
        if Seq[n:n+3] in Code:
# Se añade a la bases encontradas a los Strings StF_{0,1,2}
            locals()["StF_{}".format(ORF)]  += Code[Seq[n:n+3]]
# Se escriben los resultados obtenidos en el archivo creado
    prFile.write("StandForward_ORF{}: \n".format(ORF))
    prFile.write(locals()["StF_{}".format(ORF)])
    prFile.write("\n")
# Se repite el porceso anterior, pero esta vez la lectura se realiza en reversa y se escribe sobre el mismo archivo.
# Para evitar la repetición podriamos crear un bucle (for Strand in [Seq, rcSeq]:), pero no pudimos nombrar los 6 strings creados simultaneamente.
    locals()["StR_{}".format(ORF)]=""
    for n in range(ORF,len(rcSeq),3):
        if rcSeq[n:n+3] in Code:
            locals()["StR_{}".format(ORF)]  += Code[rcSeq[n:n+3]]
    prFile.write("StandReverse_ORF{}: \n".format(ORF))
    prFile.write(locals()["StR_{}".format(ORF)])
    prFile.write("\n")
# Se cierra el archivo
prFile.close()
            
           
                
