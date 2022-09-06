import os

def limpiarPantalla():
    os.system("cls")

#Enunciado

#Declaro variables
lista = list()
posiciones = list()
n = int()
p = int()
r = int()
opcion = str()

#Inicializo variables
lista = [1, 2, 3]
posiciones = []
n = 0   #Numero
p = 0   #Posicion
r = 0   #Repeticiones
opcion = ""

#Proceso
# Vamos a crear un programa que tenga el siguiente menú:
# 1.	Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# 2.	Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# 3.	Longitud de la lista: te muestra el número de elementos de la lista.
# 4.	Eliminar el último número: Muestra el último número de la lista y lo borra.
# 5.	Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# 6.	Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# 7.	Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# 8.	Mostrar números: Muestra los números de la lista
# 9.	Salir

while True:
    limpiarPantalla()
    print("Trabajando con listas")
    print(f"Lista actual: {lista}\n") #Mostrar lista en cada iteracion (opcional)
    print("1: Añadir numero a la lista")
    print("2: Añadir numero a la lista en una posicion especifica")
    print("3: Consultar longitud de la lista")
    print("4: Eliminar el último numero de la lista")
    print("5: Eliminar un numero en una posicion especifica")
    print("6: Contar cuantas veces aparece un numero en la lista")
    print("7: Mostrar las posiciones en las que se encuentra un numero")
    print("8: Mostrar la lista actual")
    print("9: Salir")
    opcion = input("Elija una opcion: ")
    print()

    if (opcion == "1"):
        print("Añade un numero a la lista")

        n = int(input("Ingresa un numero: "))
        lista.append(n)

    elif (opcion == "2"):
        print("Añade un numero a la lista en una determinada posicion")

        p = int(input("Ingresa una posicion: "))
        n = int(input("Ingresa un numero: "))

        if (p < 1): print("La posicion debe ser a partir de 1 en adelante")
        elif (p > len(lista)): print("Esa posicion aun no existe")
        else: lista.insert(p-1, n)

    elif (opcion == "3"):
        print(f"La lista tiene {len(lista)} elementos")

    elif (opcion == "4"):
        if (len(lista) >= 1):
            print("Se elimino el ultimo numero de la lista")
            print(f"El ultimo numero de la lista era {lista.pop()}")

        else: 
            print("No hay numeros para elimnar porque la lista esta vacia")

    elif (opcion == "5"):
        print("Elimina un numero de la lista en una determinada posicion")
        p = int(input("Ingresa una posicion: "))

        if (p < 1): print("La posicion debe ser a partir de 1 en adelante")
        elif (p > len(lista)): print("Esa posicion aun no existe")
        else: lista.pop(p-1)

    elif (opcion == "6"):
        print("Ingresa un numero y ve cuantas veces aparece en la lista")

        n = int(input("Ingresa un numero: "))
        r = lista.count(n)

        if (r == 0): print(f"El numero {n} no se encuentra en la lista")
        elif (r == 1): print(f"El numero {n} aparece una vez en la lista")
        else: print(f"El numero {n} aparece {r} veces en la lista")

    elif (opcion == "7"):
        print("Ingresa un numero y ve en que posiciones esta")
        n = int(input("Ingresa un numero: "))  

        if (n in lista):
            for i in range(len(lista)):
                if (lista[i] == n):
                    posiciones.append(i+1)
        
            if (len(posiciones) == 1): print(f"El numero {n} se encuentra en la posicion {posiciones[0]}") 
            else: print(f"El numero {n} se encuentra en las posiciones: {posiciones}")
                
        else: 
            print(f"El numero {n} no se encuentra en la lista")
        
        posiciones = [] # Reinicio variable

    elif (opcion == "8"): 
        print(f"Lista actual: {lista}")

    elif (opcion == "9"): 
        break
    
    else: 
        print("Opcion no valida")

    input("\nPulsa para continuar ")
