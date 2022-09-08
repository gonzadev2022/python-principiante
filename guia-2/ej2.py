import os
os.system("cls")

#Enunciado
# Secuencia de impares. Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente.

#Declaro variables
a = int()
b = int()

#Inicializo variables
a = 0
b = 0

#Proceso
print("Secuencia de impares")
a = int(input("Ingresa el valor del numero A: "))
b = int(input("Ingresa el valor del numero B: "))

#Validacion
while a > b:
    print("\nEl numero A debe ser menor al numero B")
    a = int(input("Ingresa el valor del numero A: "))
    b = int(input("Ingresa el valor del numero B: "))

print("\nSecuencia de impares entre A y B en forma ascendente")
for n in range(a, b+1):
    if (n % 2 != 0): print(n, end= "  ")

print("\n\nSecuencia de impares entre A y B en forma descendente")
for n in range(b, a-1, -1):
    if (n % 2 != 0): print(n, end= "  ")


#Prueba de escritorio
'''
Entrada                                 
Secuencia de impares
Ingresa el valor del numero A: 1
Ingresa el valor del numero B: 21
__________________________________________

Salida
Secuencia de impares entre A y B en forma ascendente
1  3  5  7  9  11  13  15  17  19  21

Secuencia de impares entre A y B en forma descendente
21  19  17  15  13  11  9  7  5  3  1
__________________________________________

Proceso (Valores que toman las variables)

a = 0 | 1
b = 0 | 21

n = 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21
   21 | 19 | 17 | 15 | 13 | 11 | 9 | 7 | 5 | 3 | 1
'''