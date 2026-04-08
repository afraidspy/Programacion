"""
    Diferencia entre randint y randrange de la biblioteca random
"""
import random
"""
Una biblioteca es un conjunto de módulos, funciones, clases y
herramientas ya creadas que puedes reutilizar
para no programar todo desde cero.

Por ejemplo:
random:
https://docs.python.org/es/3.14/library/random.html
es una biblioteca para trabajar con valores aleatorios
math:
https://docs.python.org/es/3.14/library/math.html
sirve para operaciones matemáticas
"""
#Funciones de la biblioteca Random
"""
    randint(a, b) incluye b
"""
numero_aleatorio = random.randint(1,10)
print(numero_aleatorio)

"""
    randrange(a, b) no incluye b
"""
numero_aleatorio = random.randrange(1, 5)
print(numero_aleatorio)

"""
    randrange(a,b,step)  acepta step
"""

numero_aleatorio = random.randrange(0, 10, 2)
print(numero_aleatorio)

print(random.random())
print(random.uniform(1, 5))
#--------------------------------------------------------------------#
#Funciones de la biblioteca math
import math

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.floor(4.9))
print(math.ceil(4.1))
print(math.fabs(-7))
print(math.factorial(5))
print(math.log(10))
print(math.log10(100))
print(math.pi)
print(math.e)
