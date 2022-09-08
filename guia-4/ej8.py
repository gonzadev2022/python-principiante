import os
os.system("cls")

#Enunciado
# Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad).

#Declaro variables
alumnos_mayores = list()
nombre = str()
edad = int()

#Inicializo variables
alumnos_mayores = []
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
        alumnos_mayores.append(alumno)

#Ordeno lista por edad de forma ascendente
alumnos_mayores.sort(key=lambda alumno: alumno[1])

print("\nAlumnos mayores de edad ordenados de forma ascendente")

for alumno in alumnos_mayores:
    print(f"{alumno[0]} {alumno[1]} años")


#Prueba de escritorio
'''
Entrada                                 
Datos del alumno
Nombre: maxi
Edad: 18

Datos del alumno
Nombre: pepe
Edad: 17

Datos del alumno
Nombre: juan
Edad: 21

Datos del alumno
Nombre: martin
Edad: 22

Datos del alumno
Nombre: maria
Edad: 19

Datos del alumno
Nombre: *
__________________________________________

Salida
Alumnos mayores de edad ordenados de forma ascendente
maxi   18 años
maria  19 años
juan   21 años
martin 22 años
__________________________________________


'''
