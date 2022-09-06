import os
os.system("cls")

#Enunciado
# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

#Declaro variables
meses = list()
diasMeses = list()
numero = int()

#Inicializo variables
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
diasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = 0

#Proceso
n = int(input("Ingresar un numero de mes: "))

while (n < 1 or n > 12):
    print("El numero de mes debe estar en el rango del 1 al 12")
    n = int(input("\nIngresar un numero de mes: "))

print(f"{meses[n-1]} tiene {diasMeses[n-1]} dias")