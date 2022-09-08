import os
os.system("cls")

#Enunciado
# Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

#Declaro variables
lista1 = list()
lista2 = list()

#Inicializo variables
lista1 = []
lista2 = []

#Proceso
print("Trabajando con listas")
print("La carga de numeros finaliza cuando se ingrese un numero negativo\n")

while True:
    n = int(input("Ingresa un numero: "))
    if (n < 0): break

    lista1.append(n)

for numero in lista1:
    if not(numero in lista2):
        lista2.append(numero)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

#Prueba de escritorio
'''
Entrada     
Trabajando con listas
La carga de numeros finaliza cuando se ingrese un numero negativo    

Ingresa un numero: 1
Ingresa un numero: 2                     
Ingresa un numero: 3
Ingresa un numero: 1
Ingresa un numero: 2
Ingresa un numero: 3
Ingresa un numero: 4
Ingresa un numero: 5
Ingresa un numero: 6
Ingresa un numero: 7
Ingresa un numero: 7
Ingresa un numero: 7
Ingresa un numero: -1
__________________________________________

Salida
Lista 1: [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 7, 7]
Lista 2: [1, 2, 3, 4, 5, 6, 7]
__________________________________________

'''