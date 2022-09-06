import os
os.system("cls")

#Enunciado
# Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
# a) Determinar y mostrar el nombre del ganador de la carrera.
# b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
# c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.

#Declaro variables
competidores = int()
tiempoRecord = int()
nombreActual = str()
tiempoActual = int()
ganador = str()
mejorTiempo = int()

#Inicializo variables
competidores = 0
tiempoRecord = 0
nombreActual = ""
tiempoActual = 0
ganador = ""
mejorTiempo = 0

#Proceso
print("Carrera de ciclistas")
competidores = int(input("Ingresar el numero de competidores: "))
tiempoRecord = int(input("Ingresar el tiempo record registrado para esta carrera: "))

for i in range(competidores):
    nombreActual = input(f"\nNombre del competidor {i+1}: ")
    tiempoActual = int(input(f"Tiempo de carrera: "))

    if (i == 0 or tiempoActual < mejorTiempo):
        ganador = nombreActual
        mejorTiempo = tiempoActual

#Resultados finales
print(f"\nEl ganador de la carrera es {ganador} con un tiempo de {mejorTiempo}")

if (mejorTiempo < tiempoRecord): 
    print("Supero el tiempo record registrado")
else: 
    print("No supero el tiempo record registrado")
