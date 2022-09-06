import os
os.system("cls")

#Enunciado
# Promedio de números aleatorios: Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de[0,100000].

#Importo modulo necesario
import random

#Declaro variables
numeroRandom = int()
total = int()
repeticiones = int()
promedio = float()

#Inicializo variables
numeroRandom = 0
total = 0
repeticiones = 1000
promedio = 0.0

#Proceso
for i in range(repeticiones):
    numeroRandom = random.randint(0, 100000)
    total += numeroRandom

promedio = total / repeticiones

print(f"El promedio de los {repeticiones} numeros aleatorios es de {promedio}")
