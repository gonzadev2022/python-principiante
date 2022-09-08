import os
os.system("cls")

#Enunciado
# Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
# a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
# b) Determinar en qué mes recibió el sueldo más bajo del período.
# c) Informar el sueldo promedio del semestre.

#Declaro variables
sueldo_actual = int()
total_sueldos = int() 
menor_sueldo = int()  
mayor_sueldo = int()
mes_menor_sueldo = int()
aguinaldo = float()
promedio = float()

#Inicializo variables
sueldo_actual = 0
total_sueldos = 0 
menor_sueldo = 0  
mayor_sueldo = 0
mes_menor_sueldo = 0
aguinaldo = 0.0
promedio = 0.0

#Proceso
print("Ingresar los sueldos del vendedor correspondientes al primer semestre")

for mes in range(1, 7):
    sueldo_actual = int(input(f"Sueldo del mes {mes}: "))

    total_sueldos += sueldo_actual

    if (mes == 1 or sueldo_actual < menor_sueldo):
        menor_sueldo = sueldo_actual
        mes_menor_sueldo = mes

    if (mes == 1 or sueldo_actual > mayor_sueldo):
        mayor_sueldo = sueldo_actual

aguinaldo = mayor_sueldo / 2
promedio = total_sueldos / 6

#Resultados finales
print(f"\nAguinaldo del semestre: ${aguinaldo}")
print(f"Sueldo mas bajo del semestre: mes {mes_menor_sueldo}")
print(f"Sueldo promedio del semestre: ${promedio}")


#Prueba de escritorio
'''
Entrada                                 
Ingresar los sueldos del vendedor correspondientes al primer semestre
Sueldo del mes 1: 5000
Sueldo del mes 2: 4000
Sueldo del mes 3: 3000
Sueldo del mes 4: 6000
Sueldo del mes 5: 5000
Sueldo del mes 6: 7000
__________________________________________

Salida
Aguinaldo del semestre: 
Sueldo mas bajo del semestre: 
Sueldo promedio del semestre:
__________________________________________

Proceso (Valores que toman las variables)

sueldo_actual =     0 | 5000 | 4000 | 3000  | 6000  | 5000  | 7000
total_sueldos =     0 | 5000 | 9000 | 12000 | 18000 | 23000 | 30000
menor_sueldo =      0 | 5000 | 4000 | 3000
mayor_sueldo =      0 | 5000 | 6000 | 7000
mes_menor_sueldo =  0 | 1 | 2 | 3
aguinaldo =       0.0 | 3500.0
promedio =        0.0 | 5000.0

'''