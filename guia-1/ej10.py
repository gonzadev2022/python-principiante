import os
os.system("cls")

#Enunciado
# Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.

#Declaro variables
fibo = list()
n = int()

#Inicializo variables
fibo = []
n = 0

#Proceso
def fibonacci(n):
    fibo = [0, 1]

    if (n <= 0): return "Numero fuera de rango"
    if (n == 1): return 0
    if (n == 2): return fibo

    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo

n = int(input("¿Cuantos numeros de la secuencia de fibonacci queres ver?: "))
print(fibonacci(n))   


#Prueba de escritorio
'''
Entrada                                 
¿Cuantos numeros de la secuencia de fibonacci queres ver?: 10
__________________________________________

Salida
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
__________________________________________

Proceso (Valores que toman las variables)
n = 0 | 10

'''
