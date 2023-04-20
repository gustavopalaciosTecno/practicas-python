"""
Excepciones: manejo de errores.
si nuestro programa da un error, las excepciones se encargan de controlar y 
mostrar en pantalla un mensaje.
"""
def excepcion():
    try:
        print("si el valor es menor a 50; se ejecutan los valores del contador puesto hasta el 49")
        contador = int(input("coloca un número: "))
        numero = 50
        while contador < numero:
            contador+=1
            print(contador)
    
    except Exception as e:
        print("Se produjo un error",e)    
    
    else:
        print(f"se imprimió el valor/es correctamente") # si falla lo de arriba, esta parte se ejecuta
    finally: # esta opción se ejecuta siempre
        print("fin de la ejecución")  
        
excepcion()              

try:
  valor = int(input("coloca un valor:"))
 
  while valor < 100:
      valor = valor + 1
      valor = int(input("coloca un valor:"))
      if valor == 100:
          print(f"el valor es igual a {100} y la ejecución terminó")
      
except Exception as e:
    print("se produjo un error", e) 


# excepciones por tipos
valor1 = 15
valor = "15"

try:
    print(valor1 + valor)

except ValueError as error: # se captura el tipo de error
    print("se produjo un error", error)
except TypeError as e: # se captura el tipo de error
    print("se produjo un error", e)               