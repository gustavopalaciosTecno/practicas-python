# Operadores Aritméticos más comunes en Python


print('esto es una suma: ', 15 + 4)
print('esto es una resta: ',15 - 4)
print('esto es una multiplicacion: ', 15 * 4)
print('esto es una división',15 / 4)
print('esto es un módulo: ',10 % 3)
print('esto es una división entera: ',10 // 3)
print('esto es un exponente: ',5 ** 3)
# combinamos los tipos de datos en un solo print
print("el resultado es: ",10 ** 2 + 3 + 2 // 5 * 3) # todos los signos se pueden combiar

# Concatenamos strings:
print("hola" + " " + "Python")
# no podemos concatenar un entero con un string
# print("hola " + 4) 
# la solución sería la siguiente:
#convertimos el número 4 en un string
print("hola " + str(4))
print('hola ' * 4) # se multiplica la palabra hola. 

"""
no se puede mutiplicar un string por un float, pero si
lo concertimos en entero, si que funciona.
"""
my_float = 5.2 * 2
print('hola ' * int(my_float))

# Operadores Comparativos

print( 3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(4 == 4)
print(3 != 4)

print("###############SEPARADOR1#################")

# Comparamos con cadenas-comprueba la ordenación alfabética por ASCII
# cuenta x palabras
print("hola" > "Python")
print("hola" >= "Python")
print("hola" < "Python")
print("aaa" <= "bbb")
print("aaaa" == "Python")
print("hola" != "Python")

print("################SEPARADOR2#################")
# Contar caracteres con len
print(len("hola") > len("Python"))
print(len("hola") < len("Python"))

print("################SEPARADOR3#################")

# Operadores Lógicos
print(3 > 4 and "hola" > "Python") # 3 no es mayor que 4 pero hola es mayor que Python en ASCII falso y verdadero es => falso
print(3 > 4 or "hola" > "Python") # 3 no es mayor que 4 o hola es mayor que Python en ASII falso o verdadero es => verdadero
#print(not 4)
print(3 < 4 and "Python" < "hola")
print(3 < 4 or "hola" < "Python")

print(3 < 4 or "hola" > "Python" and 4 == 4)
"""
tres es menor que cuatro, hola en caracter ASCII es mayor que Python y cuatro es igual a cuatro.
"""
print(not(3 > 4))