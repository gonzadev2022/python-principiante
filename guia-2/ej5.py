import os
os.system("cls")

#Enunciado
# Analisis de Texto.
# El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La frase finaliza con un punto, y las palabras están separadas por espacios únicamente. Se debe mostrar:
# a) El porcentaje de vocales respecto del total de letras de la frase.
# b) La longitud promedio de las palabras.
# c) La longitud de la palabra mas larga del texto.
# d) Cantidad de palabras que comienzan con "ta".

#Declaro variables
frase = str()
letrasIngresadas = int()
vocalesIngresadas = int()
pjeVocales = float()
palabrasIngresadas = int()
longitudPalabras = int()
promedioPalabras = float()
palabraMasLarga = int()
palabrasConTa = int()
vocales = tuple()

#Inicializo variables
frase = ""
letrasIngresadas = 0     #Punto A
vocalesIngresadas = 0    #Punto A
pjeVocales = 0.0         #Punto A
palabrasIngresadas = 0   #Punto B
longitudPalabras = 0     #Punto B
promedioPalabras = 0.0   #Punto B
palabraMasLarga = 0      #Punto C
palabrasConTa = 0        #Punto D
vocales = ("a", "e", "i", "o", "u")
        
#Proceso
print("Analisis de texto")
print("La carga de la frase finaliza cuando se ingresa un punto final\n")

while not(frase.endswith(".")):
    
    frase = input("Ingresa una frase: ").lower()
    if (frase == "."): break

    if (frase.endswith(".")): 
        fraseSinPunto = frase[0: len(frase)-1]
    else: 
        fraseSinPunto = frase

    for palabra in fraseSinPunto.split():

        #Punto A
        for letra in palabra:
            letrasIngresadas += 1
            if (letra in vocales): vocalesIngresadas += 1
        
        #Punto B
        palabrasIngresadas += 1
        longitudPalabras += len(palabra)

        #Punto C
        if (palabrasIngresadas == 1 or len(palabra) > palabraMasLarga):
            palabraMasLarga = len(palabra)
        
        #Punco D
        if palabra.startswith("ta"):
            palabrasConTa += 1
    
pjeVocales = vocalesIngresadas * 100 / (letrasIngresadas)  #Punto A, Resto 1 por el caracter (".")
promedioPalabras = longitudPalabras // palabrasIngresadas #Punto B

print("\nResultados")
print(f"Total de letras: {letrasIngresadas}")
print(f"Total de vocales: {vocalesIngresadas}")
print(f"Palabras ingresadas: {palabrasIngresadas}")
print(f"Total longitud de palabras: {longitudPalabras}")

print(f"\nPorcentaje de vocales respecto del total de letras de la frase: {pjeVocales}%")
print(f"Longitud promedio de las palabras: {promedioPalabras}")
print(f"Longitud de la palabra mas larga del texto: {palabraMasLarga}")
print(f"Cantidad de palabras que comienzan con 'ta': {palabrasConTa}")     