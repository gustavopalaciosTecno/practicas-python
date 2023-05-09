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
Escribe una función que reciba dos palabras (string) y retorne
verdadero o falso (bool) según sean o no anagramas
un anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
no hace falta comprobar que ambas palabras existan
dos palabras exactamente iguales no son anagramas.
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

# LA SUCESIÓN DE FIBONACCI
"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en cero.
la serie de Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores
0,1,1,2,3,5,8,13....
"""
def fibonacci():
    limite = 50
    previo = 0
    next = 1
    
    for i in range(limite):
        
        print(previo)
        # fib = previo + next
        # previo = next
        # next = fib
        previo, next = next, previo + next      

    
fibonacci()    




