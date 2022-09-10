#Importo modulos
import os;
import time;

# Declaro Variables
usuario_actual = str();
pin_actual = str();
saldo_actual = int();
intentos = int();

# Inicio Variables
usuario_actual = "gonza";
pin_actual = "1234";
saldo_actual = 1000;
intentos = 0;

#Proceso

#Declaro Funciones
def limpiarPantalla():
    os.system("cls");

def depositar(saldo_actual, pin_actual):
    while True:
        limpiarPantalla();
        print("Banco Nacion Argentina");
        print("Menu Deposito");
        print("1: $50");
        print("2: $100");
        print("3: $200");
        print("4: $500");
        print("5: Volver");
        op = input("\nSeleccione una cantidad: ");

        if op == "1": deposito = 50;
        elif op == "2": deposito = 100;
        elif op == "3": deposito = 200;
        elif op == "4": deposito = 500;
        elif op == "5": break;
        else: print("\nOpcion no valida");
        
        if (op == "1") or (op == "2") or (op == "3") or (op == "4"):
            
            #Ingreso de PIN para confirmar operacion
            while True:
                limpiarPantalla();
                print("Banco Nacion Argentina");
                print("Confirma tu operacion");
                pin_ingresado = input("\nIngrese su PIN: ");

                if pin_ingresado == pin_actual:
                    confirmacion = True;
                    break;

                elif pin_ingresado == "#":
                    print("Operacion Cancelada");
                    confirmacion = False;
                    break;

                else:
                    print("\n¡PIN Incorrecto!");
                    input("Pulse para volver a intentarlo: ");

            #Operacion confirmada
            if (confirmacion):
                print("\nEspere un momento...")
                time.sleep(1.5);
                saldo_actual += deposito;
                print(f"El deposito de ${deposito} se realizo correctamente");
                print(f"Su saldo actual es de ${saldo_actual}");
    
        input("Pulse para continuar: ");
    return saldo_actual;
    
def extraer(saldo_actual, pin_actual):
    while True:
        limpiarPantalla();
        print("Banco Nacion Argentina");
        print("Menu Extraccion");
        print("1: $50");
        print("2: $100");
        print("3: $200");
        print("4: $500");
        print("5: Volver");
        op = input("\nSeleccione una cantidad: ");
        
        if op == "1": extraccion = 50;
        elif op == "2": extraccion = 100;
        elif op == "3": extraccion = 200;
        elif op == "4": extraccion = 500;
        elif op == "5": break;
        else: print("\nOpcion no valida");
        
        if (op == "1") or (op == "2") or (op == "3") or (op == "4"):
            
            #Ingreso de PIN para confirmar operacion
            while True:
                limpiarPantalla();
                print("Banco Nacion Argentina");
                print("Confirma tu operacion");
                pin_ingresado = input("\nIngrese su PIN: ");

                if pin_ingresado == pin_actual:
                    confirmacion = True;
                    break;

                elif pin_ingresado == "#":
                    print("Operacion Cancelada");
                    confirmacion = False;
                    break;

                else:
                    print("\n¡PIN Incorrecto!");
                    input("Pulse para volver a intentarlo: ");

            #Operacion confirmada
            if (confirmacion):
                if (saldo_actual >= extraccion):
                    print("\nEspere un momento...")
                    time.sleep(1.5);
                    saldo_actual -= extraccion;
                    print(f"La extraccion de ${extraccion} se realizo correctamente");
                    print(f"Su saldo actual es de ${saldo_actual}");

                else:
                    print(f"No tenes fondos suficientes para extrer ${extraccion}");
                    print(f"Debido a que su saldo actual es de ${saldo_actual}");
                
        input("\nPulse para continuar: ");
    return saldo_actual;

def cambiarPin(pin_actual):
    while True:
        limpiarPantalla();
        print("Banco Nacion Argentina");
        print("Menu Cambio de PIN");
        print("1. Cambiar PIN");
        print("2. Volver");
        op = input("\nIngrese una opcion: ");

        if op == "1":
            #Ingreso de PIN actual
            while True:
                limpiarPantalla();
                print("Banco Nacion Argentina");
                print("¡Vamos a cambiar tu PIN!");
                pin_ingresado = input("\nIngrese el PIN actual: ");

                if pin_ingresado == pin_actual:
                    pin_valido = True;
                    break;

                elif pin_ingresado == "#":
                    pin_valido = False;
                    print("Operacion Cancelada");
                    input("\nPulse para volver: ");
                    break;

                else:
                    print("¡PIN Incorrecto!");
                    input("Pulse para volver a intentarlo: ");

            #Ingreso de PIN nuevo
            while (pin_valido):
                limpiarPantalla();
                print("Banco Nacion Argentina");
                print("¡Vamos a cambiar tu PIN!");
                print("\nIngrese el PIN actual:", pin_actual);
                pin_nuevo = input("Ingrese el nuevo PIN: ");

                #Validaciones
                if (pin_nuevo.isdigit() == True) and (len(pin_nuevo) == 4) and (pin_nuevo != pin_actual):
                    pin_actual = pin_nuevo;
                    print("\nEl PIN se cambio exitosamente");
                    input("Pulse para volver: ");
                    break;
                
                elif pin_nuevo == pin_actual:
                    print("\nEl PIN nuevo tiene que ser distinto al PIN actual");
                    
                else:
                    print("\nEl PIN debe tener 4 digitos");

                input("Pulse para volver a intentarlo: ");
            
        elif op == "2":
            break;
        
        else:
            print("\nOpcion no valida");
            input("Pulse para continuar: ");

    return pin_actual;

#Menu de Ingreso
while intentos < 3:
    limpiarPantalla();
    print("¡Bienvenido a Banco Nacion!");
    usuario_ingresado = input("Usuario: ");
    pin_ingresado = input("Contraseña: ");

    #Acceso al Menu Principal del Cajero
    if usuario_ingresado == usuario_actual and pin_ingresado == pin_actual:
        
        while True:
            limpiarPantalla();
            print("Banco Nacion Argentina");
            print("Menu");
            print("1: Consultar Saldo");
            print("2: Depositar");
            print("3: Retirar");
            print("4: Cambiar PIN");
            print("5: Salir");
            op = input("\nIngrese una opcion: ");

            #Operaciones Disponibles
            if op == "1": 
                print("\nSu saldo actual es de $", saldo_actual);
                input("Pulse para continuar: ");
                
            elif op == "2": 
                saldo_actual = depositar(saldo_actual, pin_actual);
                
            elif op == "3": 
                saldo_actual = extraer(saldo_actual, pin_actual);
                
            elif op == "4": 
                pin_actual = cambiarPin(pin_actual);
                
            elif op == "5": 
                limpiarPantalla();
                print("Saliste de tu cuenta");
                break;
            
            else: 
                print("\nOpcion no valida");
                input("Pulse para continuar: ");
        break;
     
    #Usuario Incorrecto 
    elif usuario_ingresado != usuario_actual:
        print("\nUsuario desconocido");
        input("Pulse para volver a intentarlo: ");

    #Contraseña Incorrecta
    else:
        print("\nContraseña incorrecta");
        intentos += 1;
        
        if intentos < 3:
            print("Intento N°", intentos);
            input("Pulse para volver a intentarlo: ");
        else:
            print("La cuenta", usuario_actual, "fue bloqueda por motivos de seguridad");
            
    
    