#Calculadora Clásica Trabajo Grupal Final - Ceballos - Yaben

#Función que indica si el valor ingresado es un flotante o un signo '='
def float_val(entrada):
    if entrada == '=':
        valido = True
    else:
        try:
            entrada = float(entrada)
        except:
            valido = False
        else:
            valido = True
    return valido

#Función que indica si el operador ingresado es uno válido
def op_val(entrada2):
    if entrada2 == '+': 
        valido2 = True
    elif entrada2 == '-': 
        valido2 = True
    elif entrada2 == '*': 
        valido2 = True
    elif entrada2 == '/': 
        valido2 = True
    elif entrada2 == '=': 
        valido2 = True
    else:
        valido2 = False
    return valido2

#Cuerpo principal de la calculadora, se ejecuta desde el selector            
def clasica():
    op = ''
    base = input("Ingrese número: ")                        #Ingreso el número que va a servir como base
    while not float_val(base):
        base = input("Ingrese un número válido: ")          #Mientras el número no sea un float o un signo igual, lo sigo pidiendo    
    if base != '=':                                         #Si la base ingresada no es un igual, lo convierto a float y pido operando        
        base = float(base)
        while op != '=':                                    #Comienzo a operar. Se puede salir ingresando un igual en cualquier momento (cuando se pide un operando o un número)
            op = input("Ingrese un operando (+, -, *, /, =): ")
            while not op_val(op):
                op = input("Ingrese un operando válido (+, -, *, /, =): ")  #Si el operando ingresado no válido, lo sigo pidiendo
            if op != '=':                                                   #Si el operando no es un igual, pido otra número para operar
                if op == '/':                                               #Separo el caso de la división para asegurarme de no poder dividir por 0
                    num = input("Ingrese número: ")
                    while (not float_val(num)):
                        num = input("Ingrese un número válido: ")           #Si el número no es un float o un signo igual, lo sigo pidiendo
                    if num != '=':
                        if num == '0':                                      #Si el número ingresado es un 0, salgo de la calculadora e imprimo un mensaje de error
                            op = '='
                            base = "Error al dividir por 0"
                        else:
                            num = float(num)                                #Si el número es válido, hago la división
                            base = base/num
                    else:
                        op = '='
                else:
                    num = input("Ingrese número: ")                         #Si el operador no es el de división, pido un número y hago la operación que corresponda
                    while not float_val(num):
                        num = input ("Ingrese un número válido: ")          #Si el número no es un flotante o un signo igual, lo sigo pidiendo
                    if num != '=':
                        num = float(num)
                        if op == '+':
                            base = base + num
                        elif op == '-':
                            base = base - num
                        else:
                            base = base * num
                    else:
                        op = '='
        print(f"Resultado: {base}")                                         #Imprimo el resultado de las operaciones cuando ingreso '=' o el mensaje de error en caso de dividir por 0
    else:
        print("Resultado: 0")                                               #Imprimo 0 como resultado en caso de ingresar un '=' inmediatamente después de iniciar la calculadora
