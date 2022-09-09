import os
os.system("cls")

#Suponiendo que el primer dia del año fue lunes, escribir una funcion que reciba un numero con el dia del año
#(de 1 a 366) y devuelva el dia de la semana que le toca. Por ejemplo si recibe 3 debe devolver miercoles,
#si recibe 9 debe devolver martes

def definirDia(n):
    if (n < 1 or n > 366): return "Numero fuera de rango"
    if(n % 7 == 1): return "Lunes"
    if(n % 7 == 2): return "Martes"
    if(n % 7 == 3): return "Miercoles"
    if(n % 7 == 4): return "Jueves"
    if(n % 7 == 5): return "Viernes"
    if(n % 7 == 6): return "Sabado"
    return "Domingo"

print(definirDia(1))
print(definirDia(7))
print(definirDia(10))
print(definirDia(12))
print(definirDia(13))


#Prueba de escritorio
'''
Entrada 
      
1
7
10        
12
13                  
__________________________________________
Salida

Lunes
Domingo
Miercoles
Viernes
Sabado
__________________________________________

'''

