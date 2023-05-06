print("programación imperativa")
valor1 = 12
valor2 = 3

print(valor1 + valor2)

print("programación con funciones")

def suma():
    valor3 = 12
    valor4 = 3
    resultado = valor3 + valor4
    return resultado


print(suma())

print("Programación con clases")

class Calculos():
    def suma(self, valor3, valor4):
        self.valor3 = valor3
        self.valor4 = valor4
        resultado = self.valor3 + self.valor4
        return resultado
    
objeto1 = Calculos()
print(objeto1.suma(12,3))    
    
    