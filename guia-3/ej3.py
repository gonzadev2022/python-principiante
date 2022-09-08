import os
os.system("cls")

#Enunciado
# Secuencia numérica. Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar
# a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
# b) Determinar la cantidad de números que son el cuadrado del número anterior
# c) Determinar la posición del mayor elemento impar de la secuencia

#Declaro variables
numero_actual = int()
divisibles_por_tres = int()
pje_divisibles_por_tres = int()
cuadrado_del_anterior = int()
numeros_ingresados = int()
mayor_impar = int() 
posicion_mayor_impar = int()
numero_anterior = int()
primer_impar = bool()

#Inicializo variables
numero_actual = 0
divisibles_por_tres = 0
pje_divisibles_por_tres = 0
cuadrado_del_anterior = 0
numeros_ingresados = 0
mayor_impar = 0 
posicion_mayor_impar = 0
numero_anterior = 0
primer_impar = True

#Proceso
print("Secuencia numerica")
print("La carga finaliza cuando se ingresa un cero\n")

while True:
    numero_actual = int(input("Ingresa un numero: "))
    if (numero_actual == 0): break

    numeros_ingresados += 1

    #Determinando nros divisibles por 3
    if (numero_actual % 3 == 0): 
        divisibles_por_tres += 1
    
    #Determinando mayor impar
    if (numero_actual % 2 != 0) and (primer_impar or numero_actual > mayor_impar):
        mayor_impar = numero_actual
        posicion_mayor_impar = numeros_ingresados
        primer_impar = False

    #Determinando nros que son cuadrados del anterior
    if (numeros_ingresados > 1) and (numero_actual == numero_anterior ** 2):
        cuadrado_del_anterior += 1

    numero_anterior = numero_actual #Guardo el nro actual para la siguente comparacion

if (numeros_ingresados > 0):
    pje_divisibles_por_tres = int(divisibles_por_tres * 100 / numeros_ingresados)

print("\nResultados generales")
print(f"Porcentaje de numeros que son divisibles por 3 en la secuencia: {pje_divisibles_por_tres}%")
print(f"Cantidad de numeros que son cuadrados del numero anterior: {cuadrado_del_anterior}")
print(f"Posicion del mayor elemento impar en la secuencia: {posicion_mayor_impar}")


#Prueba de escritorio
'''
Entrada   
Secuencia numerica
La carga finaliza cuando se ingresa un cero

Ingresa un numero: 5           
Ingresa un numero: 25  
Ingresa un numero: 30              
Ingresa un numero: 2 
Ingresa un numero: 7 
Ingresa un numero: 0  

__________________________________________

Salida
Resultados generales
Porcentaje de numeros que son divisibles por 3 en la secuencia: 20%
Cantidad de numeros que son cuadrados del numero anterior: 1
Posicion del mayor elemento impar en la secuencia: 2
__________________________________________

Proceso (Valores que toman las variables)

numero_actual =            0 |  5  |  25  |  30 |  2  |  7  |  0
divisibles_por_tres =      0 |  1
pje_divisibles_por_tres =  0 |  20
cuadrado_del_anterior =    0 |  1
numeros_ingresados =       0 |  1  |  2  |  3  |  4  |  5
mayor_impar =              0 |  5  |  25
posicion_mayor_impar =     0 |  1  |  2
numero_anterior =          0 |  5  |  25  |  30  |  2  |  7  
primer_impar =          True | False | False

'''



