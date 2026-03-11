
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1*num2

def division(num1, num2):
    if num2 == 0:
        print("No puedes dividir entre cero")
        return None
    return num1/num2


print("Menu")
print("[1] Suma")
print("[2] Resta")
print("[3] Multiplicacion")
print("[4] Division")


num1 =  float(input("Escribe el número 1"))
num2 =  float(input("Escribe el número 2"))
opcion = int(input("Elige el número de la operacion que vas a realizar"))

if opcion == 1:
    resultado = suma(num1, num2)
    print("La suma es ", resultado)
elif opcion== 2:
    resultado = resta(num1, num2)
    print("La resta es ", resultado)
elif opcion == 3:
    resultado = multiplicacion(num1, num2)
    print("La multiplicacion es ", resultado)
elif opcion == 4:
    resultado = division(num1, num2)
    print("La division es ", resultado)
else:
    print("Opcion No válida")


