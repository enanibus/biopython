#Group 5: Daniel Díaz, Rubén Gómez-Gordo, Alicia Roig

while 1:
  Seq=input("\nPlease, type your DNA sequence: ").upper() #Se pide al usuario que introduzca una secuencia de DNA, que se guardará en mayúsculas.
  if "U" in Seq and "T" in Seq: #Mediante este condicional, el programa se reiniciará si encuentra U y T en la misma secuencia...
    print("(!) This is not DNA nor RNA.") #...y se informa al usuario.
    continue
  Seq_List=list(Seq) #Queda definida una lista con cada elemento de la secuencia.
  for Nuc in Seq_List: #Mediante este bucle, si se detecta en la secuencia de DNA algo que no sea un nucleótido, el programa se reinicia.
    Restart=False #Variable que determinará si el programa debe reiniciarse.
    if Nuc!="A" and Nuc!="T" and Nuc!="C" and Nuc!="G" and Nuc!="U": #Se comprueba si el elemento de la secuencia no coincide con ningún nucleótido...
      print("(!) This is not DNA nor RNA.") #...y se informa al usuario.
      Restart=True #Reasignamos esta variable porque se ha detectado una secuencia no válida.
      break #Salimos del bucle porque no necesitamos detectar más errores en la secuencia.
  if Restart==True: #Condicional que reiniciará el programa si la secuencia detectada es errónea.
    continue    
  if "U" in Seq: #Condicional para convertir las U de la secuencia anterior en T, informando al usuario de ello. 
    Seq=Seq.replace("U","T") #Redefinimos la secuencia de RNA traducida a DNA...
    print("(!) This is an RNA sequence. It has been translated to DNA (U->T) in order to be analyzed.") #...y se informa al usuario.
    
  Nuc_List=["A","T","G","C"] #Lista con los nombres de las cuatro bases.
  L=len(Seq) #Queda definida la longitud de la secuencia dada por el usuario.
  print("\nThe length of your DNA sequence is",L,"bp.") #El programa indica la longitud de la secuencia.
  print("The % of each base in your DNA sequence:")
  for Nuc in Nuc_List: #Mediante este bucle, el programa calcula el contenido de cada base en la secuencia dada y lo imprime por pantalla.
    print("\tThis is the",Nuc,"content in your sequence: ",end="")
    print(round(Seq.count(Nuc)*100/L,2),"%") #El programa elige una base de la lista y calcula el porcentaje correspondiente, redondeando el resultado a 2 decimales.
  print("The % of each dinucleotide in your DNA sequence:")
  for Nuc1 in Nuc_List: #Realizamos el mismo proceso para obtener todos los dinucleótidos posibles...
    for Nuc2 in Nuc_List: #...pero para ello, ahora hay que concatenar dos bucles for.
      Start=0 #Posición del DNA desde la que empezará a buscar el dinucleótido.
      Success=0 #Contador de éxitos en la búsqueda del dinucleótido. Sumará 1 cada vez que el bucle de búsqueda que introduciremos a continuación se complete con éxito.
      while 1: #Bucle de búsqueda del dinucleótido.
        Start=Seq.find(Nuc1+Nuc2,Start) #La posición donde empieza la búsqueda pasará a la siguiente posición en la que se encuentre dicho dinucleotido.
        if Start==-1: #Si la búsqueda falla, el dinucleótido ya no se repite más...
          break #...por lo que paramos este bucle de búsqueda.
        else: #Si la búsqueda se completa con éxito...
          Start+=1 #...la posición de inicio de búsqueda se mueve un nucleótido a la derecha para no encontrar de nuevo el mismo dinucleótido...
          Success+=1 #...y el contador de éxitos suma una unidad, reflejando que se ha encontrado el nucleótido.
      print("\tThis is the",Nuc1+Nuc2,"content in your sequence: ",end="")
      print(round(Success*100/(L-1),2),"%") #El programa calcula el porcentaje correspondiente, redondeando el resultado a 2 decimales.
  print()
  
  RE_Dict={"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT","NotI":"GCGGCCGC"} #Diccionario con los nombres de los enzimas de restricción y sus secuencias diana.
  RE_List=RE_Dict.keys() #Hacemos una lista adicional con los nombres de esas mismas enzimas.
  for RE in RE_List: #Contador que recorrerá los números de 0 a 3 (ambos inclusive).
    if RE_Dict[RE] not in Seq: #Si no se encuentra ninguna secuencia diana, se imprime por pantalla un mensaje indicándolo. En el resto de los casos, el programa ejecuta el código de más abajo.
      print(RE,"will not cut this sequence.")
    Position=Seq.find(RE_Dict[RE]) #Variable que encuentra la posición de la primera secuencia de corte encontrada.
    while RE_Dict[RE] in Seq: #Si se encuentra una de las secuencias del diccionario se entra en el siguiente bucle.
      print(RE,"will cut in the position +"+str(Seq.find(RE_Dict[RE],Position)+1),"of your sequence.") #Se imprime por pantalla la posición donde corta el enzima.
      Position=Seq.find(RE_Dict[RE],Position+1) #Se redefine la variable "Position", de forma que el programa encuentre la siguiente secuencia a una dada.
      if Position==-1: #Si ya se han encontrado todos los sitios de corte posibles, el programa sale del bucle while.
        break #Estas acciones se repiten hasta que todos los elementos de la lista hayan sido analizados.
