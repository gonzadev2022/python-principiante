import os
os.system("cls")

#Enunciado
# Desarrollar una rutina tal que dados una base y un exponente, enteros positivos, calcule  y retorne la potencia.

#Proceso
def potenciar(base, exponente):
    if (base < 0 or exponente < 0): return
    return base ** exponente

print(potenciar(10, 2))
print(potenciar(10, 3))
print(potenciar(20, 2))
