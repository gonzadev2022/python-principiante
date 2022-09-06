import os
os.system("cls")

#Enunciado
# Mostrar por pantalla el promedio de los números ingresados por teclado. Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero).

#Declaro variables
n = int()
total = int() #Acumulador
numerosIngresados = int() #Contador
promedio = float()

#Inicializo variables
n = 0
total = 0 
numerosIngresados = 0 
promedio = 0.0

#Proceso
while True:
    n = int(input("Ingresa un numero: "))

    if n == 0: break

    total += n
    numerosIngresados += 1

promedio = total / numerosIngresados

print(f"El promedio de los numeros ingresados es de {promedio}")