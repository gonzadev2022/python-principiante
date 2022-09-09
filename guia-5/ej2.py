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

    print("La carga de numeros finalizara cuando se ingrese el un cero")

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
    porcentaje_de_pares = 0
    secuencia_menores_que7 = True

    for n in lista:

        numeros_ingresados += 1

        #Punto A: Cantidad de nros pares
        if (n % 2 == 0): 
            pares += 1

        #Punto B: Cantidad de nros terminados de 4 o 5
        if (n % 10 == 5) or (n % 10 == 4): 
            ultimo_digito += 1

        #Punto C: Determinando menor impar multiplo de 3
        if (n % 3 == 0) and (n % 2 != 0) and (numeros_ingresados == 1 or n < menor_impar):
            menor_impar = n

        #Punto D: Determinando si solo se ingresan solo nros menores que 7
        if (n >= 7):
            secuencia_menores_que7 = False

        
    
    porcentaje_de_pares = int(pares * 100 / numeros_ingresados) #Punto A
    
    #Resultados
    print(f"\nPorcentaje de numeros pares de la lista: {porcentaje_de_pares}%")
    print(f"Cantidad de numeros con ultimo digito cuatro o cinco: {ultimo_digito}")
    print(f"Menor numero impar divisible por tres: {menor_impar}")
    
    if(secuencia_menores_que7): print("La secuencia numerica solo esta formada por numeros menores que 7")
    else: print("La secuencia numerica no esta formada por numeros menores que 7")

lista = generar_secuencia()
operaciones_secuencia_numerica(lista)


#Prueba de escritorio
'''
Entrada                                 
La carga de numeros finalizara cuando se ingrese el un cero

Ingrese un numero: 6
Ingrese un numero: 12
Ingrese un numero: 18
Ingrese un numero: 24
Ingrese un numero: 30
Ingrese un numero: 3
Ingrese un numero: 1
Ingrese un numero: 0
____________________________________________________________________________________

Salida
Porcentaje de numeros pares de la lista: 71%
Cantidad de numeros con ultimo digito cuatro o cinco: 1
Menor numero impar divisible por tres: 3
La secuencia numerica no esta formada por numeros menores que 7
____________________________________________________________________________________

'''