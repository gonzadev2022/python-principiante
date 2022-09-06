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

    candidatos.sort(reverse = True)
    votosTotales = 0

    for candidato in candidatos:
        votosTotales += candidato[0]

    for candidato in candidatos:
        candidato.append(int(candidato[0] *100 / votosTotales)) #Definiendo porcentajes

    return candidatos

def mostrar_resultados(candidatos):

    print("\nResultados finales")
    for candidato in candidatos:
        print(f"Formula: {candidato[1]}  Votos: {candidato[0]} ({candidato[2]}%)")

    if (candidatos[0][2] >= 45 or (candidatos[0][2] - candidatos[1][2]) >= 10): 
        print(f"\n{candidatos[0][1]} ganan la eleccion")
    else:
        print(f"\nHabra segunda vuelta entre {candidatos[0][1]} y {candidatos[1][1]}")


candidatos = ingresar_resultados()
candidatos = procesar_resultados(candidatos)
mostrar_resultados(candidatos)

