import random
import os

def limpiarPantalla():
    os.system("cls")

#Enunciado
# Menú de opciones y validación Se pide desarrollar un programa controlado por menú de opciones que permita lo siguiente:
# 1. Ingresar números (la carga finaliza cuando se ingresa el -1) y calcular su promedio.
# 2. Generar n valores aleatorios entre -100 y 100 (n se ingresa por teclado). Determinar la cantidad de valores negativos y positivos.
# 3. Cargar la nota de un alumno e informar si está aprobado teniendo en cuenta que la nota es un valor entre 0 y 10, siendo mayor o igual a 4 si está aprobado

#Declaro variables
opcion = str()
numero = int()
numerosIngresados = int()
total = int()
promedio = int()
repeticiones = int()
positivos = int()
negativos = int()
nota = int()

#Inicializo variables
opcion = ""
numero = 0
numerosIngresados = 0
total = 0
promedio = 0
repeticiones = 0
positivos = 0
negativos = 0
nota = 0

#Proceso
while True:
    limpiarPantalla()
    print("Operaciones con secuencias numericas")
    print("1: Ingresar numeros y calcular su promedio")
    print("2: Generar valores aleatorios y determinar cantidad de valores negativos y positivos")
    print("3: Cargar la nota de un alumno en indicar si esta aprobado o no")
    print("4: Salir")
    opcion = input("Ingresa una opcion: ")
    limpiarPantalla()

    if (opcion == "1"):
        print("Calculando promedio")
        print("La carga de numeros finaliza cuando se ingrese el numero -1\n")

        while True:
            numero = int(input("Ingresa un numero: "))
            if (numero == -1): break

            total += numero
            numerosIngresados += 1

        if (numerosIngresados > 0):
            promedio = total / numerosIngresados

        print(f"\nEl promedio de los {numerosIngresados} numeros ingresados es {promedio}")

        #Reinicio variables
        numerosIngresados = 0
        total = 0  


    elif (opcion == "2"):
        print("Determinando cantidad de numeros negativos y positivos")
        repeticiones = int(input("¿Cuantos numeros aleatorios queres generar?: "))

        while (repeticiones <= 0):
            print("Se debe ingresar un numero mayor a cero")
            repeticiones = int(input("\n¿Cuantos numeros aleatorios queres generar?: "))

        for i in range(repeticiones):
            numero = random.randint(-100, 100)

            if (numero > 0): positivos += 1
            elif (numero < 0): negativos += 1

        print(f"\nSe generaron {positivos} numeros positivos y {negativos} numeros negativos")

        #Reinicio variables
        positivos = 0
        negativos = 0


    elif (opcion == "3"):
        print("Determinando aprobacion")
        nota = int(input("Ingresar nota del alumno: "))

        while (nota < 0 or nota > 10):
            print("La nota debe estar dentro del rango (del 1 al 10)")
            nota = int(input("\nIngresar nota del alumno: "))

        if (nota >= 4): print("\nEl alumno esta aprobado")
        else: print("\nEl alumno esta desaprobado")


    elif (opcion == "4"): break

    else: print("Opcion no valida")

    input("Pulse para continuar ")