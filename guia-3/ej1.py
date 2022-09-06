import os
os.system("cls")

#Enunciado
# Comisión de vendedores. Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores, para ello les solicita un sistemita que le permita calcular dichos montos. Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores(1 a 4).Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta(el proceso termina cuando se ingrese una categoría igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos:
# Categoría1:cobra una comisión de 10%
# Categoría2: cobra una comisión de 25%
# Categoría3:cobra una comisión de 30%
# Categoría4:cobra una comisión de 40%
# Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedor es que en el la empresa junto con el total general.

#Declaro variables
categoria = int()
ventas = int()
comision1 = int()
comision2 = int()
comision3 = int()
comision4 = int()
totalComisiones = int() 

#Inicializo variables
categoria = 0
ventas = 0
comision1 = 0
comision2 = 0
comision3 = 0
comision4 = 0
totalComisiones = 0 
    
#Proceso
print("Comisiones de vendedores")
print("La carga de datos finaliza cuando se ingrese categoria 0")

while True:
    print("\nDatos del vendedor")
    categoria = int(input("Categoria (1 al 4): "))
    ventas = int(input("Ventas realizadas: "))

    if (categoria == 0): break
    elif (categoria == 1): comision1 += ventas * 0.10
    elif (categoria == 2): comision2 += ventas * 0.25
    elif (categoria == 3): comision3 += ventas * 0.30
    elif (categoria == 4): comision4 += ventas * 0.40
    else: print("Categoria fuera de rango")

comisionesTotales = comision1 + comision2 + comision3 + comision4

print("\nInforme general")
print(f"Comisiones Categoria 1: {int(comision1)}")
print(f"Comisiones Categoria 2: {int(comision2)}")
print(f"Comisiones Categoria 3: {int(comision3)}")
print(f"Comisiones Categoria 4: {int(comision4)}")
print(f"Comisiones totales a abonar: {int(comisionesTotales)}")
