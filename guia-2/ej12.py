import os
os.system("cls")

#Enunciado
# Números pares e impares Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo. Los requerimientos funcionales del programa son: La sumatoria de solo los números que estén comprendidos entre 50 y 100. Cantidad de valores pares ingresados. Cantidad de valores impares ingresados. Informar si en la carga de números se ingreso al menos un número 0. Informar si la serie contiene solo números pares e impares alternados.

#Declaro variables
numeroActual = int()
suma = int()
contadorDePares = int()
contadorDeImpares = int()
ingresoDeCeros = bool()
numerosIngresados = int()
serieAlternada = bool()
numeroAnterior = int()

#Inicializo variables
numeroActual = 0
suma = 0
contadorDePares = 0
contadorDeImpares = 0
ingresoDeCeros = False
numerosIngresados = 0
serieAlternada = True
numeroAnterior = 0

#Proceso
print("La carga general finalizara cuando se ingrese un numero negativo")
while True:
    numeroActual = int(input("Ingresa un numero: "))
    if (numeroActual < 0): break
    
    numerosIngresados += 1 

    #Determinamos si el numero es par o impar
    if (numeroActual % 2 == 0): contadorDePares += 1
    else: contadorDeImpares += 1

    #Sumatoria de nros comprendidos entre 50 y 100
    if (numeroActual >= 50 and numeroActual <= 100):
        suma += numeroActual

    #Informamos si se ingresa un cero
    if (numeroActual == 0): ingresoDeCeros = True


    #Se ejecuta si la serie sigue siendo alternada
    if (serieAlternada):

        if (numerosIngresados == 1):
            numeroAnterior = numeroActual

        else:
            if (numeroAnterior % 2 == 0): #En caso de nro anterior par
                if (numeroActual % 2 == 0): serieAlternada = False
            
            else:  #En caso de nro anterior impar
                if (numeroActual % 2 != 0): serieAlternada = False
            
            numeroAnterior = numeroActual #Guardo el numero para la siguente comparacion


print("\nInforme general")
print(f"Cantidad de numeros pares ingresados: {contadorDePares}")
print(f"Cantidad de numeros impares ingresados: {contadorDeImpares}")
print(f"Sumatoria de numeros comprendidos entre 50 y 100: {suma}")

if (ingresoDeCeros): print("Se ingreso al menos un cero")
else: print("No se ingresaron ceros")

if (serieAlternada): print("La serie numerica es alternada")
else: print("La serie numerica NO es alternada")



