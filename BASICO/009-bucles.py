"""
bucles o loops(ciclos). Nos srive para iterar oseas para repetir algo
o pasar por el mismo código varias veces.
"""

# diferentes bucles - while y for
# el bucle while se repite en función de una condición

numero = 10
contador = 0

while contador < numero:
    print(f"soy el contador: {contador}")
    contador+=1

    my_condition = 0

    while my_condition < 10:
        print(my_condition)
        my_condition+=2
    
    else: # esta parte es opcional
        print("mi condición es mayor o igual que 10")   
        
        
print("Fin del programa")         


while my_condition < 20:
    my_condition+=2
    if my_condition == 15:
        print("se detiene la ejecución")
        break # se usa break para detener la ejecución del bucle
        
    print(my_condition)
   
    print("la ejecución continúa")
        
# for - nos sirve para iterar un listado de elementos
 # el bucle for se repite tantas veces como elementos tangamos iterables
 
my_list = [35,24,62,52,30,30,17]

for element in my_list:
    print(element)
    
# imprimir por pantalla una tupla, un set y un diccionario

print("######### imprimiendo tupla############")
my_tupla = ("Calle Dorrego", "Avenida las camelias", "Rivadavia", "Bandera oeste")    
for element in my_tupla:
    print(element)
    
print("######### imprimiendo set ############")
my_set = {"zapallo", "sandía", "berenjena", "zapallitos coreanos"}
for element in my_set:
    print(element)    
    
print("######### imprimiendo diccionario ############")
my_dict = {"Pais":"Argentina", "Year":1981, "Provincia":"Chaco", "ciudad":"Charata"}
for element in my_dict.keys(),my_dict.values():
    print(element)    
    
    
for element in my_dict:
    print(element)
    if element == "Year":
        break
else:
    print("el bucle for ha finalizado")    
    
for element in my_dict:
    print(element)
    if element == "Year":
        continue
    print("se ejecuta")
else:
    print("el bucle for ha finalizado")       
          