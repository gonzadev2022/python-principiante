import os
os.system("cls")

#Enunciado
# Análisis de texto: Se solicita crear un programa que permita ingresar un texto, las palabras se encontrarán separadas únicamente por espacios en blanco y el mismo debe finalizar con un punto. En base a ese texto determinar:
# a) La cantidad de palabras que comienzan y terminan en vocal
# b) La cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior
# c) El porcentaje que representa el punto a) sobre el total de palabras del texto.

#Declaro variables
palabrasConVocales = int() #Contador del punto A
palabrasConMismaLetra = int() #Contador del punto B
totalDePalabras = int() #Dato necesario para calcular el punto C
pjePalabrasConVocales = int() #Porcentaje pedido en punto C
texto = str()
primeraLetra = str()
ultimaLetra = str()
palabraActual = str()
ultimaLetraAnterior = str()
vocales = tuple()

#Inicializo variables
palabrasConVocales = 0
palabrasConMismaLetra = 0 
totalDePalabras = 0
pjePalabrasConVocales = 0
texto = ""
primeraLetra = ""
ultimaLetra = ""
palabraActual = ""
ultimaLetraAnterior = ""
vocales = ("a", "e", "i", "o", "u")

#Proceso

print("Analisis de texto")
print("La carga de texto finaliza cuando se ingresa un punto\n")

while True:
    texto = input("Ingresar texto: ").lower()
    if (texto == "."): break

    for palabraActual in texto.split():

        totalDePalabras += 1
        primeraLetra = palabraActual[0]
        ultimaLetra = palabraActual[len(palabraActual) - 1]

        if (primeraLetra in vocales and ultimaLetra in vocales):
            palabrasConVocales += 1
        
        if (totalDePalabras == 1):
            ultimaLetraAnterior = ultimaLetra
        
        else:
            if (ultimaLetraAnterior == primeraLetra):
                palabrasConMismaLetra += 1
            
            ultimaLetraAnterior = ultimaLetra #Guardo ultima letra actual para la siguiente comparacion

pjePalabrasConVocales = round(palabrasConVocales * 100 / totalDePalabras)

print("\nResultados")
print(f"Se ingresaron un total de {totalDePalabras} palabras")
print(f"A: Cantidad de palabras que comienzan y terminan en vocal: {palabrasConVocales}")
print(f"B: Cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior: {palabrasConMismaLetra}")
print(f"C: El porcentaje que representa el punto A sobre el total de palabras del texto: {pjePalabrasConVocales}%")
