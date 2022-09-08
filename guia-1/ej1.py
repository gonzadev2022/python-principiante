import os
os.system("cls")

#Enunciado
# Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras.

#Declaro variables
kilogramos = float()
libras = float()

#Inicializo variables
kilogramos = 0
libras = 0

#Proceso
kilogramos = float(input("Ingrese una cantidad de kilogramos: "))
libras = kilogramos * 2.2

print(f"\n{kilogramos} kilogramos es equivalente a {libras} libras")

#Prueba de escritorio
'''
Entrada       
Ingrese una cantidad de kilogramos: 20                  
__________________________________________

Salida
20 kilogramos es equivalente a 44 libras
__________________________________________

Proceso (Valores que toman las variables)

kilogramos =  0.0 | 20
libras     =  0.0 | 44
__________________________________________

'''
