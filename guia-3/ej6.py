import os
os.system("cls")

#Enunciado
# Secuencia de n números. Ingresar una secuencia de n números, de a uno por vez. El valor de n se ingresa por teclado, validar que sea mayor a 0. Determinar: 
# a) Cuántos números ingresados terminan en 5 
# b) La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia 
# c) Cuántos números ingresados son mayores al anterior.

#Declaro variables
repeticiones = int()
numeroActual = int()
numeroAnterior = int() 
terminadosEnCinco = int()
repeticionesPrimerNumero = int()
mayorAlAnterior = int()

#Inicializo variables
repeticiones = 0
numeroActual = 0
numeroAnterior = 0 
terminadosEnCinco = 0 #Punto A
repeticionesPrimerNumero = 0 #Punto B
mayorAlAnterior = 0 #Punto C

#Proceso
print("Secuencia numerica")
repeticiones = int(input("¿Cuantos numeros queres ingresar?: "))

while (repeticiones <= 0):
    print("Tenes que ingresar un numero mayor a cero")
    repeticiones = int(input("¿Cuantos numeros queres ingresar?: "))

for i in range(repeticiones):
    numeroActual = int(input("Ingresa un numero: "))
    
    if (numeroActual % 10 == 5): terminadosEnCinco += 1

    if (i == 0): 
        primerNumero = numeroActual 
        repeticionesPrimerNumero += 1
        numeroAnterior = numeroActual #Para el punto C
    else:
        if (numeroActual == primerNumero):
            repeticionesPrimerNumero += 1

    if (i >= 1):
        if (numeroActual > numeroAnterior):
            mayorAlAnterior += 1

        numeroAnterior = numeroActual #Guardado para las siguiente comparacion
    
print("Resultados")
print(f"Cantidad de numeros terminados en cinco: {terminadosEnCinco}")
print(f"Cantidad de veces que aparece el primer numero ingresado en la secuencia: {repeticionesPrimerNumero}")
print(f"Cantidad de numeros que son mayores al anterior: {mayorAlAnterior}")
