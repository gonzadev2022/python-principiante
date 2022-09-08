import os
os.system("cls")

#Enunciado
# Búsqueda de mayor Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de[0,100.000].

#Importo modulo necesario
import random

#Declaro variables
numero_random = int()
repeticiones = int()
numero_mayor = int()

#Inicializo variables
numero_random = 0
repeticiones = 10000
numero_mayor = 0

#Proceso
for i in range(repeticiones):
    numero_random = random.randint(0, 100000)
    
    #Guardo el mayor numero aleatorio generado 
    if (i == 0 or numero_random > numero_mayor):
        numero_mayor = numero_random

print(f"El mayor numero de los {repeticiones} numeros aleatorios generados fue el {numero_mayor}")


#Prueba de escritorio
'''
Sin entradas                           
__________________________________________
Salida
El mayor numero de los 10000 numeros aleatorios generados fue el 99993 (ejemplo)
__________________________________________

Proceso (Valores que toman las variables)

repeticiones = 10000
numero_random = (aleatorio)
numero_mayor = (depende de la variable nro_random)
'''

