import os
os.system("cls")

#Enunciado
# Galería de Arte. Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá: 
# A: verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000). 
# B: Determinar cuántos tienen antigüedad inferior a 10 años. 
# C: Si no hay ninguno, imprimir el mensaje “Renovar stock”.

#Declaro variables
año_del_cuadro = int()
cuadros_antiguos = int()
cuadros_recientes = int()

#Inicializo variables
año_del_cuadro = 0
cuadros_antiguos = 0
cuadros_recientes = 0

#Proceso
print("Ingresar el año de creacion de los siguentes cuadros")
    
for i in range(3):  
    año_del_cuadro = int(input(f"Cuadro {i+1}: "))

    if (año_del_cuadro <= 1900): #Punto A
        cuadros_antiguos += 1

    if ((2022 - año_del_cuadro) < 10): #Punto B
        cuadros_recientes += 1

print("\nResultados")

if (cuadros_antiguos == 3): print("Todos los cuadros son anteriores al siglo XX")
else: print("No todos los cuadros son anteriores al siglo XX")

if (cuadros_recientes > 0): print(f"{cuadros_recientes} cuadro/s tiene/n antiguedad inferior a 10 años")
else: print("Renovar stock")



