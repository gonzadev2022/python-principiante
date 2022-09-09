import os

#Enunciado
# Se pide que implemente el procedimiento ReparandoLaNave(). Teniendo en cuenta que el marciano de la imagen debe llegar a su hogar con suficiente combustible, se pide que recorra el camino indicado, teniendo en cuenta que en el medio se puede encontrar con combustible, el cual, es representado con celdas Rojas y Negras. El combustible podria estar en cualquier parte del camino. Si el combustible es Rojo, nuestro amigo el marciano se detendra y dejara una mancha verde en el lugar, debido a que encontro combustible de calidad, pero luego seguira su camino. Si el combustible es Negro, podra avanzar sin problemas. El camino tiene 5 celdas de ancho

#Proceso
marca = False
mapa = [
    ["H", ".", ".", ".", "."],
    ["R", ".", "N", ".", "R"],
    [".", ".", ".", ".", "."],
    ["R", "N", ".", "R", "N"],
    [".", ".", ".", ".", "."],
    ["N", ".", "R", ".", "N"],
    [".", ".", ".", ".", "."],
    ["R", ".", "R", ".", "N"],
    ["M", ".", ".", ".", "."]
]

def limpiarPantalla():
    os.system("cls")

def MostrarMapa(mapa):

    for fila in mapa:
        print("  ".join(fila))

def UbicacionMarcianito(mapa):

    for f in range(9):
        for c in range(5):
            if (mapa[f][c] == "M"):
                return [f, c]

def arriba(mapa, marca):

    #Detecto ubicacion del marcianito cumbiero
    u = UbicacionMarcianito(mapa)
    f = u[0]
    c = u[1]

    #Retorno mapa actual en caso de hacer un movimiento fuera de rango
    if (f-1 < 0 or f-1 > 8): return [mapa, marca]

    #Si el marcianito encuentra combustible rojo deja un rastro verde
    if (marca): 
        mapa[f][c] = "V"
        marca = False

    else: 
        mapa[f][c] = "."

    #Si la celda a la que nos vamos a desplazar es roja, el proximo movimiento dejara rastro
    if (mapa[f-1][c] == "R"): marca = True
    
    #El marcianito se desplaza una celda arriba
    mapa[f-1][c] = "M"
    
    return [mapa, marca]

def abajo(mapa, marca):

    u = UbicacionMarcianito(mapa)
    f = u[0]
    c = u[1]

    if (f+1 < 0 or f+1 > 8): return [mapa, marca]

    if (marca): 
        mapa[f][c] = "V"
        marca = False

    else: 
        mapa[f][c] = "."

    if (mapa[f+1][c] == "R"): marca = True

    mapa[f+1][c] = "M"
    
    return [mapa, marca]

def izquierda(mapa, marca):

    u = UbicacionMarcianito(mapa)
    f = u[0]
    c = u[1]

    if (c-1 < 0 or c-1 > 4): return [mapa, marca]

    if (marca): 
        mapa[f][c] = "V"
        marca = False

    else: 
        mapa[f][c] = "."

    if (mapa[f][c-1] == "R"): marca = True

    mapa[f][c-1] = "M"
    
    return [mapa, marca]

def derecha(mapa, marca):

    u = UbicacionMarcianito(mapa)
    f = u[0]
    c = u[1]

    if (c+1 < 0 or c+1 > 4): return [mapa, marca]

    if (marca): 
        mapa[f][c] = "V"
        marca = False

    else: 
        mapa[f][c] = "."

    if (mapa[f][c+1] == "R"): marca = True

    mapa[f][c+1] = "M"
    
    return [mapa, marca]

def ReparandoLaNave(mapa, marca):

    opcion = ""

    while (opcion != "0"):

        limpiarPantalla()
        print("Lleva al marcianito a su hogar")
        print("Controles A W S D")
        print("Pulse 0 para salir \n")
        MostrarMapa(mapa)
        opcion = input("\nMovimiento: ").upper()

        if (opcion == "A"): info = izquierda(mapa, marca)
        elif (opcion == "W"): info = arriba(mapa, marca)
        elif (opcion == "S"): info = abajo(mapa, marca)
        elif (opcion == "D"): info = derecha(mapa, marca)
        elif (opcion == "0"): break

        mapa = info[0]
        marca = info[1]

        if (mapa[0][0] == "M"):
            print("\nEl marcianito cumbiero llego a su hogar")
            print("'Suena Nunca me faltes de Antonio Rios de fondo'")
            break

ReparandoLaNave(mapa, marca)