#Grupo 1 (Tarea 2); David Alcázar Gutiérrez, Manuel Fernández Ibáñez y Eduardo Herrada Soler





MyDNA=input("Introduce secuencia DNA ") #Pedimos la secuencia DNA a introducir
MyDNA=MyDNA.upper()                     #Convertimos la secuencia a mayúscula, si procede



l= len(MyDNA)                           #Introducimos las variables que computará el programa (longitud Dna, cuenta de número de nucleótidos y dinucleótidos)
nºA=MyDNA.count('A')
nºC=MyDNA.count('C')
nºG=MyDNA.count('G')
nºT=MyDNA.count('T')
nºU=MyDNA.count('U')
nºAA=MyDNA.count('AA')
nºAC=MyDNA.count('AC')
nºAG=MyDNA.count('AG')
nºAT=MyDNA.count('AT')
nºAU=MyDNA.count('AU')
nºCA=MyDNA.count('CA')
nºCC=MyDNA.count('CC')
nºCG=MyDNA.count('CG')
nºCT=MyDNA.count('CT')
nºCU=MyDNA.count('CU')
nºGA=MyDNA.count('GA')
nºGC=MyDNA.count('GC')
nºGG=MyDNA.count('GG')
nºGT=MyDNA.count('GT')
nºGU=MyDNA.count('GU')
nºTA=MyDNA.count('TA')
nºTC=MyDNA.count('TC')
nºTG=MyDNA.count('TG')
nºTT=MyDNA.count('TT')
nºTU=MyDNA.count('TU')
nºUA=MyDNA.count('UA')
nºUC=MyDNA.count('UC')
nºUG=MyDNA.count('UG')
nºUU=MyDNA.count('UU')

nº_nucleotidos_RNA= nºA+ nºC+ nºG + nºU                  #Introducimos estas 2 variables para computar el numero de letras pertenecientes a ADN y ARN
nº_nucleotidos_DNA= nºA+ nºC+ nºG + nºT 


NA=nºA/l*100                  #Variables que representan el porcentaje de los nucleótidos y dinucleótidos introducidos en la secuencia
NC=nºC/l*100                                             
NG=nºG/l*100
NT=nºT/l*100
NU=nºU/l*100
NAA=nºAA/(l-1)*100            #A la hora de calcular el porcentaje de dinucleótidos, aplicamos el matiz (longitud DNA -1) ya que para una secuencia de p.e 8 nucleótidos, el 100% de parejas de dinucleótidos es 7 (8-1)
NAC=nºAC/(l-1)*100
NAG=nºAG/(l-1)*100
NAT=nºAT/(l-1)*100
NAU=nºAU/(l-1)*100
NCA=nºCA/(l-1)*100
NCC=nºCC/(l-1)*100
NCG=nºCG/(l-1)*100
NCT=nºCT/(l-1)*100
NCU=nºCU/(l-1)*100
NGA=nºGA/(l-1)*100
NGC=nºGC/(l-1)*100
NGG=nºGG/(l-1)*100
NGT=nºGT/(l-1)*100
NGU=nºGU/(l-1)*100
NTA=nºTA/(l-1)*100
NTC=nºTC/(l-1)*100
NTG=nºTG/(l-1)*100
NTT=nºTT/(l-1)*100
NUA=nºUA/(l-1)*100
NUC=nºUC/(l-1)*100
NUG=nºUG/(l-1)*100
NUU=nºUU/(l-1)*100



MyDNA.count("U")                    #Hacemos que el programa cuente el número de Uracilos 
Uracilos= MyDNA.count("U")          #Definimos el número de uracilos como "Uracilos"



if Uracilos !=0 and l==nº_nucleotidos_RNA:   #Para distinguir RNA, introducimos las condiciones: Uracilos distino de 0 y que la longitud de la secuencia introducida sea igual al nº nucleótidos de RNA
                                        


    print("Has introducido secuencia RNA, pero te lo convierto a DNA y continuamos")
    
    print("longitud DNA ", l)   #reflejamos los resultados   
    print("%A", NA)
    print("%C", NC)
    print("%G", NG)
    print("%T", NU)            #Como hemos computado el nº de Uracilos, plasmamos el número de Timinas en función del número de Uracilos; igual con los dinucleótidos
    print("%AA",NAA)
    print("%AC",NAC)
    print("%AG",NAG)
    print("%AT",NAU)
    print("%CA",NCA)
    print("%CC",NCC)
    print("%CG",NCG)
    print("%CT",NCU)
    print("%GA",NGA)
    print("%GC",NGC)
    print("%GG",NGG)
    print("%GT",NGU)
    print("%TA",NUA)
    print("%TC",NUC)
    print("%TG",NUG)
    print("%TT",NUU)
    
else:   #Para cubrir el resto de situaciones posibles
    
    if l != nº_nucleotidos_DNA:     #condición para distinguir entre DNA y proteína: si el nº nucleótidos es distinto al tamaño de la secuencia introducida, no es DNA
        print("Por favor introduzca secuencia DNA")
        print ("fin del programa")
    else:                           #la opción restante es que la secuencia introducida sea DNA
        print("longitud DNA ", l)   #reflejamos los resultados
        print("%A", NA)
        print("%C", NC)
        print("%G", NG)
        print("%T", NT)
        print("%AA",NAA)
        print("%AC",NAC)
        print("%AG",NAG)
        print("AT%",NAT)
        print("%CA",NCA)
        print("%CC",NCC)
        print("%CG",NCG)
        print("%CT",NCT)
        print("%GA",NGA)
        print("%GC",NGC)
        print("%GG",NGG)
        print("%GT",NGT)
        print("%TA",NTA)
        print("%TC",NTC)
        print("%TG",NTG)
        print("%TT",NTT)

if Uracilos!=0 and l==nº_nucleotidos_RNA or l==nº_nucleotidos_DNA: #Solo ejecutaremos la busqueda de corte si la secuencia introducida es RNA (traducimos y seguimos) o DNA, pero nada que no sea eso

 Enz={"ECORI":"GAATTC", "BAMHI":"GGATCC", "HINDIII":"AAGCTT", "NOTI":"GCGGCCGC"} #Definimos el diccionario con las enzimas y las secuencias de corte
 z ="la enzima que sea" 
 while (z != "") :    #Mientras z sea distinto de nada, se ejecutará el bucle
    z=input(' type any enz and then press enter (enter en blanco para salir)') #el usuario define la z, que será la enzima
    z=z.upper() #conversión a mayúsculas, si procede

    if z in Enz : #Si la enzima está en el diccionario, se ejecuta la condición

        CutEnz=Enz[z] in MyDNA  #CutEnz es un buleano que le pregunta al programa si la enzima(su secuencia de corte) está en el DNA introducido
        print("Will your sequence be cut? " , CutEnz)  
        if Enz[z] in MyDNA :    #Si la respuesta al anterior buleano es "True", el programa accederá a esta condición
             t=(MyDNA.find(Enz[z]))  #definimos t como la posición de nuestra enzima (primer nucleótido de corte) en la secuencia introducida
             while t > 0 :           #aplicamos el bucle while: mientras que la posición del DNA que busque sea mayor que 0
                 print("posición de la enzima en el DNA = posición" , t)  
                 t2=(MyDNA.find(Enz[z], t+1))  #introducimos un contador a t para que continúe buscando secuencias de restricción de las enzimas en la secuencia introducida
                 t= t2                         #Finalmente convertimos la variable t en t2 para que ejecute dicha búsqueda
        

             
    else:
        print("esta enzima no está contemplada")    #si z la enzima no esta contemplada en nuestro diccionario, se ejecutará este comando    
    

        
