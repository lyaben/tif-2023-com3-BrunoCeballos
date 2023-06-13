def es_int(valor):
    try:
        valor = int(valor)
    except:
        valido = False
    else:
        if valor >= 0:
            valido = True
        else:
            valido = False
    return valido
    
def op_val(opcion):
    if opcion == '1':
        valido2 = True
    elif opcion == '2':
        valido2 = True
    elif opcion == '3':
        valido2 = True
    else:
        valido2 = False
    return valido2
    
def conv_bin_oct(numero, base):
    orig = numero
    resul = ""
    while numero >= base:
        resul = str(numero%base) + resul
        numero = numero//base
    resul = str(numero) + resul
    print (f"{orig} en base {base} es: {resul}")

def dig_hex(digito):
    if digito < 10:
        return str(digito)
    elif digito == 10:
        return 'A'
    elif digito == 11:
        return 'B'
    elif digito == 12:
        return 'C'
    elif digito == 13:
        return 'D'
    elif digito == 14:
        return 'E'
    elif digito == 15:
        return 'F'
    
def conv_hex(numero):
    orig = numero
    resul = ""
    while numero >= 16:
        resul = dig_hex(numero%16) + resul
        numero = numero//16
    resul = dig_hex(numero) + resul
    print (f"{orig} en base 16 es: {resul}")
        
def conversora():
    numero = input("Ingrese el número a convertir: ")
    while not es_int(numero):
        numero = input("Ingrese un valor válido (entero positivo): ")
    numero = int(numero)
    print (" ___________________________________________ \n"
        "|Seleccione base a la que quiere convertir: |\n"
        "|1. Bin                                     |\n"
        "|2. Hex                                     |\n"
        "|3. Oct                                     |\n"
        "|___________________________________________|\n")
    op = input()
    while not op_val(op):
        op = input("Seleccione una opción válida (1-3): ")
    if op == '1':
        conv_bin_oct(numero, 2)
    elif op == '2':
        conv_hex(numero)
    else:
        conv_bin_oct(numero, 8)   
