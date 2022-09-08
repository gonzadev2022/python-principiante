import os
os.system("cls")

#Enunciado
# Promedio de números aleatorios: Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de[0,100000].

#Importo modulo necesario
import random

#Declaro variables
numero_random = int()
total = int()
repeticiones = int()
promedio = float()

#Inicializo variables
numero_random = 0
total = 0
repeticiones = 1000
promedio = 0.0

#Proceso
for i in range(repeticiones):
    numero_random = random.randint(0, 100000)
    total += numero_random

promedio = total / repeticiones

print(f"El promedio de los {repeticiones} numeros aleatorios es de {promedio}")

#Prueba de escritorio
'''
Sin Entradas                             
__________________________________________
Salida
El promedio de 1000 los numeros aleatorios es de 48172 (ejemplo)
__________________________________________

Proceso (Valores que toman las variables)

repeticiones =  1000 | 
numero_random =    0 | (aleatorio)
total =            0 | (depende de la variable nro_random)
promedio =       0.0 | (depende de la variable total)

'''