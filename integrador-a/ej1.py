import os
os.system("cls")

#Enunciado
# Escribir funciones que resuelvan los siguientes problemas
#Punto A: Dado un año indicar si es bisiesto. Nota: un año es bisiesto si un nro es divible por 4 pero no por 100, o si es divisile por 400
#Punto B: Dado un mes y un año, devolver la cantidad de dias correspondientes
#Punto C: Dada una fecha (dia, mes, año), indicar si es valida o no
#Punto D: Dada una fecha, indicar los dias que faltan hasta fin de mes
#Punto E: Dada una fecha, indicar los dias que faltan hasta fin de año  
#Punto F: Dada una fecha, indicar la cantidad de dias transcurridos en ese año hasta la fecha
#Punto G: Dadas dos fechas (dia1, mes1, año1, dia2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y dias
# Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible

#Punto A
def AñoBisiesto(año):

    if ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0): return True
    return False

#Punto B
def DiasDelMes(mes, año):

    if (mes < 1 or mes > 12): return 0

    if (AñoBisiesto(año)): dias_de_febrero = 29
    else: dias_de_febrero = 28

    dias_del_mes = [31, dias_de_febrero, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return dias_del_mes[mes - 1]

#Punto C
def FechaValida(dia, mes, año):

    if (dia < 1 or dia > DiasDelMes(mes, año)): return False
    return True

#Punto D
def DiasRestantesDelMes(dia, mes, año):

    if (FechaValida(dia, mes, año)): return DiasDelMes(mes, año) - dia
    return "Fecha no valida"

#Punto E
def DiasRestantesDelAño(dia, mes, año):

    if not(FechaValida(dia, mes, año)): return "Fecha no valida"

    dias_restantes = 0
    dias_restantes += DiasRestantesDelMes(dia, mes, año)

    for mes_actual in range(mes+1, 13):
        dias_restantes += DiasDelMes(mes_actual, año)

    return dias_restantes

#Punto F
def DiasTranscurridosDelAño(dia, mes, año):

    if not(FechaValida(dia, mes, año)): return "Fecha no valida"

    dias_transcurridos = 0 

    for mes_actual in range(1, mes):
        dias_transcurridos += DiasDelMes(mes_actual, año)

    dias_transcurridos += dia
    return dias_transcurridos

#Punto G
def DiferenciaEntreFechas(dia1, mes1, año1, dia2, mes2, año2):
    
    if not(FechaValida(dia1, mes1, año1)): return "Fecha 1 no valida"
    if not(FechaValida(dia2, mes2, año2)): return "Fecha 2 no valida"

    dias_transcurridos = 0  

    #Solucion 1: solo diferencia de dias
    if (mes1 == mes2 and año1 == año2): 
        dias_transcurridos = dia2 - dia1

    #Solucion 2: diferencia de fechas en el mismo año
    elif (año1 == año2):

        dias_transcurridos += DiasRestantesDelMes(dia1, mes1, año1)

        for mes_actual in range(mes1+1, mes2):
            dias_transcurridos += DiasDelMes(mes_actual, año1)

        dias_transcurridos += dia2

    #Solucion 3: diferencia de fechas en diferentes años
    else:
        for año_actual in range(año1, año2+1):

            if (año_actual == año1):
                dias_transcurridos += DiasRestantesDelAño(dia1, mes1, año1)

            elif (año_actual == año2):
                dias_transcurridos += DiasTranscurridosDelAño(dia2, mes2, año2)

            else:
                if (AñoBisiesto(año_actual)): dias_transcurridos += 366
                else: dias_transcurridos += 365

    return dias_transcurridos
    
#Casos de prueba
print(DiferenciaEntreFechas(1, 4, 2012, 30, 4, 2012))
print(DiferenciaEntreFechas(1, 4, 2012, 1, 10, 2012))
print(DiferenciaEntreFechas(1, 4, 2012, 6, 4, 2013))


#Prueba de escritorio
'''
Entrada     

Desde           Hasta
1, 4, 2012,    30, 4 , 2012
1, 4, 2012,    1 , 10, 2012
1, 4, 2012,    6 , 4 , 2013
___________________________________________

Salida (expresado en dias)
29
183
370
___________________________________________

'''
