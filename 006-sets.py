### SETS ####
"""
Un set no es una estructura ordenada. no se pueden acceder a los elementos.
no admite valores o elementos repetidos. Ordena los valores por un has interno.

"""

my_set = set()

my_other_set = {}
print(type(my_other_set)) # me dice que incialmente es un diccionario // es una curiosidad
print(type(my_set))

my_other_set = {"carancho", "rata", "paloma", "águila"}
print(type(my_other_set))

# contar los elementos con len
print(len(my_other_set))

# agregar elemento a mi set
my_other_set.add("Coyote")
print(my_other_set)

