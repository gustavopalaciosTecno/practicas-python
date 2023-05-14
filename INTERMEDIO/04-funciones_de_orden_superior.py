### Higher Order Functions ###
### Funciones de orden superior ###

# una función puede llamar dentro a otra función
# pueden ejecutar otras funciones
# todas las funciones de orden superio necesitan de un iterable y de una función
from functools import reduce

def sum_one(value):
    return value + 1

def sum_two_values_and_add_one(first_value, secound_value):
    return sum_one(first_value + secound_value)


print(sum_two_values_and_add_one(5,2))

# agregar una función 
def sumar_dos(valor):
    return valor + 2

def sumar_varios_valores(primer_valor, segundo_valor, funcionNueva):
    return funcionNueva(primer_valor + segundo_valor )

print(sumar_varios_valores(10,10,sumar_dos))

##### Closures ##### concepto de función que define una función y retorna una función
def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_closure = sum_ten()    
print(add_closure(5))

print("\n")

def suma(primer_valor):
    def agregar(valor):
        return valor + 1 + primer_valor
    return agregar

# agregar_closure = suma(18)
# print(agregar_closure(20))

print(suma(18)(20)) # otra forma alternativa de imprimir en pantalla

# Funciones de orden superior que ya existen en el propio lenguaje
# Map

numeros = [2,4,6,8,15]
# Map itera cada uno de los elementos en la lista y ejecuta en cada valor la función que hemos creado

def multiplicar(numero):
    return numero * 2

print(list(map(multiplicar,numeros)))
print(list(map(lambda numero: numero * 2, numeros)))

# Filter recorre todos los valores y ejecuta una función que retorna True o False para saber como filtrar los valores del iterador

def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False
    
print(list(filter(filter_greater_than_ten, numeros)))
print(list(filter(lambda number:number > 10, numeros)))

numeros_cualquiera = [2,5,10,15,25,35,15,21]
# Reduce opera con un valor mas el acumulador
# va a sumar el valor anterior con el siguiente
def valores_suma(primer_valor, segundo_valor):
    print(primer_valor)
    print(segundo_valor)
    return primer_valor + segundo_valor

print(reduce(valores_suma,numeros_cualquiera))






