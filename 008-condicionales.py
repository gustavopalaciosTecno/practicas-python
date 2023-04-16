"""
Condicionales. Es la manera de establecer flujo de información de 
nuestro código, es decir decidir si algo de nuestro cópdigo se va a 
ejecutar o no.

"""

numero1 = int(input("Ingrese un primer valor numérico: "))
numero2 = int(input("Ingrese un segundo valor numérico: "))

if numero1 > numero2:
    print(f"el número: {numero1} es mayor que el {numero2}")
elif numero1 < numero2:
    print(f"el número: {numero2} es mayor que el {numero1}")
else:
    print("los dos son valores iguales !!!")        

my_condition = True

if my_condition:
    print("se ejecuta la condición")
    
print("El programa continua...")    


print("##### programa de acceso a la bailanta ######")

edad = int(input("coloca tu edad: "))
dinero = int(input("coloca tu nivel adquisitivo: "))
if edad >= 18 and dinero >= 5000:
    print("Podes ingresar")
else:
    print("No podes ingresar a la bailanta")    

  
print("##########")

my_string = ""

if not my_string: # realizamos la negación del string
    print("mi cadena no está vacía") 



