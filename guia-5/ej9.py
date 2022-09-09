import os
os.system("cls")

#Enunciado
# Desarrollar una rutina tal que dada una fecha (AAAAMMDD) y un número natural que representa una cantidad de días, calcule y retorne la nueva fecha en tres parámetros  año (AAAA), mes (MM) y día (DD) que resulte de incrementar al parámetro fecha con el parámetro cantidad de días.

#Proceso
def tiempo_transcurrido(año, mes, dia, n): 

    dias_del_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    #Validaciones previas
    if (mes < 1 or mes > 12): return "Mes no valido"
    if (dia < 1 or dia > dias_del_mes[mes-1]): return "Dia no valido"
    if (n < 0): return "Dias a transcurrir no valido"

    #Se repite hasta que ya no queden dias por sumar
    while (n != 0):

        if (dia + n > dias_del_mes[mes-1]):
            n -= dias_del_mes[mes-1] - dia
            dia = 0
            mes += 1

            if (mes == 13):
                mes = 1
                año += 1

        else:
            dia += n
            n -= dia

    return [año, mes, dia]

#Año, mes, dias, tiempo_a_transcurrir
print(tiempo_transcurrido(2012, 0, 10, 30))
print(tiempo_transcurrido(2012, 2, 30, 31))
print(tiempo_transcurrido(2012, 2, 28, -1))
print(tiempo_transcurrido(2012, 2, 28, 32))


#Prueba de escritorio
'''
Entrada  (año, mes, dias, n)  

2012, 0, 10, 30
2012, 2, 30, 31
2012, 2, 28, -1
2012, 2, 28, 32
__________________________________________

Salida

Mes no valido
Dia no valido
Dias a transcurrir no valido
[2012, 4, 1] 
__________________________________________



'''