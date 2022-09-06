import os
os.system("cls")

#Enunciado
# División con resto. Plantear un algoritmo que permita informar, para dos valores a y b el resultado de la división a/b y el resto de esa división.

#Declaro variables
a = int()
b = int()

#Inicializo variables
a = 0
b = 0

#Proceso
a = int(input("Ingrese el dividendo: "))
b = int(input("Ingrese el divisor: "))

print(f"\nEl cociente es {int( a / b)}")
print(f"El resto es {a % b}")