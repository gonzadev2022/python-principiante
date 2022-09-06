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