import os
os.system("cls")

#Enunciado
# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).

#Declaro variables
lista = list()
numero = int()

#Inicializo variables
lista = []
numero = 0

#Proceso
print("La carga de numeros finalizara cuando se ingresa un numero negativo")

while True:
    numero = int(input("Ingresa un numero: "))
    if (numero < 0): break

    lista.append(numero)

print(f"\nLista: {lista}")


#Prueba de escritorio
'''
Entrada                                 
La carga de numeros finalizara cuando se ingresa un numero negativo
Ingresa un numero: 10
Ingresa un numero: 20
Ingresa un numero: 30
Ingresa un numero: 40
Ingresa un numero: -1
__________________________________________
Salida
Lista: [10, 20, 30, 40]
__________________________________________

'''