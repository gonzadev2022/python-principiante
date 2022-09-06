import os
os.system("cls")

#Enunciado
# Sólo menores que 7. Desarrollar un programa de Phyton que permita cargar por teclado un secuencia de números, uno por uno. Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a procesar. El programa debe:
# a) Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números ingresados.
# b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.
# c) Determinar el menor de los números ingresados que sean divisibles por 3.
# d) Determinar si la secuencia estaba formada sólo por números menores que 7

#Proceso
def generar_secuencia():
    
    lista = []
    n = 0

    print("La carga de numeros finalizara cuando se ingrese el numero cero")

    while True:
        n = int(input("Ingrese un numero: "))
        if (n == 0): break

        lista.append(n)

    return lista

def operaciones_secuencia_numerica(lista):

    numeros_ingresados = 0
    pares = 0
    ultimo_digito = 0
    menor_impar = 0
    primer_impar = True
    porcentaje_de_pares = 0
    secuencia_menores_que7 = True

    for n in lista:

        #Punto A
        if (n % 2 == 0): 
            pares += 1

        #Punto B
        if (n % 10 == 5 or n % 10 == 4): 
            ultimo_digito += 1

        #Punto C
        if (n % 3 == 0):
            if (primer_impar or n < menor_impar):
                menor_impar = n

            primer_impar = False

        #Punto D
        if (n >= 7):
            secuencia_menores_que7 = False

        numeros_ingresados += 1
    
    porcentaje_de_pares = int(pares * 100 / numeros_ingresados)
        
    print(f"\nPorcentaje de numeros pares de la lista: {porcentaje_de_pares}%")
    print(f"Cantidad de numeros con ultimo digito cuatro o cinco: {ultimo_digito}")
    print(f"Menor numero impar divisible por tres: {menor_impar}")
    
    if(secuencia_menores_que7): print("La secuencia numerica solo esta formada por numeros menores que 7")
    else: print("La secuencia numerica no esta formada por numeros menores que 7")

lista = generar_secuencia()
operaciones_secuencia_numerica(lista)

