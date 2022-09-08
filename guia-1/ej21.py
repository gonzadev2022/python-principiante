import os
os.system("cls")

#Enunciado
# Elecciones presidenciales. Según la Ley Electoral de la República Argentina, el Presidente y el Vicepresidente se eligen de acuerdo a las siguientes reglas: Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %) de los votos afirmativos válidamente emitidos; en su defecto, aquella que hubiere obtenido el cuarenta por ciento (40 %) por lo menos de los votos afirmativos válidamente emitidos y, además, existiere una diferencia mayor de diez puntos porcentuales respecto del total de los votos afirmativos válidamente emitidos sobre la fórmula que le sigue en número de votos.
# Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escrutinio ejecutado por las Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por la Asamblea Legislativa atento lo dispuesto por el arơculo 120 de la presente ley, se realizará una segunda vuelta dentro de los treinta (30) días.
# Articulo 151. — En la segunda vuelta participarán solamente las dos fórmulas más votadas en la primera, resultando electa la que obtenga mayor número de votos afirmativos válidamente emitidos. 
# Desarrollar un programa que permita ingresar, para los 3 parados más votados: fórmula (presidente + vice) y cantidad de votos obtenidos. Luego determinar: Qué fórmula obtuvo el mayor porcentaje. Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes participan de la segunda vuelta.

#Declaro variables
candidatos = list()
formula = str()
votos = int()
votosTotales = int()

#Inicializo variables
candidatos = []
formula = ""
votos = 0
votosTotales = 0

#Proceso
def ingresar_resultados():
    
    print("Ingresar la informacion correspondiente de las elecciones presidenciales")
    candidatos = []

    for i in range(3):
        print(f"\nPartido politico {i+1}")
        formula = input("Formula (Presidente + Vice): ")
        votos = int(input("Votos: "))

        candidatos.append([votos, formula])
    
    return candidatos

def procesar_resultados(candidatos):

    #Ordenando lista de forma ascendente por votos
    candidatos.sort(reverse = True)
    votosTotales = 0

    #Contando votos totales
    for candidato in candidatos:
        votosTotales += candidato[0]

    #Definiendo y agregando porcentajes a cada lista
    for candidato in candidatos:
        candidato.append(int(candidato[0] *100 / votosTotales)) #Los porcentajes estan redondeados pa abajo

    return candidatos

def mostrar_resultados(candidatos):

    #Muestro resultados
    print("\nResultados finales")
    for candidato in candidatos:
        print("{} {} votos ({}%)".format(candidato[1], candidato[0], candidato[2]))
       
    #Ganador directo por obtener 45 puntos o mas, o por diferencia de 10 o mas puntos (de porcentaje)
    if (candidatos[0][2] >= 45 or (candidatos[0][2] - candidatos[1][2]) >= 10): 
        print(f"\n{candidatos[0][1]} ganan la eleccion")
    
    #Segunda vuelta entre los dos primeros
    else:
        print(f"\nHabra segunda vuelta entre {candidatos[0][1]} y {candidatos[1][1]}")


candidatos = ingresar_resultados()
candidatos = procesar_resultados(candidatos)
mostrar_resultados(candidatos)


#Prueba de escritorio
'''
Entrada                                 
Ingresar la informacion correspondiente de las elecciones presidenciales

Partido politico 1
Formula (Presidente + Vice): Peter Parker y Mery Jenny
Votos: 500

Partido politico 2
Formula (Presidente + Vice): Gohan y El señor Picoro
Votos: 300

Partido politico 3
Formula (Presidente + Vice): Antonio Rios y Nestor en Bloque
Votos: 700

__________________________________________
Salida
Resultados finales
Antonio Rios y Nestor en Bloque 600 votos(42%)
Peter Parker y Mery Jenny 500 votos (35%)
Gohan y El señor Picoro 300 votos (21%)

Habra segunda vuelta entre Antonio Rios y Nestor en Bloque y Peter Parker y Mery Jenny
__________________________________________

Proceso (Valores que toman las variables)

i =            1 | 2 | 3
formula =     "" | "Peter Parker y Mery Jenny" | "Gohan y El señor Picoro" | "Antonio Rios y Nestor en Bloque"
votos =        0 | 500 | 300 | 600
votosTotales = 0 | 600 | 1100 | 1400                       

candidatos = [] | (todos los cambios abajo)
#Primer paso: ingresar_resultados()

[[500, "Peter Parker y Mery Jenny"]] |
[[500, "Peter Parker y Mery Jenny"], [300, "Gohan y El señor Picoro"]] |
[[500, "Peter Parker y Mery Jenny"], [300, "Gohan y El señor Picoro"], [600, "Antonio Rios y Nestor en Bloque"]] |

#Segundo paso: procesar_resultados(candidatos) 

#Ordeno la lista anidada por votos de forma ascendente
[[600, "Antonio Rios y Nestor en Bloque"],
 [500, "Peter Parker y Mery Jenny"], 
 [300, "Gohan y El señor Picoro"]] 

#Añado los porcentajes de cada formula (redondeados)
[[600, "Antonio Rios y Nestor en Bloque", 42],
 [500, "Peter Parker y Mery Jenny", 35], 
 [300, "Gohan y El señor Picoro", 20]] 

'''

