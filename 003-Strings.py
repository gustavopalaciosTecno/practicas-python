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