import os
os.system("cls")

#Escribir un programa que le pida al usuario que ingrese una sucesion de numeros naturales
#(primero uno, luego otro, y asi hasta que el usuario ingrese -1 como condicion de salida).
#Al final, el programa debe imprimir cuantos numeros fueron ingresados, la suma total de los valores y el promedio

def sucesionDeNumeros():
    n = 0 
    suma = 0 #Acumula y suma los nros ingresados
    nrosIngresados = 0 #Cuenta los numeros ingresados

    while True:
        n = int(input("Ingresa un numero master: "))
        if (n == -1): break
        
        suma += n
        nrosIngresados += 1
    
    #Resultados finales
    promedio = suma / nrosIngresados
    print(f"La suma de los numeros ingresados es {suma}")
    print(f"Se ingresaron un total de {nrosIngresados} numero/s")
    print(f"El promedio de los numeros ingresados es {promedio}")

print(sucesionDeNumeros())