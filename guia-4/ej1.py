import random
import os
os.system("cls")

#Enunciado
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

#Declaro variables
numeros = list()
cuadrado = int()
cubo = int()

#Inicializo variables
numeros = []
cuadrado = 0
cubo = 0

#Proceso
for i in range(10):
    numeros.append(random.randint(1, 10))

for n in numeros:
    print(f"Numero: {n}   Al cuadrado: {n*2}   Al cubo: {n*3}")


