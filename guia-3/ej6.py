import os
os.system("cls")

#Enunciado
# Secuencia de n números. Ingresar una secuencia de n números, de a uno por vez. El valor de n se ingresa por teclado, validar que sea mayor a 0. Determinar: 
# a) Cuántos números ingresados terminan en 5 
# b) La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia 
# c) Cuántos números ingresados son mayores al anterior.

#Declaro variables
repeticiones = int()
numero_actual = int()
numero_anterior = int() 
terminados_en_cinco = int()
repeticionesPrimerNumero = int()
mayor_al_anterior = int()

#Inicializo variables
repeticiones = 0
numero_actual = 0
numero_anterior = 0 
terminados_en_cinco = 0
primer_numero = 0  
repeticiones_primer_numero = 0
mayor_al_anterior = 0

#Proceso
print("Secuencia numerica")
repeticiones = int(input("¿Cuantos numeros queres ingresar?: "))

#Validacion
while (repeticiones < 1):
    print("Tenes que ingresar un numero mayor a cero")
    repeticiones = int(input("¿Cuantos numeros queres ingresar?: "))

for i in range(repeticiones):
    numero_actual = int(input("Ingresa un numero: "))
    
    #Punto A: Cantidad de numeros terminados en cinco
    if (numero_actual % 10 == 5): 
        terminados_en_cinco += 1

    #Punto B: Cantidad de veces que se repite el primer numero de la secuencia
    if (i == 0): 
        primer_numero = numero_actual 
      
    elif (numero_actual == primer_numero):
        repeticiones_primer_numero += 1

    #Punto C: Cantidad de numeros que son mayores al anterior
    if (i > 0) and (numero_actual > numero_anterior):
        mayor_al_anterior += 1

    numero_anterior = numero_actual #Guardado para las siguiente comparacion
    
print("\nResultados")
print(f"Cantidad de numeros terminados en cinco: {terminados_en_cinco}")
print(f"Cantidad de veces que se repite el primer numero ingresado en la secuencia: {repeticiones_primer_numero}")
print(f"Cantidad de numeros que son mayores al anterior: {mayor_al_anterior}")


#Prueba de escritorio
'''
Entrada                                 
Secuencia numerica
¿Cuantos numeros queres ingresar?: 6

Ingresa un numero: 5
Ingresa un numero: 10
Ingresa un numero: 15
Ingresa un numero: 20
Ingresa un numero: 5
Ingresa un numero: 1
__________________________________________

Salida
Resultados
Cantidad de numeros terminados en cinco: 3
Cantidad de veces que se repite el primer numero ingresado en la secuencia: 1
Cantidad de numeros que son mayores al anterior: 3
__________________________________________

Proceso (Valores que toman las variables)

repeticiones =               0 | 6
numero_actual =              0 | 5 | 10 | 15 | 20 | 5 | 1 
numero_anterior =            0 | 5 | 10 | 15 | 20 | 5 | 1 
terminados_en_cinco =        0 | 1 | 2  | 3
primer_numero =              0 | 5
repeticiones_primer_numero = 0 | 1
mayor_al_anterior =          0 | 1 | 2  | 3

'''
