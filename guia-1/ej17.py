import os
os.system("cls")

#Enunciado
# Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

#Declaro variables
a = int()
b = int()
c = int()
suma = int()

#Inicializo variables
a = 0
b = 0
c = 0
suma = 0

#Proceso
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingresa el tercer numero: "))
suma = a + b + c
    
if (suma > 10):
    print(f"{suma} / 2 = {(suma/2)}")
else:
    print(f"{suma} al cubo = {suma**3}")


#Prueba de escritorio
'''
Entrada                                 
Ingresa el primer numero: 10
Ingresa el segundo numero: 20
Ingresa el tercer numero: 30
__________________________________________
Salida
60 / 2 = 30

__________________________________________

Proceso (Valores que toman las variables)
a = 0 | 10
b = 0 | 20
c = 0 | 30

'''