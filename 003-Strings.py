#### STRINGS ####
mi_string = "Mi nombre es Jorge"
mi_otro_string = 'Palacios Meyer'

print("el tamaño del contenido de la variable es : ",len(mi_string))
print("el tamaño del contenido de la otra variable es : ", len(mi_otro_string))

#concatenar y agregar espacios
print(mi_string + " " + mi_otro_string)

# strings con salto de líneas
mi_strig_con_salto_linea='esto es un corto comentario \nespero sepan enternder \ny no den tantas vueltas'
print(mi_strig_con_salto_linea)

# strings con tabulación
mi_strig_con_tab='\testo es un corto comentario \tespero sepan enternder \ty no den tantas vueltas'
print(mi_strig_con_tab)

# strings escapando salto y tabulación
mi_string_escape = '\\testo es un corto comentario \\nespero sepan enternder \\ny no den tantas vueltas'
print(mi_string_escape)

# formateo- diferentes maneras de darle formato a lo que se desea imprimir por pantalla
name, surname, age = "Néstor", "Palacios Meyer", 41
print("mi nombre y apellidos son: {0} {1} y mi edad es {2}".format(name, surname, age))
print("mi nombre y apellidos son: {} {} y mi edad es {}".format(name, surname, age))
print("mi nombre y apellidos son: %s %s y mi edad es %d" %(name, surname, age))
print("mi nombre y apellidos son: " + name + " " + surname + " y mi edad es: " + str(age))
print(f"mi nombre y apellidos son: {name} {surname} y mi edad es: {age}") # interpolacón referencial

# Desempaquetado de caracteres
lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División
lenguaje_slice = lenguaje
print(lenguaje_slice[0:3])
print(lenguaje_slice[1:3])
print(lenguaje_slice[2:3])
print(lenguaje_slice[3:3])
print(lenguaje_slice[:6])
print(lenguaje_slice[4:6])
print(lenguaje_slice[:])
print("####### de derecha a izquierda #######")
print(lenguaje_slice[-2])
print(lenguaje_slice[:-4])

# Reverse - imprimir al revés los valores
reverse_lenguaje = lenguaje
print(reverse_lenguaje[::-1]) # de derecha a izquierda empieza de menos uno.

print("imprimir nombre")

# Funciones

print(lenguaje.capitalize()) # coloca la primera letra en mayúscula
print(lenguaje.upper()) # transforma minúscula en mayúscula
print(lenguaje.count("y")) # cuenta las letras que se repiten
print(lenguaje.isnumeric()) # nos avisa si es un número
print("1".isnumeric())
print(lenguaje.lower()) # transforma en minúscula
print(lenguaje.upper().isupper()) # pregunta si el string esta en mayúscula
print(lenguaje.startswith("Py")) # nos dice si empieza con las palabras que le especifico
print(lenguaje.startswith("py"))
          


        



 









