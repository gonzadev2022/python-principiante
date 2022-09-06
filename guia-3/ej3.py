import os
os.system("cls")

#Enunciado
# Secuencia numérica. Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar
# a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
# b) Determinar la cantidad de números que son el cuadrado del número anterior
# c) Determinar la posición del mayor elemento impar de la secuencia

#Declaro variables
n = int()
divisiblesPorTres = int()
cuadradoDelAnterior = int()
numerosIngresados = int()
mayorImpar = int() 
posicionMayorImpar = int()
numeroAnterior = int()
primerImpar = bool()

#Inicializo variables
n = 0
divisiblesPorTres = 0
cuadradoDelAnterior = 0
numerosIngresados = 0
mayorImpar = 0 
posicionMayorImpar = 0
numeroAnterior = 0
primerImpar = True

#Proceso
print("Secuencia numerica")
print("La carga finaliza cuando se ingresa un cero\n")

while True:
    numeroActual = int(input("Ingresa un numero: "))
    if (numeroActual == 0): break

    numerosIngresados += 1

    #Determinando nros divisibles por 3
    if (numeroActual % 3 == 0): 
        divisiblesPorTres += 1
    
    #Determinando mayor impar
    if (numeroActual % 2 != 0): 

        if (numeroActual > mayorImpar or primerImpar):
            mayorImpar = numeroActual
            posicionMayorImpar = numerosIngresados
            
        primerImpar = False

    #Determinando nros que son cuadrados del anterior
    if (numerosIngresados == 1):
        numeroAnterior = numeroActual
    else:
        if (numeroActual == numeroAnterior ** 2): 
            cuadradoDelAnterior += 1

        numeroAnterior = numeroActual #Guardo el nro actual para la siguente comparacion

if (numerosIngresados > 0):
    pjeDivisiblesPorTres = int(divisiblesPorTres * 100 / numerosIngresados)

print("\nResultados generales")
print(f"Porcentaje de numeros que son divisibles por 3 en la secuencia: {pjeDivisiblesPorTres}%")
print(f"Cantidad de numeros que son cuadrados del numero anterior {cuadradoDelAnterior}")
print(f"Posicion del mayor elemento impar en la secuencia: {posicionMayorImpar}")


