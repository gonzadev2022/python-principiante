import os
os.system("cls")

#Enunciado
# Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.Por cada habitantes e ingresa:sexo(M/F) y edad. La carga de datos finaliza al ingresar cualquier otro valor para sexo. El programa debe informar:A qué sexo corresponde la mayor cantidad de habitantes(considerar que puede ser igual)Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad.

#Declaro variables
cantidadDeHombres = int()
cantidadDeMujeres = int()
mujeresEdadEscolar = int()
hombreMayorDeEdad = bool()

#Inicializo variables
cantidadDeHombres = 0
cantidadDeMujeres = 0
mujeresEdadEscolar = 0
hombresMayorDeEdad = False

#Proceso
print("Ingresar datos del Censo")

while True:
    print(f"\nDatos del habitante")
    sexo = input("Sexo (M/F): ").upper()
    edad = int(input("Edad: "))

    if (sexo == "M"): 
        cantidadDeHombres += 1
        if (edad > 80): hombresMayorDeEdad = True

    elif (sexo == "F"):
         cantidadDeMujeres += 1
         if (edad >= 4 and edad <= 18): mujeresEdadEscolar += 1

    else: break

print("\nInforme general del Censo")
print(f"Cantidad de hombres: {cantidadDeHombres}")
print(f"Cantidad de mujeres: {cantidadDeMujeres}")

if (cantidadDeHombres > cantidadDeMujeres): print("La mayor cantidad de habitantes son hombres")
elif (cantidadDeMujeres > cantidadDeHombres): print("La mayor cantidad de habitantes son mujeres")
else: print("Misma cantidad de habitantes entre hombres y mujeres")

print(f"Cantidad de mujeres en edad escolar: {mujeresEdadEscolar}")

if (hombresMayorDeEdad): print("Hay al menos un varon mayor de edad")
else: print("No hay hombres mayores de edad")