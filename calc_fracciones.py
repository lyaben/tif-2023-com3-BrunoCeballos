#Calculadora de Fracciones Trabajo Grupal Final - Ceballos - Yaben

#Función que verifica que la entrada sea un número entero o el signo '='
def nume_val(entrada):
    if entrada == '=':
        valido = True
    else:
        try:
            entrada = int(entrada)
        except:
            valido = False
        else:
            valido = True
    return valido

#Función que verifica que el denominador ingresado sea un entero distinto de '0'
def deno_val(entrada2):
    if entrada2 == '0':
        valido2 = False
    else:
        try:
            entrada2 = int(entrada2)
        except:
            valido2 = False
        else:
            valido2 = True
    return valido2

#Función que verifica que el operador ingresdo sea válido
def op_val(entrada3):
    if entrada3 == '+': 
        valido3 = True
    elif entrada3 == '-': 
        valido3 = True
    elif entrada3 == '*': 
        valido3 = True
    elif entrada3 == '/': 
        valido3 = True
    elif entrada3 == '=': 
        valido3 = True
    else:
        valido3 = False
    return valido3

#Función que devuelve el denominador para sumas y restas (si el denominador de ambas fracciones es el mismo, devuelve ese)
def deno_op(deno_base, deno_num):
    if deno_base != deno_num:
        resul = deno_base * deno_num
    else:
        resul = deno_base
    return resul

#Función que devuelve el numerador de una suma de fracciones
def nume_sum(nume_base, deno_aux, nume_num, deno_num, deno_base):
    resul2 = ((deno_base//deno_aux)*nume_base)+((deno_base//deno_num)*nume_num)
    return resul2

#Función que devuelve el numerador de una resta de fracciones
def nume_res(nume_base, deno_aux, nume_num, deno_num, deno_base):
    resul3 = ((deno_base//deno_aux)*nume_base)-((deno_base//deno_num)*nume_num)
    return resul3
 
#Cuerpo principal de la calculadora, se ejecuta desde el selector            
def fracciones():
    error = 0
    op = ''
    nume_base = input("Ingrese numerador: ")    #Pido el ingreso de la primera fracción, comenzando por el numerador
    while not nume_val(nume_base):              #Verifico que el numero ingresado sea un entero
            nume_base = input ("Ingrese un numerador valido (entero): ")
    if nume_base != '=':                        #Si ingreso el operador '=' como primera entrada, salgo de la calculadora
        nume_base = int(nume_base)
        deno_base = input("Ingrese denominador: ")  #Pido el ingreso del denominador de la primera fracción
        while not deno_val(deno_base):              #Verifico que sea un entero distinto de 0
            deno_base = input("Ingrese un denominador válido (entero distinto de 0): ")
        deno_base = int(deno_base)
        while op != '=':                            #Inicio el loop pidiendo operadores (siempre que el operador ingresado sea distinto a '=')
            op = input("Ingrese un operando (+, -, *, /, =): ")
            while not op_val(op):                   #Verifico que el operador ingresado sea uno de los 5 válidos
                op = input("Ingrese un operando válido (+, -, *, /, =): ")
            if op != '=':
                if op == '/':                       #Si el operador es '/', pido una segunda fracción (verificando su num y deno) y opero
                    nume_num = input("Ingrese numerador: ")
                    while (not nume_val(nume_num)):     #Verifico que lo ingresado sea válido como numerador
                        nume_num = input("Ingrese un numerador válido (entero): ")    
                    if nume_num != '=':             #Chequeo que el numerador ingresado no sea un signo '=' para salir
                        if nume_num == '0':         #Si el numerador ingresado es un 0, levanto el flag de error por división por cero y pongo '=' como operador, para salir
                            op = '='
                            error = 1
                        else:                       #En caso contrario, opero después de pedir y verificar un numerador válido
                            nume_num = int(nume_num)
                            deno_num = input("Ingrese denominador: ")
                            while not deno_val(deno_num):
                                deno_num = input("Ingrese un denominador válido (entero distinto de 0): ")
                            deno_num = int(deno_num)
                            nume_base = nume_base * deno_num
                            deno_base = deno_base * nume_num                       
                    else:
                        op = '='
                else:                           #En caso de que la operación no sea división, pido una segunda fracción y opero
                    nume_num = input("Ingrese numerador: ")
                    while not nume_val(nume_num):       #Verifico que lo ingresado sea válido como numerador
                        nume_num = input ("Ingrese un numerador válido (entero): ")
                    if nume_num != '=':         #Chequeo que el numerador ingresado no sea un signo '=' para salir
                        nume_num = int(nume_num)
                        deno_num = input("Ingrese denominador: ")   #Pido el numerador de la segunda fracción
                        while not deno_val(deno_num):       #Verifico que el denominador ingresado sea válido
                            deno_num = input("Ingrese un denominador válido (entero distinto de 0): ")
                        deno_num = int(deno_num)
                        if op == '+':           #Si el operador es '+', ejecuto la suma de fracciones      
                            deno_aux = deno_base
                            deno_base = deno_op(deno_base, deno_num)
                            nume_base = nume_sum(nume_base, deno_aux, nume_num, deno_num, deno_base)
                        elif op == '-':         #Si el operador es '-', ejecuto la resta de fracciones
                            deno_aux = deno_base
                            deno_base = deno_op(deno_base, deno_num)
                            nume_base = nume_res(nume_base, deno_aux, nume_num, deno_num, deno_base)
                        else:                   #Ejecuto la multiplicación de fracciones en última instancia (el operador ya está verificado como uno válido)
                            nume_base = nume_base * nume_num
                            deno_base = deno_base * deno_num
                    else:
                        op = '='                #Si ingreso '=' como numerador, pongo '=' en el operador para salir de la calculadora
        if error == 1:          #Si el flag de error está arriba, imprimo el mensaje de error
            print("Error al dividir por 0")
        else:                   #En caso contrario, saco el signo menos del denominador (en caso de tenerlo) e imprimo el resultado
            if deno_base < 0:
                nume_base = nume_base * -1
                deno_base = deno_base * -1
            print(f"Resultado: {nume_base}/{deno_base}")
    else:
        print("Resultado: 0")   #Imprimo 0 como resultado si ingreo '=' ni bien arranco la calculadora