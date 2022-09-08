import os
os.system("cls")

#Enunciado
# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
# a) La temperatura media de cada día
# b) Los días con menos temperatura
# c) Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.

#Declaro variables
temperaturas = list()
temperaturas_ordenadas = list()
minima = int()
maxima = int()
media = int()
dia = int()
temperatura_buscada = int()

#Inicializo variables
temperaturas = []
temperaturas_ordenadas = []
minima = 0
maxima = 0
media = 0
dia = 0
temperatura_buscada = 0

#Proceso
print("Temperaturas de la semana")

for dia in range(1, 6):
    print(f"\nDia {dia}")
    minima = int(input("Temperatura minima: "))
    maxima = int(input("Temperatura maxima: "))

    #Punto A: Temperatura media de cada dia
    media = (minima + maxima) / 2
    print(f"Temperatura media: {media}")

    temperaturas.append([minima, maxima, dia])

#Punto B: Mostrando los dias con menos temperatura
temperaturas_ordenadas = sorted(temperaturas)
print("\nDias con menos temperatura")
print(f"Dia {temperaturas_ordenadas[0][2]} con {temperaturas_ordenadas[0][0]} grados")
print(f"Dia {temperaturas_ordenadas[1][2]} con {temperaturas_ordenadas[1][0]} grados")

#Punto C
print("\nConsulta una temperatura maxima en la semana")
temperatura_buscada = int(input("Ingresa una temperatura: "))

print("\nTemperaturas maxima buscada")
for dia in temperaturas:

    if (dia[1] == temperatura_buscada):
        print(f"Dia {dia[2]}: coincide")
    else:
        print(f"Dia {dia[2]}: no coincide")


#Prueba de escritorio
'''
Entrada                                 
Temperaturas de la semana

Dia 1
Temperatura minima: 10
Temperatura maxima: 30

Dia 2
Temperatura minima: 20
Temperatura maxima: 30

Dia 3
Temperatura minima: 30
Temperatura maxima: 36

Dia 4
Temperatura minima: 5
Temperatura maxima: 15
 
Dia 5
Temperatura minima: 20 
Temperatura maxima: 26

(Punto c)
Consulta una temperatura maxima en la semana
Ingresa una temperatura: 30
__________________________________________

Salida
Temperatura media: 20
Temperatura media: 25
Temperatura media: 33
Temperatura media: 10
Temperatura media: 23

Dias con menos temperatura
Dia 4 con 5 grados
Dia 1 con 10 grados

(Punto c)
Temperatura maxima buscada
Dia 1 coincide
Dia 2 coincide
Dia 3 no coincide
Dia 4 no coincide
Dia 5 no coincide
__________________________________________

Proceso (Valores que toman las variables)

temperaturas =           [] | [ [10, 30, 1], [20, 30, 2], [30, 36, 3], [5, 15, 4], [20, 26, 5] ] (minima, maxima, dia)
temperaturas_ordenadas = [] | [ [5, 15, 4], [10, 30, 1], [20, 26, 5], [20, 30, 2], [30, 36, 3] ] (lista ordenada por temp minima)

minima =  0 | 10 | 20 | 30 | 5  | 20
maxima =  0 | 30 | 30 | 36 | 15 | 26
media =   0 | 15 | 25 | 33 | 10 | 23
dia =     0 | 1  | 2  | 3  | 4  | 5 
temperatura_buscada = 30

'''