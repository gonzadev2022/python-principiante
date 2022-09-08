import os
os.system("cls")

#Enunciado
# Análisis de texto: Se solicita crear un programa que permita ingresar un texto, las palabras se encontrarán separadas únicamente por espacios en blanco y el mismo debe finalizar con un punto. En base a ese texto determinar:
# a) La cantidad de palabras que comienzan y terminan en vocal
# b) La cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior
# c) El porcentaje que representa el punto a) sobre el total de palabras del texto.

#Declaro variables
palabras_con_vocales = int() #Contador del punto A
palabras_con_misma_letra = int() #Contador del punto B
palabras_ingresadas = int() #Dato necesario para calcular el punto C
pje_palabras_con_vocales = int() #Porcentaje pedido en punto C
texto = str()
texto_sin_punto = str()
primera_letra = str()
ultima_letra = str()
palabra_actual = str()
ultimaLetraAnterior = str()
vocales = tuple()

#Inicializo variables
palabras_con_vocales = 0
palabras_con_misma_letra = 0 
palabras_ingresadas = 0
pje_palabras_con_vocales = 0
texto = ""
texto_sin_punto = ""
primera_letra = ""
ultima_letra = ""
palabra_actual = ""
ultima_letra_anterior = ""
vocales = ("a", "e", "i", "o", "u")

#Proceso

print("Analisis de texto")
print("Ingresar un texto finalizado con un punto\n")

texto = input("Ingresar texto: ").lower()

#Le quito el punto final al texto para poder iterar palabra por palabra sin problemas
if (texto.endswith(".")): texto_sin_punto = texto[0: len(texto)-1]
else: texto_sin_punto = texto

for palabra_actual in texto_sin_punto.split():

    palabras_ingresadas += 1

    #Cantidad de palabras que comienzan y terminan en vocal
    primera_letra = palabra_actual[0]
    ultima_letra = palabra_actual[len(palabra_actual) - 1]

    if (primera_letra in vocales) and (ultima_letra in vocales):
        palabras_con_vocales += 1
        
    #Cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior
    if (palabras_ingresadas > 1) and (ultima_letra_anterior == primera_letra) :
        palabras_con_misma_letra += 1
            
    ultima_letra_anterior = ultima_letra #Guardo ultima letra actual para la siguiente comparacion

pje_palabras_con_vocales = int(palabras_con_vocales * 100 / palabras_ingresadas)

print("\nResultados")
print(f"Se ingresaron un total de {palabras_ingresadas} palabras")
print(f"A: Cantidad de palabras que comienzan y terminan en vocal: {palabras_con_vocales}")
print(f"B: Cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior: {palabras_con_misma_letra}")
print(f"C: El porcentaje que representa el punto A sobre el total de palabras del texto: {pje_palabras_con_vocales}%")


#Prueba de escritorio
'''
Entrada                                 
Analisis de texto
Ingresar un texto finalizado con un punto

Ingresar texto: yo era bueno programando hasta que me doble el tobillo.
__________________________________________

Salida
Resultados
Se ingresaron un total de 10 palabras
A: Cantidad de palabras que comienzan y terminan en vocal: 1
B: Cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior: 1
C: El porcentaje que representa el punto A sobre el total de palabras del texto: 10%
__________________________________________

Proceso (Valores que toman las variables)

palabras_con_vocales =      0 | 1 (era)
palabras_con_misma_letra =  0 | 1 (doble el)
palabras_ingresadas =       0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
pje_palabras_con_vocales =  0 | 10 (porcentaje)
texto =                    "" | "yo era bueno programando hasta que me doble el tobillo."
texto_sin_punto =          "" | "yo era bueno programando hasta que me doble el tobillo"
palabra_actual =           "" | "yo"| "era"| "bueno" | "programando" | "hasta" | "que" | "me" | "doble" | "el" | "tobillo"
primera_letra =            "" | "y" | "e" | "b" | "p" | "h" | "q" | "m" | "d" | "e" | "t"
ultima_letra =             "" | "o" | "a" | "o" | "o" | "a" | "e" | "e" | "e" | "l" | "o"
ultima_letra_anterior =    "" | "o" | "a" | "o" | "o" | "a" | "e" | "e" | "e" | "l" | "o"
vocales = ("a", "e", "i", "o", "u")

'''