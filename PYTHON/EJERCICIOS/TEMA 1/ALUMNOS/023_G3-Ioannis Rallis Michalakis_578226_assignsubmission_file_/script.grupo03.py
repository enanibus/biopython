
### My_group: g3 (Maria Juliana Rodriguez, Ioannis Rallis, Patricia Palacios Ibañez)

### 1. El usuario ingresa la cadena de ADN y el nombre de la enzima de interes

userValue = input ("Ingrese una secuencia de ADN (luego presione enter): ")
userEnzymeName = input ("Ingrese el nombre de la enzima de interes (luego presione enter): ")

### 2. Calcula la cantidad (en porcentaje) de cada una de la bases presentes en la cadena de ADN ingresada por el usuario
## 2.1 Primero coloca las letras de la cadena ingresada en mayuscula, y luego cuenta la cantidad de cada base
cantidadCitosina = userValue.upper().count("C")
cantidadAdenina = userValue.upper().count("A")
cantidadGuanina = userValue.upper().count("G")
cantidadTimina = userValue.upper().count("T")
## 2.2 Cuenta el total de bases que estan incluidas en la cadena
totalesBases = (cantidadCitosina+cantidadAdenina+cantidadGuanina+cantidadTimina)
## 2.3 Calcula el porcentaje con los valores obtenidos anteriormente, y le informa al usuario. Adicionalmente, redondea la cifra obtenida a 2 decimales
porcentajeCitosina = round(((cantidadCitosina/totalesBases)*100),2)
print ("El porcentaje de Citosina en la secuencia es de: " + str(porcentajeCitosina))
porcentajeAdenina = round(((cantidadAdenina/totalesBases)*100),2)
print ("El porcentaje de Adenina en la secuencia es de: " + str(porcentajeAdenina))
porcentajeGuanina = round(((cantidadGuanina/totalesBases)*100),2)
print ("El porcentaje de Guanina en la secuencia es de: " + str(porcentajeGuanina))
porcentajeTimina = round(((cantidadTimina/totalesBases)*100),2)
print ("El porcentaje de Timina en la secuencia es de: " + str(porcentajeTimina))

### 3. Crea un diccionario que contiene el nombre de la enzima unida con la secuencia que reconoce la misma en la secuencia ingresada por el usuario
REnz ={"EcoRI":"GAATTC", "BamHI":"GGATCC","HindIII":"AAGCTT", "NotI":"GCGGCCGC"}

### 4. Busca en la secuencia ingresada por el usuario, si existe algun punto de union para la enzima seleccionada
secuenciaBlanco= userValue.find(REnz[userEnzymeName])

### 5. Se le informa al usuario si la cadena puede o no ser digerida por la enzima.
### De ser posible un mensaje en la pantalla de lo indicará; de lo contrario, otro mensaje tambien lo evaluara
### 6. Si la respuesta obtenida anteriormente es afimativa, se le informa al usuario cual es el primer sitio al se puede unir la enzima,
### de lo contrario le pedirá al usuario que presione enter para salir del programa
if REnz[userEnzymeName] in userValue:
    print ("La secuencia puede ser digerida por la enzima seleccionada")
    print("El primer sitio de union para la enzima es: "+ str(secuenciaBlanco))
    input("Presione enter para salir")
    exit()
else:
    print("La secuencia NO puede ser digerida por la enzima seleccionada")
    input("Presione enter para salir")
    exit()







