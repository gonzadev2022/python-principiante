import os
os.system("cls")

#Enunciado
# Mostrar por pantalla el promedio de los números ingresados por teclado. Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero).

#Declaro variables
n = int()
total = int() 
numeros_ingresados = int() 
promedio = float()

#Inicializo variables
n = 0
total = 0 
numeros_ingresados = 0 
promedio = 0.0

#Proceso
print("Promedio de numeros")
print("La carga finaliza cuando se ingrese un cero\n")

while True:
    n = int(input("Ingresa un numero: "))

    if n == 0: break

    total += n
    numeros_ingresados += 1

promedio = total / numeros_ingresados

print(f"El promedio de los numeros ingresados es de {promedio}")


#Prueba de escritorio
'''
Entrada                                 
Promedio de numeros
La carga finaliza cuando se ingrese un cero

Ingresa un numero: 10
Ingresa un numero: 30
Ingresa un numero: 50
Ingresa un numero: 0
__________________________________________
Salida
El promedio de los numeros ingresados es de 30
__________________________________________

Proceso (Valores que toman las variables)
n =                   0 | 10 | 30 | 50
total =               0 | 10 | 40 | 90
numeros_ingresados =  0 | 1  | 2  | 3
promedio =          0.0 | 30.0

'''