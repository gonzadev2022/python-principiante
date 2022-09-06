import os
os.system("cls")

#Enunciado
# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
# a) La temperatura media de cada día
# b) Los días con menos temperatura
# c) Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.

#Declaro variables
temperaturas = list()
temperaturasOrdenadas = list()
minima = int()
maxima = int()
media = int()
dia = int()

#Inicializo variables
temperaturas = []
temperaturasOrdenadas = []
minima = 0
maxima = 0
media = 0
dia = 0

#Proceso
print("Temperaturas de la semana")

for dia in range(1, 6):
    print(f"\nDia {dia}")
    minima = int(input("Temperatura minima: "))
    maxima = int(input("Temperatura maxima: "))

    #Punto A
    media = (minima + maxima) / 2
    print(f"Temperatura media: {media}")

    temperaturas.append([minima, maxima, dia])

#Punto B
temperaturasOrdenadas = sorted(temperaturas)
print("\nDias con menos temperatura")
print(f"Dia {temperaturasOrdenadas[0][2]} con {temperaturasOrdenadas[0][0]} grados")
print(f"Dia {temperaturasOrdenadas[1][2]} con {temperaturasOrdenadas[1][0]} grados")

#Punto C
print("\nConsulta una temperatura maxima en la semana")
temperaturaBuscada = int(input("Ingresa una temperatura: "))
 
for dia in temperaturas:

    if (dia[1] == temperaturaBuscada):
        print(f"Dia {dia[2]}: Temperatura encontrada")
    
    else:
        print(f"Dia {dia[2]}: Temperatura no encontrada")