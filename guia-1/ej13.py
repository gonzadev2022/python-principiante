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
    print()

    if (opcion == "1"):
        dolares = int(input("Ingresa una cantidad de dolares: "))
        pesos = dolares * cotizacion
        print(f"{dolares} dolares son {pesos} pesos")

    elif (opcion == "2"):
        pesos = int(input("Ingresa una cantidad de pesos: "))
        dolares = pesos / cotizacion
        print(f"{pesos} pesos son {dolares} dolares")

    elif (opcion == "3"): break

    input("\nPulse para continuar ")