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
# Sumar tuplas
print("######## suma de tuplas ########")
print(mi_tupla + mi_tupla2)
mi_nueva_tupla = mi_tupla + mi_tupla2
print(mi_nueva_tupla)
print(mi_nueva_tupla[3:6]) # incluye los indices del 3 al 5

# convertir tupla en lista
print("########## tupla a lista #############")
mi_nueva_tupla = list(mi_nueva_tupla)
print(type(mi_nueva_tupla))

"""
 al convertir la tupla a lista, ahora pueda insertar valores o modifarlos
"""
mi_nueva_tupla.insert(1, "Rodriguez")
print(mi_nueva_tupla)
mi_nueva_tupla[8] = "numero ocho"
print(mi_nueva_tupla)

# convertir de lista a tupla
print("######## convertir de lista a tupla ###########")
mi_nueva_tupla = tuple(mi_nueva_tupla)
print(type(mi_nueva_tupla))
# imprimimos y vemos los valores
print(mi_nueva_tupla)

# borrar una tupla
del mi_nueva_tupla
print(mi_nueva_tupla) # este print dará un error porque antes he borrado la tupla
