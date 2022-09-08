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
opcion = str()
numero = int()
repeticiones = int()
suma_cuadrados = int()
palabras_con_vocal = int()
vocales = tuple()
texto = str()
ultima_letra = str()
pares = int()
impares = int()

#Inicializo variables
opcion = ""
numero = 0
repeticiones = 0
suma_cuadrados = 0
palabras_con_vocal = 0
vocales = ("a", "e", "i", "o", "u")
texto = ""
ultima_letra = ""
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

    #Suma de los cuadrados
    if (opcion == "A"):

        print("Suma de los cuadrados")
        repeticiones = int(input("¿Cuantos numeros queres ingresar?: "))

        for i in range(repeticiones):

            numero = int(input("Ingresa un numero: "))
            suma_cuadrados += numero ** 2

        print(f"\nLa suma del cuadrado de los numeros es {suma_cuadrados}")
        suma_cuadrados = 0 #Reinicio acumulador

    #Cantidad de palabras terminadas con vocal
    elif (opcion == "B"):

        print("Determinando palabras terminadas en vocal")
        print("Se debe cargar un texto finalizado con un punto\n")

        texto = input("Ingresa un texto: ").lower()
        
        #Le quito el punto al texto antes de iterar las cada una de las palabras
        if (texto.endswith(".")): texto_sin_punto = texto[0: len(texto)-1]
        else: texto_sin_punto = texto

        #Itero cada una de las palabras del texto
        for palabra in texto_sin_punto.split(): 

            ultima_letra = palabra[len(palabra) - 1]
            if (ultima_letra in vocales): palabras_con_vocal += 1

        print(f"\n{palabras_con_vocal} de las palabras ingresadas terminan con vocal")
        palabras_con_vocal = 0 #Reinicio contador

    #Cantidad de pares e impares
    elif (opcion == "C"):

        print("Determinando cantidad de numeros pares e impares")
        print("La carga finaliza cuando se ingresa el valor 0\n")

        while True:
            numero = int(input("Ingresa un numero: "))
            
            if (numero == 0): break
            elif (numero % 2 == 0): pares += 1
            else: impares += 1

        if (pares > impares): print("\nSe ingresaron mas numeros pares")
        elif (impares > pares): print("\nSe ingresaron mas numeros impares")
        else: print("\nSe ingresaron la misma cantidad de numeros pares e impares")

        #Reinicio contadores
        pares = 0
        impares = 0
    
    elif (opcion == "D"): break

    else: print("Opcion no valida")

    input("Pulse para continuar ")


#Prueba de escritorio
'''
Entradas y Salidas                         
-------------------------------------------------------------------------------------------------
Operaciones con secuencias numericas
A: Generar una serie de numeros y mostrar la suma de los cuadrados
B: Ingresar un texto y determinar la cantidad de palabras finalizadas con vocales
C: Ingresar una serie de numeros y determinar si hay mayor cantidad de valores pares o de impares
D: Salir")
Ingresa una opcion: A

Suma de los cuadrados
¿Cuantos numeros queres ingresar?: 3
Ingresa un numero: 2
Ingresa un numero: 5
Ingresa un numero: 10

La suma del cuadrado de los numeros es 129   (Primera Salida)
Pulse para continuar
-------------------------------------------------------------------------------------------------

Operaciones con secuencias numericas
A: Generar una serie de numeros y mostrar la suma de los cuadrados
B: Ingresar un texto y determinar la cantidad de palabras finalizadas con vocales
C: Ingresar una serie de numeros y determinar si hay mayor cantidad de valores pares o de impares
D: Salir")
Ingresa una opcion: B

Determinando palabras terminadas en vocal
Se debe cargar un texto finalizado con un punto

Ingresa un texto: que onda man.

2 de las palabras ingresadas terminan con vocal   (Segunda salida)
Pulse para continuar
-------------------------------------------------------------------------------------------------     

Operaciones con secuencias numericas
A: Generar una serie de numeros y mostrar la suma de los cuadrados
B: Ingresar un texto y determinar la cantidad de palabras finalizadas con vocales
C: Ingresar una serie de numeros y determinar si hay mayor cantidad de valores pares o de impares
D: Salir")
Ingresa una opcion: C


Determinando cantidad de numeros pares e impares
La carga finaliza cuando se ingresa el valor 0

Ingresa un numero: 10
Ingresa un numero: 15
Ingresa un numero: 20
Ingresa un numero: 25
Ingresa un numero: 30
Ingresa un numero: 0

Se ingresaron mas numeros pares  (Tercer salida)
Pulse para continuar
-------------------------------------------------------------------------------------------------

Operaciones con secuencias numericas
A: Generar una serie de numeros y mostrar la suma de los cuadrados
B: Ingresar un texto y determinar la cantidad de palabras finalizadas con vocales
C: Ingresar una serie de numeros y determinar si hay mayor cantidad de valores pares o de impares
D: Salir")
Ingresa una opcion: D
__________________________________________

Proceso (Valores que toman las variables)

opcion =                      "" | "A" | "B" | "C" | "D"
repeticiones =                 0 |  3
numero =                       0 |  2  |  5  |  10  | 10 |  15  |  20  |  25  |  30  |  0
suma_cuadrados =               0 |  4  | 29  |  129 | 0  (reinicio de acumulador)
palabras_con_vocal =           0 |  1  |  2  |  3   | 0  (reinicio de contador)
texto =                       "" | "que onda man."
texto_sin_punto =             "" | "que onda man"
ultima_letra =                "" | "e" | "a" | "n" 
pares =                        0 |  1  |  2  |  3   | 0  (reinicio de contador)
impares =                      0 |  1  |  2  |  0        (reinicio de contador)
vocales = ("a", "e", "i", "o", "u") 

'''
