import os
os.system("cls")

#Enunciado
# Escriba un programa que transforme todas las letras de una palabra en mayúsculas, minúsculas y la primera con minúsculas(capitalización).

#Declaro variables
palabra = str()

#Inicializo variables
palabra = ""

#Proceso
palabra = input("Ingrese una palabra: ")

print(f"\n{palabra.upper()}  {palabra.lower()}  {palabra.capitalize()}")


#Prueba de escritorio
'''
Entrada                                 
Ingrese una palabra: teclado                
__________________________________________

Salida
TECLADO  teclado  Teclado 
__________________________________________

Proceso (Valores que toman las variables)
palabra = "" | "teclado"

'''