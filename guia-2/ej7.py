import os
os.system("cls")

#Enunciado
# Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce:cantidad de espectadores y descuento(S/N).La carga termina cuando la cantidad de espectadores sea igual a 0(cero).El programa deberá:Calcular la recaudación total del complejo,considerando que el valor de la entrada es de $50 en los días con descuento y $75 en los días sin descuento.Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones

#Declaro variables
espectadores = int()
descuento = str()
precio_de_entrada = int()
recaudacion_por_funcion = int()
recaudacion_total = int()
total_de_funciones = int()
funciones_con_descuento = int()
porcentaje = int() 

#Inicializo variables
espectadores = 0
descuento = ""
precio_de_entrada = 0
recaudacion_por_funcion = 0
recaudacion_total = 0
total_de_funciones = 0
funciones_con_descuento = 0
porcentaje = 0 #Porcentaje de funciones con descuento

#Proceso
print("Funciones de cine")
print("La carga finaliza cuando se ingrese un cero en cantidad de espectadores")

while True:
    print("\nFuncion de cine")
    espectadores = int(input("Cantidad de espectadores: "))
    if (espectadores == 0): break

    descuento = input("Descuento aplicable (S/N): ").upper()

    if (descuento == "S"):
        funciones_con_descuento += 1 #Contador de funciones con descuento
        precio_de_entrada = 50
    
    elif (descuento == "N"):
        precio_de_entrada = 75
    
    else: continue

    recaudacion_por_funcion = espectadores * precio_de_entrada
    recaudacion_total += recaudacion_por_funcion #Acumulador de recaudacion total

    total_de_funciones += 1 #Contador de funciones generales

#Resultados finales
print("\nInformacion general")
print(f"La recaudacion total fue de ${recaudacion_total}")
print(f"Se efectuaron {funciones_con_descuento} funciones con descuento")

if (total_de_funciones > 0):
    porcentaje = funciones_con_descuento * 100 / total_de_funciones
    print(f"El porcentaje de funciones con descuento fue del {int(porcentaje)}%")


#Prueba de escritorio
'''
Entrada                                 
Funciones de cine
La carga finaliza cuando se ingrese un cero en cantidad de espectadores

Funcion de cine
Cantidad de espectadores: 10
Descuento aplicable (S/N): N

Funcion de cine
Cantidad de espectadores: 20
Descuento aplicable (S/N): S

Funcion de cine
Cantidad de espectadores: 30
Descuento aplicable (S/N): N

Funcion de cine
Cantidad de espectadores: 0
__________________________________________
Salida
Informacion general
La recaudacion total fue de
Se efectuaron funciones con descuento
El porcentaje de funciones con descuento fue del % 

__________________________________________

Proceso (Valores que toman las variables)

espectadores =              0 |  10  |  20  | 30
descuento =                "" |  "N" |  "S" | "N"
precio_de_entrada =         0 |  75  |  50  | 75
recaudacion_por_funcion =   0 |  750 | 1000 | 2250
recaudacion_total =         0 |  750 | 1750 | 4000
total_de_funciones =        0 |   1  |  2   |  3 
funciones_con_descuento =   0 |   1  |
porcentaje =                0 |  33

'''
