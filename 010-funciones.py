"""
Funciones: se utilizan para encapsular una lógica muy concreta y 
tambien trata de evitar errores.

"""

def calculadora():
    primer_valor = float(input("Ingresa un primer dato: "))
    segundo_valor = float(input("Ingresa un segundo dato: "))
    operacion = input("Elegí la operación que queres realizar: suma/resta/multiplicacion/division: ")
    
    if operacion == "suma" or operacion == "SUMA":
        resultado = (primer_valor + segundo_valor)
        print(resultado)    
    elif operacion == "resta" or operacion == "RESTA":
        resultado = (primer_valor - segundo_valor)
        print(resultado)    
    elif operacion == "multiplicacion" or operacion == "MULTIPLICACION":
        resultado = (primer_valor * segundo_valor)
        print(resultado)
    elif operacion == "division" or operacion == "DIVISION":
        resultado = (primer_valor / segundo_valor)
        print(resultado) 
    else:
        print("Coloca el nombre de la operacion correctamente: en minúscula o mayúscula sin tilde")                
        
calculadora() 

print("##### otra forma de ejecutar la función son con los parámetros #####")

def calculos(primer_valor, segundo_valor):
    return (primer_valor + segundo_valor)
    
    
print("el total es: ",calculos(15,4578))  



def print_data(name, surname):
    return (f"mi nombre es: {name} y mi apellido es: {surname}")


print(print_data("Gustavo", "Palacios"))


# crear parámetros con valores infinitos
def texts(*text):
    return text


print(texts("hola gente como estan?", "es todo una mentira"))


# iterar un texto en una función
def texts2(*text):
    for texto in text:
        print(texto)
# no es necesario poner un print        
texts2("hola", "muhcas gracias por su colaboración", "encantado de conocerte")

# imprimir en mayúsculas
def texts2(*text):
    for texto in text:
        print(texto.upper())
# no es necesario poner un print        
texts2("hola", "muhcas gracias por su colaboración", "encantado de conocerte")   

       