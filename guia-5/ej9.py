import os
os.system("cls")

#Enunciado
# Desarrollar una rutina tal que dada una fecha (AAAAMMDD) y un número natural que representa una cantidad de días, calcule y retorne la nueva fecha en tres parámetros  año (AAAA), mes (MM) y día (DD) que resulte de incrementar al parámetro fecha con el parámetro cantidad de días.

#Proceso
def tiempo_transcurrido(año, mes, dia, n): 

    dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #Validaciones previas
    if (mes < 1 or mes > 12): return "Mes no valido"
    if (dia < 1 or dia > dias_del_mes[mes-1]): return "Dia no valido"
    if (n < 0): return "Los dias a transcurrir debe ser un numero positivo"

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

resultado = tiempo_transcurrido(2012, 2, 28, 31) #Año, mes, dias, tiempo_a_transcurrir
print(resultado)