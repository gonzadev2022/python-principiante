import os
os.system("cls")

#Enunciado
# Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.

#Declaro variables
nombre = str()

#Inicializo variables
nombre = ""

#Proceso
nombre = input("Ingrese un nombre de usuario: ")
    
if (len(nombre) % 2 == 0): print("Par")
else: print("Impar")


#Prueba de escritorio
'''
Entrada                                 
Ingrese un nombre de usuario: matias                    
__________________________________________

Salida
Par
__________________________________________

Proceso (Valores que toman las variables)
nombre = "" | "matias"

'''
