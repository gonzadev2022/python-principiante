import os
os.system("cls")

#Enunciado
# Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
# a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
# b) Determinar en qué mes recibió el sueldo más bajo del período.
# c) Informar el sueldo promedio del semestre.

#Declaro variables
sueldoActual = int()
totalSueldos = int()
menorSueldo = int()
mayorSueldo = int()
mesMenorSueldo = int()
aguinaldo = float()
promedio = float()

#Inicializo variables
sueldoActual = 0
totalSueldos = 0 
menorSueldo = 0  
mayorSueldo = 0
mesMenorSueldo = 0
aguinaldo = 0.0
promedio = 0.0

#Proceso
print("Ingresar los sueldos del vendedor correspondientes al primer semestre")

for mes in range(1, 7):
    sueldoActual = int(input(f"Sueldo del mes {mes}: "))

    totalSueldos += sueldoActual

    if (mes == 1 or sueldoActual < menorSueldo):
        menorSueldo = sueldoActual
        mesMenorSueldo = mes

    if (mes == 1 or sueldoActual > mayorSueldo):
        mayorSueldo = sueldoActual

aguinaldo = mayorSueldo / 2
promedio = totalSueldos / 6

#Resultados finales
print(f"\nAguinaldo del semestre: ${aguinaldo}")
print(f"Sueldo mas bajo del semestre: mes {mesMenorSueldo}")
print(f"Sueldo prmedio del semestre: ${promedio}")

