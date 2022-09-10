#Importo modulos
import os;
import random;

#Declaro variables
usuario = str();
contraseña = str();
opcion = str();
token_acceso = str();
token_transferencia = str();
token_reautenticacion = str();
digitos_transferencia = str();

#Inicio variables
usuario = "gonza"
contraseña = "1234";
opcion = "";
token_acceso = "none";
token_transferencia = "none";
token_reautenticacion = "none";
digitos_transferencia = "123456"; #Caso de Prueba

#Proceso

#Declaro funciones
def limpiarPantalla():
    os.system("cls");

#Funciones Token
def generador_token_acceso(contraseña):
    limpiarPantalla();
    print("HSBC Mobile");
    print("Generador de Codigo de Seguridad de Acceso");
    
    #Solicitud de contraseña
    contraseñaI = input("\nIngrese su contraseña: ");
    input("Pulse para Generar: ");

    #Generacion de codigo
    codigo = "";
    for i in range(6):
        num = random.randint(0,9);
        codigo += str(num);
    
    #Muestro codigo en pantalla
    limpiarPantalla();
    print("-----------------------------");
    print("Codigo de Seguridad de Acceso");
    print(f"          {codigo}          ");
    print("-----------------------------");
    print("Ten en cuenta que si ingresaste un dato incorrecto, el codigo sera invalido");
    input("\nPulse para volver: ");

    #Validacion
    if contraseñaI != contraseña:
        codigo = "invalido";
    
    return codigo;

def generador_token_transferencia(contraseña, digitos_transferencia):
    limpiarPantalla();
    print("HSBC Mobile");
    print("Generador de Codigo de Seguridad de Transaccion");
    
    #Solicitud de datos
    digitosI = input("\nIngresa los ultimos 6 digitos del CBU destino: ");
    contraseñaI = input("Ingrese su contraseña: ");
    input("\nPulse para Generar: ");

    #Generacion de codigo
    codigo = "";
    for i in range(6):
        num = random.randint(0,9);
        codigo += str(num);
    
    #Muestro codigo en pantalla
    limpiarPantalla();
    print("----------------------------------");
    print("Codigo de Seguridad de Transaccion");
    print(f"           {codigo}              ");
    print("----------------------------------");
    print("Ten en cuenta que si ingresaste un dato incorrecto, el codigo sera invalido");
    input("\nPulse para volver: ");

    #Validacion
    if contraseñaI != contraseña or digitosI != digitos_transferencia:
        codigo = "invalido";
    
    return codigo;

def generador_token_reautenticacion(contraseña):
    #Informacion
    limpiarPantalla();
    print("HSBC Mobile");
    print("Gnerador de Codigo de Seguridad de Reautenticacion");

    #Solicitud de contraseña
    contraseñaI = input("\nIngrese su contraseña: ");
    input("Pulse para Generar: ");

    #Generacion de codigo
    codigo = "";
    for i in range(6):
        num = random.randint(0,9);
        codigo += str(num);
    
    #Muestro codigo en pantalla
    limpiarPantalla();
    print("--------------------------------------");
    print("Codigo de Seguridad de Reautenticacion");
    print(f"              {codigo}               ");
    print("--------------------------------------");
    print("Ten en cuenta que si ingresaste un dato incorrecto, el codigo sera invalido");
    input("\nPulse para volver: ");

    #Validacion
    if contraseñaI != contraseña:
        codigo = "invalido";
    
    return codigo;

#Menu de Inicio
while True:
    limpiarPantalla();
    print("HSBC");
    print("Dispositivo de Seguridad Digital");
    print("\nMenu de Inicio");
    print("1: Generar codigo de seguridad");
    print("2: Contacto");
    print("3: HSBC Argentina Mobile Banking");
    print("4: Salir");
    print("5: Informacion de codigos actuales");
    opcion = input("\nIngrese una opcion: ");

    if opcion == "1":
        #Menu Token
        while True:
            limpiarPantalla();
            print("Selecciona el codigo de seguridad que necesitas generar");
            print("\nMenu");
            print("1: Codigo de seguridad de Acceso");
            print("2: Codigo de seguridad de Transaccion");
            print("3: Codigo de seguridad de Reautenticacion");
            print("4: Volver");
            opcion = input("\nIngrese una opcion: ");

            if opcion == "1":
                token_acceso = generador_token_acceso(contraseña);

            elif opcion == "2":
                token_transferencia = generador_token_transferencia(contraseña, digitos_transferencia);

            elif opcion == "3":
                token_reautenticacion = generador_token_reautenticacion(contraseña);

            elif opcion == "4":
                break;

            else:
                print("\nOpcion no valida");
                input("Pulse para continuar");
            
    elif opcion == "2":
        print("\nNumero de Atencion al Cliente: 0800-2901-2093");
        input("Pulse para continuar: ");

    elif opcion == "3":
        print("\nHome Banking Proximamente");
        input("Pulse para continuar: ");
    
    elif opcion == "4":
        limpiarPantalla();
        print("Fin del Programa");
        break;

    #Seccion para verificar el estado de las variables
    elif opcion == "5":
        limpiarPantalla();
        print("Codigos de Seguridad actuales");
        print("Codigo de Acceso:", token_acceso);
        print("Codigo de Transaccion:", token_transferencia);
        print("Codigo de Reautenticacion:", token_reautenticacion);
        input("\nPulse para continuar: ");
    
    else:
        print("\nOpcion no valida");
        input("Pulse para continuar: ");
    