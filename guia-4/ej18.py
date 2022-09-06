import os

def limpiarPantalla():
    os.system("cls")

#Enunciado
# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
# - Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# - Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# - Eliminar: Me pide una cadena, y la elimina de la lista.
# - Mostrar: Muestra la lista de cadenas
# - Terminar

#Declaro variables
lista = list()
cadena = str()
cadenaNueva = str()
r = int() #Repeticiones

#Inicializo variables
lista = ["messi", "mbappe", "ronaldo", "maradona", "riquelme", "riquelme", "mbappe", "mbappe"]
cadena = ""
cadenaNueva = ""
r = 0

#Proceso
while True:
    limpiarPantalla()
    print("Trabajando con listas")
    print(f"Lista actual: {lista}\n") #Mostrar lista en cada iteracion (opcional)
    print("1: Contar cuantas veces aparece una cadena en la lista")
    print("2: Reemplazar una cadena por una nueva")
    print("3: Eliminar una cadena de la lista")
    print("4: Mostrar lista actual")
    print("5: Salir")
    opcion = input("Elija una opcion: ")
    print()

    if (opcion == "1"):
        print("Ingresa una cadena para ver cuantas veces aparece en la lista")
        cadena = input("Ingresa una cadena: ").lower()

        r = lista.count(cadena)

        if (r == 0): print(f"{cadena} no se encuentra en la lista")
        elif (r == 1): print(f"{cadena} aparece una vez en la lista")
        else: print(f"{cadena} aparece {r} veces en la lista") 

    elif (opcion == "2"):
        print("Modifica una cadena de la lista")
        cadena = input("Ingresa la cadena a modificar: ").lower()
        cadenaNueva = input("Ingresa una cadena nueva: ").lower().strip()

        if (cadena in lista):
            for elemento in lista:
                if(elemento == cadena):
                    i = lista.index(cadena)
                    lista[i] = cadenaNueva
        else:
            print(f"{cadena} no se encuentra en la lista")       

    elif (opcion == "3"):
        print("Elimina una cadena de la lista")
        cadena = input("Ingresa una cadena: ").lower()

        if (cadena in lista):
            r = lista.count(cadena)
            for i in range(r): 
                lista.remove(cadena)
        else:
            print(f"{cadena} no se encuentra en la lista")

    elif (opcion == "4"):
        print(f"Lista actual: {lista}")

    elif (opcion == "5"):
        break

    else: 
        print("Opcion no valida")

    input("\nPulsa para continuar ")

