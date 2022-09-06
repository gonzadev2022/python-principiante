import os
os.system("cls")

#Enunciado
# Se quiere generar el codigo de programacion necesario para realizar la afinacion de un piano. Para esto, el afinador posee un dispositivo que escucha la nota de cada tecla, la compara con una nota esperada, e indica si es correcta o no. La nota escuchada en el piano representa la nota esperada. Hay dos tipos de telcas, blancas o negras, por lo que hay dos formas de representar la nota, con una celda blanca(vacia) o negra. En el caso contrario, el dispositivo indicara que la nota del piano debe afinarse y esto representara marcando la nota mediante una celda de color rojo. La siguiente imagen muestra un ejemplo antes y despues de la verificacion donde:

#Cada columna representa una tecla o nota del piano
#Solo se representan las primeras 12 teclas del piano
#La cuarta tecla tambien esta afinada, pues ambas son de color blanco
#La segunda tecla esta desafinada, pues la nota del piano escuchada es de color negro, y la esperada es de color blanco.
#Se le pide que implemente el procedimiento VerificarAfinacionDePiano() que indica con un casillero rojo aquellas nteclas del piano que deben afinarse, para un piano de 88 teclas.

#Proceso

# N = Tecla Negra   B = Tecla Blanca
nota_piano = ["N", "N", "B", "B", "N", "N", "N", "B", "N", "B", "B", "N"]
nota_esperada = ["N", "B", "N", "B", "B", "N", "B", "N", "B", "B", "N", "N"]

def VerificarAfinacionDePiano(nota_piano, nota_esperada):

    # B = nota afinada   R = Debe afinarse
    afinacion = []

    for i in range(12):
        if (nota_piano[i] == nota_esperada[i]): 
            afinacion.append("No")
        else: 
            afinacion.append("Si")

    print("\nLuego de llamar al procedimiento")
    print("Nota Piano:      ","  |  ".join(nota_piano))
    print("Nota esperada:   ","  |  ".join(nota_esperada))
    print("¿Debe afinarse?: "," |  ".join(afinacion))


print("Antes de llamar al procedimiento")
print("Nota Piano:      "," | ".join(nota_piano))
print("Nota esperada:   "," | ".join(nota_esperada))
VerificarAfinacionDePiano(nota_piano, nota_esperada)



