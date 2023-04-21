### SETS ####
"""
Un set no es una estructura ordenada. no se pueden acceder a los elementos por su índice
no admite valores o elementos repetidos. Ordena los valores por un has interno.
sus elementos se pueden eliminar.
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

# Comprobar si existe un valor dentro del set
print( "carancho" in my_other_set)
print("caranchoo" in my_other_set)

# eliminar elementos
my_other_set.remove("Coyote")
print(my_other_set)

# vaciar el set
my_other_set.clear()
print(my_other_set)
print(len(my_other_set)) # el resultado me dará (0) ya que elimimé todos los elementos.

# borrar el set
del my_other_set
#print(my_other_set) # nos dará un error porque el set ya ha sido eliminado

# Convertir un set a una lista
my_set = ("zapallo", "rabanito", "lechuga")
my_set = list(my_set)
print(type(my_set))
print(my_set) # al convertir a una lista, los elementos se me ordenan
#ahora si puede acceder a los elementos
print(my_set[0])
print(my_set[1])

# unir dos sets
my_set = set(my_set)
my_other_set = {"Python", "Javascript", "Css"}
my_new_set = my_set.union(my_other_set) # se produjo la unión de dos sets
print(my_new_set)
print(my_new_set.union(my_set).union(my_other_set)) # no se repiten los elementos
print(my_new_set.union(my_set).union(my_other_set).union("HTML", "Bootstrap"))

print(my_new_set.difference(my_set)) # le quito los elemento de myset