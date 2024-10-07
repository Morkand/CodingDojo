numero1 = 70 #declaracion de variable. Inicializar string.
numero2 = 3.14 #declaracion de variable. Inicializar decimal.
booleano = False #declaracion de variable. Inicializar boolean.
cadena = 'Hola Mundo' #declaracion de variable. Inicializar string.
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #declaracion de variable. Inicializar array de strings
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #declaracion de variable. Inicializar diccionario
frutas = ('guayaba', 'fresa', 'papaya') #declaracion de variable. Inicializacion de tupla
print(type(frutas)) #Funcion Impresion optener tipo de dato de frutas. Devuelve tuple
print(ingredientes_pastel[2])#Funcion Impresion de elemento del array. Devuelve la cadena 'Huevos'
ingredientes_pastel.append('Mantequilla')#Metodo append se agrega la cadena 'Mantequilla' al final del array
print(persona['nombre'])#Funcion Impresion de elemento nombre del diccionario. Retorna 'Patricio'
persona['nombre'] = 'Kevin'#Cambiar valor del elemento nombre del diccionario de 'Patricio' a 'Kevin'
persona['color_ojos'] = 'cafe'#Agregar valor. Se agrega un nuevo elemento al diccionario.
print(frutas[2])#Funcion Impresion tercer elemento de la tupla. Retorna papaya.

if numero1 > 45: #Condicional If.Condicion: numero1 es mayor que 45
    print("Numero mayor") #Funcion Impresion de cadena
else: #Condicional Else, que hacer en caso que no se cumpla la condicion en el if
    print("Numero menor") #Funcion Impresion de cadena

if len(cadena) < 5: #Condicional If. Condicion longitud de la cadena es menor que 5
    print("Cadena corta") #Funcion Impresion de cadena
elif len(cadena) > 15: #Condicional elif. Condicion longitud de cadena es mayor que 15
    print("Cadena larga") #Funcion Impresion de cadena
else: #Condicional else. Se ejecuta si no se cumples las condiciones establecidas anteriormente.
    print("Cadena perfecta")#Funcion Impresion de cadena

for x in range(8):#Bucle for. Ciclo de 0 a 7
    print(x) #Funcion Impresion de variable. Retornara 0,1,2,3,4,5,6,7
for x in range(2,8):#Bucle for. Cliclo de 2 a 7
    print(x) #Funcion Impresion de variable. Retornara 2,3,4,5,6,7
for x in range(2,8,2):#Bucle for. Ciclo de 2 a 7 saltando de a 2
    print(x) #Funcion Impresion de variable. Retornara 2,4,6
x = 0#Declaracion de variable. Inicializa entero
while(x < 8):#Bucle while. Condicion mientras x sea menor a 8
    print(x) #Funcion Impresion de variable x. Retornara 0,1,2,3,4,5,6,7
    x += 1 #Modificacion de variable. Incrementar valor de x en 1

ingredientes_pastel.pop()#Metodo pop. Elimina del array el ultimo elemento y retorna dicho elemento eliminado es 'Chocolate'
ingredientes_pastel.pop(1)#Meotodo pop. Elimina del array el segundo elemento y retorna dicho elemento es 'Leche'.

print(persona) #Funcion Impresion de diccionario. Retorna todo el diccionario
persona.pop('color_ojos') #Meodo pop. Elimina el elemento 'color_ojos' del diccionario y retorna su valor
print(persona)# Funcion Impresion de diccionario. Retorna todo el diccionario esta vez con el elemento color_ojos eliminado.

for ingrediente in ingredientes_pastel: #Ciclo For. Recorre los elementos dentro de la lista
    if ingrediente == 'Harina':#Condicional If. Condicion ingrediente es igual a 'Harina'
        continue #Bucle for. continuo se corta esta iteracion
    print('Después de la primera sentencia')#Imprime la cadena
    if ingrediente == 'Chocolate':#Condicional If. Condicion si ingrediente es igual a 'Chocolate'
        break #Ciclo for. Break corta la interacion completamente

def imprime_hola_10_veces(): # definicion de Funcion
    for numero in range(10): #Ciclo for. Ciclo de 0 a 9
        print('Hola') #Funcion Impresion. retorna 'Hola' nueve veces

imprime_hola_10_veces()#definicion de Funcion. Se llama a la funcion anterior para que se ejecute

def imprime_hola_n_veces(n): #Funcion parametro n
    for numero in range(n): #Ciclo for. Ciclo desde 0 hasta n
        print('Hola') # Funcion Impresion se retornara en n veces la cadena 'Hola'

imprime_hola_n_veces(5)#Funcion. Llamada se ejecutala funcion anterior parasandole el parametro 5 que ahora sera el valor de n

def imprime_hola_n_o_diez_veces(n = 10):#Funcion con parametro n que tiene un valor default de 10
    for numero in range(n):#Ciclo for. Ciclo de 0 a n
        print('Hola')#Funcion Impresion. Retornara 'Hola' n veces

imprime_hola_n_o_diez_veces()#Funcion se llama y se ejecuta con su valor predeterminado
imprime_hola_n_o_diez_veces(5)#Funcion se llama y se ejecuta pasandole el parametro 5


"""
Sección BONUS
"""

# print(numero3) #Error variable no definida
# numero3 = 86 #Declaracion de variable. Inicializar entero
# frutas[0] = 'naranja' #Error una tupla es inmutable
# print(persona['hobbies']) #Error no existe ese elemento en el diccionario
# print(ingredientes_pastel[11]) #Error esa posicion no esta definida
#   print(booleano)#Funcion imprime false
# frutas.append('manzana') #Error una tupla no tiene el metodo append.
# frutas.pop(1) #Error no existe el meotodo pop en un tupla.