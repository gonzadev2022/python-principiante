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
a = int(input("Ingrese un dividendo: "))
b = int(input("Ingrese un divisor: "))

print(f"\nEl cociente es {int( a / b)}")
print(f"El resto es {a % b}")

#Prueba de escritorio
'''
Entrada                                 
Ingrese un dividendo: 11
Ingrese un divisor: 2  
__________________________________________

Salida
El cociente es 5
El resto es 1
__________________________________________

Proceso (Valores que toman las variables)
a = 0 | 11
b = 0 | 2

'''