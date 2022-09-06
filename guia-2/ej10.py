import os
os.system("cls")

#Enunciado
# Búsqueda de mayor Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de[0,100.000].

#Importo modulo necesario
import random

#Declaro variables
numeroRandom = int()
repeticiones = int()
numeroMayor = int()

#Inicializo variables
numeroRandom = 0
repeticiones = 10000
numeroMayor = 0

#Proceso
for i in range(repeticiones):
    numeroRandom = random.randint(0, 100000)
    
    if (i == 0 or numeroRandom > numeroMayor):
        numeroMayor = numeroRandom

print(f"El mayor numero de los {repeticiones} numeros aleatorios generados fue el {numeroMayor}")

