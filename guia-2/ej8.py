import os
os.system("cls")

#Enunciado
# Ventas por sucursal. Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes sucursales de un país de una determinada empresa. Los requerimientos del programa son: Informar la cantidad de ventas ingresadas. Total de ventas. Cantidad de ventas cuyo valores estén comprendidos entre 100 y 300 unidades. Cantidad de ventas con 400,500 y 600 unidades. Indicar si hubo una cantidad de ventas inferior a 50 unidades. Usted deberá ingresar cantidad es de ventas hasta que se ingrese un valor negativo.

#Declaro variables
ventas_de_sucursal = int()
cantidad_de_ventas = int()
ventas_totales = int()
ventas_bajas = int()
ventas_medias = int()
ventas_altas = int()

#Inicializo variables
ventas_de_sucursal = 0
cantidad_de_ventas = 0
ventas_totales = 0
ventas_bajas = 0
ventas_medias = 0
ventas_altas = 0

#Proceso
print("Ventas de sucursal")
print("La carga finaliza cuando se ingresa un numero negativo\n")

while True:
    ventas_de_sucursal = int(input("Ingresar las ventas de la sucursal: "))
    if (ventas_de_sucursal < 0): break 

    #Dependiendo la cantidad de ventas las clasifico como bajas, medias o altas
    if (ventas_de_sucursal < 50): ventas_bajas += 1
    elif (ventas_de_sucursal >= 100 and ventas_de_sucursal <= 300): ventas_medias += 1
    elif (ventas_de_sucursal >= 400 and ventas_de_sucursal <= 600): ventas_altas += 1

    cantidad_de_ventas += 1
    ventas_totales += ventas_de_sucursal

#Resultados finales
print("\nInforme general")
print(f"Cantidad de ventas ingresadas: {cantidad_de_ventas} sucursales")
print(f"Total de ventas: {ventas_totales}")
print(f"Cantidad de ventas medias (entre 100 y 300 unidades): en {ventas_medias} sucursales")
print(f"Cantidad de ventas altas (entre 400 y 600 unidades): en {ventas_altas} sucursales")

if (ventas_bajas > 0): print("Hubo una cantidad de ventas inferior a 50 unidades")
else: print("No hubo una cantidad de ventas inferior a 50 unidades")


#Prueba de escritorio
'''
Entrada             
Ventas de sucursal
La carga finaliza cuando se ingresa un cero                   
Ingresar las ventas de la sucursal: 40
Ingresar las ventas de la sucursal: 100
Ingresar las ventas de la sucursal: 200
Ingresar las ventas de la sucursal: 300
Ingresar las ventas de la sucursal: 500
Ingresar las ventas de la sucursal: 0
__________________________________________

Salida
Informe general
Cantidad de ventas ingresadas: 5 sucursales
Total de ventas: 1140
Cantidad de ventas medias (entre 100 y 300 unidades): en 3 sucursales
Cantidad de ventas altas (entre 400 y 600 unidades): en 1 sucursales
Hubo una cantidad de ventas inferior a 50 unidades
__________________________________________

Proceso (Valores que toman las variables)

ventas_de_sucursal =  0 | 40 | 100 | 200 | 300 | 500
cantidad_de_ventas =  0 | 1  |  2  |  3  |  4  |  5
ventas_totales =      0 | 40 | 140 | 340 | 640 | 1140
ventas_bajas =        0 | 1
ventas_medias =       0 | 1  |  2  |  3
ventas_altas =        0 | 1

'''