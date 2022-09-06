import os
os.system("cls")

#Enunciado
# Conversión de medidas. Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: yardas pulgadas centimetros metros Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro = 100 centimetros

#Declaro variables
pies = int()
yardas = float()
pulgadas = int()
centimetros = float()
metros = float()

#Inicializo variables
pies = 0
yardas = 0
pulgadas = 0
centimetros = 0.0
metros = 0.0

#Proceso
print("Conversion de medidas")
pies = int(input("Ingresar una medida en pies: "))

pulgadas = pies * 12
yardas = pies / 3
centimetros = pulgadas * 2.54
metros = centimetros / 100

print(f"\n{pies} pie/s es igual a: ")
print(f"{pulgadas} pulgadas")
print(f"{yardas} yardas")
print(f"{centimetros} centimetros")
print(f"{metros} metros")