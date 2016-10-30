##Ejercicio 2, Grupo 7
DNA=input ("Introduzca su secuencia de DNA: ")
uDNA=DNA.upper() #definimos una nueva variable para que el programa siempre trabaje con mayusculas, independientemente de cómo introduzca la secuencia el usuario. 

##definimos una variable con todas las letras del abecedario excepto A, C, G, T y U. Para detectar cuando el usuario no introduce una secuencia de ácido nucleico.
x=['B','D','E','F','H','I','J','K','L','M','N','O','P','Q','R','S','W','X','Y','Z']
i=0 
while i<20:#como hay 20 caracteres ponemos i<20. 
 if x[i] in uDNA: #definimos i=0 y hacemos que busque entre los diferentes términos de la variable x para ver si están en la secuencia.
        print ("Su secuencia no corresponde a un ácido nucleico.")
        break #en el caso de estar presentes algunas de esas letras sale del bucle, y acaba el programa. 
 i=i+1
if i==20: #cuando llega i a 20 significa que ninguno de los caracteres se encuentra en la secuencia, y por tanto se trata de ácido nucleico. 
        if "U" in uDNA: #si hay alguna U en la secuencia de ácido nucleico significa que es RNA. 
                print ("La secuencia introducida corresponde a RNA.")
                print ("La secuencia se DNA correspondiente sería:",end= "")
                print (uDNA.replace("U","T"))#cambiamos el caracter U por T para pasar el RNA a DNA.
                
        ##calculo de la longitud del DNA        
        print ("longitud del DNA:", end= " ")
        print (len(uDNA))
        
        ##cálculo del porcentaje de los distintos nucleótidos
        print ("porcentaje de A:", end= ' ')
        print (round(uDNA.count('A')/len(uDNA)*100,1))
        print ("porcentaje de C:", end= ' ')
        print (round(uDNA.count('C')/len(uDNA)*100,1))
        print ("porcentaje de G:", end= ' ')
        print (round(uDNA.count('G')/len(uDNA)*100,1))
        print ("porcentaje de T:", end= ' ')
        print (round(uDNA.count('T')/len(uDNA)*100,1))
        
        ##cálculo del porcentaje de los distintos dinucleótidos
        print ("porcentaje de AA:", end= ' ')
        print (round(uDNA.count('AA')/len(uDNA)*50,1))
        print ("porcentaje de AC:", end= ' ')
        print (round(uDNA.count('AC')/len(uDNA)*50,1))
        print ("porcentaje de AG:", end= ' ')
        print (round(uDNA.count('AG')/len(uDNA)*50,1))
        print ("porcentaje de AT:", end= ' ')
        print (round(uDNA.count('AT')/len(uDNA)*50,1))
        print ("porcentaje de CA:", end= ' ')
        print (round(uDNA.count('CA')/len(uDNA)*50,1))
        print ("porcentaje de CC:", end= ' ')
        print (round(uDNA.count('CC')/len(uDNA)*50,1))
        print ("porcentaje de CG:", end= ' ')
        print (round(uDNA.count('CG')/len(uDNA)*50,1))
        print ("porcentaje de CT:", end= ' ')
        print (round(uDNA.count('CT')/len(uDNA)*50,1))
        print ("porcentaje de GA:", end= ' ')
        print (round(uDNA.count('GA')/len(uDNA)*50,1))
        print ("porcentaje de GC:", end= ' ')
        print (round(uDNA.count('GC')/len(uDNA)*50,1))
        print ("porcentaje de GG:", end= ' ')
        print (round(uDNA.count('GG')/len(uDNA)*50,1))
        print ("porcentaje de GT:", end= ' ')
        print (round(uDNA.count('GT')/len(uDNA)*50,1))
        print ("porcentaje de TA:", end= ' ')
        print (round(uDNA.count('TA')/len(uDNA)*50,1))
        print ("porcentaje de TC:", end= ' ')
        print (round(uDNA.count('TC')/len(uDNA)*50,1))
        print ("porcentaje de TG:", end= ' ')
        print (round(uDNA.count('TC')/len(uDNA)*50,1))
        print ("porcentaje de TT:", end= ' ')
        print (round(uDNA.count('TT')/len(uDNA)*50,1))

        ultimaPosicion = 0 #Defino que la variable es la ultima posicion

        print("Enzimas de restricción que cortan el DNA: ")
        EnzimaRestriccion=["GAATTC","GGATCC","AAGCTT","GCGGCCGC"] #Lista con las secuencias que son cortadas por las enzimas de restriccion
        Nombres={"GAATTC":"EcoRI", "GGATCC":"BamHI", "AAGCTT":"HindIII", "GCGGCCGC":"NotI"} #Diccionario con las enzimas y su secuencia de corte

        for s in EnzimaRestriccion:#bucle para buscar las distintas secuencias de corte en la secuencia de DNA
            if s in uDNA:# Nos dice si esta la secuencia en el DNA
                    ultimaPosicion = 0 # Reinicia la variable para que empiece a buscar desde el principio de la cadena
                    print (Nombres[s] + ", en la/s posicion/es: ") # Nos dice el nombre de la enzima si es encontrada su secuencia de corte
                    while ultimaPosicion > -1: # Este bucle va encontrando las distintas secuencias de corte gracias a una variable que guarda la posicion de la ultima ocurrencia de la cadena
                        ultimaPosicion = uDNA.find(s, ultimaPosicion)
                        if ultimaPosicion > -1:
                            print(ultimaPosicion)
                            ultimaPosicion = ultimaPosicion + 1
                        pass
