import os
os.system("cls")

#Enunciado
# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
# - Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
# - Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

#Declaro variables
equipos = list()
resultados = list()

#Inicializo variables
equipos = [
    [#Jornada 1
    ["Boca Juniors", "River Plate"],
    ["Racing Club", "Independiente"],
    ["San Lorenzo", "Huracan"],
    ["Estudiantes LP", "Gimnasia LP"]
    ],
    [#Jornada 2
    ["San Lorenzo", "Racing Club"],
    ["River Plate", "Independiente"],
    ["Gimnasia LP", "Boca Juniors"],
    ["Huracan", "Estudiantes LP"]  
    ],
    [#Jornada 3
    ["Estudiantes LP", "River Plate"],
    ["Independiente", "San Lorenzo"],
    ["Racing Club", "Gimnasia LP"],
    ["Boca Juniors", "Huracan"]  
    ]
]

resultados = [
    [#Jornada 1
    [2, 1],
    [2, 2],
    [1, 4],
    [3, 2]
    ],
    [#Jornada 2
    [2, 3],
    [1, 5],
    [3, 3],
    [1, 1]
    ],
    [#Jornada 3
    [0, 0],
    [2, 0],
    [3, 0],
    [1, 0]
    ]
]

#Proceso
def mostrarJornada(equipos, resultados, j): # j = nro de jornada a mostrar

    print(f"Resultados de la Fecha {j+1}")
    for i in range(4): #4 Partidos por Jornada
        print(f"{equipos[j][i][0]} {resultados[j][i][0]}  {equipos[j][i][1]} {resultados[j][i][1]}")

def mostrarTemporada(equipos, resultados):

    print("Resultados de la Temporada actual")
    for j in range(len(equipos)):
        print(f"\nResultados de la Fecha {j+1}")

        for i in range(4): #4 Partidos por Jornada
            print(f"{equipos[j][i][0]} {resultados[j][i][0]}  {equipos[j][i][1]} {resultados[j][i][1]}")


# mostrarJornada(equipos, resultados, 2)
# mostrarTemporada(equipos, resultados)   



