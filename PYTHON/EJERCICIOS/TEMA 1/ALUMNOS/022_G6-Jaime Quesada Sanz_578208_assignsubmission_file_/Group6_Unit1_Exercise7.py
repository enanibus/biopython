REnz = {"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT","NotI":"GCGGCCGC"}

#Construimos una biblioteca en la que el nombre de cada enzima de restriccion esta asociado a un valor que corresponde con la secuencia de su sitio de restriccion.

DNA_Sequence = input("Introduce your DNA sequence: ").upper()

#La secuencia de DNA queda ligada a la variable DNA_Sequence, de tipo string.
#Utilizamos la funcion upper() para que la secuencia este en mayusculas, aunque el usuario la introduzca en minusculas.

print("Percentage of A in your DNA sequence is " + str(round((DNA_Sequence.count("A")/len(DNA_Sequence)) * 100,2)) + " %")
print("Percentage of T in your DNA sequence is " + str(round((DNA_Sequence.count("T")/len(DNA_Sequence)) * 100,2)) + " %")
print("Percentage of G in your DNA sequence is " + str(round((DNA_Sequence.count("G")/len(DNA_Sequence)) * 100,2)) + " %")
print("Percentage of C in your DNA sequence is " + str(round((DNA_Sequence.count("C")/len(DNA_Sequence)) * 100,2)) + " %")

#Con la expresion DNA_Sequence.count("X")/len(DNA_Sequence)*100 ordenamos al programa que cuente el numero de A, T, G y C's mayusculas dentro de la secuencia, que lo divida por el total
#de bases y lo multiplique por 100 para obtener el %.

#Con la funcion round( ,2) ordenamos al programa que redondee el porcentaje a la segunda cifra decimal.
#Con la funcion str() convertimos el float que resulta del redondeo a una string. Ahora podemos concatenarla con otras strings.

#Utilizamos los simbolos "+" para concatenar tres strings, de manera que se convierten en una sola, que es la que el programa devuelve gracias a la funcion print().
#En vez de "+" podriamos haber utilizado "," (en este caso no habriamos tenido que convertir el resultado del redondeo a string), pero al no concatenarlas no podriamos controlar el espaciado.

Enzyme_Name = input("What Restriction Enzyme do you want to use? Choose between EcoRI, BamHI, HindIII or NotI: ")

#El nombre del enzima de restriccion deseado queda ligado a la variable Enzyme_Name, de tipo string.

Restriction_Site = REnz[Enzyme_Name]

#Creamos una nueva variable en la que almacenamos el sitio de restriccion asociado al nombre del enzima de restriccion en la biblioteca. Esta variable tambien es de tipo string.

print("Is your DNA sequence digested by the selected Restriction Enzyme?", Restriction_Site in DNA_Sequence)

#Con la expresion Restriction_Site in DNA_Sequence ordenamos al programa que busque el sitio de restriccion en la secuencia de DNA.
#La funcion print() nos devuelve una string y un booleano que nos indica si hay un sitio de restriccion en la secuencia introducida (True) o no (False).

print("The first cutting position of this Restriction Enzyme is", DNA_Sequence.find(Restriction_Site)+1)

#Con la expresion DNA_Sequence.find(Restriction_Site)+1 ordenamos al programa que encuentre la posicion del sitio de restriccion en la secuencia del DNA y le sume 1 (recordar que en python al
#primer caracter de la string DNA_Sequence se le asigna el indice 0, pero en bioquimica el primer nucleotido de una secuencia es el numero 1).
#La funcion print() nos devuelve una string y un integer que indica la posicion del primer nucleotido que forma parte del sitio de restriccion. Si en la secuencia no hay sitio de
#restriccion se nos devolvera el valor -1 + 1 = 0.
