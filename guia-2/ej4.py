import os
os.system("cls")

#Enunciado
# Decimal a Hexadecimal: Generar n números aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar el numero hexadecimal.

#Importo modulo necesario
import random

#Declaro variables
repeticiones = int()
decimal = int()
hexadecimal = int()

#Inicializo variables
repeticiones = 0
decimal = 0
hexadecimal = 0

#Proceso
print("Conversion de Numeros decimales a hexadecimales")
repeticiones = int(input("Ingresar la cantidad de numeros aleatorios a generar: "))

for i in range(repeticiones):
    decimal = random.randint(5000, 45000)
    hexadecimal = hex(decimal)
    print(f"Numero decimal: {decimal}   Numero hexadecimal: {hexadecimal}")


#Prueba de escritorio
'''
Entrada                                 
Conversion de Numeros decimales a hexadecimales
Ingresar la cantidad de numeros aleatorios a generar: 3
__________________________________________

Salida
Numero decimal: 22110  Numero hexadecimal: 0x565e
Numero decimal: 22346  Numero hexadecimal: 0x574a
Numero decimal: 27092  Numero hexadecimal: 0x69d4
__________________________________________

Proceso (Valores que toman las variables)

repeticiones = 0 | 3
decimal =      0 | 22110  | 22346  | 27092
hexadecimal =  0 | 0x565e | 0x574a | 0x69d4

'''