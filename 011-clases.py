"""
Clases:

"""
"""
class Calcular: # la primera letra se escrine con mayúscula
    def calculo_Auxiliar(self):
        valor = float(input("Coloca un valor: "))
        descuento1 = float(input("Coloca primer valor para descontar: "))
        descuento2 = float(input("Coloca segundo valor para descontar: "))
        descuento3 = float(input("Coloca tercer valor para descontar: "))
    
        suma_descuentos = descuento1 + descuento2 + descuento3
        resultado = (valor - suma_descuentos)
        print("el resutlado final de la operación es: ",resultado)


objeto1 = Calcular()
objeto1.calculo_Auxiliar()
"""
class Person:
    def __init__(self, name, surname):
       self.full_name = f"{name} {surname}"
       
    def caminar(self):
        print(f"{self.full_name} está caminando")   
       
        
my_person = Person("Néstor", "Palacios Meyer")
print(my_person.full_name)  
my_person.caminar()

class Person1:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
my_person1 = Person1("carlita")
print(my_person1.nombre)
      
        
        
         
        

    