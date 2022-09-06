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
# El programa debe mostrar la ubicación del robot al inicio de cada

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
    if (y > 0): posicionY= f"Tito esta {y} pasos al Norte"
    elif (y < 0): posicionY = f"Tito esta {abs(y)} pasos al Sur"
    else: posicionY = f"Tito es en el centro del Norte y Sur"

    if (x > 0): posicionX= f" y {x} pasos al Este"
    elif (x < 0): posicionX = f" y {abs(x)} pasos al Oeste"
    else: posicionX = f" y en el centro del Este y Oeste"

    return posicionY + posicionX

def operaciones():
    #Generando posicion inicial random
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)

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
        limpiarPantalla()

        if (opcion == "1"): y += 10
        elif (opcion == "2"): y -= 20
        elif (opcion == "3"): x += 10
        elif (opcion == "4"): x -= 20
        elif (opcion == "5"): break
        else: print("Opcion no valida")

operaciones()
