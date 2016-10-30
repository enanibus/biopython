#Grupo8: Álvaro Alfayate, Andrea de la Fuente, Carla Guillén y Jorge Nuevo

#Diccionario de Enzimas de Restricción: Asocia la secuencia de corte de cada enzima al nombre de la misma.
REnz={'EcoRI':'GAATTC','BamHI':'GGATCC', 'HindIII':'AAGCTT','NotI':'GCGGCCGC'}
DNA_Code1=['A','C','G','T']
DNA_Code2=['A','C','G','T']


print('\nWelcome to our DNA analyzer. Enjoy your trip')
while True:
    #Input: Pedimos al usuario que introduzca la secuencia de DNA que vamos a analizar con el programa.
    DNA=input('\nPlease, introduce your DNA sequence or press enter to finish: ').upper()  #DNA será la variable que contenga la secuencia a analizar.
    #Upper por si algún científico decide meter algo en minúsculas...
    if DNA=='':
        break ##Directamente termina el bucle porque han pulsado enter.
    elif (DNA.count('A')+DNA.count('C')+DNA.count('G')+DNA.count('T')+DNA.count('U'))!=len(DNA): #Si estos dos no son iguales significaría que hay letras adicionales que no son de DNA
        print('Remember. This program only works with DNA. Avoid other sequences.\nTry again')
        continue ##Que se salte todo lo del bucle pero vuelva al principio para volverlo a intentar.
    elif 'U' in DNA: #Si hay U significa que es RNA
        DNA=DNA.replace('U','T') #Por si deciden meter un RNA, que se transforme y lo cuente igual como si fuera un DNA
        #Asignamos de nuevo la variable DNA a la modificación. DNA continúa siendo nuestra secuencia a analizar.
        #If the provided sequence is RNA, warn the user, but translate it to DNA and continue.
        print('Warning. You should introduce a DNA sequence. Your RNA has been translated to DNA.')
    #Report detailed sequence statistics: sequence length, % of each base and % of each dinucleotide
    print('\nSEQUENCE STADISTICS')  ##Printea el titular de estadísticas de tu secuencia
    print('\n- Sequence length: '+str(len(DNA))+' pb') ##Calcula la longitud de la secuencia y la printea en pares de bases
    print('\n- Nucleotides Percentage')
    for Nucleotide in DNA_Code1: ##Bucle para que en un paso, printee todos los porcentajes de nucleótidos
        print('\t'+ Nucleotide+' percentage '+str(round(DNA.count(Nucleotide)/len(DNA)*100,2))+' %')#Nucleotide es cada nucleótido en cada ciclo del bucle
    print('\n- Dinucleotides Percentage')
    for Nucleotide1 in DNA_Code1: 
        for Nucleotide2 in DNA_Code2: ##De esta forma, genera combinaciones 2 a 2 de todos los nucleótidos de ambas bibliotecas.  
            Dinucleotide=str(Nucleotide1)+str(Nucleotide2) ##Concatena ambos nucleótidos, de los cuales posteriormente se determinarán los %. 
            Counter=0 ##El contador para que se vaya moviendo una base cada vez que corra el bucle
            Match=0 ##Contador que suma +1 cada vez que hay un Match para ese dinucleótido
            while True:
                Counter=DNA.find(Dinucleotide,Counter) ##Ahora Counter va a ser la posición dónde se encuentra ese dinucleótido (-1 si no está)
                if Counter==-1:
                    break
                else:
                    Counter=Counter+1 ##Para que se mueva SOLO una base, y no dos.
                    Match=Match+1 ##Para que cuente que ya se ha encontrado ese dinucleótido una vez
            print('\t'+ Dinucleotide+' percentage '+str(round(Match/(len(DNA)-1)*100,2))+'%') ##Printea el % de cada dinucleótido. 

    #Indicate if the DNA sequence will be digested by the selected enzyme. Indicate the (first) cutting position of the selected restriction enzyme, if applicable.
    print('\nRESTRICTION SEQUENCES FINDER:\n')
    for Enz in REnz.keys(): ##Asignamos a Enz cada una de las keys del diccionario 
        if REnz[Enz] in DNA: ##Si la secuencia asociada a la Enz en el bucle actual está en el DNA ocurrirá lo que viene a continuación 
            print('\t- Your DNA sequence can be cut by '+Enz) #Te dice si se puede cortar por tu enzima
            Position=0 ##Fijamos la posición como 0 para tener la variable declarada desde EL ORIGEN.
            while Position < len(DNA): 
                Position=DNA.find((REnz[Enz]),Position) ##Para que busque en el DNA la secuencia de corte partiendo de la posición que toque en ese bucle.
                if Position ==-1:
                    break
                print('\t    Cutting sequence in nucleotide: +',str(Position+1)) ##+1 para que lo imprima empezando por 1 y no por 0
                Position=Position+len(REnz[Enz]) #Para que no vuelva a repetirlo durante la longitud de la secuencia, si no se repetiría la solución.
        elif REnz[Enz] not in DNA:
            print('\t- Your DNA sequence can\'t be cut by '+Enz) #Te dice si no se puede cortar por tu enzima
print('\nEND. Thank you for trusting our program.')
