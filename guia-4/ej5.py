import random
import os
os.system("cls")

#Enunciado
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.

#Declaro variables
numeros = list()

#Inicializo variables
numeros = []

#Proceso
for i in range(10):
    numeros.append(random.randint(1, 100))

print(f"Lista aleatoria inicial: {numeros}")
numeros.sort()
print(f"Lista ordenada: {numeros}")


#Prueba de escritorio
'''
Sin Entrada                                 
__________________________________________
Salida
Lista aleatoria inicial: [17, 49, 93, 69, 10, 66, 48, 26, 49, 72] 
Lista ordenada: [10, 17, 26, 48, 49, 49, 66, 69, 72, 93]
__________________________________________

'''