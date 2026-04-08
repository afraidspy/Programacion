'''
Programa interactivo para hacer la conversión de peso a libra y de libra a peso
author: Jessica
date: 2026
version 1.1
'''
#los kgs que vale una libra
VALOR_LIBRAS = 0.453592
print("Tipo de VALOR_LIBRAS ", type(VALOR_LIBRAS))

#las libras que vale un kilogramo
VALOR_KILOS = 2.20462

print("Escribe tu nombre: ")
nombre = input()
#print(type(nombre))
print("Bienvenido a mi programa " + nombre)
print("Escribe tu peso en kilogramos: ")
peso_kilitos = input()
print("Tipo de peso kilitos es: ", type(peso_kilitos))
conversion_kilitos = float(peso_kilitos)
print("El tipo de dato de conversion es: ", type(conversion_kilitos))

libras = conversion_kilitos * VALOR_KILOS

print("En libras pesas ", libras)
