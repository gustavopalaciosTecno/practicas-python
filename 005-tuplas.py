##### tuplas ######

# hay dos formas de definir una tupla. como se muestra abajo
mi_tupla = ("peras", "bananas", "frutillas", 1458, 1.78, False)
mi_tupla2 = (1,15,10,150,145,887,15,11,25,15,10,)

print(mi_tupla)
print(type(mi_tupla)) # para saber el tipo de clase que es. en este caso es una tupla
print(mi_tupla[0])
print(mi_tupla[3])
print(mi_tupla[-1])
#print(mi_tupla[-8]) # me dará un error porque el índice 8 no existe

print("#### usando count #######")
# en las tuplas se puede usar la función count
print(mi_tupla2.count(10)) # me imprime cuantas veces se repite el 10

print("######### para saber el índice de un elemento #######")
print("el indice de frutillas es: " + str(mi_tupla.index("frutillas"))) # uso str para convertir a string
print(mi_tupla.index("frutillas")) # sin convertir

"""
las tuplas no se pueden modificar, insertar elementos, sus valores
son inmutables. se pueden guardar datos en ellas, pero ya estos valores
estan cerrados.
"""