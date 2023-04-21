#import module
from module import sum, excepcion
# hay dos formas de importar los módulos.(con import directamente)
# o con from luego nombre del archivo y luego import y nombre de la función
"""
Módulos. Se utiliza para organizar mis códigos en librerias
tambien son librerías que tiene creado el sistema.
"""

#module.sum(15,18,25)
sum(15,18,35)
#module.excepcion()
excepcion()

import math

math.pi
# otra forma de importar el módulo math es como se visualiza abajo.
from math import pi
# se le puede agregar un alias
#from math import pi as PI_VALUE

print("el valor de pi es: ",math.pi)

print("el valor de 2 elevado a la 8 es: ",math.pow(2,8))

