import os
os.system("cls")

#Enunciado
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

#Declaro variables
nota = int()
notas = list()

#Inicializo variables
nota = 0
notas = []

#Proceso

while len(notas) < 5: 

    nota = int(input("Ingresa una nota (del 0 al 10): "))

    #Validacion
    while (nota < 0 or nota > 10):
        print("Nota no valida")
        nota = int(input("\nIngresa una nota (del 0 al 10): "))
    
    notas.append(nota)

print(f"\nNotas ingresadas: {notas}")
notas.sort()
print(f"Nota mas baja: {notas[0]}")
print(f"Nota media: {notas[2]}")
print(f"Nota mas alta: {notas[4]}")


#Prueba de escritorio
'''
Entrada                                 
Ingresa una nota (del 0 al 10): 5
Ingresa una nota (del 0 al 10): 10
Ingresa una nota (del 0 al 10): 3
Ingresa una nota (del 0 al 10): 6
Ingresa una nota (del 0 al 10): 7
__________________________________________

Salida
Notas ingresadas: [5, 10, 3, 6, 7]
Nota baja: 3
Nota media: 6
Nota mas alta: 10
__________________________________________

'''