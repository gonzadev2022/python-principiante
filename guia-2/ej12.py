import os
os.system("cls")

#Enunciado
# Números pares e impares Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo. Los requerimientos funcionales del programa son: La sumatoria de solo los números que estén comprendidos entre 50 y 100. Cantidad de valores pares ingresados. Cantidad de valores impares ingresados. Informar si en la carga de números se ingreso al menos un número 0. Informar si la serie contiene solo números pares e impares alternados.

#Declaro variables
numero_actual = int()
suma = int()
pares = int()
impares = int()
ceros = bool()
numeros_ingresados = int()
serie_alternada = bool()
numero_anterior = int()

#Inicializo variables
numero_actual = 0
suma = 0
pares = 0
impares = 0
ceros = False
numeros_ingresados = 0
serie_alternada = True
numero_anterior = 0

#Proceso
print("Secuencia numerica")
print("La carga general finalizara cuando se ingrese un numero negativo")

while True:

    numero_actual = int(input("Ingresa un numero: "))
    if (numero_actual < 0): break
    
    numeros_ingresados += 1 

    #Contador de numeros pares e impares
    if (numero_actual % 2 == 0): pares += 1
    else: impares += 1

    #Sumatoria de nros comprendidos entre 50 y 100
    if (numero_actual >= 50 and numero_actual <= 100):
        suma += numero_actual

    #Informa si se ingresa un cero
    if (numero_actual == 0): ceros = True

    #Se ejecuta si la serie sigue siendo alternada y si hay minimo 2 numeros para comparar
    if (serie_alternada) and (numeros_ingresados > 1) and (numero_actual % 2 == numero_anterior):
        serie_alternada = False #La serie alternada se rompe o finaliza
        
    numero_anterior = numero_actual % 2 #Guardo par o impar actual para la proxima comparacion

print("\nInforme general")
print(f"Cantidad de numeros pares ingresados: {pares}")
print(f"Cantidad de numeros impares ingresados: {impares}")
print(f"Sumatoria de numeros comprendidos entre 50 y 100: {suma}")

if (ceros): print("Se ingreso al menos un cero")
else: print("No se ingresaron ceros")

if (serie_alternada): print("La serie numerica es alternada")
else: print("La serie numerica NO es alternada")


#Prueba de escritorio
'''
Entrada                                 
Secuencia numerica
La carga general finalizara cuando se ingrese un numero negativo

Ingresa un numero: 50
Ingresa un numero: 85
Ingresa un numero: 100
Ingresa un numero: 115
Ingresa un numero: 119
Ingresa un numero: -1
__________________________________________
Salida
Informe general
Cantidad de numeros pares ingresados: 2
Cantidad de numeros impares ingresados: 3
Sumatoria de numeros comprendidos entre 50 y 100: 235
No se ingresaron ceros
La serie numerica NO es alternada

__________________________________________

Proceso (Valores que toman las variables)

numeros_ingresados =     0 | 1  |  2  |  3  |  4  |  5 
numero_actual =          0 | 50 | 85  | 100 | 115 | 119
suma =                   0 | 50 | 135 | 285
pares =                  0 | 1  | 2 
impares =                0 | 1  | 2   |  3
ceros =                False
serie_alternada =      True| False                        (se rompe la serie cuando se ingresa el quinto numero)
numero_anterior =        0 |  0 |  1  |  0  |  1  |  1    (0 = nro par   1 = nro impar) (el primer cero es la inicializacion, no influye en la serie)
 
'''

