####MyGroup_Group 6 (Alejandro Asensio, Marina Gonzalo, MªJose Jimenez y Jaime Quesada)



###definimos un diccionario con las secuencias diana asociadas a los nombres de las enzimas de restriccion correspondientes

REnz = {"GAATTC":"EcoRI","GGATCC":"BamHI", "AAGCTT":"HindIII", "GCGGCCGC":"NotI"}

###Definimos una lista con los nucleotidos posibles que nos podemos encontrar en la secuencia de un acido nucleico (DNA y RNA).

Nucleotides=["A","C","G","T","U"]

###Asignamos la secuencia introducida por el usuario, en mayusculas, a la variable DNA_Sequence, de tipo string.
DNA_Sequence = input("Introduce your DNA sequence: ").upper()

###Ahora introducimos un loop for de manera que analiza letra a letra la secuencia.
###En el caso de que la letra este en la lista Nucleotides se asigna el booleano Nucleic_Acid al valor True y el lopp vuelve a empezar.
###Si la letra analizada no es un nucleotido, el booleano Nucleic_Acid se asigna al valor False y el programa sale del loop. Ademas se informa al usuario de que la secuencia introducida no es valida.
for letter in DNA_Sequence:
    if letter in Nucleotides:
        Nucleic_Acid = True
        continue
    else:
        Nucleic_Acid = False
        print("Error. You introduced a non-valid sequence.")
        break
###Si la secuencia inroducida es un acido nucleico se ejecuta el siguiente bloque:    
if Nucleic_Acid == True:
###Si el usuario ha introducido un RNA, se transforma en DNA (hebra complementaria) y se avisa al usuario de que su secuencia ha sido convertida.
    if "U" in DNA_Sequence:
        DNA_Sequence = DNA_Sequence.replace("U","T")
        print("Attention! What you introduced is a RNA sequence. Don't you worry, we have converted it to DNA")
###con la funcion round(argument,2) redondeamos a dos decimales la operacion que conforma el argumento.
###La operacion consiste en contar el numero de veces que aparece el nucleotido “X” en la secuencia, dividirlo por el total de nucleotidos (len(DNA_Sequence) y multiplicarlo por 100.

    print("Sequence statistics:")
    print("The lenth of your sequence is", len(DNA_Sequence), "nucleotides")
    print("\t For Adenine:")
    print("\t % A in your sequence is", round((DNA_Sequence.count("A")/len(DNA_Sequence)) * 100,2))
    print("\t For Thymine:")
    print("\t % T in your sequence is", round((DNA_Sequence.count("T")/len(DNA_Sequence)) * 100,2))
    print("\t For Guanine:")
    print("\t % G in your sequence is", round((DNA_Sequence.count("G")/len(DNA_Sequence)) * 100,2))
    print("\t For Cytosine:")
    print("\t % C in your sequence is", round((DNA_Sequence.count("C")/len(DNA_Sequence)) * 100,2))

###Ahora definimos dos listas con los desoxirribonucleotidos.


    FirstNucleotide = ["A","C","G","T"]
    SecondNucleotide = ["A","C","G","T"]
    print("% of dinucleotides:")
###Procedemos a concatenar dos bucles for, de manera que se establece una variable nueva dentro del segundo bucle llamada Dinucleotide. Esta variable es el resultado del redondeo a la segunda cifra decimal del porcentaje del numero de veces que la combinacion de los nucleotidos definidos por las variables x e y aparecen en la secuencia respecto al total de dinucleotidos posibles en la secuencia (len(DNA_sequence) -1).   
    for x in FirstNucleotide:
        print("\t Dinucleotides starting with", x)
        for y in SecondNucleotide:
            out=x+y
            Dinucleotide=round((DNA_Sequence.count(out)/(len(DNA_Sequence)-1))* 100,2)
            print("\t % of", out, "is", Dinucleotide)


###El programa analiza si cada uno de los indices de la lista REnz.keys(), que contiene los key del diccionario REnz (las secuencias de las enzimas de restriccion), aparece en la secuencia. 
###Si el sitio de corte esta en la DNA_Sequence, se informa del sitio de corte (determinado con la funcion (DNA_Sequence.find()+1), ya que el primer nucleotido se designa con el numero 1 pero el primer elemnto de la string tiene indice 0.
###Para obtener los siguientes sitios de corte, se redefine la variable DNA_Sequence como un segmento de la introducida originalmente pero cortada en la posicion de la secuencia de restriccion y eligiendo el segundo de los dos fragmentos obtenidos tras el corte (indice 1 de la lista generada###Se define una nueva variable Next_Restriction_Site_Position, que resulta de sumar Restriction_Site_Position a la posicion del nuevo sitio en la nueva secuencia.Se analiza si sigue habiendo secuencias de corte para ese enzima, pero no se vuelve a cortar la secuencia.
###Se define una nueva variable Next_Restriction_Site_Position, que resulta de sumar Restriction_Site_Position a la posicion del nuevo sitio en la nueva secuencia.
###Se analiza si hay mas sitios de corte en la nueva secuencia.
    print("Restriction enzymes:")
    Complete_DNA = DNA_Sequence
    for z in REnz.keys():
        if z in DNA_Sequence:
            Restriction_Site_Position = DNA_Sequence.find(z)+1
            print("\tYour sequence has one restriction site for", REnz[z], "in this position:",  Restriction_Site_Position)
            DNA_Sequence = DNA_Sequence.split(z,1)[1]
            Next_Restriction_Site_Position = DNA_Sequence.find(z)+Restriction_Site_Position
            while z in DNA_Sequence:
                Next_Restriction_Site_Position += DNA_Sequence.find(z)
                DNA_Sequence = DNA_Sequence.split(z,1)[1]
                print("\tYour sequence has another restriction site for", REnz[z], "in this position:", Next_Restriction_Site_Position)
            DNA_Sequence = Complete_DNA
        else:
            print("There are no restriction sites for", REnz[z])

###En el caso de que la secuencia introducida contenga algun otro caracter que no sea un nucleotido, se imprime el mensaje a continuacion porque dicha secuencia no es un acido nucleico:
else:
     print("This program only accepts DNA sequences.")





