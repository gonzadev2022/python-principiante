import os
os.system("cls")

#Enunciado
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

#Declaro variables
lista1 = list()
lista2 = list()
lista3 = list()

#Inicializo variables
lista1 = []
lista2 = []
lista3 = []

#Proceso
print("Ingresar 5 numeros para la lista 1")
for i in range(5):
    n = int(input("Ingresar numero: "))
    lista1.append(n)

print("\nIngresar 5 numeros para la lista 2")
for i in range(5):
    n = int(input("Ingresar numero: "))
    lista2.append(n)

print(f"\nLista 1: {lista1}")
print(f"Lista 2: {lista2}")

lista3 = lista1 + lista2
print(f"Lista 3: {lista3}")