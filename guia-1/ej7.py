import os
os.system("cls")

#Enunciado
# Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero? ¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado).

#Declaro variables
numero = int()

#Inicializo variables
numero = 0

#Proceso
numero = int(input("Ingrese un numero entero: "))

print(f"Ultimo digito: {numero % 10}")
print(f"Ultimos dos digitos: {numero % 100}") 