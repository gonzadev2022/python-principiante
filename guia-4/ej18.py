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
lista = ["messi", "mbappe", "ronaldo", "maradona", "ronaldo"]
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
    
    #1: Contando la cantidad de veces que aparece una cadena en la lista
    if (opcion == "1"):

        print("Ingresa una cadena para ver cuantas veces aparece en la lista")
        cadena = input("Ingresa una cadena: ").lower()

        r = lista.count(cadena)

        if (r == 0): print(f"\n{cadena} no se encuentra en la lista")
        elif (r == 1): print(f"\n{cadena} aparece una vez en la lista")
        else: print(f"\n{cadena} aparece {r} veces en la lista") 

    #2: Modificando una cadena de la lista
    elif (opcion == "2"):

        print("Modifica una cadena de la lista")
        cadena = input("Ingresa la cadena a modificar: ").lower()
        cadenaNueva = input("Ingresa una cadena nueva: ").lower().strip()

        if (cadena in lista):
            for elemento in lista:

                if(elemento == cadena):
                    i = lista.index(cadena)
                    lista[i] = cadenaNueva

            print("\nLa cadena se modifico correctamente")

        else:
            print(f"\n{cadena} no se encuentra en la lista")       

    #3: Eliminando una cadena de la lista
    elif (opcion == "3"):

        print("Elimina una cadena de la lista")
        cadena = input("Ingresa una cadena: ").lower()

        if (cadena in lista):

            r = lista.count(cadena)

            for i in range(r): 
                lista.remove(cadena)

            print("\nLa cadena se elimino correctamente")

        else:
            print(f"\n{cadena} no se encuentra en la lista")

    #4: Mostrando lista actual
    elif (opcion == "4"):
        print(f"Lista actual: {lista}")

    #5: Fin del bucle
    elif (opcion == "5"):
        break
    
    #En caso de error
    else: 
        print("Opcion no valida")

    input("\nPulsa para continuar ")


#Prueba de escritorio
'''
Entradas y Salidas        
Vista general de como se ejecutan cada una de las opciones                     
__________________________________________________________________
Trabajando con listas
Lista actual: ["messi", "mbappe", "ronaldo", "maradona", "ronaldo"]

1: Contar cuantas veces aparece una cadena en la lista
2: Reemplazar una cadena por una nueva
3: Eliminar una cadena de la lista
4: Mostrar lista actual
5: Salir
Elija una opcion:
__________________________________________________________________

#OPCION 1
Lista actual: ["messi", "mbappe", "ronaldo", "maradona", "ronaldo"]

Ingresa una cadena para ver cuantas veces aparece en la lista
Ingresa una cadena: ronaldo

ronaldo aparece 2 veces en la lista
Pulsa para continuar
__________________________________________________________________

#OPCION 2
Lista actual: ["messi", "mbappe", "ronaldo", "maradona", "ronaldo"]

Modifica una cadena de la lista
Ingresa la cadena a modificar: ronaldo
Ingresa una cadena nueva: riquelme

La cadena se modifico correctamente  
Pulsa para continuar
__________________________________________________________________

#OPCION 3
Lista actual: ["messi", "mbappe", "riquelme", "maradona", "riquelme"]

Elimina una cadena de la lista
Ingresa una cadena: riquelme

La cadena se elimino correctamente  
Pulsa para continuar
__________________________________________________________________

#OPCION 4
Lista actual: ["messi", "mbappe", "maradona"]
Pulsa para continuar 
__________________________________________________________________

'''

