import calc_clasica as clas
import calc_fracciones as frac
import calc_conversora as conv

def mostrar_interfaz():
    print(" _______________________________\n"
    "|Ingrese función deseada:       |\n"
    "|1. Calculadora Clásica         |\n"
    "|2. Calculadora de Fracciones   |\n"
    "|3. Calculadora de Conversiones |\n"
    "|4. Salir                       |\n"
    "|_______________________________|")
    
def check_val(valor):
    if valor == '1':
        valido = True
    elif valor == '2':
        valido = True
    elif valor == '3':
        valido = True
    elif valor == '4':
        valido = True
    else:
        valido = False
    return valido

op = '0'
while op != '4':
    mostrar_interfaz()
    op = input("Función: ")
    while not check_val(op):
            op = input("Ingrese una función correcta (1-4): ")
    if op == '1':
        clas.clasica()
    elif op == '2':
        frac.fracciones()
    elif op == '3':
        conv.conversora()
    
    
