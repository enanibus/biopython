#Archivo abierto
DNA_Fasta = open("Human_HRAS.fasta.txt", "r")
DNA_Fasta.readline()

#Dos listas para DNA y reversa complementaria. Lleno lista DNA con la funcion append y la uno con join para hacer una string

My_DNA = []
my_dna = []
for st in DNA_Fasta:
    DNA_Sequence = st.strip()
    My_DNA.append(DNA_Sequence)
DNA_Fasta.close()
My_DNA = "".join(My_DNA)


#Leo la string DNA al reves y transformo cada nucleotido en el complementario especificado en el diccionario. Guardo la secuencia en la lista my_dna y la convierto a string con .join() method
Comp = {"A":"T", "T":"A", "C":"G","G":"C"}
for R in My_DNA[::-1]:
    New_base = Comp[R]
    my_dna.append(New_base)
my_dna = "".join(my_dna)

#Defino dos diccionarios (1 para aa en nomenclatura de tres letras, 2 para nomenclatura de 1 letra). Abro el excell del codigo genetico. Con split() corto por los espacios en blanco, generando una lista, con strip() elimino los espacios en blanco.
#Con replace('"', '') sustituyo las "" por nada. Para cada linea en el codigo genetico, asigno el indice [0] (secuencia) en los dos diccionarios a [2] (3 letras, en dic1) o [1] (1 letra, en dic2)
aa_dic1 = {}
aa_dic2 = {}
Code = open("GeneticCode_standard.csv", "r")
for line in Code:
    Genetic_Code = line.replace('"', "").strip().split('\t')
    aa_dic1[Genetic_Code[0]]=Genetic_Code[2]
    aa_dic2[Genetic_Code[0]]=Genetic_Code[1]   
Code.close()

#Defino la lista Frames y la relleno con las distintas fases de lectura de la cadena directa y de la inversa, usando un bucle for y unos condicionales

Frames = []
for l in range(0,6):
    if l <=2:
        Frame = My_DNA[l:]
        Frames.append(Frame)
    elif l <=5:
        Frame = my_dna[l-3:]
        Frames.append(Frame)


List_of_lists1 = []
List_of_lists2 = []

for n in range (0,6):
    
    current_Frame = Frames[n]
    Protein1 = ""
    Protein2 = ""
    Protein_list1 = []
    Protein_list2 = []
#Dentro de este bucle for, establecemos otro bucle while para evitar problemas cuando al llegar al ultimo codon de la secuencia, este no tiene una longitud de 3 nucleotidos, por lo que daria error
    Protein_Start = False 
    Protein_End = False
    while len(current_Frame) >= 3:
        Codon = current_Frame[0:3]
        current_Frame = current_Frame.split(Codon,1)[1]
        #Establecemos el inicio y el final de la proteina, que posteriormente usaremos para saber cuando empezar a leer y cuando dejar de leer en el caso de encontrar un stop codon 
        if aa_dic1[Codon]== "Met" and aa_dic2[Codon] == "M":
            Protein_Start = True
            
        elif aa_dic1[Codon]== "Ter" and aa_dic2[Codon] == "*":
            Protein_End == True
            
        else:
             pass
        
        if Protein_Start == True and Protein_End == False:
            
            Protein1 += aa_dic1[Codon]
            Protein2 += aa_dic2[Codon]
           #Ahora, cuando se cumplan las condiciones que indiquen que no estamos en el final de una proteina, añadimos los aa_dic[Codon] a Protein 
        elif Protein_Start == True and Protein_End == True:
            #Añadimos las proteinas una vez finalizada la lectura a sus variables Protein1 y Protein2
            Protein_Start = False
            Protein_End = False
            Protein1 = Protein1 + "\n\n"
            Protein2 = Protein2 + "\n\n"
            Protein_list1.append(Protein1)
            Protein_list2.append(Protein2)
            Protein1 = ""
            Protein2 = ""
        
        elif Protein_Start == False:
            
            continue
            

    
    if len(current_Frame) < 3:
        
        Protein_list1.append(Protein1)
        Protein_list2.append(Protein2)
        Protein1 = ""
        Protein2 = ""
    
    if Protein_list1 == [""] or Protein_list2 == [""]:
        
        Protein_list1 = ["\tNO ORF FOUND"]
        Protein_list2 = ["\tNO ORF FOUND"]
        
        
    Protein_list1 = "".join(str(ORF) for ORF in Protein_list1) 
    Protein_list2 = "".join(str(ORF) for ORF in Protein_list2) 
    
    List_of_lists1.append(Protein_list1)  
    List_of_lists2.append(Protein_list2)

Translation = open("Translated_Protein.txt","w")
Translation.write("These are the six possible proteins encoded by your DNA sequence: \n \n")
for k in range(0,6):
    if k <= 2:
        Translation.write("5'3'Frame " + str(k+1) +":\n \n\tThree-letter notation: \n" +List_of_lists1[k] + "\n \n\tOne-letter notation: \n" +List_of_lists2[k] + "\n \n")
    elif k <= 5:
        Translation.write("3'5'Frame " + str(k-2) + ":\n \n\tThree-letter notation: \n" +List_of_lists1[k] + "\n \n\tOne-letter notation: \n" +List_of_lists2[k] + "\n \n")
Translation.close()

import os
place = os.getcwd()
print("A file named Translated_Protein.txt containing the translations from Human_HRAS.fasta.txt has been created in " + str(place) )
        
    

