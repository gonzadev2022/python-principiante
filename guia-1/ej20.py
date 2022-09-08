from random import randint
import os
os.system("cls")

#Enunciado
# Tarjeta de Bingo. Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaría la tarjeta de bingo de una persona. Una vez generado los números aleatorios solicitar al usuario que ingrese 3 números enteros, a parƟr de allí mostrar los siguientes mensajes: Si el usuario no marcó ninguno de los números, indicarlo diciendo “El jugador tiene mala suerte, no marcó ninguna casilla”. Caso contrario mostrar “El jugador marcó algún número de la tarjeta”.

#Declaro variables
cartonBingo = list()
numero = int()
adivinados = int()

#Inicializo variables
cartonBingo = []
numero = 0
adivinados = 0

#Proceso
print("Adivina los numeros del carton de Bingo")

for i in range(15):
    cartonBingo.append(randint(1, 100))
    
for i in range(3):
    numero = int(input("Ingresa un numero: "))

    if (numero in cartonBingo):
        adivinados += 1

print(f"\nCarton de Bingo: {cartonBingo}") #Carton generado

if (adivinados == 0): 
    print("El jugador tiene mala suerte, no marco ningun numero de la carton")
else:
    print(f"El jugador marco {adivinados} numero/s del carton")


#Prueba de escritorio
'''
Entrada                                 
Adivina los numeros del carton de Bingo
Ingresa un numero: 10
Ingresa un numero: 50
Ingresa un numero: 80
__________________________________________
Salida
Carton de Bingo: [91, 71, 54, 67, 10, 13, 38, 17, 38, 88, 93, 1, 58, 65, 36]
El jugador marco 1 numero/s del carton
__________________________________________

Proceso (Valores que toman las variables)

cartonBingo = [] | [91, 71, 54, 67, 10, 13, 38, 17, 38, 88, 93, 1, 58, 65, 36]
numero =      0  | 10 | 50 | 80
adivinados =  0  | 1

'''