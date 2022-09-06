import os
os.system("cls")

#Enunciado
# Sílaba "de" en la primera mitad: Desarrollar un programa en Python que permita cargar por teclado un texto completo. Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
# a) Determinar cuántas palabras tenían al menos un caracter que era en realidad un dígito (un caracter entre '0' y '9').
# b) Determinar cuántas palabras tenían 3 o menos letras, cuántas tenían 4 y hasta 6 letras, y cuántas tenían más de 6 letras.
# c) Determinar la longitud de la palabra más larga del texto
# d) Determinar cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra

#Declaro variables
texto = str()
textoSinPunto = str()
palabra = str()
palabras_ingresadas = int()
palabras_con_digitos = int()
palabras_cortas = int()
palabras_medianas = int()
palabras_largas = int()
palabra_mas_larga = int()
palabras_con_de = int()

#Inicializo variables
texto = ""
textoSinPunto = ""
palabra = ""
palabras_ingresadas = 0
palabras_con_digitos = 0
palabras_cortas = 0
palabras_medianas = 0
palabras_largas = 0
palabra_mas_larga = 0
palabras_con_de = 0

#Proceso

def analisis_de_texto():
    print("Analisis de texto")
    print("La carga de texto finalizara cuando se ingrese un punto\n")

    while not(texto.endswith(".")):

        texto = input("Ingresar texto: ").lower()
        if (texto == "."): break

        if (texto.endswith(".")): textoSinPunto = texto[0: len(texto)-1]
        else: textoSinPunto = texto

        for palabra in textoSinPunto.split():

            #Punto A
            if not palabra.isalpha(): palabras_con_digitos += 1

            #Punto B
            if len(palabra) <= 3: palabras_cortas += 1
            if len(palabra) >= 4 and len(palabra) <= 6: palabras_medianas += 1
            if len(palabra) > 6: palabras_largas += 1

            #Punto C
            if (palabras_ingresadas == 1 or len(palabra) > palabra_mas_larga):
                palabra_mas_larga = len(palabra)

            #Punto D
            if (palabra.find("de") < int(len(palabra) / 2) and palabra.find("de") != -1):
                palabras_con_de += 1

    print("\nResultados")
    print(f"Cantidad de palabras que contenian al menos un digito: {palabras_con_digitos}")
    print(f"Cantidad de palabras que tienen 3 letras o menos: {palabras_cortas}")
    print(f"Cantidad de palabras que tienen entre 4 y 6 letras: {palabras_medianas}")
    print(f"Cantidad de palabras que tienen mas de 6 letras: {palabras_largas}")
    print(f"Longitud de la palabra mas larga del texto: {palabra_mas_larga} letras")
    print(f"Cantidad de palabras que contienen la expresion de en la primera mitad de la palabra: {palabras_con_de}")

# analisis_de_texto()
