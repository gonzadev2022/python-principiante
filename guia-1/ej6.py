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