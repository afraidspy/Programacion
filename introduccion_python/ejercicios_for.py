def suma_y_producto_primeros_pares_impares(n):
    suma_pares = 0
    suma_impares = 0
    producto_pares = 1
    producto_impares = 1

    for i in range(1, n + 1):
        numero_par = 2 * i
        numero_impar = 2 * i - 1

        suma_pares += numero_par
        suma_impares += numero_impar

        producto_pares *= numero_par
        producto_impares *= numero_impar

    print("Suma de los primeros", n, "números pares:", suma_pares)
    print("Suma de los primeros", n, "números impares:", suma_impares)
    print("Producto de los primeros", n, "números pares:", producto_pares)
    print("Producto de los primeros", n, "números impares:", producto_impares)


def factorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado


def invertir_numero(numero):
    numero_invertido = 0

    while numero > 0:
        digito = numero % 10
        numero_invertido = numero_invertido * 10 + digito
        numero //= 10

    return numero_invertido


def es_numero_perfecto(numero):
    suma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        return True
    else:
        return False


def mostrar_numeros_perfectos():
    print("Números perfectos entre 1 y 1000:")

    for numero in range(1, 1001):
        if es_numero_perfecto(numero):
            print(numero)


def principal():
    print("Menú de ejercicios")
    print("1. Suma y producto de los primeros n números pares e impares")
    print("2. Factorial de un número")
    print("3. Invertir un número")
    print("4. Números perfectos entre 1 y 1000")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        n = int(input("Ingresa un número entero positivo: "))
        suma_y_producto_primeros_pares_impares(n)

    elif opcion == 2:
        n = int(input("Ingresa un número entero no negativo: "))
        print("Factorial:", factorial(n))

    elif opcion == 3:
        numero = int(input("Ingresa un número entero positivo: "))
        print("Número invertido:", invertir_numero(numero))

    elif opcion == 4:
        mostrar_numeros_perfectos()

    else:
        print("Opción no válida")


principal()

