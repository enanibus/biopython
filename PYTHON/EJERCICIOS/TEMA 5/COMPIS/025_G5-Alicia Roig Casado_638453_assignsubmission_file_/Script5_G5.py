#Group 5: Daniel Díaz, Rubén Gómez-Gordo, Alicia Roig


def GetGroups(Regex,Str): #Creamos una función que nos devuelva una tupla con los grupos de una expesión regular (Regex) encontrados en un string (Str).
  MyRE=re.compile(Regex) #Compilamos nuestra expresión regular.
  Obj=MyRE.search(Str) #Almacenamos el objeto que obtenemos al buscar la expresión regular en el string.
  Res=Obj.groups() #Creamos una tupla con los grupos definidos del objeto.
  if len(Res)==0: #En el caso de que nuestra expresión regular no contenga ningún grupo definido entre paréntesis...
    Res=Obj.group() #...almacenaremos el string completo del objeto.
  return(Res) #La función devuelve el resultado.

def GetAccNum(InputN): #Creamos una función que nos devuelva el número de acceso de una secuencia en formato FASTA (InputN).
  MyFile=open(InputN,"r") #Abrimos para lectura el fichero FASTA.
  for Line in MyFile: #Este bucle irá leyendo cada línea del fichero.
    if ">" in Line: #Este condicional asegura que el número de acceso sea buscado en la línea de cabecera.
      RegEx=r"[NX]M_\d+\.\d" #Definimos el string de nuestra expresión regular para el número de acceso.
      AccNum=GetGroups(RegEx,Line) #Almacenamos el número de acceso encontrado en el fichero.
  MyFile.close() #Cerramos el fichero.
  return(AccNum) #La función devuelve el número de acceso.

def GetDNA(InputN): #Creamos una función que nos devuelva la secuencia de DNA contenida en un fichero tipo FASTA (InputN).
  DNA="" #Definimos una variable vacía que almacenará la secuencia de DNA contenida en el fichero.
  MyFile=open(InputN,"r") #Abrimos para lectura el fichero FASTA.  
  for Line in MyFile: #Este bucle irá leyendo cada línea del fichero.
    if not ">" in Line: #Con este condicional aseguramos que la línea de cabecera no se incluya en la secuencia. 
      DNA+=Line.strip() #Todas las líneas con secuencia de DNA van a quedar guardadas de manera concatenada dentro de la variable local 'DNA'.
  MyFile.close() #Cerramos el fichero.
  return(DNA.upper()) #La función nos devuelve la secuencia de DNA, siempre en mayúsculas.

def GetCode(InputN): #Creamos una función que nos devuelva un diccionario que contenga un código genético, a partir de un fichero '.csv' (InputN).
  GenCode={} #Diccionario que contendrá cada codón como 'key' y su respectivo aminoácido como 'value' (en forma de lista con las notaciones de 1 y 3 letras).
  MyFile=open(InputN,"r") #Abrimos para lectura el fichero que contiene el código genético.
  RegEx=r"([ACTG]{3})\t([^BJUXZ])\t([A-Z][a-z]{2})" #Definimos el string de nuestra expresión regular para cada línea del código genético.
  for Line in MyFile: #Este bucle irá leyendo cada línea del fichero.
    Code=GetGroups(RegEx,Line)#Almacenamos una tupla con los elementos de cada línea del código genético.
    GenCode[Code[0]]=Code[1:] #Guardamos en el diccionario cada codón como "key", y cada aminoácido como "value" en forma de lista (ej: 'TTT':['P','Phe']).
  MyFile.close() #Cerramos el fichero.
  return(GenCode) #La función nos devuelve el diccionario con el código genético.
  
def Get_rcDNA(DNA): #Creamos una función que nos devuelva el reverso complementario de una secuencia de DNA.
  Complementary={"A":"T","T":"A","C":"G","G":"C"} #Diccionario que contiene cada base asociada a su base complementaria.
  rcDNA="" #Variable que almacenará la secuencia de la cadena (-) de DNA.
  for Nuc in DNA[::-1]: #Este bucle va a pasar por todos los nucleótidos de la cadena (+) de DNA en sentido 3' -> 5'...
    rcDNA+=Complementary[Nuc] #...y se van a introducir uno a uno los nucleótidos complementarios, obteniendo la cadena (-) de DNA.
  return(rcDNA) #La función nos devuelve el DNA reverso complementario.

def Translate(DNAs,GenCode,OutputN): #Creamos una función cuyos argumentos son: 1) Una lista de secuencias de DNA (en este caso 2: cadena positiva y cadena negativa).
#2)Un diccionario con el código genético. 3) El nombre del fichero que vamos a generar.
#La función nos devuelve un fichero con todas las posibles traducciones a proteína, según las 3 pautas de lectura.
  MyFile=open(OutputN,"w") #Abrimos para escritura un fichero en el que introduciremos las secuencias proteicas obtenidas.
  s="+" #Variable que nos informa de que se va a traducir la cadena (+).
  for Strand in DNAs: #Primer bucle: el programa pasará primero por la cadena (+) de DNA y después por la cadena (-).
    MyFile.write('## STRAND ('+s+')\n') #Escribimos en el fichero cuál de las dos cadenas se va a traducir
    for Frame in [0,1,2]: #Segundo bucle: el programa pasará por las 3 posibles pautas de lectura: +1, +2 y +3.
      Protein="" #Definimos una variable vacía que almacenará la secuencia de proteína cada vez que el DNA sea traducido.
      for Position in range(Frame,len(Strand),3): #Tercer bucle: el programa avanzará 3 nucleótidos a la derecha cada vez.
      #El origen dependerá de la pauta de lectura empleada en cada caso.
        CurrentCodon=Strand[Position:Position+3] #Definimos la subsecuencia de 3 nucleótidos equivalente a un codón, que dependerá de los bucles anteriores.
        if len(CurrentCodon)==3: #Evitamos que el programa falle al llegar al final, cuando quedan 1 ó 2 nucleótidos fuera de la pauta de lectura.
          Protein+=GenCode[CurrentCodon][0] #Traduce codón a codón y obtiene la secuencia de proteína, almacenándola en la variable "Protein".
      MyFile.write("# Frame +"+str(Frame+1)+":\n"+Protein+"\n\n") #Introducimos cada secuencia de proteína en el fichero, tras indicar la pauta de lectura.
    s="-" #Variable que nos informa de que se va a traducir la cadena (-).
    MyFile.write("\n") #Introducimos un retorno de carro en el fichero, para dejar más espacio visual entre ambas cadenas.
  MyFile.close() #Finalmente cerramos el fichero.

def main(): #Creamos una función a partir de las anteriores que sirva para ejecutar todo el programa.
  Acc_Num=GetAccNum(sys.argv[1]) #Variable que almacena el número de acceso de la secuencia.
  Seq=GetDNA(sys.argv[1]) #Variable que almacene la secuencia de DNA.
  #En los dos casos anteriores, el nombre del fichero FASTA corresponde al primer argumento introducido por el usuario en el intérprete interactivo.
  Gen_Code=GetCode("GeneticCode_standard.csv") #Variable que almacena el diccionario con el código genético (en este caso, el código estándar).
  Sequences=[Seq,Get_rcDNA(Seq)] #Lista que contiene las secuencias de las dos cadenas de DNA.
  Translate(Sequences,Gen_Code,Acc_Num+".txt") #Ejecución de la función "Translate". #El fichero creado llevará por nombre el nº de acceso de la secuencia.

if __name__=="__main__": #Condicional que asegura que este script no se ejecute cuando sea importado como módulo en otro script.
  import sys #Importamos el módulo sys.
  import re #Importamos el módulo re.
  try: #Entramos en un bloque try.
    if len(sys.argv)==2: #El programa funcionará si el usuario introduce el nombre del fichero FASTA tras el nombre del programa.
      main() #Ejecutamos la función que contiene todo el bloque de código necesario para que el programa funcione.
    else: #Si el usuario ejecuta mal el programa en el intérprete, recibirá una notificación que le enseñe a utilizarlo correctamente.
      print("(!) Type the name of your FASTA file after the name of the script (e.g., 'python program.py DNA.fasta'")
  except AttributeError: #Si en el fichero FASTA no se encuentra ningún número de acceso, el programa daría error...
    print("Oops! Your file does not contain any RefSeq number. Please, try with another file.")#...por lo que en ese caso avisaríamos al usuario por pantalla.
  except FileNotFoundError: #Si el fichero FASTA indicado no es localizable, el programa daría error...
    print("Oops! Your file was not found. Please, check you're typing the full name, including the extension.") #...y avisaríamos al usuario por pantalla.
  except: #Si ocurre cualquier otro tipo de error...
    print("Oops! There is something wrong with your input. Please, check you're introducing a FASTA file.") #...también será advertido.
