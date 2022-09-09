import os
os.system("cls")

#Escribir un programa que le pida al usuario que ingrese una sucesion de numeros naturales
#(primero uno, luego otro, y asi hasta que el usuario ingrese -1 como condicion de salida).
#Al final, el programa debe imprimir cuantos numeros fueron ingresados, la suma total de los valores y el promedio

def sucesionDeNumeros():
    n = 0 
    sumatoria = 0 
    numeros_ingresados = 0 

    print("Sucesion de numeros")
    print("La carga finaliza cuando se ingrese un numero negativo\n")

    while True:
        n = int(input("Ingresa un numero: "))
        if (n == -1): break
        
        sumatoria += n
        numeros_ingresados += 1
    
    #Resultados finales
    promedio = sumatoria / numeros_ingresados
    print(f"La suma de los numeros ingresados es {sumatoria}")
    print(f"Se ingresaron un total de {numeros_ingresados} numero/s")
    print(f"El promedio de los numeros ingresados es {promedio}")

print(sucesionDeNumeros())


#Prueba de escritorio
'''
Entrada                                 
Sucesion de numeros
La carga finaliza cuando se ingrese un numero negativo

Ingresa un numero: 10
Ingresa un numero: 20
Ingresa un numero: 30
Ingresa un numero: 40
Ingresa un numero: 50
Ingresa un numero: -1
__________________________________________

Salida

La suma de los numeros ingresados es 150
Se ingresaron un total de 5 numero/s
El promedio de los numeros ingresados es 30.0
__________________________________________

'''