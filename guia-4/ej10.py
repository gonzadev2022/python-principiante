import os
os.system("cls")

#Enunciado
# Diseñar el algoritmo correspondiente a un programa, que:
# a) Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# b) Carga la tabla con valores numéricos enteros.
# c) Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

#Declaro variables
filas = int()
columnas = int()

#Inicializo variables
filas = 5
columnas = 5

#Proceso
def CrearTabla(filas, columnas):

    tabla = []

    for f in range(filas):
        tabla.append([])
    
        for c in range(columnas):
            tabla[f].append(0)

    return tabla

#Creando tabla 5x5
tabla = CrearTabla(filas, columnas)

#Mostrando tabla
for fila in tabla:

    for elemento in fila:
        print(elemento, end="  ")
    print() #Salto de linea por fila


#Prueba de escritorio
'''
Sin Entrada                                 
__________________________________________

Salida (tabla 5x5)
0  0  0  0  0 
0  0  0  0  0 
0  0  0  0  0 
0  0  0  0  0 
0  0  0  0  0 
__________________________________________

Proceso (Valores que toman las variables)

tabla =
[[0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0]]

'''