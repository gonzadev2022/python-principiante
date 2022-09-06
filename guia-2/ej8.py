import os
os.system("cls")

#Enunciado
# Ventas por sucursal. Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes sucursales de un país de una determinada empresa. Los requerimientos del programa son: Informar la cantidad de ventas ingresadas. Total de ventas. Cantidad de ventas cuyo valores estén comprendidos entre 100 y 300 unidades. Cantidad de ventas con 400,500 y 600 unidades. Indicar si hubo una cantidad de ventas inferior a 50 unidades. Usted deberá ingresar cantidad es de ventas hasta que se ingrese un valor negativo.

#Declaro variables
ventasDeSucursal = int()
cantidadDeVentas = int() #Contador
ventasTotales = int() #Acumulador
ventasBajas = int() #Contador
ventasMedias = int() #Contador
ventasAltas = int() #Contador

#Inicializo variables
ventasDeSucursal = 0
cantidadDeVentas = 0
ventasTotales = 0
ventasBajas = 0
ventasMedias = 0
ventasAltas = 0

#Proceso
while True:
    ventasDeSucursal = int(input("Ingresar las ventas de la sucursal: "))
    if (ventasDeSucursal < 0): break 

    if (ventasDeSucursal < 50): ventasBajas += 1
    elif (ventasDeSucursal >= 100 and ventasDeSucursal <= 300): ventasMedias += 1
    elif (ventasDeSucursal >= 400 and ventasDeSucursal <= 600): ventasAltas += 1

    cantidadDeVentas += 1
    ventasTotales += ventasDeSucursal

#Resultados finales
print("\nInforme general")
print(f"Cantidad de ventas ingresadas: {cantidadDeVentas} sucursales")
print(f"Total de ventas: {ventasTotales}")
print(f"Cantidad de ventas medias (entre 100 y 300 unidades): en {ventasMedias} sucursales")
print(f"Cantidad de ventas altas (entre 400 y 600 unidades): en {ventasAltas} sucursales")

if (ventasBajas > 0): print("Hubo una cantidad de ventas inferior a 50 unidades")
else: print("No hubo una de ventas inferior a 50 unidades")

