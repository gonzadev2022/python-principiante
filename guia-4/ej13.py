import os
os.system("cls")

#Enunciado
# Una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
# - Nombre: Lista para guardar los nombres de los conductores.
# - kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor. Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

#Declaro variables
nombre = list()
kms = list()
total_kms = list()

#Inicializo variables
nombre = []
kms = []
total_kms = []

#Proceso
nombre = ["matias", "ivan", "fernando", "carlitos", "markitos"]
kms = [
    [5, 5, 5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6, 6, 6],
    [7, 7, 7, 7, 7, 7, 7],
    [8, 8, 8, 8, 8, 8, 8],
    [9, 9, 9, 9, 9, 9, 9]
]

#Creando lista anidada con conductores y sus respectivos km recorridos
for i in range(len(nombre)):
    total_kms.append([nombre[i], sum(kms[i])])

#Mostrando lista
for conductor in total_kms:
    print(f"El conductor {conductor[0]} realizo {conductor[1]} kilometros")

#Prueba de escritorio
'''
Sin Entrada                                 
__________________________________________

Salida
El conductor matias realizo 35 kilometros
El conductor ivan realizo 42 kilometros
El conductor fernando realizo 49 kilometros
El conductor carlitos realizo 56 kilometros
El conductor markitos realizo 63 kilometros
__________________________________________

Proceso (Valores que toman las variables)

total_kms =
[
 ["matias", 35]
 ["ivan", 42]
 ["fernando", 49]
 ["carlitos", 56]
 ["markitos", 63]
]

'''