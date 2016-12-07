### My_group: g3 (Maria Juliana Rodriguez, Ioannis Rallis, Patricia Palacios Ibáñez)
### 1. El usuario ingresa la cadena de DNA y el nombre de la enzyma de restriction(el programa cambia todas las letras en mayusculas para evitar errores tipograficos).
DNAorRNA = input("Insert  DNA or RNA sequence: ").upper()
### 2. Crea un diccionario que contiene el nombre de la enzima unida con la secuencia que reconoce la misma en la secuencia ingresada por el usuario.
REnz = {"ECORI":"GAATTC","BAMHI":"GGATCC","HINDIII":"AAGCTT","NOTI":"GCGGCCGC"}
### 3. Se identifica si la secuencia posee nucleotidos del tipo Uracilo y los cambia por Timina
DNA=DNAorRNA.replace("U","T")
### 4.La secuencia ingresada es de DNA o de RNA solo si la suma de los nucleotidos es igual con la suma de las letras en DNA.
### Si no, hay letras adicionales en la secuencia.
if (DNA.count('A')+DNA.count('C')+DNA.count('G')+DNA.count('T')+DNA.count('U'))!=len(DNA):
        print("I only accept DNA or RNA sequence.")
        input("press ENTER to exit")
        exit()
### 5. Si la secuencia además, es de RNA, envia una alerta al usuario. Luego imprime la longitud de la secuencia ingresada por el usuario y el porcentaje 
###  de cada una de las bases nitrogenadas por separado A, G, T, C.
for Uracil in ["U"]:
    if Uracil in DNAorRNA:
       print("Warning this is an RNA sequence! I will transform it into a DNA sequence.")
    print("DNA sequence length: ", len(DNAorRNA),"nucleotides")
    print("DNA base percentage:")
    for nucl in ["A","T","G","C"]:
       print(nucl,":"+str(round((DNA.count(nucl)/len(DNA)) * 100,2)),"%")
### 6. Ahora evalua el porcentaje en la secuancia ingresada por el usuario de cada dinucleotido posible.
###    Porque contamos dinucleotidos dividimos el numero total de las bases con 2. 
    print("DNA dinucleotide percentage:")
    for dinucl in ["AT","AG","AC","AA","CT","CG","CC","CA","GT","GG","GC","GA","TT","TG","TC","TA"]:
       print(dinucl,": "+str(round((DNA.count(dinucl)/(len(DNA)-1))*100,2)),"%")
### 7. Identifica si cada enzyma dentro del diccionario  puede o no cortar a la secuancia ingresada por el usuario.
###    De ser asi, indica todos los sitios en los que esto podria ocurrir en la sequencia.(La sequencia que reconoce la enzima no aparece).   
###    Finalmente, cierra el programa.
    for enzyme in REnz.keys():
       if REnz[enzyme] in DNA:
           print("The sequence will be digested by:",enzyme)
           print("Exact cutting position (the recognised by the enzyme sequence do not appear):")
           print(DNA.split(REnz[enzyme]))
       elif enzyme not in DNA:
            print("The sequence will not be digested by:",enzyme)
    input("press enter to exit")
    exit()




