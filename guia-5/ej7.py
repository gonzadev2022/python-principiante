import os
os.system("cls")

#Enunciado
# Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA. El dato que recibe es un longint con una fecha en formato aaaammdd.

#Proceso
def cambiarFormatoFecha(aaaa, mm, dd):
    dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (mm < 1 or mm > 12): return "Mes fuera de rango"
    if (dd < 1 or dd > dias_del_mes[mm-1]): return "Dia fuera de rango"
    return f"{dd}/{mm}/{str(aaaa)[2:4]}"

fecha = cambiarFormatoFecha(2010, 11, 30)
print(fecha)

