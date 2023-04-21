# Listas
"""
 las listas ordena los valores o elementos. los elementos se pueden modificar, borrar
 y agregar nuevos elementos. se pueden acceder a estos elementos.
"""
mi_lista = list()
my_other_list = []

print(mi_lista)
print(len(my_other_list))



my_other_list = [41, 1.77, 'Gustavo', 'Palacios Meyer']
print(my_other_list)
print(type(mi_lista))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-3])
print(my_other_list[-4])
#print(my_other_list[-5]) nos dará error-> list index out of range (lista de índice fuera de rango)
#print(my_other_list[-5]) nos dará un error->list index out of range

frutas = ["manzanas", "peras", "bananas", "manzanas", "peras", "frutillas", "manzanas"]
print(frutas.count("manzanas"))

# desempaquetado de valores
age = 35
height = 1.77
name = "Julio"
surname = "Saldaña"
mi_otra_lista = [35, 1.77, "Julio", "Saldaña"]
age, height, name, surname = mi_otra_lista
print(name, surname, age, height)

# Concatenar dos listas
nenas = ["Florencia", "Isabella", "Noemí", "Raquel"]
varones = ["Julio", "Alberto", "Jahziel", "Mauro"]
print(nenas + varones)

# Crear una lista y agregarle elementos
print("###### Crear una lista y agregarle elementos #####")
apellidos = ["Fernandez", "Salto", "lopez", "Maldonado", "Iglesias"]
apellidos.append("Palacios")
print(apellidos)

# Insertar un elemento a la lista.
print("###### Insertar un elemento a la lista #####")
apellidos.insert(0,"Perez") # al indicar el índice cero me agrega al principo de la lista
print(apellidos)

print("##### cambiamos el valor del índice dos de salto a Estebanez ######")
apellidos[2] = "Estebanez" 
print(apellidos)

# Remover un elemento a la lista.
print("###### Remover un elemento a la lista #####")
apellidos.remove("lopez")
print(apellidos)

# Remover el último elemento de la lista.
print("###### Remover último elemento a la lista #####")
apellidos.pop()
print(apellidos)

del apellidos[2] # elimina el elemento del índice 2 (elimina apellido salto)
print(apellidos)

# antes de borrar apellidos, vamos a copiar 

mi_nueva_lista = apellidos.copy() # copiamos la lista de apellidos

print("###### vacicar una lista ######")
# vaciar una lista

print("############## invertimos los elementos de la lista ####################")
# invertimos los elementos de la lista
apellidos.reverse()
print(apellidos)

apellidos.clear() 
"""
no es lo mismo que remove, ya que clear vacía todos los elementos de 
la lista, en cambio del elimina por índice

"""
print(apellidos)
print(mi_nueva_lista) # la lista apellidos se vació, pero mi_nueva_lista sigue con los elementos

# ordenamos la lista
print("###### ordenamos la lista #########")
mi_nueva_lista.sort()
print(mi_nueva_lista)
print("###### tambien me ordena los números #########")
# tambien me ordena los números
numeros = [15,14,25,10,9,15,16,25,89,55,23,11]
print(numeros)
numeros.sort()
print(numeros)





