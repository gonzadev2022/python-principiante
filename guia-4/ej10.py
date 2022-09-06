import os
os.system("cls")

#Enunciado
# Diseñar el algoritmo correspondiente a un programa, que:
# a) Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# b) Carga la tabla con valores numéricos enteros.
# c) Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

#Declaro variables
tabla = list()
filas = int()
columnas = int()

#Inicializo variables
tabla = []
filas = 5
columnas = 5

#Proceso
def crearTabla(filas, columnas):

    for f in range(filas):
        tabla.append([])
    
        for c in range(columnas):
            tabla[f].append(0)

    return tabla

tabla = crearTabla(filas, columnas)

#Mostrando tabla
for fila in tabla:

    for elemento in fila:
        print(elemento, end="  ")
    print() #Salto de linea por fila
