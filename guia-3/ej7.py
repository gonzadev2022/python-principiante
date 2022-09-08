import os
os.system("cls")

#Enunciado
# Secuencia numérica II. Ingresar un secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar:
# a) El promedio de los números que son múltiplos de 6
# b) Cantidad de números que son divisor exacto del anterior
# c) Indicar la cantidad de veces que se generó una secuencia ascendente de 3 o más números impares

#Declaro variables
numero_actual = int()
numero_anterior = int()
numeros_ingresados = int()
total_multiplos_de_seis = int()    
cantidad_multiplos_de_seis = int()        
promedio = float()           
numeros_divisor_exacto = int()   
impares = int()          
secuencia_impar = int()  

#Inicializo variables
numero_actual = 0
numero_anterior = 0
numeros_ingresados = 0
total_multiplos_de_seis = 0            #Punto A
cantidad_multiplos_de_seis = 0         #Punto A 
promedio = 0.0                         #Punto A
numeros_divisor_exacto = 0             #Punto B
impares = 0                            #Punto C
secuencia_impar = 0                    #Punto C

#Proceso
print("Secuencia numerica")
print("La carga finaliza cuando se ingresa el cero\n")

while True:
    numero_actual = int(input("Ingresa un numero: " ))
    if (numero_actual == 0): break

    numeros_ingresados += 1
    
    #Punto A: Determinando nros multiplos de seis
    if (numero_actual % 6 == 0):
        total_multiplos_de_seis += numero_actual
        cantidad_multiplos_de_seis += 1
    
    #Punto B: Determinando cantidad de nros que son divisor exacto del anterior
    if (numeros_ingresados > 1) and (numero_anterior % numero_actual == 0):
        numeros_divisor_exacto += 1
        
    #Punto C: Determinando si se generar sucesiones numericas ascendentes impares
    if (numero_actual % 2 != 0): 
        if (impares == 0 or numero_actual > numero_anterior): impares += 1 #Caso 1: se suma impar a la secuencia
        else: impares = 1 #Caso 2 se iguala la secuencia a 1

    else: impares = 0 #Caso 3: se reinicia la secuencia

    if (impares == 3):
        secuencia_impar += 1

    numero_anterior = numero_actual 

if (cantidad_multiplos_de_seis > 0):
    promedio = total_multiplos_de_seis / cantidad_multiplos_de_seis #Punto A

print("\nResultados")
print(f"Promedio de numeros multiplos de seis ingresados: {promedio}")
print(f"Cantidad de números que son divisor exacto del anterior: {numeros_divisor_exacto}")
print(f"Cantidad de veces que se generó una secuencia ascendente de 3 o más números impares: {secuencia_impar}")


#Prueba de escritorio
'''
Entrada                                 
Secuencia numerica
La carga finaliza cuando se ingresa el cero

Ingresa un numero: 10
Ingresa un numero: 5
Ingresa un numero: 12
Ingresa un numero: 3
Ingresa un numero: 5
Ingresa un numero: 7
Ingresa un numero: 0
__________________________________________

Salida
Resultados
Promedio de numeros multiplos de seis ingresados: 9.0
Cantidad de números que son divisor exacto del anterior: 2
Cantidad de veces que se generó una secuencia ascendente de 3 o más números impares: 1
__________________________________________

Proceso (Valores que toman las variables)

numeros_ingresados =         0 | 1  | 2 | 3  | 4 | 5 | 6 |
numero_actual =              0 | 10 | 5 | 12 | 3 | 5 | 7 | 0
numero_anterior =            0 | 10 | 5 | 12 | 3 | 5 | 7 |
total_multiplos_de_seis =    0 | 12        
cantidad_multiplos_de_seis = 0 | 1     
promedio =                 0.0 | 12.0                 
numeros_divisor_exacto =     0 | 1  | 2           
impares =                    0 | 0  | 1 | 0  | 1 | 2 | 3       
secuencia_impar =            0 | 1           
'''