# variables
my_cadena_variable = 'mi cadena de variable'
print(my_cadena_variable)

my_int_variable = 85
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# imprimir diferentes variables separadas por comas- concatenación de variables en un print
print(my_cadena_variable, my_int_variable, my_bool_variable)

# Convertir entero a string
my_into_to_str_variable = str(my_int_variable)
print(my_into_to_str_variable)
print(type(my_into_to_str_variable))
print("este es el valor de: ", my_bool_variable)


# Algunas funciones del sistema
print(len(my_cadena_variable)) # cuenta los caracteres

# Variables en una sola línea
name, surname, alias, age = "Gustavo", "Palacios Meyer", "PalaTecno", 41
print("me llamo: ", name, surname, ". mi edad es de: ", age, ". y mi alias es: ",alias)
# otra forma de imprimir por pantalla
print(f"mi nombres es: {name} {surname}, mi edad es de unos: {age} años, y mi alias es:  {alias}")



