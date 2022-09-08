import os
os.system("cls")

#Enunciado
# Proceso de discriminantes Un matemático desea un simple programa que le permita cargar una serie de números quere presentan los discriminantes de diferentes ecuaciones de segundo grado, el proceso de la secuencia analiza cuando el matemático no desea seguir cargando discriminantes. Usted debe:
# a) Determinar la cantidad de discriminantes quedarán 2 raíces
# b) Determinar la cantidad de discriminantes quedarán una única raíz
# c) Determinar la cantidad de discriminantes quedaran raíces en el campo de los números imaginarios
# d) Indicar el porcentaje que representa el punto c sobre el total de discriminantes procesados por el matemático

#Declaro variables
discriminante = int()
dos_raices = int()
una_raiz = int()
sin_solucion_real = int()
respuesta = str()

#Inicializo variables
discriminante = 0
dos_raices = 0
una_raiz = 0
sin_solucion_real = 0
respuesta = ""

#Proceso
print("Proceso de discriminantes")

while True:
    discriminante = int(input("\nIngresar discriminante: "))

    if (discriminante > 0): dos_raices += 1
    elif (discriminante == 0): una_raiz += 1
    else: sin_solucion_real += 1

    respuesta = input("¿Seguir ingresando? (S/N): ").upper()
    if (respuesta == "N"): break

print("\nResultado de discriminantes")
print(f"Cantidad de discriminantes con dos raices: {dos_raices}")
print(f"Cantidad de discriminantes con una raiz: {una_raiz}")
print(f"Cantidad de discriminantes sin solucion real: {sin_solucion_real}")

    
#Prueba de escritorio
'''
Entrada                                 
Proceso de discriminantes

Ingresar discriminante: 20
¿Seguir ingresando? (S/N): S

Ingresar discriminante: 0
¿Seguir ingresando? (S/N): S

Ingresar discriminante: 30
¿Seguir ingresando? (S/N): S

Ingresar discriminante: 0
¿Seguir ingresando? (S/N): S

Ingresar discriminante: -1
¿Seguir ingresando? (S/N): N
__________________________________________

Salida
Resultado de discriminantes
Cantidad de discriminantes con dos raices: 2
Cantidad de discriminantes con una raiz: 2
Cantidad de discriminantes sin solucion real: 1 
__________________________________________

Proceso (Valores que toman las variables)

discriminante =      0 | 20 | 0 | 30 | 0 | -1
dos_raices =         0 | 1  | 2
una_raiz =           0 | 1  | 2
sin_solucion_real =  0 | 1
respuesta =         "" |"S" |"S" |"S" |"S" |"N" 

'''
