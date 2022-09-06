import os
os.system("cls")

#Enunciado
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

#Declaro variables

#Inicializo variables
nota = int()
notas = []

#Proceso

while True: 
    nota = int(input("Ingresa una nota (del 0 al 10): "))

    while (nota < 0 or nota > 10):
        print("Te dije del 0 al 10 pedazo de bobi")
        nota = int(input("\nIngresa una nota (del 0 al 10): "))
    
    notas.append(nota)

    if (len(notas) == 5): break

print(f"\nNotas ingresadas: {notas}")
notas.sort()
print(f"Nota Baja: {notas[0]}")
print(f"Nota Media: {notas[2]}")
print(f"Nota Alta: {notas[4]}")