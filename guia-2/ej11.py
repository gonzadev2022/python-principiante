import os
os.system("cls")

#Enunciado
# Menores y promedio Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que permita:Determinar el menor de los numeros generados en forma aleatoria.Calcular el valor promedio de los números menores a 10.000.

#Importo modulo necesario
import random

#Declaro variables
numeroRandom = int()
repeticiones = int()
numeroMenor = int()
menoresQueMil = int()
cantidad_menoresQueMil = int()
promedio = float()

#Inicializo variables
numeroRandom = 0
repeticiones = 5000
numeroMenor = 0
menoresQueMil = 0  #Acumulador
cantidad_menoresQueMil = 0 #Contador
promedio = 0.0

#Proceso
for i in range(repeticiones):
    numeroRandom = random.randint(0, 100000)
    
    if (i == 0 or numeroRandom < numeroMenor):
        numeroMenor = numeroRandom
    
    if (numeroRandom < 1000):
        menoresQueMil += numeroRandom
        cantidad_menoresQueMil += 1

promedio = menoresQueMil / cantidad_menoresQueMil

print(f"El menor numero de los {repeticiones} numeros aleatorios generados fue el {numeroMenor}")
print(f"El promedio de los numeros menores a 1000 es de {promedio}")