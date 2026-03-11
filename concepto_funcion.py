"""numero =  abs(-5)

print(numero)"""

"""
Creaciòn de nuestras propias funciones
"""

def imprime_mensaje():
    print("Este es un mensaje desde el curso de Programaciòn")
    
p = imprime_mensaje()

print(p)


def imprime_mensaje(nombre):
    print("Bienvenido al curso de progra, " +  nombre)
    
#Mandamos a llamar a la función que recibe un nombre
imprime_mensaje("Jessica")

#No recibe nada pero si regresa algo
def calculos():
    a = 5
    b = 10
    suma = a + b
    return suma

resultado = calculos()
print("El resultado de calculos es: ", resultado)

#Recibe algo y regresa algo

def calculo_edad(anio_nacimiento):
    return (2026 - anio_nacimiento)

edad =  calculo_edad(2000)

print("La edad es ", edad)



    