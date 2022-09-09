import os
os.system("cls")

#Enunciado
# Solamente 'a' Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en punto. En base al texto ingresado, determinar: 
# a) Cuál es la longitud de la palabra más larga. 
# b) Cuántas palabras tienen la a como única vocal 
# c) Qué porcentaje representan las que sólo tienen la vocal a sobre el total de palabras. 
# Ejemplo: "el agua clara salta por las piedras." La longitud de la palabra más larga es 7 letras. Las palabras cuya única vocal es la a son: 3 El porcentaje de estas palabras sobre el total es 43 %


#Proceso
def analisis_de_texto(texto):

    vocales = ("e", "i", "o", "u")
    palabras_ingresadas = 0
    palabra_mas_larga = 0
    palabras_con_a = 0     #Palabras con A como unica vocal
    pje_palabras_con_a = 0 #Porcentaje
    contador = 0

    for palabra in texto.split():

        palabras_ingresadas += 1

        #Punto A: Determinando palabra mas larga (longitud)
        if (palabras_ingresadas == 1 or len(palabra) > palabra_mas_larga):
            palabra_mas_larga = len(palabra)
        
        #Punto B: palabras con A como unica vocal
        for letra in palabra:

            if (letra in vocales): 
                contador += 1

        if (contador == 0): 
            palabras_con_a += 1 
        
        contador = 0 
            
    pje_palabras_con_a = int(palabras_con_a * 100 / palabras_ingresadas) #Punto A

    print(f"La longitud de la palabra mas larga es de {palabra_mas_larga} letras")
    print(f"Palabras cuya unica vocal es la A: {palabras_con_a}")
    print(f"El porcentaje de estas palabras sobre el total es {pje_palabras_con_a} %")

analisis_de_texto("el agua clara salta por las piedras")


#Prueba de escritorio
'''
Entrada                                 
el agua clara salta por las piedras
__________________________________________

Salida
La longitud de la palabra mas larga es de 7 letras
Palabras cuya unica vocal es la A: 3
El porcentaje de estas palabras sobre el total es {pje_palabras_con_a} 43%
__________________________________________

'''