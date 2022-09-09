import os
os.system("cls")

#Enunciado
# Dada la fracción P/Q, para P y Q naturales informar la mayor cantidad de simplificaciones. Desarrolle y utilice una función que reciba dos números naturales y retorne el menor factor común. Ej: 360/60 = 180/30 = 90/15 = 30/5 = 6/1

#Proceso
def simplificar(P, Q):
    primos = (2, 3, 5, 7, 11)

    for n in primos:
    
        while True:
            if (P % n == 0 and Q % n == 0):
                P /= n
                Q /= n
            
            else: break
    
    return [int(P), int(Q)]

#Casos de prueba
fraccion1 = simplificar(105, 210)
fraccion2 = simplificar(15, 45)
fraccion3 = simplificar(22, 44)
fraccion4 = simplificar(9, 24)

print(f"{fraccion1[0]}/{fraccion1[1]}")
print(f"{fraccion2[0]}/{fraccion2[1]}")
print(f"{fraccion3[0]}/{fraccion3[1]}")
print(f"{fraccion4[0]}/{fraccion4[1]}")

#Prueba de escritorio
'''
Entrada (4 casos de prueba)                        
105 / 210
15 / 45
22 / 44
9 / 4
__________________________________________

Salida
1 / 2
1 / 3
1 / 2
3 / 8
__________________________________________

'''