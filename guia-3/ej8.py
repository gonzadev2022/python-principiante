import random
import os

def limpiarPantalla():
    os.system("cls")

limpiarPantalla()
#Enunciado
# Tito el robot: Desarrollar un programa controlado por menú de opciones, que permita simular el desplazamiento de un robot sobre un plano. Inicialmente se genera la posición aleatoria del robot en forma de punto (x,y). Luego se presenta un menú de opciones que permita los siguientes movimientos:
# a) Girar al norte y avanzar 10 pasos
# b) Girar al sur y avanzar 20 pasos
# c) Girar al este y avanzar 10 pasos
# d) Girar al oeste y avanzar 20 pasos 
# El programa debe mostrar la ubicación del robot al inicio de cada iteracion

#Declaro variables
x = int()
y = int()
opcion = str()
posicionX = str()
posicionY = str()


#Inicializo variables
x = 0
y = 0
opcion = ""
posicionX = ""
posicionY = ""

#Proceso
def mostrarPosicion(x, y):

    #Posicion en eje Y (Norte y Sur)
    if (y > 0): posicionY= f"Tito esta {y} pasos al Norte"
    elif (y < 0): posicionY = f"Tito esta {abs(y)} pasos al Sur"
    else: posicionY = f"Tito es en el centro del Norte y Sur"

    #Posicion en eje X (Este y Oeste)
    if (x > 0): posicionX= f" y {x} pasos al Este"
    elif (x < 0): posicionX = f" y {abs(x)} pasos al Oeste"
    else: posicionX = f" y en el centro del Este y Oeste"

    return posicionY + posicionX

def operaciones():

    #Posicion inicial predeterminada (Opcion 1)
    x = -5
    y = 5

    #Posicion inicial aleatoria (Opcion 2)
    # x = random.randint(-20, 20)
    # y = random.randint(-20, 20)

    while True:
        limpiarPantalla()
        print("Tito el Robotito")
        print("Simulador de desplazamiento")
        print(mostrarPosicion(x, y))
        
        print("\nOpciones de desplazamiento")
        print("1: Girar al Norte y avanzar 10 pasos")
        print("2: Girar al Sur y avanzar 20 pasos")
        print("3: Girar al Este y avanzar 10 pasos")
        print("4: Girar al Oeste y avanzar 20 pasos")
        print("5: Salir")
        opcion = input("Elija una opcion: ")
  
        #Desplazamientos
        if (opcion == "1"): y += 10
        elif (opcion == "2"): y -= 20
        elif (opcion == "3"): x += 10
        elif (opcion == "4"): x -= 20
        elif (opcion == "5"): break

operaciones()

#Prueba de escritorio
'''
Entradas y Salidas  (Entradas = elegir una opcion  | Salidas = la ubicacion del robot)
---------------------------------------------------                 
Tito el Robotito
Simulador de desplazamiento
Tito esta 5 pasos al Norte y 5 pasos al Oeste  (Primera salida aleatoria o predeterminada)

Opciones de desplazamiento
1: Girar al Norte y avanzar 10 pasos
2: Girar al Sur y avanzar 20 pasos
3: Girar al Este y avanzar 10 pasos
4: Girar al Oeste y avanzar 20 pasos
5: Salir")
Elija una opcion: 1
---------------------------------------------------

Tito el Robotito
Simulador de desplazamiento
Tito esta 15 pasos al Norte y 5 pasos al Oeste  (Segunda salida)

Opciones de desplazamiento
1: Girar al Norte y avanzar 10 pasos
2: Girar al Sur y avanzar 20 pasos
3: Girar al Este y avanzar 10 pasos
4: Girar al Oeste y avanzar 20 pasos
5: Salir")
Elija una opcion: 2

---------------------------------------------------

Tito el Robotito
Simulador de desplazamiento
Tito esta 5 pasos al Sur y 5 pasos al Oeste  (Tercer salida)

Opciones de desplazamiento
1: Girar al Norte y avanzar 10 pasos
2: Girar al Sur y avanzar 20 pasos
3: Girar al Este y avanzar 10 pasos
4: Girar al Oeste y avanzar 20 pasos
5: Salir")
Elija una opcion: 3

---------------------------------------------------

Tito el Robotito
Simulador de desplazamiento
Tito esta 5 pasos al Sur y 5 pasos al Este  (Cuarta salida)

Opciones de desplazamiento
1: Girar al Norte y avanzar 10 pasos
2: Girar al Sur y avanzar 20 pasos
3: Girar al Este y avanzar 10 pasos
4: Girar al Oeste y avanzar 20 pasos
5: Salir")
Elija una opcion: 4

---------------------------------------------------

Tito el Robotito
Simulador de desplazamiento
Tito esta 5 pasos al Sur y 15 pasos al Oeste  (Quinta salida)

Opciones de desplazamiento
1: Girar al Norte y avanzar 10 pasos
2: Girar al Sur y avanzar 20 pasos
3: Girar al Este y avanzar 10 pasos
4: Girar al Oeste y avanzar 20 pasos
5: Salir")
Elija una opcion: 5
____________________________________________________

Proceso (Valores que toman las variables)

y =           0 |  5  | 15 | -5
x =           0 | -5  | 5  | -15
opcion =     "" | "1" | "2" |  "3" |  "4" |  "5" | 

    posicionY =                     posicionX =              
"Tito esta 5 pasos al Norte"      "y 5 pasos al Oeste"    (Iteracion 1: posicion aleatoria o predeterminada)
"Tito esta 15 pasos al Norte"     "y 5 pasos al Oeste"    (Iteracion 2: 10 pasos al Norte)
"Tito esta 5 pasos al Sur"        "y 5 pasos al Oeste"    (Iteracion 3: 20 pasos al Sur)
"Tito esta 5 pasos al Sur"        "y 5 pasos al Este"     (Iteracion 4: 10 pasos al Este)
"Tito esta 5 pasos al Sur"        "y 15 pasos al Oeste    (Iteracion 5: 20 pasos al Oeste)

'''