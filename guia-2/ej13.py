import os
os.system("cls")

#Enunciado
# Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.Por cada habitantes e ingresa:sexo(M/F) y edad. La carga de datos finaliza al ingresar cualquier otro valor para sexo. El programa debe informar:A qué sexo corresponde la mayor cantidad de habitantes(considerar que puede ser igual)Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad.

#Declaro variables
cantidad_hombres = int()
cantidad_mujeres = int()
mujeres_edad_escolar = int()
hombres_mayores = bool()

#Inicializo variables
cantidad_hombres = 0
cantidad_mujeres = 0
mujeres_edad_escolar = 0
hombres_mayores = False

#Proceso
print("Ingresar datos del Censo")
print("La carga finaliza cuando se ingresa un sexo distinto a M o F")

while True:
    print(f"\nDatos del habitante")
    sexo = input("Sexo (M/F): ").upper()
    edad = int(input("Edad: "))

    #Sumantoria de hombres
    if (sexo == "M"): 
        cantidad_hombres += 1
        if (edad > 80): hombres_mayores = True

    #Sumatoria de mujeres
    elif (sexo == "F"):
         cantidad_mujeres += 1
         if (edad >= 4 and edad <= 18): mujeres_edad_escolar += 1

    #La carga finaliza cuando se ingrese un valor de sexo distinto a M y F
    else: break

print("\nInforme general del Censo")
print(f"Cantidad de hombres: {cantidad_hombres}")
print(f"Cantidad de mujeres: {cantidad_mujeres}")

if (cantidad_hombres > cantidad_mujeres): print("La mayor cantidad de habitantes son hombres")
elif (cantidad_mujeres > cantidad_hombres): print("La mayor cantidad de habitantes son mujeres")
else: print("Misma cantidad de habitantes entre hombres y mujeres")

print(f"Cantidad de mujeres en edad escolar: {mujeres_edad_escolar}")

if (hombres_mayores): print("Hay al menos un varon mayor de edad")
else: print("No hay hombres mayores de edad")


#Prueba de escritorio
'''
Entrada                                 
Ingresar datos del Censo
La carga finaliza cuando se ingresa un sexo distinto a M o F

Datos del habitante
Sexo (M/F): M
Edad: 30

Datos del habitante
Sexo (M/F): M
Edad: 81

Datos del habitante
Sexo (M/F): F
Edad: 15

Datos del habitante
Sexo (M/F): F
Edad: 18 

Datos del habitante
Sexo (M/F): F
Edad: 29

Datos del habitante
Sexo (M/F): Q
Edad: 20
__________________________________________
Salida

Informe general del Censo
Cantidad de hombres: 2
Cantidad de mujeres: 3
La mayor cantidad de habitantes son mujeres
Cantidad de mujeres en edad escolar: 2
Hay al menos un varon mayor de edad
__________________________________________

Proceso (Valores que toman las variables)

cantidad_hombres =      0 | 1 | 2
cantidad_mujeres =      0 | 1 | 2 | 3
mujeres_edad_escolar =  0 | 1 | 2
hombres_mayores =   False | True

'''