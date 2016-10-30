#Grupo 7, programa 3

#Abrimos los archivos (tienen que estar guardados en la misma carpeta) y los leemos
MySeq=open("Human_HRAS.fasta.txt",'r')
MyDNA=MySeq.read().strip()
MyCode=open("GeneticCode_standard.csv",'r')


#Crea una tabla que nos permite crear la cadena complementaria del DNA
frm='ATCG'
to='TAGC'
trans_table=str.maketrans(frm, to)#creamos una tabla que traduzca ATCG a TAGC
DNAcompl=MyDNA.translate(trans_table)#pasamos la cadena de ADN a la complementaria usando dicha tabla
DNAcompl = DNAcompl[::-1]

#Creamos un diccionario vacio
GenCode={}
#Bucle que nos rellena el diccionario con los codones y su aminoacido correspondientes
for Gen in MyCode:
  Gen=Gen.strip()
  MyGenCode=Gen.split('\t')
  GenCode[MyGenCode[0]]=MyGenCode[2]#Nos selecciona que el diccionario nos lo devuelva con los codones y las siglas de aminoacido

n=3#Hace que en las listas que se crean mas adelante se divida el DNA de tres en tres
#Crea una lista vacia para poner las distintas `proteinas en las distintas pautas de lectura
proteins = ["","",""]
complprotein = ["", "", ""]
#Bucle para que nos busque las proteinas
for j in range(3):
  MyDNAlist=[MyDNA[i:i+3] for i in range (j, len(MyDNA), n)] #Nos crea la lista con los codones
  for codon in MyDNAlist: #Busca los codones de la lista y si estan en el genoma los imprime
    if codon in GenCode:
      proteins[j]=proteins[j]+GenCode[codon]
      if GenCode[codon] == "Ter":#Condicional que hace que si hay un codon de terminacion acabe de transcribir la proteina
        break
  
  DNAcompllist=[DNAcompl[i:i+3] for i in range (j, len(DNAcompl), n)]#Busca los codones de la lista y si estan en el genoma los imprime, en la cadena complementaria
  for codon in DNAcompllist: #Busca los codones de la lista y si estan en el genoma los imprime, en la cadena complementaria
    if codon in GenCode:
      complprotein[j]+= GenCode[codon]#Condicional que hace que si hay un codon de terminacion acabe de transcribir la proteina, en la cadena complementaria
      if GenCode[codon] == "Ter":
        break

#Hace que se guarde un archivo txt y hace que se escriban en el las cadenas de proteinas
OutputFile=open("Proteins.txt",'w')
for i in range(3):#i será el número de la proteína
  OutputFile.write("\n")
  OutputFile.write("\nProteina " + str(i+1) + ":\n")#sumamos 1 a i para que no aparezca como 0
  OutputFile.write(proteins[i])#escribimos la proteína
  OutputFile.write("\n")#repetimos el proceso con la proteína complementaria
  OutputFile.write("\nProteina complementaria" + str(i+1) + ":\n")
  OutputFile.write(complprotein[i])
  OutputFile.write("\n")


#Cerramos los archivos de texto
MySeq.close()
MyCode.close()
OutputFile.close()

print("Proceso terminado correctamente. Se ha creado un archivo de texto bajo el nombre 'Proteins'.")
