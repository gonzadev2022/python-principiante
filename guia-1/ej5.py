import os
os.system("cls")

#Enunciado
# Cuadrado de un binomio. Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo.

#Declaro variables
a = int()
b = int()
binomio = int()

#Inicializo variables
a = 0
b = 0
binomio = 0

#Proceso
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
binomio = (a+b)**2

print(f"\nCuadrado del binomio: {binomio}")


#Prueba de escritorio
'''
Entrada                                 
Ingrese el valor de A: 20
Ingrese el valor de B: 10
__________________________________________

Salida
Cuadrado del binomio: 900
__________________________________________

Proceso (Valores que toman las variables)
a = 0 | 20
b = 0 | 10
binomio = 0 | 900

'''
