import os
os.system("cls")

#Enunciado
# Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.

#Declaro variables
n = int()

#Inicializo variables
n = 0

#Proceso
n = int(input("Consulta la tabla de un numero: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


#Prueba de escritorio
'''
Entrada                                 
Consulta la tabla de un numero: 12
__________________________________________

Salida
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
__________________________________________

Proceso (Valores que toman las variables)
n = 0 | 12
i = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12

'''