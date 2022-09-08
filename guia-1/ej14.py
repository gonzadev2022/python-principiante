import os
os.system("cls")

#Enunciado
# Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.

#Declaro variables
ahorros = float()

#Inicializo variables
ahorros = 0.0

#Proceso
print("Ingresar sueldo de todos los meses para determinar ahorros\n")

for i in range(1, 13):
    ahorros += int(input(f"Sueldo Mes {i}: ")) * 0.10

print(f"\nTotal ahorrado: ${ahorros}")


#Prueba de escritorio
'''
Entrada                                 
Ingresar sueldo de todos los meses para determinar ahorros
Sueldo Mes 1: 1000
Sueldo Mes 2: 1000
Sueldo Mes 3: 1000
Sueldo Mes 4: 1000
Sueldo Mes 5: 2000
Sueldo Mes 6: 2000
Sueldo Mes 7: 2000
Sueldo Mes 8: 2000
Sueldo Mes 9: 3000
Sueldo Mes 10: 3000
Sueldo Mes 11: 3000
Sueldo Mes 12: 3000
__________________________________________
Salida
Total ahorrado: $2400
__________________________________________

Proceso (Valores que toman las variables)

ahorros = 0.0 | 100 | 200 | 300 | 400 | 600 | 800 | 1000 | 1200 | 1500 | 1800 | 2100 | 2400

'''