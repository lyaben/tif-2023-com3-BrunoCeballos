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

def deno_op(deno_base, deno_num):
    if deno_base != deno_num:
        resul = deno_base * deno_num
    else:
        resul = deno_base
    return resul

def nume_sum(nume_base, deno_aux, nume_num, deno_num, deno_base):
    resul2 = ((deno_base//deno_aux)*nume_base)+((deno_base//deno_num)*nume_num)
    return resul2

def nume_res(nume_base, deno_aux, nume_num, deno_num, deno_base):
    resul3 = ((deno_base//deno_aux)*nume_base)-((deno_base//deno_num)*nume_num)
    return resul3
            
def fracciones():
    error = 0
    op = ''
    nume_base = input("Ingrese numerador: ")
    while not nume_val(nume_base):
            nume_base = input ("Ingrese un numerador valido (entero): ")
    if nume_base != '=':
        nume_base = int(nume_base)
        deno_base = input("Ingrese denominador: ")
        while not deno_val(deno_base):
            deno_base = input("Ingrese un denominador válido (entero distinto de 0): ")
        deno_base = int(deno_base)
        while op != '=':
            op = input("Ingrese un operando (+, -, *, /, =): ")
            while not op_val(op):
                op = input("Ingrese un operando válido (+, -, *, /, =): ")
            if op != '=':
                if op == '/':
                    nume_num = input("Ingrese numerador: ")
                    while (not nume_val(nume_num)):
                        nume_num = input("Ingrese un numerador válido (entero): ")    
                    if nume_num != '=':
                        if nume_num == '0':
                            op = '='
                            error = 1
                        else:
                            nume_num = int(nume_num)
                            deno_num = input("Ingrese denominador: ")
                            while not deno_val(deno_num):
                                deno_num = input("Ingrese un denominador válido (entero distinto de 0): ")
                            deno_num = int(deno_num)
                            nume_base = nume_base * deno_num
                            deno_base = deno_base * nume_num                       
                    else:
                        op = '='
                else:
                    nume_num = input("Ingrese numerador: ")
                    while not nume_val(nume_num):
                        nume_num = input ("Ingrese un numerador válido (entero): ")
                    if nume_num != '=':
                        nume_num = int(nume_num)
                        deno_num = input("Ingrese denominador: ")
                        while not deno_val(deno_num):
                            deno_num = input("Ingrese un denominador válido (entero distinto de 0): ")
                        deno_num = int(deno_num)
                        if op == '+':
                            deno_aux = deno_base
                            deno_base = deno_op(deno_base, deno_num)
                            nume_base = nume_sum(nume_base, deno_aux, nume_num, deno_num, deno_base)
                        elif op == '-':
                            deno_aux = deno_base
                            deno_base = deno_op(deno_base, deno_num)
                            nume_base = nume_res(nume_base, deno_aux, nume_num, deno_num, deno_base)
                        else:
                            nume_base = nume_base * nume_num
                            deno_base = deno_base * deno_num
                    else:
                        op = '='
        if error == 1:
            print("Error al dividir por 0")
        else:
            if deno_base < 0:
                nume_base = nume_base * -1
                deno_base = deno_base * -1
            print(f"Resultado: {nume_base}/{deno_base}")
    else:
        print("Resultado: 0")