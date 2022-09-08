import os
os.system("cls")

#Enunciado
# Área de un triángulo. Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.

#Declaro variables
base = int() 
altura = int()
area = float()

#Inicializo variables
base = 0 
altura = 0
area = 0.0

#Proceso
base = int(input("Base del triangulo: "))
altura = base**2
area = base * altura / 2

print(f"Altura del triangulo: {altura}")
print(f"Area del triangulo: {area}")


#Prueba de escritorio
'''
Entrada                                 
Base del triangulo = 50
__________________________________________

Salida
Altura del triangulo: 2500
Area del triangulo: 6250
__________________________________________

Proceso (Valores que toman las variables)
base =   0 | 50
altura = 0 | 2500
area = 0.0 | 6250.0

'''