import random
import os
os.system("cls")

#Enunciado
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

#Declaro variables
numeros = list()

#Inicializo variables
numeros = []

#Proceso
for i in range(10):
    numeros.append(random.randint(1, 10))

for n in numeros:
    print(f"{n} al cuadrado = {n**2}   {n} al cubo = {n**3}")


#Prueba de escritorio
'''
Se generan 10 numeros aleatorios entre el 1 y el 10                                 
__________________________________________

Salida

7  al cuadrado = 49    7 al cubo = 343
5  al cuadrado = 25    5 al cubo = 125
9  al cuadrado = 81    9 al cubo = 729
9  al cuadrado = 81    9 al cubo = 729
5  al cuadrado = 25    5 al cubo = 125
1  al cuadrado = 1     1 al cubo = 1
3  al cuadrado = 9     3 al cubo = 27
2  al cuadrado = 4     2 al cubo = 8
7  al cuadrado = 49    7 al cubo = 343
10 al cuadrado = 100   10 al cubo = 1000
__________________________________________

'''