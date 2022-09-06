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

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))

