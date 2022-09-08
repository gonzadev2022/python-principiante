import os
os.system("cls")

#Enunciado
# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
# A Las cantidades totales de cada artículo.
# B La cantidad de artículos en la sucursal 2.
# C La cantidad del artículo 3 en la sucursal 1.
# D La recaudación total de cada sucursal.
# E La recaudación total de la empresa.
# F La sucursal de mayor recaudación.

#Declaro variables
precio_articulo = list()   #Precio de articulos
sucursales = list()        #Cantidad de articulos por sucursal
ventas = int()
total_ventas = int()
mayores_ventas = int()
sucursalMayoresVentas = int()
articulos = int()

#Inicializo variables
precio_articulo = [100, 200, 300, 400, 500]
sucursales = [
    [10, 20, 30, 40, 50], #Sucursal 1
    [10, 15, 20, 25, 30], #Sucursal 2
    [10, 25, 35, 45, 55], #Sucursal 3
    [10, 12, 14, 16, 18]  #Sucursal 4
]
ventas = 0
total_ventas = 0
mayores_ventas = 0
sucursal_mayores_ventas = 0
articulos = 0

#Proceso

#Punto A: Cantidades de cada articulo
print("Cantidades totales de cada articulo")

for a in range(5): #5 Articulos
    
    for s in range(4): #4 Sucursales
        articulos += sucursales[s][a]
    
    print(f"Articulo {a+1}: {articulos} unidades") 
    articulos = 0

#Punto B y Punto C
print(f"\nCantidad de articulos en la sucursal 2: {sum(sucursales[1])} unidades") 
print(f"Cantidad del articulo 3 en la sucursal 1: {sucursales[0][2]} unidades")   

#Punto D
print("\nRecaudaciones por sucursal")

for s in range(4): #4 sucursales
    
    for i in range(5): #5 articulos
        ventas += precio_articulo[i] * sucursales[s][i]

    if (s == 0 or ventas > mayores_ventas):
        mayores_ventas = ventas
        sucursal_mayores_ventas = s+1

    print(f"Sucursal {s+1}: ${ventas}") 
    total_ventas += ventas
    ventas = 0
    
#Punto E y Punto F
print(f"\nRecaudacion total de la empresa: ${total_ventas}")
print(f"La sucursal {sucursal_mayores_ventas} tuvo la mayor recaudacion") 


#Prueba de escritorio
'''
Sin entradas por teclado                                 
Para el proceso de utilizan variables precio_articulo y sucursales

precio_articulo = [100, 200, 300, 400, 500]
sucursales = [
    [10, 20, 30, 40, 50], #Sucursal 1
    [10, 15, 20, 25, 30], #Sucursal 2
    [10, 25, 35, 45, 55], #Sucursal 3
    [10, 12, 14, 16, 18]  #Sucursal 4
]
__________________________________________

Salida
Cantidades totales de cada articulo
Articulo 1: 40 unidades
Articulo 2: 72 unidades
Articulo 3: 99 unidades
Articulo 4: 126 unidades
Articulo 5: 153 unidades

Cantidad de articulos en la sucursal 2: 100 unidades
Cantidad del articulo 3 en la sucursal 1: 30 unidades

Recaudaciones por sucursal
Sucursal 1: $55000
Sucursal 2: $35000
Sucursal 3: $62000
Sucursal 4: $23000

Recaudacion total de la empresa: $175000
La sucursal 3 tuvo la mayor recaudacion

'''