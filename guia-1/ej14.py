import os
os.system("cls")

#Enunciado
# Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.

#Declaro variables
ahorros = float()

#Inicializo variables
ahorros = 0.0

#Proceso
print("Ingresar sueldo del mes para determinar ahorros\n")

for i in range(1, 13):
    ahorros += int(input(f"Sueldo Mes {i}: ")) * 0.10

print(f"\nTotal ahorrado: ${ahorros}")