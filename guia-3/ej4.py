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
dosRaices = int()
unaRaiz = int()
sinSolucionReal = int()
respuesta = str()

#Inicializo variables
discriminante = 0
dosRaices = 0
unaRaiz = 0
sinSolucionReal = 0
respuesta = ""

#Proceso
print("Proceso de discriminantes")
while True:
    discriminante = int(input("\nIngresar discriminante: "))

    if (discriminante > 0): dosRaices += 1
    elif (discriminante == 0): unaRaiz += 1
    else: sinSolucionReal += 1

    respuesta = input("¿Seguir ingresando? (S/N): ").upper()
    if (respuesta == "N"): break

print("\nResultado de discriminantes")
print(f"Cantidad de discriminantes con dos raices: {dosRaices}")
print(f"Cantidad de discriminantes con una raiz: {unaRaiz}")
print(f"Cantidad de discriminantes sin solucion real: {sinSolucionReal}")

    

