"""
Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos 
(variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:

Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 

Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)

Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.

Nota: para saber si el número i es par hacer i % 2 == 0
"""

def inputNames():
    nombres = []
    while len(nombres) < 10:
        nombre = input("Ingresa un nombre: ")
        
        # Verificar si el nombre ya está en la lista
        if nombre in nombres:
            print("El nombre ya ha sido ingresado. Por favor, ingresa un nombre diferente.")
        else:
            nombres.append(nombre)

    # Mostrar la lista de nombres ingresados
    print("\nLos nombres ingresados son:")
    for nombre in nombres:
        print(nombre)
    
    return nombres

def deleteNames(nombres):
    
    if len(nombres) > 2: 
        del nombres[2]  
    if len(nombres) > 0: 
        del nombres[-1]  
    nombres.sort()

    print("\nLa lista después de eliminar y ordenar es:")
    for nombre in nombres:
        print(nombre)
        
def createPerson():
    
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    dni = input("Ingresa el DNI: ")
    email = input("Ingresa el email: ")
    fecha_nacimiento = input("Ingresa la fecha de nacimiento (DD/MM/AAAA): ")

    return {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "email": email,
        "fecha_nacimiento": fecha_nacimiento
    }


def createFamily():
     
    familia = {}

    for i in range(1, 5):
        print(f"\nIngrese los datos para la persona {i}:")
        familia[f"persona_{i}"] = createPerson()

    print("\nDatos de la familia:")
    for clave, datos in familia.items():
        print(f"\n{clave.capitalize()}:")
        for k, v in datos.items():
            print(f"  {k.capitalize()}: {v}")

def tuplePair():

    n = int(input("Ingresa el valor de n: "))

    numeros_pares = tuple(2 * i for i in range(n))

    print("\nLos primeros", n, "números pares son:")
    print(numeros_pares)

names = inputNames()

deleteNames(names)

createFamily()

tuplePair()
