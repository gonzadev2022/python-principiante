import os
os.system("cls")

#Enunciado
# Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar. Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería: soledad.steffolani@umet.edu.ar

#Declaro variables
nombre = str()
apellido = str()
dominio = str()
mail = str()

#Inicializo variables
nombre = ""
apellido = ""
dominio = ""
mail = ""

#Proceso
nombre = input("Ingrese su nombre: ").lower()
apellido = input("Ingrese su apellido: ").lower()
dominio = input("Ingrese su dominio: ").lower()

if (nombre[0] == apellido[0]): 
    mail = nombre + "." + apellido + "@" + dominio
else: 
    mail = nombre[0] + apellido + "@" + dominio

print(f"\nMail sugerido: {mail}")