import os
os.system("cls")

#Enunciado
# La letra T y los porcentajes. Desarrollar un programa en Python que permita cargar por teclado un texto completo. Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
# a) Determinar la cantidad de palabras en las que solo aparece una única vez la letra “t”
# b) Determinar la cantidad de palabras cuya cantidad de letras es mayor a la cantidad de letras de la palabra anterior
# c) Determinar la cantidad de palabras con la cantidad de letras pares y comienzan con la letra “c”
# d) Determinar el porcentaje que representa el primer punto sobre el total de las palabras del texto procesado.

#Proceso

def analisis_de_texto(texto):
    
    palabras_ingresadas = 0
    palabras_con_t = 0
    pje_palabras_con_t = 0
    palabras_pares = 0
    palabra_anterior = ""
    mas_letras = 0  #Me dio flojera llamar esta variable con un nombre como "palabras_con_mas_letras_que_la_palabra_anterior" xd

    for palabra in texto.split():
        palabras_ingresadas += 1

        #Punto A
        if (palabra.count("t") == 1):
            palabras_con_t += 1
        
        #Punto C
        if (len(palabra) % 2 == 0 and palabra.startswith("c")):
            palabras_pares += 1

        #Punto B
        if (palabras_ingresadas == 1):
            palabra_anterior = palabra

        else:
            if (len(palabra) > len(palabra_anterior)):
                mas_letras += 1

            palabra_anterior = palabra
    
    pje_palabras_con_t = int(palabras_con_t * 100 / palabras_ingresadas)

    print(f"Cantidad de palabras en las que solo aparece una única vez la letra T: {palabras_con_t}")
    print(f"Cantidad de palabras cuya cantidad de letras es mayor a la cantidad de letras de la palabra anterior: {mas_letras}")
    print(f"Cantidad de palabras con la cantidad de letras pares y comienzan con la letra C: {palabras_pares}")
    print(f"Porcentaje que representan las palabras con T sobre el total de palabras ingresadas: {pje_palabras_con_t} %")

# analisis_de_texto("que onda gente todo bien master suera rototon")