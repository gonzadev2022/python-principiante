import os
os.system("cls")

#Enunciado
# Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce:cantidad de espectadores y descuento(S/N).La carga termina cuando la cantidad de espectadores sea igual a 0(cero).El programa deberá:Calcular la recaudación total del complejo,considerando que el valor de la entrada es de $50 en los días con descuento y $75 en los días sin descuento.Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones

#Declaro variables
espectadores = int()
descuento = str()
precioDeEntrada = int()
recaudacionPorFuncion = int()
recaudacionTotal = int()
totalDeFunciones = int()
funcionesConDescuento = int()
porcentaje = int()

#Inicializo variables
espectadores = 0
descuento = ""
precioDeEntrada = 0
recaudacionPorFuncion = 0
recaudacionTotal = 0
totalDeFunciones = 0
funcionesConDescuento = 0
porcentaje = 0

#Proceso
while True:
    print("\nFuncion de cine")
    espectadores = int(input("Cantidad de espectadores: "))
    if (espectadores == 0): break

    descuento = input("Descuento aplicable (S/N): ").upper()

    if (descuento == "S"):
        funcionesConDescuento += 1 #Contador de funciones con descuento
        precioDeEntrada = 50
    
    elif (descuento == "N"):
        precioDeEntrada = 75
    
    else: continue

    recaudacionPorFuncion = espectadores * precioDeEntrada
    recaudacionTotal += recaudacionPorFuncion #Acumulador de recaudacion total

    totalDeFunciones += 1 #Contador de funciones generales

#Resultados finales
print("\nInformacion general")
print(f"La recaudacion total fue de ${recaudacionTotal}")
print(f"Se efectuaron {funcionesConDescuento} funciones con descuento")

if (totalDeFunciones > 0):
    porcentaje = funcionesConDescuento * 100 / totalDeFunciones
    print(f"El porcentaje de funciones con descuento fue del {round(porcentaje)}%")


