import os
def limpiarPantalla():
    os.system("cls")
limpiarPantalla()

#Enunciado
# Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.

#Declaro variables
cotizacion = float()
pesos = float()
dolares = float()
opcion = str()

#Inicializo variables
cotizacion = 0.0
pesos = 0.0
dolares = 0.0
opcion = ""

#Proceso
cotizacion = int(input("Ingresar cotizacion del dia: "))

while True:
    limpiarPantalla()
    print("Conversor de moneda")
    print("1: Convertir dolares a pesos")
    print("2: Convertir pesos a dolares")
    print("3: Salir")
    opcion = input("Elija una opcion: ")

    if (opcion == "1"): #Dolares a pesos
        dolares = int(input("\nIngresa una cantidad de dolares: "))
        pesos = dolares * cotizacion

        print(f"{dolares} dolares son {pesos} pesos")

    elif (opcion == "2"): #Pesos a dolares
        pesos = int(input("\nIngresa una cantidad de pesos: "))
        dolares = pesos / cotizacion

        print(f"{pesos} pesos son {dolares} dolares")

    elif (opcion == "3"): break

    input("\nPulse para continuar ")


#Prueba de escritorio
'''
Entrada y Salida

Ingresar cotizacion del dia: 300

Conversor de moneda
1: Convertir dolares a pesos
2: Convertir pesos a dolares
3: Salir
Elija una opcion: 1

Ingresa una cantidad de dolares: 5
5 dolares son 1500 pesos           #Salida 1
Pulse para continuar

Conversor de moneda
1: Convertir dolares a pesos
2: Convertir pesos a dolares
3: Salir
Elija una opcion: 2

Ingresa una cantidad de pesos: 5000
3000 pesos son 10 dolares          #Salida 2
Pulse para continuar

Conversor de moneda
1: Convertir dolares a pesos
2: Convertir pesos a dolares
3: Salir
Elija una opcion: 3
__________________________________________

Proceso (Valores que toman las variables)

cotizacion = 0.0 | 300
pesos =      0.0 | 1500| 3000
dolares =    0.0 |  5  |  10
opcion =     ""  | "1" | "2" | "3"

'''