#Importo modulos
import os;
import random;

#Declaro variables
usuario = str();
contraseña = str();
saldo_actual = int();
token_acceso = str();
token_tranferencia = str();
token_reautenticacion = str();
digitos_transferencia = str();
opcion = str();

#Inicio variables
usuario = "gonza";
contraseña = "1234";
saldo_actual = 100000;
token_acceso = "none";
token_tranferencia = "none";
token_reautenticacion = "none";
digitos_transferencia = "none";
opcion = "";
servicio1 = [False, "SIN PAGAR"];
servicio2 = [False, "SIN PAGAR"];

#Proceso

#Funcion Limpiar Pantalla
def limpiarPantalla():
    os.system("cls");

#3 Funciones Token
def generador_token_acceso(contraseña):
    #Informacion
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

#3 Funciones HomeBanking
def transferencia(saldo_actual):
    while True:    
        limpiarPantalla();
        print("HSBC Home Banking");
        print("Menu");
        print("1: Realizar nueva Transferencia");
        print("2: Volver");
        opcion = input("\nIngrese una opcion: ");
    
        if opcion == "1":

            #Variables
            cuenta = "Caja de Ahorro";
            nro_cuenta = "123456789000";
            token_transferencia = "none";
            linea = "--------------------------------------------";

            #Paso 1: Ingreso de datos
            while True:
                try:
                    limpiarPantalla();
                    print("HSBC Home Banking");
                    print("Nueva tranferencia");
                    print("Paso 1: Ingreso de datos");

                    print(linea);
                    print("Datos Personales");
                    print("Cuenta:", cuenta);
                    print("Numero:", nro_cuenta);
                    print("Saldo: ARS", saldo_actual);

                    print(linea);
                    print("Datos del Beneficiario");
                    nombreB = input("Nombre: ").capitalize();
                    nro_cuentaB = input("CBU: ");
                    tipoB = input("Tipo de cuenta: ").capitalize();

                    print(linea);
                    print("Detalles de tranferencia");
                    importe = float(input("Importe a tranferir: "));
                    concepto = input("Concepto: ").capitalize();
                    print(linea);

                    #Validaciones
                    if importe <= 0:
                        print("\nEl importe a transferir debe ser mayor a cero");
                        input("Pulse para volver a intentarlo: ");

                    elif importe > saldo_actual:
                        print("\nNo tenes fondos suficientes para realizar esta tranferencia");
                        input("Pulse para volver a intentarlo: ");

                    #Simulando que un CBU tenga 12 digitos
                    elif len(nro_cuentaB) != 12 or nro_cuentaB.isdigit() == False:
                        print("\nEl CBU del beneficiario debe contener 12 digitos");
                        input("Pulse para volver a intentarlo: ");

                    else:
                        digitos_transferencia = nro_cuentaB[6:12];
                        input("\nPulse para continuar: ");
                        break;

                except ValueError:
                    print("\nError: Ingresaste un caracter no valido");
                    print("Pulse para avolver a intentarlo: ");

            #Paso 2: Ingreso de Codigo de seguridad de transaccion
            while True:
                limpiarPantalla();
                print("HSBC Home Banking");
                print("Nueva tranferencia");
                print("Paso 2: Ingreso de Codigo de Seguridad");
                print("----------------------------------------------------------------");
                print("Para continuar con la transferencia debera ingresar un Codigo");
                print("de Transaccion generado por su dispositivo de seguridad");
                print(f"\nUltimos 6 digitos del CBU del Beneficiario: {digitos_transferencia} (Dato requerido)");
                print("Ingrese # para generar su codigo de transferencia");
                print("----------------------------------------------------------------");

                token_transferenciaI = input("\nCodigo de Tranferencia: ");

                if token_transferenciaI == "#":
                    token_transferencia = generador_token_transferencia(contraseña, digitos_transferencia);

                elif token_transferenciaI != token_transferencia:
                    print("\n¡Codigo de Transferencia Invalido!");
                    input("Pulse para volver a intentarlo: ");
                else:
                    print("\n¡Codigo de Transferencia Correcto!");
                    input("Pulse para continuar: ");
                    break;

            #Paso 3: Verificacion de datos
            while True:
                limpiarPantalla();
                print("HSBC Home Banking");
                print("Nueva tranferencia");
                print("Paso 3: Verificacion de Datos");

                print(linea);
                print("Datos personales");
                print("Cuenta:                      ", cuenta);
                print("CBU:                         ", nro_cuenta);
                print("Saldo:                        ARS", saldo_actual);
                print("\nDatos del beneficiario");
                print("Titular de la cuenta destino:", nombreB);
                print("CBU destino:                 ", nro_cuentaB);
                print("Tipo de cuenta destino:      ", tipoB);
                print("\nDetalles de la tranferencia");
                print("Importe a acreditar:          ARS", importe);
                print("Importe a debitar:            ARS", importe);
                print("Concepto:                    ", concepto);
                print("Banco de la cuenta destino:  ","Banco Nacion Argentina\n");
                print(linea);
                opcion = input("\nPulse 1 para Confirmar / Pulse 9 para Cancelar: ");

                if opcion == "1":
                    confirmacion = True;
                    saldo_actual -= importe;
                    break;

                elif opcion == "9":
                    confirmacion = False;
                    print("\nQue rancio que sos man, hiciste todo lo anterior al pedo");
                    input("Pulse para volver: ");
                    break;

                else:
                    print("\nOpcion no valida");
                    input("Pulse para volver a intentarlo: ");

            #Paso 4: Operacion confirmada
            if (confirmacion):
                limpiarPantalla();
                print("HSBC Home Banking");
                print(f"Su transferencia de $ {importe} desde su {cuenta} {nro_cuenta} a {nombreB} fue exitosa");

                nro_control = "";
                for i in range(4):
                    num = random.randint(0,9);
                    nro_control += str(num);

                print(linea);
                print("Numero de control:       ", nro_control);
                print("Importe a acreditar:      ARS", importe);
                print("Importe a debitar:        ARS", importe);
                print("CBU destino:             ", nro_cuentaB);
                print("Concepto:                ", concepto);
                print(linea);
                input("Pulse para volver: ");

        elif opcion == "2":
            break;

        else:
            print("\nOpcion no valida");
            input("Pulse para continuar: ");
    
    return saldo_actual;

def plazoFijo(saldo_actual):
    while True:    
        limpiarPantalla();
        print("HSBC Home Banking");
        print("Menu");
        print("1: Constituir Plazo Fijo");
        print("2: Volver");
        opcion = input("\nIngrese una opcion: ");
    
        if opcion == "1":

            #Variables
            cuenta = "Caja de Ahorro";
            nro_cuenta = "123456789000";
            nro_ref = "";
            nro_plazo = "";
            linea = "--------------------------------------------";

            #Paso 1: Ingreso de datos
            while True:
                try:
                    limpiarPantalla();
                    print("HSBC Home Banking");
                    print("Constitucion del plazo fijo");
                    print("Paso 1: Ingreso de datos");

                    print(linea);
                    print(f"Cuenta debito: {cuenta} {nro_cuenta} ARS {saldo_actual}");
                    print("Monto del plazo fijo: Pesos");
                    plazo = int(input("Plazo: "));
                    monto = float(input("Monto a depositar: "));
                    print(linea);

                    #Validaciones
                    if plazo < 30 or plazo > 365:
                        print("El plazo fijo puede ser minimo de 30 dias y maximo de 365 dias");
                        input("Pulse para volver a intentarlo: ");

                    elif monto <= 300:
                        print("El monto a depositar debe ser como minimo $300");
                        input("Pulse para volver a intentarlo: ");
                    
                    elif monto > saldo_actual:
                        print("No tenes fondos suficientes para realizar este Plazo Fijo");
                        input("Pulse para volver a intentarlo: ");

                    else:
                        input("Pulse para continuar: ");
                        break;

                except ValueError:
                    print("Error: Ingresaste un caracter no valido");
                    input("Pulse para volver a intentarlo: ");

            #Paso 2: Verificacion de datos
            while True:
                #Calculos
                tna = 0.48;
                tea = 0.6012;
                intereses = (plazo * tna * monto) / 365;
                fecha = "20 de Junio de 2022";

                limpiarPantalla();
                print("HSBC Home Banking");
                print("Constitucion del plazo fijo");
                print("Paso 2: Verificacion");
                print(linea);
                print(f"Producto:             Plazo fijo");
                print(f"Plazo:                {plazo}");
                print(f"Cuenta debito:        {cuenta} {nro_cuenta}");
                print(f"Tasa Nominal Anual:   {tna*100}%");
                print(f"Tasa Efectiva Anual:  {tea*100}%");
                print(f"Intereses a percibir: ARS {intereses}");
                print(f"Monto a depositar:    ARS {monto}");
                print(f"Fecha de Apertura:    {fecha}");
                print(linea);
                opcion = input("Pulse 1 para Confirmar / Pulse 9 para Cancelar: ");

                if opcion == "1":
                    confirmacion = True;
                    saldo_actual -= monto;
                    break;

                elif opcion == "9":
                    confirmacion = False;
                    print("\nOperacion Cancelada");
                    input("Pulse para volver: ")
                    break;

                else:
                    print("\nOpcion no valida");
                    input("Pulse para volver a intentarlo: ")

            #Paso 3: Operacion confirmada
            if (confirmacion):
                limpiarPantalla();
                print("HSBC Home Banking");
                print("Constitucion del plazo fijo");
                print("\nSu Plazo Fijo se realizo correctamente");

                #Calculo de intereses
                monto_total = monto + intereses;
                
                for i in range(4):
                    num = random.randint(0,9);
                    nro_ref += str(num);

                for i in range(10):
                    num = random.randint(0,9);
                    nro_plazo += str(num);

                print(linea);
                print(f"Numero de Plazo Fijo:     {nro_ref}");
                print(f"Producto:                 Plazo fijo");
                print(f"Numero de Plazo Fijo:     {nro_plazo}");
                print(f"Tasa Nominal Anual:       {tna*100}%");
                print(f"Tasa Efectiva Anual:      {tea*100}%");
                print(f"Monto capital:            ARS {monto}");
                print(f"Monto total:              ARS {monto_total}");
                print(f"Fecha de Alta:            {fecha}");
                print(linea);
                input("Pulse para volver: ");

        elif opcion == "2":
            break;

        else:
            print("\nOpcion no valida");
            input("Pulse para continuar: ");

    return saldo_actual;

def pagoServicios(saldo_actual, servicio1, servicio2):
    token_reautenticacion = "none";
    while True:
        limpiarPantalla();
        print("HSBC");
        print("Pago de Servicios");
        print("---------------------------------------------------------------------------------");
        print("                             Proximos vencimientos\n");
        print("     Empresa          Importe a pagar       Vencimiento         Estado");
        print(f"1: Personal - Flow         $5000              01/07/22          {servicio1[1]}");
        print(f"2: Metrogas                $7000              01/07/22          {servicio2[1]}");  
        print("3: Volver");
        print("---------------------------------------------------------------------------------");
        opcion = input("Ingrese una opcion: ");

        if opcion == "1":
            #Validaciones previas
            if servicio1[0] == True:
                print("\nEl servicio ya fue pagado");
                input("Pulse para continuar: ");

            elif saldo_actual < 5000:
                print("\nNo tenes fondos suficientes para pagar este servicio");
                print(f"Debido a que tu saldo actual es de ${saldo_actual}");
                input("Pulse para continuar: ");

            #Pago de Servicio Personal-Flow
            else: 
                while True:
                    #Paso 1: Ingreso de Codigo de Reautenticacion
                    limpiarPantalla();
                    print("HSBC");
                    print("Pago de Servicios");
                    print("-----------------------------------------------------------------------");
                    print("Para realizar este pago deberas ingresar el Codigo de Reautenticacion");
                    print("generado por su Dispositivo de Seguridad");
                    print("\nIngrese # si quiere generar su codigo");
                    print("Ingrese 0 si quiere cancelar esta operacion");
                    print("-----------------------------------------------------------------------");
                    codigoI = input("\nCodigo de Reautenticacion: ");

                    if codigoI == "#":
                        token_reautenticacion = generador_token_reautenticacion(contraseña);

                    elif codigoI == "0":
                        break;

                    elif codigoI != token_reautenticacion:
                        print("\nCodigo Incorrecto");
                        input("Pulse para volver a intentarlo: ");

                    else:
                        #Paso 2: Confirmacion
                        servicio1[0] = True;
                        servicio1[1] = "PAGADO";
                        saldo_actual -= 5000;

                        limpiarPantalla();
                        print("HSBC");
                        print("Pago de Servicios");
                        print("\nEl pago del servicio Personal-Flow por $5000 se realizo correctamente");
                        print(f"Su saldo actual es de ${saldo_actual}")
                        input("\nPulse para volver: ");
                        break;

        elif opcion == "2":
            #Validaciones previas
            if servicio2[0] == True:
                print("\nEl servicio ya fue pagado");
                input("Pulse para continuar: ");

            elif saldo_actual < 7000:
                print("\nNo tenes fondos suficientes para pagar este servicio");
                print(f"Debido a que tu saldo actual es de ${saldo_actual}");
                input("Pulse para continuar: ");

            #Pago de Servicio Metrogas
            else: 
                while True:
                    #Paso 1: Ingreso de Codigo de Reautenticacion
                    limpiarPantalla();
                    print("HSBC");
                    print("Pago de Servicios");
                    print("-----------------------------------------------------------------------");
                    print("Para realizar este pago deberas ingresar el Codigo de Reautenticacion");
                    print("generado por su Dispositivo de Seguridad");
                    print("\nIngrese # si quiere generar su codigo");
                    print("Ingrese 0 si quiere cancelar esta operacion");
                    print("-----------------------------------------------------------------------");
                    codigoI = input("\nCodigo de Reautenticacion: ");

                    if codigoI == "#":
                        token_reautenticacion = generador_token_reautenticacion(contraseña);

                    elif codigoI == "0":
                        break;

                    elif codigoI != token_reautenticacion:
                        print("\nCodigo Incorrecto");
                        input("Pulse para volver a intentarlo: ");

                    else:
                        #Paso 2: Confirmacion
                        servicio2[0] = True;
                        servicio2[1] = "PAGADO";
                        saldo_actual -= 7000;

                        limpiarPantalla();
                        print("HSBC");
                        print("Pago de Servicios");
                        print("\nEl pago del servicio Metrogas por $5000 se realizo correctamente");
                        print(f"Su saldo actual es de ${saldo_actual}")
                        input("\nPulse para volver: ");
                        break;

        elif opcion == "3":
            break;

        else:
            print("\nOpcion no valida");
            input("Pulse para continuar: ");

    #Retorno la informacion necesaria para mantener actualizada la lista de proximos vencimientos
    dataServicios = [saldo_actual, servicio1, servicio2]
    return dataServicios;

#Interfaz del Home Banking

#Ingreso nombre de usuario
while True:
    limpiarPantalla();
    print("HSBC");
    print("Ingreso a Online Banking");
    usuarioI = input("\nIngresa tu nombre de usuario: ");

    if usuarioI != usuario:
        print("\n¡Usuario Incorrecto!");
        input("Pulse para volver a intentarlo: ");
    else:
        break;

#Ingreso codigo de acceso
while True:
    limpiarPantalla();
    print("HSBC");
    print("Ingreso a Online Banking");
    print("------------------------------------------------------------");
    print("Buenas tardes", usuario.capitalize());
    print("Para ingresar a su cuenta de Home Banking debera ingresar");
    print("un Codigo de acceso generado por su dispositivo de seguridad");
    print("\nIngrese # para generar su codigo de acceso");
    print("------------------------------------------------------------");
    token_accesoI = input("\nCodigo de Acceso: ");

    if token_accesoI == "#":
        token_acceso = generador_token_acceso(contraseña);

    elif token_accesoI != token_acceso:
        print("\n¡Codigo de Acceso Invalido!");
        input("Pulse para volver a intentarlo: ");
    
    else:
        break;

#Menu Principal Home Banking
while True:
    limpiarPantalla();
    print("¡Bienvenido/a a la plataforma Home Banking!");
    print("\nMenu Principal");
    print("1: Consultar saldo");
    print("2: Tranferencias");
    print("3: Constitucion de Plazo Fijo");
    print("4: Pago de Servicios");
    print("5: Salir");
    opcion = input("\nIngrese una opcion: ");

    if opcion == "1":
        print("\nTu saldo actual es de $", saldo_actual);
        input("Pulse para continuar: ");

    elif opcion == "2":
        saldo_actual = transferencia(saldo_actual);

    elif opcion == "3":
        saldo_actual = plazoFijo(saldo_actual);
    
    elif opcion == "4":
        dataServicios = pagoServicios(saldo_actual, servicio1, servicio2);
        saldo_actual = dataServicios[0];
        servicio1 = dataServicios[1];
        servicio2 = dataServicios[2];

    elif opcion == "5":
        limpiarPantalla();
        print("Saliste de tu cuenta");
        break;

    else:
        print("\nOpcion no valida");
        input("Pulse para continuar: ");
    
    