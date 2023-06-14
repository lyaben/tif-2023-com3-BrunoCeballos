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
            
def clasica():
    op = ''
    base = input("Ingrese número: ")
    while not float_val(base):
        base = input("Ingrese un número válido: ")
    if base != '=':
        base = float(base)
        while op != '=':
            op = input("Ingrese un operando (+, -, *, /, =): ")
            while not op_val(op):
                op = input("Ingrese un operando válido (+, -, *, /, =): ")
            if op != '=':
                if op == '/':
                    num = input("Ingrese número: ")
                    while (not float_val(num)):
                        num = input("Ingrese un número válido: ")    
                    if num != '=':
                        if num == '0':
                            op = '='
                            base = "Error al dividir por 0"
                        else:
                            num = float(num)
                            base = base/num
                    else:
                        op = '='
                else:
                    num = input("Ingrese número: ")
                    while not float_val(num):
                        num = input ("Ingrese un número válido: ")
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
        print(f"Resultado: {base}")
    else:
        print("Resultado: 0")
