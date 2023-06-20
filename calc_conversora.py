#Calculadora Conversora Trabajo Grupal Final - Ceballos - Yaben

#Función que verifica que la entrada sea un entero positivo
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

#Función que verifica que la opción elegida sea válida    
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

#Función que convierte un número en base decimal en un string en base 2 u 8 y lo imprime
def conv_bin_oct(numero, base):
    orig = numero
    resul = ""
    while numero >= base:
        resul = str(numero%base) + resul
        numero = numero//base
    resul = str(numero) + resul
    print (f"{orig} en base {base} es: {resul}")

#Función que convierte digitos en base decimal a caracteres en base hexadecimal
def dig_hex(digito):
    if digito < 10:
        hexa = str(digito)
    elif digito == 10:
        hexa = 'A'
    elif digito == 11:
        hexa = 'B'
    elif digito == 12:
        hexa = 'C'
    elif digito == 13:
        hexa = 'D'
    elif digito == 14:
        hexa = 'E'
    elif digito == 15:
        hexa = 'F'
    return hexa

#Función que convierte un número en base decimal en un sting en base 16 y lo imprime
def conv_hex(numero):
    orig = numero
    resul = ""
    while numero >= 16:
        resul = dig_hex(numero%16) + resul
        numero = numero//16
    resul = dig_hex(numero) + resul
    print (f"{orig} en base 16 es: {resul}")

#Cuerpo principal de la calculadora, se ejecuta desde el selector         
def conversora():
    numero = input("Ingrese el número a convertir: ")   #Pido el número a convertir, verificando que sea un entero positivo
    while not es_int(numero):
        numero = input("Ingrese un valor válido (entero positivo): ")
    numero = int(numero)
    print (" ___________________________________________ \n"    #Imprimo la interfaz de selección
        "|Seleccione base a la que quiere convertir: |\n"
        "|1. Bin                                     |\n"
        "|2. Hex                                     |\n"
        "|3. Oct                                     |\n"
        "|___________________________________________|\n")
    op = input()                    #Ingreso la opción elegida
    while not op_val(op):           #Verifico que la opción ingresada sea válida
        op = input("Seleccione una opción válida (1-3): ")
    if op == '1':                   #Derivo la opción a la función correspondiente
        conv_bin_oct(numero, 2)
    elif op == '2':
        conv_hex(numero)
    else:
        conv_bin_oct(numero, 8)   
