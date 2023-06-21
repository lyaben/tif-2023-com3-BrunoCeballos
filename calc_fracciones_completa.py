#Esta función ve si el número ingresado es una fracción.
def fraccionValida(n):
    try:
        #Descomponer fracción
        resultado = 0
        longitud = len(n)
        inicio = 0
        ubicacionBarra = 0
        hayBarra = False
        while inicio < longitud:
            #print(f"Caracter: '{n[inicio:inicio+1]}'")
            inicio = inicio + 1
            if n[inicio:inicio+1] == "/":
                ubicacionBarra = inicio #arrancando en 0 la cadena
                hayBarra = True
                #print(f"ubicacionBarra: '{ubicacionBarra}'")
        
        if hayBarra:
            numerador = n[:ubicacionBarra]
            #print(f"numerador: '{numerador}'")
            denominador = n[ubicacionBarra+1:]
            #print(f"denominador: '{denominador}'")
            resultado = int(numerador) / int(denominador)
            #print(f"resultado: '{resultado}'")
        else:
            #puede ser que que sea un numero sin denominador
            resultado = int(n) / 1
            #print(f"resultado: '{resultado}'")
        return True
    except ValueError:
            print(f"El valor '{n}' no pudo ser procesado...")
            return False

#Esta función devuelve el numerador de una fracción.
def fraccionNumerador(n):
    try:
        longitud = len(n)
        inicio = 0
        ubicacionBarra = 0
        while inicio < longitud:
            #print(f"Caracter: '{n[inicio:inicio+1]}'")
            inicio = inicio + 1
            if n[inicio:inicio+1] == "/":
                ubicacionBarra = inicio #arrancando en 0 la cadena
                #print(f"ubicacionBarra: '{ubicacionBarra}'")
        if ubicacionBarra == 0:
            return n
        else:
            return n[:ubicacionBarra]
    except ValueError:
            print(f"El valor '{n}' no pudo ser procesado...")
            return 0

#Esta función devuelve el denominador de una fracción.
def fraccionDenominador(n):
    try:
        longitud = len(n)
        inicio = 0
        ubicacionBarra = 0
        while inicio < longitud:
            #print(f"Caracter: '{n[inicio:inicio+1]}'")
            inicio = inicio + 1
            if n[inicio:inicio+1] == "/":
                ubicacionBarra = inicio #arrancando en 0 la cadena
                #print(f"ubicacionBarra: '{ubicacionBarra}'")
        if ubicacionBarra == 0:
            return 1
        else:
            return n[ubicacionBarra+1:]
    except ValueError:
            print(f"El valor '{n}' no pudo ser procesado...")
            return 0

#Esta función devuelve la suma de dos fracciones
def sumarFraccion(f1, f2):
    try:
        resultado = ""
        numeradorTotal = 0
        num1 = 0
        num2 = 0
        den1 = 0
        den2 = 0
        
        if f1 == "":
            return f2
        else:
            #aca hago la suma de f1 + f2
            numerador1 = fraccionNumerador(f1)
            denominador1 = fraccionDenominador(f1)
            numerador2 = fraccionNumerador(f2)
            denominador2 = fraccionDenominador(f2)
            if denominador1 != denominador2:
                #Me fijo si un denominador es divisor del otro.
                if (int(denominador1) % int(denominador2)) == 0 or (int(denominador2) % int(denominador1)) == 0:
                    if int(denominador1) > int(denominador2):
                        #1ra fracción
                        num1 = int(numerador1)
                        den1 = int(denominador1)
                        #2da fracción
                        num2 = int(numerador2) * (int(denominador1)/int(denominador2))
                        den2 = int(denominador2) * (int(denominador1)/int(denominador2))
                        
                        numeradorTotal = num1 + num2
                        resultado = str(int(numeradorTotal)) +  "/" + str(int(den1))
                    else:
                        #1ra fracción
                        num1 = int(numerador1) * (int(denominador2)/int(denominador1))
                        den1 = int(denominador1) * (int(denominador2)/int(denominador1))
                        #2da fracción
                        num2 = int(numerador2)
                        den2 = int(denominador2)
                        
                        numeradorTotal = num1 + num2
                        resultado = str(int(numeradorTotal)) +  "/" + str(int(den1))
                else:
                    #1ra fracción
                    num1 = int(numerador1) * int(denominador2)
                    den1 = int(denominador1) * int(denominador2)
                    #2da fracción
                    num2 = int(numerador2) * int(denominador1)
                    den2 = int(denominador2) * int(denominador1)
                    
                    numeradorTotal = num1 + num2
                    resultado = str(int(numeradorTotal)) +  "/" + str(int(den1))
            else:
                numeradorTotal = int(numerador1) + int(numerador2)
                resultado = str(int(numeradorTotal)) +  "/" + str(int(denominador1))
        
        return resultado
    except ValueError:
        print(f"La suma de fracciones no pudo ser procesada...")
        return ""

#Esta función devuelve la resta de dos fracciones
def restarFraccion(f1, f2):
    try:
        resultado = ""
        numeradorTotal = 0
        num1 = 0
        num2 = 0
        den1 = 0
        den2 = 0
        
        if f1 == "":
            return f2
        else:
            #aca hago la resta de f1 - f2
            numerador1 = fraccionNumerador(f1)
            denominador1 = fraccionDenominador(f1)
            numerador2 = fraccionNumerador(f2)
            denominador2 = fraccionDenominador(f2)
            if denominador1 != denominador2:
                #Me fijo si un denominador es divisor del otro.
                if (int(denominador1) % int(denominador2)) == 0 or (int(denominador2) % int(denominador1)) == 0:
                    if int(denominador1) > int(denominador2):
                        #1ra fracción
                        num1 = int(numerador1)
                        den1 = int(denominador1)
                        #2da fracción
                        num2 = int(numerador2) * (int(denominador1)/int(denominador2))
                        den2 = int(denominador2) * (int(denominador1)/int(denominador2))
                        
                        numeradorTotal = num1 - num2
                        resultado = str(int(numeradorTotal)) +  "/" + str(int(den1))
                    else:
                        #1ra fracción
                        num1 = int(numerador1) * (int(denominador2)/int(denominador1))
                        den1 = int(denominador1) * (int(denominador2)/int(denominador1))
                        #2da fracción
                        num2 = int(numerador2)
                        den2 = int(denominador2)
                        
                        numeradorTotal = num1 - num2
                        resultado = str(int(numeradorTotal)) +  "/" + str(int(den1))
                else:
                    #1ra fracción
                    num1 = int(numerador1) * int(denominador2)
                    den1 = int(denominador1) * int(denominador2)
                    #2da fracción
                    num2 = int(numerador2) * int(denominador1)
                    den2 = int(denominador2) * int(denominador1)
                    
                    numeradorTotal = num1 - num2
                    resultado = str(int(numeradorTotal)) +  "/" + str(int(den1))
            else:
                numeradorTotal = int(numerador1) - int(numerador2)
                resultado = str(int(numeradorTotal)) +  "/" + str(int(denominador1))
        
        return resultado
    except ValueError:
        print(f"La resta de fracciones no pudo ser procesada...")
        return ""

#Esta función devuelve la multiplicación de dos fracciones
def multiplicarFraccion(f1, f2):
    try:
        resultado = ""
        numeradorTotal = 0
        num1 = 0
        num2 = 0
        den1 = 0
        den2 = 0
        
        if f1 == "":
            return f2
        else:
            numerador1 = fraccionNumerador(f1)
            denominador1 = fraccionDenominador(f1)
            numerador2 = fraccionNumerador(f2)
            denominador2 = fraccionDenominador(f2)
            num = int(numerador1) * int(numerador2)
            den = int(denominador1) * int(denominador2)
            resultado = str(int(num)) +  "/" + str(int(den))
        return resultado
    except ValueError:
        print(f"La multiplicación de fracciones no pudo ser procesada...")
        return ""

#Esta función devuelve la división de dos fracciones
def dividirFraccion(f1, f2):
    try:
        resultado = ""
        numeradorTotal = 0
        num1 = 0
        num2 = 0
        den1 = 0
        den2 = 0
        
        if f1 == "":
            return f2
        else:
            numerador1 = fraccionNumerador(f1)
            denominador1 = fraccionDenominador(f1)
            numerador2 = fraccionNumerador(f2)
            denominador2 = fraccionDenominador(f2)
            num = int(numerador1) * int(denominador2)
            den = int(denominador1) * int(numerador2)
            resultado = str(int(num)) +  "/" + str(int(den))
        return resultado
    except ValueError:
        print(f"La división de fracciones no pudo ser procesada...")
        return ""

#Calculadora de Fracciones
def calculadoraFracciones():
    print('Calculadora de Fracciones')
    print("Operaciones disponibles:")
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicación")
    print("4: División")
    operacion = input()
    print(f"operacion '{operacion}'")
    resultado = ""
    
    if operacion != "1" and operacion != "2" and operacion != "3" and operacion != "4":
        print("Ingrese una opción valida.")
        operacion = "5"
    
    #Suma
    if int(operacion) == 1:
        fraccion = ""
        fraccion = input("Ingrese numero:")
        if fraccionDenominador(fraccion) != "0":
            while fraccion != "=":
                resultado = sumarFraccion(resultado, fraccion)
                fraccion = input("Ingrese numero:")
                if fraccionDenominador(fraccion) == "0":
                    print("El denominador no puede ser cero.")
                    fraccion = "="
                    resultado = ""
            if resultado != "":
                print(f"Resultado {resultado}")
        else:
            print("El denominador no puede ser cero.")
    #Resta
    if int(operacion) == 2:
        fraccion = ""
        fraccion = input("Ingrese numero:")
        if fraccionDenominador(fraccion) != "0":
            while fraccion != "=":
                resultado = restarFraccion(resultado, fraccion)
                fraccion = input("Ingrese numero:")
                if fraccionDenominador(fraccion) == "0":
                    print("El denominador no puede ser cero.")
                    fraccion = "="
                    resultado = ""
            if resultado != "":
                print(f"Resultado {resultado}")
        else:
            print("El denominador no puede ser cero.")
    #Multiplicación
    if int(operacion) == 3:
        fraccion = ""
        fraccion = input("Ingrese numero:")
        if fraccionDenominador(fraccion) != "0":
            while fraccion != "=":
                resultado = multiplicarFraccion(resultado, fraccion)
                fraccion = input("Ingrese numero:")
                if fraccionDenominador(fraccion) == "0":
                    print("El denominador no puede ser cero.")
                    fraccion = "="
                    resultado = ""
            if resultado != "":
                print(f"Resultado {resultado}")
        else:
            print("El denominador no puede ser cero.")
    #División
    if int(operacion) == 4:
        fraccion = ""
        fraccion = input("Ingrese numero:")
        if fraccionDenominador(fraccion) != "0":
            while fraccion != "=":
                resultado = dividirFraccion(resultado, fraccion)
                fraccion = input("Ingrese numero:")
                if fraccionDenominador(fraccion) == "0":
                    print("El denominador no puede ser cero.")
                    fraccion = "="
                    resultado = ""
            if resultado != "":
                print(f"Resultado {resultado}")
        else:
            print("El denominador no puede ser cero.")
