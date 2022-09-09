import os
os.system("cls")

#Enunciado
# Desarrollar un procedimiento tal que dada una hora (HHMMSS) y un tiempo también en formato HHMMSS devuelva la nueva hora que surge de sumar el tiempo a la hora  inicial, considere también si cambió el día.

#Proceso


def agregar_cero(n):
    if (len(str(n)) == 1): return "0" + str(n)
    return n

def sumando_horas(h1, m1, s1, h2, m2, s2):
    
    dia = 1

    #Validaciones previas
    if (h1 < 0 or h1 > 23 or h2 < 0 or h2 > 23): return "Hora no valida"
    if (m1 < 0 or m1 > 59 or s2 < 0 or m2 > 59): return "Minutos no validos"
    if (s1 < 0 or s1 > 59 or s2 < 0 or s2 > 59): return "Segundos no validos"

    #Todos los bucles se repiten hasta que ya no quede tiempo por sumar

    #Segundos
    while (s2 != 0):

        if (s1 + s2 >= 60):
            s2 -= 60 - s1
            s1 = 0
            m1 += 1

        else:
            s1 += s2
            s2 -= s2

    #Minutos
    while (m2 != 0 or m1 == 60):

        if (m1 + m2 >= 60):
            m2 -= 60 - m1
            m1 = 0
            h1 += 1

        else:
            m1 += m2
            m2 -= m2

    #Horas
    while (h2 != 0 or h1 == 24):
        
        if (h1 + h2 >= 24):
            h2 -= 24 - h1
            h1 = 0
            dia += 1 #El dia cambia despues de transcurrir 24 hs

        else:
            h1 += h2
            h2 -= h2

    h1 = agregar_cero(h1)
    m1 = agregar_cero(m1)
    s1 = agregar_cero(s1)
    
    return "Dia {}  {}:{}:{}".format(dia, h1, m1, s1) 


# h1, m1, s1 = horas, minutos y segundos actuales
# h2, m2, s2 = horas, minutos y segundos a sumar

print(sumando_horas(23, 59, 59, 10, 20, 20))
print(sumando_horas(20, 40, 50, 2, 20, 0))
print(sumando_horas(5, 0, 0, 10, 30, 30))

#Prueba de escritorio
'''
Entrada (3 casos de prueba)      

Hora actual    Tiempo a sumar
23, 59, 59,    10, 20, 20
20, 40, 50,    2 , 20, 0
5,  0,  0,     10, 30, 30
__________________________________________

Salida
Dia 2  10:20:19
Dia 1  23:00:50
Dia 1  15:30:30
__________________________________________

'''


