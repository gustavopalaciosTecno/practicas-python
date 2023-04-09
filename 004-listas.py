# Listas

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
