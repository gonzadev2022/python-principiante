import os
os.system("cls")

#Enunciado
# Solamente 'a' Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en punto. En base al texto ingresado, determinar: 
# a) Cuál es la longitud de la palabra más larga. 
# b) Cuántas palabras tienen la a como única vocal 
# c) Qué porcentaje representan las que sólo tienen la vocal a sobre el total de palabras. 
# Ejemplo: "el agua clara salta por las piedras." La longitud de la palabra más larga es 7 letras. Las palabras cuya única vocal es la a son: 3 El porcentaje de estas palabras sobre el total es 43 %

#Perdon por mi ignorancia, pero todavia no entiendo la finalidad de ingresar una frase con punto final.
#Por lo que veo el punto no se tiene en cuenta a la hora de determinar los resultados que pide el ejercicio xd.

#Declaro variables

#Inicializo variables

#Proceso
def analisis_de_texto(texto):

    vocales = ["e", "i", "o", "u"]
    palabras_ingresadas = 0
    palabra_mas_larga = 0
    palabras_con_a = 0
    pje_palabras_con_a = 0 #Porcentaje

    for palabra in texto.split():
        palabras_ingresadas += 1

        #Punto A
        if (palabras_ingresadas == 1 or len(palabra) > palabra_mas_larga):
            palabra_mas_larga = len(palabra)
        
        #Punto B
        #Resolver
            
    pje_palabras_con_a = int(palabras_con_a * 100 / palabras_ingresadas)

    print(f"La longitud de la palabra mas larga es de {palabra_mas_larga} letras")
    print(f"Palabras cuya unica vocal es la A: {palabras_con_a}")
    print(f"El porcentaje de estas palabras sobre el total es {pje_palabras_con_a} %")

analisis_de_texto("el agua clara salta por las piedras")
