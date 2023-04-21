def sum(numberOne,numberTwo,numberThree):
    
    print(numberOne + numberTwo + numberThree)
    
    
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
    
