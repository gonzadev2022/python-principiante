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
def añoBisiesto(año):

    if (año % 4 == 0 and año % 100 != 0 or año % 400 == 0): return True
    return  False

#Punto B
def diasPorMes(mes, año):

    if añoBisiesto(año): diasFebrero = 29
    else: diasFebrero = 28

    meses = {
            1 : 31, 
            2 : diasFebrero, 
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
    
    try: return [meses[mes], meses]
    except KeyError: return [0]

#Punto C
def validarFecha(dia, mes, año):

    resultado = diasPorMes(mes, año);
    diasDelMes = resultado[0]

    if (dia > 0 and dia <= diasDelMes): return True
    return False

#Punto D
def diasRestantes_DelMes(dia, mes, año):

    fechaValida = validarFecha(dia, mes, año)
    
    if (fechaValida): 
        datos = diasPorMes(mes, año)
        diasDelMes = datos[0]
        return diasDelMes - dia

    return "La fecha no es valida"

#Punto E
def diasRestantes_DelAño(dia, mes, año):

    fechaValida = validarFecha(dia, mes, año)

    if not(fechaValida): return "La fecha no es valida"

    resultado = diasPorMes(mes, año)
    meses = resultado[1]    #Retorno el diccionario de meses para poder iterarlo
        
    diasRestantes = 0  #Contador de Dias

    for mesActual, diasDelMes in meses.items():
            
        if (mesActual == mes): 
            diasRestantes += diasDelMes - dia 

        if (mesActual > mes):
            diasRestantes += diasDelMes

    return diasRestantes
    
#Punto F
def diasTranscurridos_DelAño(dia, mes, año):

    fechaValida = validarFecha(dia, mes, año)

    if not(fechaValida): return "La fecha no es valida"

    resultado = diasPorMes(mes, año)
    meses = resultado[1]    #Retorno el diccionario de meses para poder iterarlo
        
    diasTranscurridos = 0  #Contador de Dias

    for mesActual, diasDelMes in meses.items():
            
        if (mesActual < mes): 
            diasTranscurridos += diasDelMes

        if (mesActual == mes): 
            diasTranscurridos += dia 

    return diasTranscurridos   
    
#Punto G
def diferenciaEntreFechas(dia1, mes1, año1, dia2, mes2, año2):
    
    fechaValida1 = validarFecha(dia1, mes1, año1)
    fechaValida2 = validarFecha(dia2, mes2, año2)

    #En caso de que alguna de las dos fechas se invalida, termino la funcion
    if not(fechaValida1 and fechaValida2): return "Fecha ingresada no valida"

    diferenciaEnAños = año2 - año1
    diferenciaEnMeses = (mes2 - mes1) + (diferenciaEnAños * 12)

    #Calculo de dias: Primera forma
    if (año1 == año2 and mes1 == mes2):
        diferenciaEnDias = dia2 - dia1
        return [diferenciaEnAños, diferenciaEnMeses, diferenciaEnDias]

    #Calculo de dias: Segunda forma
    if (año1 == año2):
        resultado = diasPorMes(mes1, año1) #Retorno el objeto meses para poder iterarlo
        meses = resultado[1]    
        diferenciaEnDias = 0 #Contador de dias transcurridos

        for mesActual, diasDelMes in meses.items():
            if (mesActual == mes1): 
                diferenciaEnDias += diasDelMes - dia1

            if (mesActual > mes1 and mesActual < mes2): 
                diferenciaEnDias += diasDelMes

            if (mesActual == mes2): 
                diferenciaEnDias += dia2
                break

        return [diferenciaEnAños, diferenciaEnMeses, diferenciaEnDias]
    
    #Calculo de dias: Tercera forma
    for i in range(diferenciaEnAños + 1):
        
        #Sumo dias restantes del primer año
        if (i == 0): 
            resultado = diasRestantes_DelAño(dia1, mes1, año1)
            diferenciaEnDias = resultado

        #Sumo un año completo
        elif (i < diferenciaEnAños):
            año1 += 1
            resultado = añoBisiesto(año1)
            
            if (resultado): diferenciaEnDias += 366
            else: diferenciaEnDias += 365

        #Sumo dias transcurridos del ultimo año
        else:
            resultado = diasTranscurridos_DelAño(dia2, mes2, año2)
            diferenciaEnDias += resultado
        
    return [diferenciaEnAños, diferenciaEnMeses, diferenciaEnDias]

resultado = diferenciaEntreFechas(30, 4, 2012, 1, 8, 2013)
print(resultado)
