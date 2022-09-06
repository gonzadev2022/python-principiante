import os
os.system("cls")

#Enunciado
# Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.

#Declaro variables
n = int()

#Inicializo variables
n = 0

#Proceso
n = int(input("Ingrese un numero: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")