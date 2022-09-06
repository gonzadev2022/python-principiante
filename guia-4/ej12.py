import os
os.system("cls")

#Enunciado
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’. Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
# 111111111111111
# 100000000000001
# 100000000000001
# 100000000000001
# 111111111111111
# Visualiza el contenido de la matriz en pantalla.

#Declaro variables
tabla = list()
filas = int()
columnas = int()

#Inicializo variables
tabla = []
filas = 5
columnas = 15

#Proceso
def crearTablaMarco(filas, columnas):

    for f in range(filas):
        tabla.append([])

        for c in range(columnas):
            if (f == 0 or f == filas-1): n = 1
            elif (c == 0 or c == columnas-1): n = 1
            else: n = 0
            tabla[f].append(n)
    
    return tabla

tabla = crearTablaMarco(filas, columnas)

#Mostrando tabla
for fila in tabla:

    for elemento in fila:
        print(elemento, end=" ")
    print() #Salto de linea por fila