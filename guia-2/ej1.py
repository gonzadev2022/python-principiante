import os
os.system("cls")

#Enunciado
# Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
# a) Determinar y mostrar el nombre del ganador de la carrera.
# b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
# c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.

#Declaro variables
competidores = int()
tiempo_record = int()
nombre_actual = str()
tiempo_actual = int()
ganador = str()
menor_tiempo = int()

#Inicializo variables
competidores = 0
tiempo_record = 0
nombre_actual = ""
tiempo_actual = 0
ganador = ""
menor_tiempo = 0

#Proceso
print("Carrera de ciclistas")
competidores = int(input("Ingresar el numero de competidores: "))
tiempo_record = int(input("Ingresar el tiempo record registrado para esta carrera (en minutos): "))

for i in range(competidores):
    nombre_actual = input(f"\nNombre del competidor {i+1}: ")
    tiempo_actual = int(input(f"Tiempo de carrera: "))

    #Guardo valores en caso de ser la primera iteracion o si el tiempo actual es menor al menor tiempo registrado
    if (i == 0 or tiempo_actual < menor_tiempo):
        ganador = nombre_actual
        menor_tiempo = tiempo_actual

#Resultados finales
print(f"\nEl ganador de la carrera es {ganador} con un tiempo de {menor_tiempo} minutos")

if (menor_tiempo < tiempo_record): 
    print("Supero el tiempo record registrado")
else: 
    print("No supero el tiempo record registrado")


#Prueba de escritorio
'''
Entrada                                 
Carrera de ciclistas
Ingresar el numero de competidores: 3
Ingresar el tiempo record registrado para esta carrera (en minutos): 80

Nombre del competidor 1: El rayo macqueen
Tiempo de carrera: 90

Nombre del competidor 2: Nikola Tesla
Tiempo de carrera: 70

Nombre del competidor 3: Mario Bros
Tiempo de carrera: 100

__________________________________________

Salida
El ganador de la carrera es Nikola Tesla con un tiempo de 70 minutos
Supero el tiempo record registrado
__________________________________________

Proceso (Valores que toman las variables)

competidores =   0  | 3
tiempo_record =  0  | 80
nombre_actual =  "" | "El rayo macqueen" | "Nikola Tesla" | "Mario Bros"
tiempo_actual =  0  | 90 | 70 | 100
ganador =        "" | "El rayo macqueen" | "Nikola Tesla"
menor_tiempo =   0  | 90 | 70

'''