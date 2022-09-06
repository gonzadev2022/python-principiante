import os
os.system("cls")

#Enunciado
# Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad).

#Declaro variables
alumnosMayores = list()
nombre = str()
edad = int()

#Inicializo variables
alumnosMayores = []
nombre = ""
edad = 0

#Proceso
print("La carga de datos finaliza cuando se ingresa un asterisco (*)")

while True:
    print("\nDatos del alumno")

    nombre = input("Nombre: ")
    if (nombre == "*"): break

    edad = int(input("Edad: "))

    if (edad >= 18):
        alumno = [nombre, edad]
        alumnosMayores.append(alumno)

alumnosMayores.sort(key=lambda alumno: alumno[1])

print("\nAlumnos mayores de edad ordenados de forma ascendente")
for alumno in alumnosMayores:
    print(f"{alumno[0]} {alumno[1]} años")


