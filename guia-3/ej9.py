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
numeros_ingresados = int()
total = int()
promedio = int()
repeticiones = int()
positivos = int()
negativos = int()
nota = int()

#Inicializo variables
opcion = ""
numero = 0
numeros_ingresados = 0
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

    #1: Calculo de promedio
    if (opcion == "1"):

        print("Calculando promedio")
        print("La carga de numeros finaliza cuando se ingrese el numero -1\n")

        while True:
            numero = int(input("Ingresa un numero: "))
            if (numero == -1): break

            total += numero
            numeros_ingresados += 1

        if (numeros_ingresados > 0):
            promedio = total / numeros_ingresados

        print(f"\nEl promedio de los {numeros_ingresados} numeros ingresados es {promedio}")

        #Reinicio variables
        numeros_ingresados = 0
        total = 0  

    #2: Cantidad de numeros negativos y positivos
    elif (opcion == "2"):

        print("Determinando cantidad de numeros negativos y positivos")
        repeticiones = int(input("¿Cuantos numeros aleatorios queres generar?: "))

        #Validacion
        while (repeticiones <= 0):
            print("Se debe ingresar un numero mayor a cero")
            repeticiones = int(input("\n¿Cuantos numeros aleatorios queres generar?: "))

        #Se generan los numeros aleatorios
        for i in range(repeticiones):
            numero = random.randint(-100, 100)

            if (numero > 0): positivos += 1
            elif (numero < 0): negativos += 1

        print(f"\nSe generaron {positivos} numeros positivos y {negativos} numeros negativos")

        #Reinicio variables
        positivos = 0
        negativos = 0

    #3: Determinando aprobacion
    elif (opcion == "3"):

        print("Determinando aprobacion")
        nota = int(input("Ingresar nota del alumno: "))

        #Validacion
        while (nota < 0 or nota > 10):
            print("La nota debe estar dentro del rango (del 0 al 10)")
            nota = int(input("\nIngresar nota del alumno: "))

        if (nota >= 4): print("\nEl alumno esta aprobado")
        else: print("\nEl alumno esta desaprobado")


    elif (opcion == "4"): break

    else: print("Opcion no valida")

    input("Pulse para continuar ")


#Prueba de escritorio
'''
Entradas y Salidas
-------------------------------------------------------------------------------------
Operaciones con secuencias numericas
1: Ingresar numeros y calcular su promedio
2: Generar valores aleatorios y determinar cantidad de valores negativos y positivos
3: Cargar la nota de un alumno en indicar si esta aprobado o no
4: Salir
Ingresa una opcion: 1

Calculando promedio
La carga de numeros finaliza cuando se ingrese el numero -1

Ingresa un numero: 10     
Ingresa un numero: 15  
Ingresa un numero: 20 
Ingresa un numero: -1

El promedio de los 3 numeros ingresados es 15.0   ---->  (Primer salida)
Pulse para continuar
-------------------------------------------------------------------------------------

Operaciones con secuencias numericas
1: Ingresar numeros y calcular su promedio     
2: Generar valores aleatorios y determinar cantidad de valores negativos y positivos
3: Cargar la nota de un alumno en indicar si esta aprobado o no
4: Salir
Ingresa una opcion: 2   

Determinando cantidad de numeros negativos y positivos
¿Cuantos numeros aleatorios queres generar?: 10

Se generaron 1 numeros positivos y 9 numeros negativos")  ----> (Segunda salida) 
Pulse para continuar
-------------------------------------------------------------------------------------

Operaciones con secuencias numericas
1: Ingresar numeros y calcular su promedio
2: Generar valores aleatorios y determinar cantidad de valores negativos y positivos
3: Cargar la nota de un alumno en indicar si esta aprobado o no
4: Salir
Ingresa una opcion: 3

Determinando aprobacion
Ingresar nota del alumno: 4

El alumno esta aprobado    ----> (Tercer salida)
Pulse para continuar
-------------------------------------------------------------------------------------

Operaciones con secuencias numericas
1: Ingresar numeros y calcular su promedio
2: Generar valores aleatorios y determinar cantidad de valores negativos y positivos
3: Cargar la nota de un alumno en indicar si esta aprobado o no
4: Salir
Ingresa una opcion: 4
_____________________________________________________________________________________

Proceso (Valores que toman las variables)

opcion =               "" | "1" | "2" | "3" | "4"
numero =                0 | 10  | 15  | 20  | -1
numeros_ingresados =    0 |  1  |  2  |  3  |  0
total =                 0 | 10  | 25  | 45  |  0
promedio =              0 | 15.0
repeticiones =          0 | 10  
positivos =             0 |  1  | 0
negativos =             0 |  9  | 0
nota =                  0 | 4 

'''