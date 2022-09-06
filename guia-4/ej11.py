import os
os.system("cls")

#Enunciado
# Diseñar el algoritmo correspondiente a un programa, que:
# a) Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# b) Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
# c) Muestra el contenido de la tabla en pantalla.

#Declaro variables
tabla = list()
filas = int()
columnas = int()

#Inicializo variables
tabla = []
filas = 5
columnas = 5

#Proceso
def crearTablaDiagonal(filas, columnas):

    for f in range(filas):
        tabla.append([])
    
        for c in range(columnas):

            if (f == c or f + c == (columnas-1)): n = 1
            else: n = 0
            tabla[f].append(n)
        
    return tabla

tabla = crearTablaDiagonal(filas, columnas)

#Mostrando tabla
for fila in tabla:

    for elemento in fila:
        print(elemento, end="  ")
    print() #Salto de linea por fila