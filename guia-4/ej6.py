import os
os.system("cls")

#Enunciado
# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

#Declaro variables
mes = list()
dias_del_mes = list()
n = int()

#Inicializo variables
mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = 0

#Proceso
n = int(input("Ingresar un numero de mes: "))

#Validacion
while (n < 1 or n > 12):
    print("El numero de mes debe estar en el rango del 1 al 12")
    n = int(input("\nIngresar un numero de mes: "))

print(f"{mes[n-1]} tiene {dias_del_mes[n-1]} dias")


#Prueba de escritorio
'''
Entrada                                 
Ingresar un numero de mes: 11
__________________________________________

Salida
Noviembre tiene 30 dias
__________________________________________

'''