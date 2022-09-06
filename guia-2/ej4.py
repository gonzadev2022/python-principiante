import os
os.system("cls")

#Enunciado
# Decimal a Hexadecimal: Generar n números aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar el numero hexadecimal.

#Importo modulo necesario
import random

#Declaro variables
n = int()
numeroDecimal = int()
numeroHexadecimal = int()

#Inicializo variables
numeroDecimal = 0
numeroHexadecimal = 0

#Proceso
print("Conversion de Numeros decimales a hexadecimales")
n = int(input("Ingresar la cantidad de numeros aleatorios a generar: "))

for i in range(n):
    numeroDecimal = random.randint(5000, 45000)
    numeroHexadecimal = hex(numeroDecimal)
    print(f"Numero decimal: {numeroDecimal}   Numero hexadecimal: {numeroHexadecimal}")