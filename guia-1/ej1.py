import os
os.system("cls")

#Enunciado
# Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras.

#Declaro variables
kilogramos = int()
libras = int()

#Inicializo variables
kilogramos = 0
libras = 0


#Proceso
kilogramos = int(input("Ingrese una cantidad de kilogramos: "))
libras = kilogramos * 2.2

print(f"\n{kilogramos} kilogramos es equivalente a {libras} libras")