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
frase_sin_punto = str()
letras_ingresadas = int()
vocales_ingresadas = int()
pje_vocales = float()
palabras_ingresadas = int()
longitud_palabras = int()
promedio = float()
palabra_mas_larga = int()
palabras_con_ta = int()
vocales = tuple()

#Inicializo variables
frase = ""
frase_sin_punto = ""
letras_ingresadas = 0     #Punto A
vocales_ingresadas = 0    #Punto A
pje_vocales = 0.0         #Punto A
palabras_ingresadas = 0   #Punto B
longitud_palabras = 0     #Punto B
promedio = 0.0   #Punto B
palabra_mas_larga = 0      #Punto C
palabras_con_ta = 0        #Punto D
vocales = ("a", "e", "i", "o", "u")
        
#Proceso
print("Analisis de texto")
print("La carga de la frase finaliza cuando se ingresa un punto final\n")

while not(frase.endswith(".")):
    
    frase = input("Ingresa una frase: ").lower()
    if (frase == "."): break

    if (frase.endswith(".")): 
        frase_sin_punto = frase[0: len(frase)-1]
    else: 
        frase_sin_punto = frase

    for palabra in frase_sin_punto.split():

        #Punto A
        for letra in palabra:

            letras_ingresadas += 1
            if (letra in vocales): 
                vocales_ingresadas += 1
        
        #Punto B
        palabras_ingresadas += 1
        longitud_palabras += len(palabra)

        #Punto C
        if (palabras_ingresadas == 1) or (len(palabra) > palabra_mas_larga):
            palabra_mas_larga = len(palabra)
        
        #Punto D
        if palabra.startswith("ta"):
            palabras_con_ta += 1
    
pje_vocales = vocales_ingresadas * 100 / (letras_ingresadas)  #Punto A
promedio = longitud_palabras // palabras_ingresadas #Punto B

print("\nResultados")
print(f"Total de letras: {letras_ingresadas}")
print(f"Total de vocales: {vocales_ingresadas}")
print(f"Palabras ingresadas: {palabras_ingresadas}")
print(f"Total longitud de palabras: {longitud_palabras}")

print(f"\nPorcentaje de vocales respecto del total de letras de la frase: {pje_vocales}%")
print(f"Longitud promedio de las palabras: {promedio}")
print(f"Longitud de la palabra mas larga del texto: {palabra_mas_larga}")
print(f"Cantidad de palabras que comienzan con 'ta': {palabras_con_ta}")     


#Prueba de escritorio

