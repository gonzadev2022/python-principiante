import os
os.system("cls")

#Enunciado
# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

#Declaro variables
lista1 = list()
lista2 = list()
cadena = str()

#Inicializo variables
lista1 = []
lista2 = []
cadena = ""

#Proceso
for i in range(5):
    cadena = input("Ingresa una cadena: ")
    lista1.append(cadena)

lista2 += lista1
lista2.reverse()

print(f"\nLista 1: {lista1}")
print(f"Lista 2: {lista2}")


#Prueba de escritorio
'''
Entrada                                 
Ingresa una cadena: cadena1
Ingresa una cadena: cadena2
Ingresa una cadena: cadena3
Ingresa una cadena: cadena4
Ingresa una cadena: cadena5

__________________________________________

Salida
Lista 1: [cadena1, cadena2, cadena3, cadena4, cadena5]
Lista 2: [cadena5, cadena4, cadena3, cadena2, cadena1]
__________________________________________


'''