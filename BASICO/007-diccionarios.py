"""
Dicccionarios. los datos se organizan en una relación clave - valor.

"""
my_other_dic = {}
mi_diccionario = dict()
my_dict = {"paris":"francia", "Bs.As":"Argentina", "Bogotá":"Colombia"}
print(type(my_dict))
print(type(mi_diccionario))

my_other_dic = {"Nombre":"Gustavo", "Apellidos":"Palacios", "edad":41, "estado_civil":"casado", 1:"Python", 2:"Java"}
print(my_other_dic)

is_other_dictionary = {
    "lenguajes des estilo":"CSS",
    "lenguaje de etiquetas":"HTML",
    "Lenguaje de programación front-end":"Javascript",
    "Lenguajes de programación back-end":{"Python", "PHP", "JAVA"},
    "Lenguaje de consultas":"SQL"
}
print(is_other_dictionary["Lenguajes de programación back-end"])
print(len(is_other_dictionary))
print("mi nombre es: ",my_other_dic["Nombre"])

# Actualizar una clave
is_other_dictionary["Lenguaje de consultas"]="NO-SQL"
my_other_dic["Apellidos"]="Palacios Meyer"
print(is_other_dictionary)
print(my_other_dic)

# Agregar una clave valor al diccionario my_other_dic
my_other_dic["Domicilio"]="Barrio Víctor Arrudi nuevo"
print(my_other_dic)

# Eliminar un solo elemento de mi diccionario
del my_dict["paris"]
print(my_dict)

# Se buscan los valores por clave
print("Nombre" in my_other_dic)
print("Surname" in my_other_dic)

print("#################")
print(my_other_dic.items()) # devuelve un listado con cada uno de los items
print(my_other_dic.keys()) # devuelo solo las claves
print(my_other_dic.values()) # devuelve solo los valores

# crea un diccionario nuevo pero sin valores
my_new_dic = {"name":"Peter", "surname":"Johnson"}
print(my_dict.fromkeys(("paris", "Bs.As")))
#my_dict.clear()

# crear una lista y pasarlo al fromkeys
mi_lista = [23, 45,"perro", "gato"]
print(mi_lista)
print(my_dict.fromkeys((mi_lista)))

# agregar a los elementos del diccionario, otras caracterísitcas
dict2 = {"perro":"gran danés", "gato":"siamaés"}
dic1 = dict.fromkeys(dict2,("posee 4 patas", "es mamífero")) # estos valores se van a duplicar en todas las claves
print(dic1.fromkeys(dict2.values(), dict2.keys()))
print(dic1)

print(list(dic1)) # imprime solo las claves

# convertir dict1 a una tupla, un diccionario y un set
print(tuple(dic1)) # es una tupla
print(dict(dic1)) # es un diccionario
print(set(dic1)) # es un set
print(dic1.values())