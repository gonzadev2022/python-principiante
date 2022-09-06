import os
os.system("cls")

#Enunciado
# Jornal de un Operario. Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas. La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.

#Declaro variables
turno = int()
horas = int()

#Inicializo variables
turno = 0
horas = 0

#Proceso
turno = int(input("Ingresar turno (1 o 2): ")) #1: Diurno #2: Nocturno
horas = int(input("Horas trabajadas: "))
    
if (turno == 1): pago = 35.50
elif (turno == 2): pago = 40.60
else: pago = 0

print(f"\nEl jornal del operario es de ${pago * horas}")