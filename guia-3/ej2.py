import os

def limpiarPantalla():
    os.system("cls")

#Enunciado
# Menu de Opciones con secuencias. Escribir un programa que le permita al usuario, a través de un menú de opciones, las siguientes operaciones: 
# a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados 
# b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales 
# c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares 
# d) Salir

#Declaro variables
opcion = int()
numero = int()
repeticiones = int()
sumaDeCuadrados = int()
palabrasConVocal = int()
vocales = tuple()
texto = str()
textoSinPunto = str()
ultimaLetra = str()
pares = int()
impares = int()

#Inicializo variables
opcion = 0
numero = 0
repeticiones = 0
sumaDeCuadrados = 0
palabrasConVocal = 0
vocales = ("a", "e", "i", "o", "u")
texto = ""
ultimaLetra = ""
pares = 0
impares = 0

#Proceso
while True:

    limpiarPantalla()
    print("Operaciones con secuencias numericas")
    print("A: Generar una serie de numeros y mostrar la suma de los cuadrados")
    print("B: Ingresar un texto y determinar la cantidad de palabras finalizadas con vocales")
    print("C: Ingresar una serie de numeros y determinar si hay mayor cantidad de valores pares o de impares")
    print("D: Salir")
    opcion = input("Ingresa una opcion: ").upper()
    limpiarPantalla()

    if (opcion == "A"):
        print("Suma de los cuadrados")
        repeticiones = int(input("¿Cuantos numeros queres ingresar?: "))

        for i in range(repeticiones):
            numero = int(input("Ingresa un numero: "))
            sumaDeCuadrados += numero ** 2

        print(f"\nLa suma del cuadrado de los numeros es {sumaDeCuadrados}")
        sumaDeCuadrados = 0 #Reinicio acumulador

    elif (opcion == "B"):
        print("Determinando palabras terminadas en vocal")
        print("La carga finaliza cuando se ingrese un punto\n")

        while True:
            texto = input("Ingresa un texto: ").lower()
            if (texto == "."): break

            for palabra in texto.split():

                ultimaLetra = palabra[len(palabra) - 1]
                if (ultimaLetra in vocales): palabrasConVocal += 1

        print(f"\n{palabrasConVocal} de las palabras ingresadas terminan con vocal")
        palabrasConVocal = 0 #Reinicio contador

    elif (opcion == "C"):
        print("Determinando cantidad de numeros pares e impares")
        print("La carga finaliza cuando se ingresa el valor 0\n")

        while True:
            numero = int(input("Ingresa un numero: "))
            if (numero == 0): break

            if (numero % 2 == 0): pares += 1
            else: impares += 1

        if (pares > impares): print("\nSe ingresaron mas numeros pares")
        elif (impares > pares): print("\nSe ingresaron mas numeros impares")
        else: print("\nSe ingresaron la misma cantidad de numeros pares e impares")

        #Reinicio contadores
        par = 0
        impar = 0
    
    elif (opcion == "D"): break

    else: print("Opcion no valida")

    input("Pulse para continuar ")
