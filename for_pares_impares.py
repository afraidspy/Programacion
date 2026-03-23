
def suma_pares_impares(n):
    """
        Calcula la suma y producto de los primeros n
        pares e impares
        
    """
    suma_pares = 0
    suma_impares = 0
    producto_pares = 1
    producto_impares = 1
    
    for i in range (1, n + 1, 1):
        if i % 2 == 0: #Valida si es par
            print("Sig par: ", i)
            suma_pares += i
            producto_pares  *= i
        else:#Si no, es impar
            print("Sig impar: ", i)
            suma_impares += i
            producto_impares += i
    
    print ("Suma de pares: " , suma_pares)
    print ("Suma de impares: " , suma_impares)
    
    print ("Producto de pares: " , producto_pares)
    print ("Producto de impares: " , producto_impares)
            
            
def factorial(n):
    # n * n(n-1)!
    factorial_res = 1
    for i in range(1, n + 1):
        factorial_res *= i
    
    return factorial_res

def numero_reves(n):
    numero_invertido = 0
    
    while n > 0:
        digito_residuo = n % 10
        n = n // 10
        print("Numero invertido antes: ",numero_invertido )
        numero_invertido = numero_invertido*10 + digito_residuo 
        print("Numero_invertido: ", numero_invertido)
        print("NUMERO: ", n)
    
    return numero_invertido
    
        
    
opcion =  int(input("Escribe un numero: "))
#suma_pares_impares(opcion)
#print(factorial(3))

print(numero_reves(opcion))
