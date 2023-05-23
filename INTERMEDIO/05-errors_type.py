### Errors type ####

# SintaxError

# print "hola comunidad"
print ("hola comunidad")

# nameError
lenguaje = "Español" # si comento esta variable, me da un errorName
print(lenguaje)    

#indexError
mi_lista = ["Python", "Java", "Dart", "Javascript"]
print(mi_lista[:])
print(mi_lista[1:4])
print(mi_lista[1:3])
print(mi_lista[1:2])
print(mi_lista[1:1])
print(mi_lista[0:4])
print(mi_lista[1:-1])
print(mi_lista[1:-2])
print(mi_lista[1:-3])
#print(mi_lista[7]) # esta opcion de dará indexError // se puede descomentar para mostrar el error

# ModuleNotfoundError
#import maths // descomentar para error. nos devolverá moduleNotFoundErros
import math

# AttributeError
#print(math.PI) # me dará error de atributo
print(math.pi)

# keyError
mi_diccionario = {'nombre': 'Pedro', 'apellido': 'Palacios'}
print(mi_diccionario['nombre'])
#print(mi_diccionario['eda']) # me dará el error keyError // descomentar para error
print(mi_diccionario["apellido"])

# typeError
#print(mi_lista["nombre"]) # me dará un error de typeError
print(mi_lista[0])
 

