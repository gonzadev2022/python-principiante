import os
os.system("cls")

#Enunciado
# Menores y promedio Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que permita:Determinar el menor de los numeros generados en forma aleatoria.Calcular el valor promedio de los números menores a 10.000.

#Importo modulo necesario
import random

#Declaro variables
numero_random = int()
repeticiones = int()
menor = int()
menoresQueMil = int()
cantidad_menoresQueMil = int()
promedio = float()

#Inicializo variables
numero_random = 0
repeticiones = 5000
menor = 0
menores_que_mil = 0  #Acumulador
cantidad_menores_que_mil = 0 #Contador
promedio = 0.0

#Proceso
for i in range(repeticiones):
    numero_random = random.randint(0, 100000)
    
    #Guardo numero menor aleatorio generado
    if (i == 0 or numero_random < menor):
        menor = numero_random
    
    #Guardo numeros menores que mil
    if (numero_random < 1000):
        menores_que_mil += numero_random
        cantidad_menores_que_mil += 1

#Calculo promedio de los numeros menores que mil
promedio = menores_que_mil / cantidad_menores_que_mil

print(f"El menor numero de los {repeticiones} numeros aleatorios generados fue el {menor}")
print(f"El promedio de los numeros menores a 1000 es de {promedio}")

#Prueba de escritorio
'''
Sin Entradas                             
__________________________________________
Salida
El menor numero de los 5000 numeros aleatorios generados fue el 122 (ejemplo)
El promedio de los numeros menores a 1000 es de 567.05 (ejemplo)
__________________________________________

Proceso (Valores que toman las variables)

repeticiones =          5000 |
numero_random =            0 | (aleatorio)

(el resto de variables dependen del nro_random generado)
menor =                    0 | 
menores_que_mil =          0 | 
cantidad_menores_que_mil = 0 |
promedio =               0.0 |

'''