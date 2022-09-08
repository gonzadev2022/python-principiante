import os
os.system("cls")

#Enunciado
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

#Declaro variables
lista1 = list()
lista2 = list()
lista3 = list()
n = int()

#Inicializo variables
lista1 = []
lista2 = []
lista3 = []
n = 0

#Proceso
print("Ingresar 5 numeros para la lista 1")

for i in range(5):
    n = int(input("Ingresar numero: "))
    lista1.append(n)

print("\nIngresar 5 numeros para la lista 2")

for i in range(5):
    n = int(input("Ingresar numero: "))
    lista2.append(n)

lista3 = lista1 + lista2

print(f"\nLista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")


#Prueba de escritorio
'''
Entrada                                 
Ingresar 5 numeros para la lista 1
Ingresar numero: 1
Ingresar numero: 2
Ingresar numero: 3
Ingresar numero: 4
Ingresar numero: 5

Ingresar 5 numeros para la lista 2
Ingresar numero: 6
Ingresar numero: 7
Ingresar numero: 8
Ingresar numero: 9
Ingresar numero: 10
__________________________________________

Salida
Lista 1: [1, 2, 3, 4, 5]
Lista 2: [6, 7, 8, 9, 10]
Lista 3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
__________________________________________

'''