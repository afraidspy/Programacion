import math
from punto import Punto

class Triangulo:
    """
    Clase que representa un triángulo formado por tres puntos.

    Permite calcular las longitudes de sus lados, el perímetro,
    el semiperímetro, el área, validar si forma un triángulo
    y determinar su tipo según sus lados.
    
    """
    
    def __init__(self, punto1: object = Punto(2,5), punto2: object = Punto(6,1), punto3: object = Punto(4,2)):
        """
        Inicializa un objeto de tipo Triangulo con tres puntos.

        Parámetros:
            punto1 (object): Primer vértice del triángulo.
            punto2 (object): Segundo vértice del triángulo.
            punto3 (object): Tercer vértice del triángulo.
        """
        self.__punto1 = punto1
        self.__punto2 = punto2
        self.__punto3 = punto3
        
    def calcular_longitud_lado1(self) -> float:
        """
        Calcula la longitud del lado formado por punto1 y punto2.

        Retorna:
            float: Distancia entre punto1 y punto2.
        """
        distancia = self.__punto1.distancia(self.__punto2)
        return distancia
    
    def calcular_longitud_lado2(self) -> float:
        """
        Calcula la longitud del lado formado por punto2 y punto3.

        Retorna:
            float: Distancia entre punto2 y punto3.
        """
        return self.__punto2.distancia(self.__punto3)
    
    def calcular_longitud_lado3(self) -> float:
        """
        Calcula la longitud del lado formado por punto1 y punto3.

        Retorna:
            float: Distancia entre punto1 y punto3.
        """
        return self.__punto1.distancia(self.__punto3)
    
    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del triángulo.

        Retorna:
            float: Suma de las longitudes de los tres lados.
        """
        return self.calcular_longitud_lado1() + self.calcular_longitud_lado2() + self.calcular_longitud_lado3()
    
    def calcular_semiperimetro(self) -> float:
        """
        Calcula el semiperímetro del triángulo.
        s=(a+b+c​)/2
        Retorna:
            float: Mitad del perímetro del triángulo.
        """
        return self.calcular_perimetro() / 2
    
    def calcular_area(self) -> float:
        """
        Calcula el área del triángulo usando la fórmula de Herón.
        s=(a+b+c)/2
        A=raiz_cuadrada[s(s−a)(s−b)(s−c)]
​
	​


        Retorna:
            float: Área del triángulo.
        """
        lado1 = self.calcular_longitud_lado1()
        lado2 = self.calcular_longitud_lado2()
        lado3 = self.calcular_longitud_lado3()
        
        s = self.calcular_semiperimetro()
        return math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    
    def es_triangulo_valido(self) -> bool:
        """
        Verifica si los tres lados cumplen la desigualdad triangular.
        a desigualdad triangular verifica si realmente es posible construir un triángulo con tres lados dados. Para que sí se pueda, la suma de dos lados siempre debe ser mayor que el lado que falta
        
        a+b>c
        a+c>b
        b+c>a

        Retorna:
            bool: True si los puntos forman un triángulo válido,
            False en caso contrario.
        """
        lado1 = self.calcular_longitud_lado1()
        lado2 = self.calcular_longitud_lado2()
        lado3 = self.calcular_longitud_lado3()
        
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
    
    def determinar_tipo_lados(self) -> str:
        """
        Determina el tipo de triángulo según la longitud de sus lados.

        Retorna:
            str: 'Equilátero', 'Isósceles', 'Escaleno' o
            'No identificado'.
            
        """
        lado1 = self.calcular_longitud_lado1()
        lado2 = self.calcular_longitud_lado2()
        lado3 = self.calcular_longitud_lado3()
        if lado1== lado2 ==lado3:
            return "Equilátero"
        ## Isoceles
        if lado1 == lado2 or lado1== lado3 or lado2 == lado3:
            return "Isóceles"
        #Escaleno
        if lado1!= lado2 and lado2!=lado3 and lado1!=lado3:
            return "Escaleno"
        
        return "No identificado"

    
    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del triángulo.

        Retorna:
            str: Cadena con los tres puntos del triángulo.
        """
        return f"Triángulo({self.__punto1}, {self.__punto2}, {self.__punto3})"
    
    def __eq__(self, otro: object) -> bool:
        """
        Compara si dos triángulos son iguales.

        Parámetros:
            otro (object): Objeto con el que se va a comparar.

        Retorna:
            bool: True si los triángulos tienen los mismos puntos
            en el mismo orden, False en caso contrario.
        """
        if not isinstance(otro, Triangulo):
            return False
        
        return (
            self.__punto1 == otro.__punto1 and
            self.__punto2 == otro.__punto2 and
            self.__punto3 == otro.__punto3
        )


punto1 = Punto(1, 2)
punto2 = Punto(6, 3)
punto3 = Punto()  # Se crea por defecto el punto (1,1)

triangulo1 = Triangulo(punto1, punto2, punto3)
triangulo2 = Triangulo()

while True:
    print("\nMENÚ TRIÁNGULO ")
    print("[0] Salir")
    print("[1] Calcular longitud del lado 1")
    print("[2] Calcular longitud del lado 2")
    print("[3] Calcular longitud del lado 3")
    print("[4] Calcular perímetro")
    print("[5] Calcular semiperímetro")
    print("[6] Calcular área")
    print("[7] Verificar si es triángulo válido")
    print("[8] Determinar tipo según sus lados")
    print("[9] Mostrar triángulo")
    print("[10] Comparar con otro triángulo")
    
    opcion = int(input("Elige una opción: "))
    
    match opcion:
        case 0:
            print("Se terminó el programa.")
            break
        
        case 1:
            print("Longitud del lado 1:", triangulo1.calcular_longitud_lado1())
        
        case 2:
            print("Longitud del lado 2:", triangulo1.calcular_longitud_lado2())
        
        case 3:
            print("Longitud del lado 3:", triangulo1.calcular_longitud_lado3())
        
        case 4:
            print("Perímetro:", triangulo1.calcular_perimetro())
        
        case 5:
            print("Semiperímetro:", triangulo1.calcular_semiperimetro())
        
        case 6:
            print("Área:", triangulo1.calcular_area())
        
        case 7:
            print("¿Es triángulo válido?:", triangulo1.es_triangulo_valido())
        
        case 8:
            print("Tipo según sus lados:", triangulo1.determinar_tipo_lados())
        
        case 9:
            print(triangulo1)
        
        case 10:
            print("¿triangulo1 es igual a triangulo2?:", triangulo1 == triangulo2)
        
        case _:
            print("Opción no válida.")