# Enunciado 
# Una empresa que vende latas te pide que realices un programa el cual pueda registar las compras de un determinado numero de clientes

# Por cada cliente se debe ingresar:
# Numero de cliente
# Tipo de lata (A o B)
# Unidades compradas

# Aclaraciones:
# El tipo de lata "A" tiene un valor de $120
# El tipo de lata "B" tiene un valor de $150
# La cantidad de clientes a registrar se ingresa al principio del programa

#En base a esto, determinar:
# 1. ¿Cual fue el cliente que mas compro en pesos?
# 2. ¿Cuantos clientes compraron mas de 100 latas?
# 3. ¿Cuantas latas de tipo "A" se vendieron?

#Declaro variables
LATA_A = int()
LATA_B = int()
nro_compras = int()
nro_cliente = str()
tipo_lata = str()
unidades = int()
precio = int()
precio_maximo = int()
nro_cliente_maximo = int()
contador_cliente = int()
acumulador_latas = int()

#Inicializo variables
LATA_A = 120
LATA_B = 150
nro_compras = 0
nro_cliente = ""
tipo_lata = ""
unidades = 0
precio = 0
precio_maximo = 0
nro_cliente_maximo = 0
contador_clientes = 0
acumulador_latas = 0


#Proceso
nro_compras = int(input("¿Cuantas compras queres registrar?: "));

for i in range(nro_compras):

    #Ingreso de datos
    nro_cliente = input("\nNumero de cliente: ")
    tipo_lata = input("Tipo de lata (A o B): ").upper()
    unidades = int(input("Unidades compradas: "))

    if (tipo_lata == "A"): precio = LATA_A * unidades
    else: precio = LATA_B * unidades

    #Punto 1
    if (i == 0 or precio > precio_maximo):
        precio_maximo = precio
        nro_cliente_maximo = nro_cliente

    #Punto 2
    if (unidades > 100):
        contador_clientes += 1

    #Punto 3
    if (tipo_lata == "A"):
        acumulador_latas += unidades

#Salida
print(f"\nEl cliente que mas compro en pesos fue el cliente nro {nro_cliente_maximo}")
print(f"{contador_clientes} clientes compraron mas de 100 latas")
print(f"Se vendieron {acumulador_latas} latas de tipo A")


#Prueba de Escritorio
'''
#Entrada

¿Cuantas compras queres registrar?: 3

Numero de cliente: 001
Tipo de lata (A o B): A
Unidades compradas: 50

Numero de cliente: 002
Tipo de lata (A o B): B
Unidades compradas: 150

Numero de cliente: 003
Tipo de lata (A o B): A
Unidades compradas: 120

#Salida

El cliente que mas compro en pesos fue el cliente nro 002
2 clientes compraron mas de 100 latas")
Se vendieron 170 latas de tipo A")

#Proceso (Valores que toman las variables)

LATA_A = 120
LATA_B = 150
nro_compras =         0 |  3
nro_cliente =        "" | "001" | "002" | "003"
tipo_lata =          "" |  "A"  |  "B"  |  "C"
unidades =           0  |   50  |  150  |  120
precio =             0  |  6000 | 22500 |  14400
precio_maximo =      0  |  6000 | 22500
nro_cliente_maximo = 0  | "001" | "002"
contador_clientes =  0  |   1   |   2
acumulador_latas =   0  |   50  |  170
'''
