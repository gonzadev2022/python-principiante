import os
os.system("cls")

#Enunciado
# Secuencia numérica II. Ingresar un secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar:
# a) El promedio de los números que son múltiplos de 6
# b) Cantidad de números que son divisor exacto del anterior
# c) Indicar la cantidad de veces que se generó una secuencia ascendente de 3 o más números impares

#Declaro variables
numeroActual = int()
numerosIngresados = int()
totalMultiplosDeSeis = int()    
multiplosDeSeis = int()        
promedio = float()           
numerosDivisorExacto = int()   
numerosImpares = int()          
secuenciaImpar = int()  
primerImpar = bool()

#Inicializo variables
numeroActual = 0
numerosIngresados = 0
totalMultiplosDeSeis = 0    #Punto A
multiplosDeSeis = 0         #Punto A 
promedio = 0.0              #Punto A
numerosDivisorExacto = 0    #Punto B
numerosImpares = 0          #Punto C
secuenciaImpar = 0          #Punto C
primerImpar = True          #Punto C

#Proceso
print("Secuencia numerica")
print("La carga finaliza cuando se ingresa el cero\n")

while True:
    numeroActual = int(input("Ingresa un numero: " ))
    if (numeroActual == 0): break

    numerosIngresados += 1
    
    #Punto A
    if (numeroActual % 6 == 0):
        totalMultiplosDeSeis += numeroActual
        multiplosDeSeis += 1
    
    #Punto B
    if (numerosIngresados == 1):
        numeroAnterior = numeroActual
    else:
        if (numeroAnterior % numeroActual == 0):
            numerosDivisorExacto += 1
        
    #Punto C
    if (numeroActual % 2 != 0):
        if (numeroActual > numeroAnterior or primerImpar):
            numerosImpares += 1
            primerImpar = False
        
            if (numerosImpares == 3):
                secuenciaImpar += 1
                print(f"Serie ascendente impar completa")
        else: 
            numerosImpares = 1 #Igualo la variable a uno en caso que un nro impar rompa la serie ascendente

    else:
        numerosImpares = 0 #Reinicio variable cada vez se ingresa un numero par
        primerImpar = True
        print(f"Serie ascendente rota")

    numeroAnterior = numeroActual #Actualizo variable para las comparaciones del punto B y C

if (multiplosDeSeis > 0):
    promedio = totalMultiplosDeSeis / multiplosDeSeis #Punto A

print("\nResultados")
print(f"Promedio de numeros multiplos de seis ingresados: {promedio}")
print(f"Cantidad de números que son divisor exacto del anterior: {numerosDivisorExacto}")
print(f"Cantidad de veces que se generó una secuencia ascendente de 3 o más números impares: {secuenciaImpar}")


