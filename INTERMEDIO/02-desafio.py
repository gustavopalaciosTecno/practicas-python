### challenges ####
# EL FAMOSO FIZZBUZZ

"""
Escribe un programa que muestre por consola (con un print) los
numeros de 1 al 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- multuplipos de 3 por la palabra "fizz".
- multiplo de 5 por la palabra "buzz".
. multiplo de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
"""
def mostrarConsola():
    for i in range(1,160):
        if i % 3 == 0:
            print("fizz", end="\n")
        elif i % 5 == 0:
            print("buzz", end="\n")  
        elif i % 5 == 0 and i % 3 == 0:
            print(f"el valor {i} es multiplo de 3 y de 5: se lee: fizzbuzz") 
        else:
            print(f"este valor {i} no es múltiplo ni de 3 ni de 5")                                
               
       

mostrarConsola()   
"""
"""
Escribe una función que reciba dos palabras (string) y retorne
verdadero o falso (bool) según sean o no anagramas
un anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
no hace falta comprobar que ambas palabras existan
dos palabras exactamente iguales no son anagramas.
"""                       
"""
def Recibe(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    
    if len(palabra1) == len(palabra2):
        if sorted(palabra1) == sorted(palabra2):
            return (f"es una angrama y retorna: ",True)
    else:
        return(f"NO es una angrama y retorna: ",False)        
        
        
print(Recibe("amorUIO", "roma"))        
"""
# LA SUCESIÓN DE FIBONACCI
"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en cero.
la serie de Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores
0,1,1,2,3,5,8,13....
"""

def fibonacci():
    limite = int(input("coloca un valor acá: "))
    previo = 0
    next = 1
    
    for i in range(limite):
        
        print(previo)
        # fib = previo + next
        # previo = next
        # next = fib
        previo, next = next, previo + next      

    
fibonacci()  
  
# n = int(input("Ingresa un número: "))

# a, b = 0, 1
# while a < n:
#     print(a)
#     a, b = b, a + b  

# ¿ES UN NÚMERO PRIMO?
# Escribe un  programa que se encargue de controlar si un número es o no primo
# Hecho esto.imrpime los números primos entre 1 y 100.

# x = int(input("ingrese un número: "))
# i = 2
# for x in range(1,100):
#     while i <= x**(.5) and x % i != 0:
#         i+= 1
#     if i > x**(.5):
#         print(f"{x} es un número primo")
#     else:
#         print(x, "No es un número primo, es divisible por", i)
 

# def is_prime():
#     # for number in range(int(input("Coloca un valor para saber los números primos: "))):
#     for number in range(1,101):
#         if number >=2:
#             is_divisible = False
            
#             for index in range(2, number):
#                 if number % index == 0:
#                     is_divisible = True
#                     break
                
#             if not is_divisible:
#                 print(f"es número primo: {number}")   
                        
  
    
# is_prime()    
# INVERTIENDO CADENAS
# Crear un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática
# si le pasamos "hola mundo", nos retoraría "odnum aloh"                 

# texto = input("Coloca una palabra o frase: ")                      

# print(texto[::-1])

# def reverse(text):
#     text_len = len(text)
#     reversed_text = ""
#     for index in range(0, text_len):
#         reversed_text += text[text_len - index -1]
#     return reversed_text

# print(reverse("Hola Mundo"))

# Invertir el orden de las palabras

# texto2 = input("escribe una palabra: ")
# texto1 = input("escribe otra palabra: ")
# texto = []
# texto.append(texto2)
# texto.append(texto1)
# texto.reverse()
# print(texto)




# Crear un programa que calcule la media de dos números ingresados por teclado
# numero1 = int(input("coloca primer número: "))
# numero2 = int(input("coloca segundo número: "))

# media = (numero1 + numero2) / 2
# print(f"la media es: {media}")
     


    
    
    
        
      


