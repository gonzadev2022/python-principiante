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
filas = int()
columnas = int()

#Inicializo variables
filas = 5
columnas = 15

#Proceso
def CrearTablaMarco(filas, columnas):

    tabla = []

    for f in range(filas):
        tabla.append([])

        for c in range(columnas):
            if (f == 0 or f == filas-1): n = 1
            elif (c == 0 or c == columnas-1): n = 1
            else: n = 0
            tabla[f].append(n)
    
    return tabla

#Creando tabla marco 5x15
marco = CrearTablaMarco(filas, columnas)

#Mostrando tabla
for fila in marco:

    for elemento in fila:
        print(elemento, end=" ")
    print() #Salto de linea por fila


#Prueba de escritorio
'''
Sin Entrada                                                        
__________________________________________

Salida
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
__________________________________________

Proceso (Valores que toman las variables)

marco =
[
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

'''