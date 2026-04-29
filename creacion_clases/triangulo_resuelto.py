from punto import Punto
import math
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
        return self.__punto1.distancia(self.__punto2)
    
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
        perimetro = self.calcular_longitud_lado1() + self.calcular_longitud_lado2() + self.calcular_longitud_lado3()
        return perimetro
    
    def calcular_semiperimetro(self) -> float:
        """
        Calcula el semiperímetro del triángulo.

        Retorna:
            float: Mitad del perímetro del triángulo.
        """
        return self.calcular_perimetro() / 2
    
    def calcular_area(self) -> float:
        """
        Calcula el área del triángulo usando la fórmula de Herón.
         s=(a+b+c)/2
          A=raiz_cuadrada[s(s−a)(s−b)(s−c)]

        Retorna:
            float: Área del triángulo.
        """
        a = self.calcular_longitud_lado1()
        b = self.calcular_longitud_lado2()
        c = self.calcular_longitud_lado3()
        s = self.calcular_semiperimetro()
        return math.sqrt(s * (s-a)*(s-b)*(s-c))
    
    def es_triangulo_valido(self) -> bool:
        """
        Verifica si los tres lados cumplen la desigualdad triangular.
        a+b>c
        a+c>b
        b+c>a

        Retorna:
            bool: True si los puntos forman un triángulo válido, p1(0,0)p2(0,0)p3(0,0)
            False en caso contrario.
        """
        a = self.calcular_longitud_lado1()
        b = self.calcular_longitud_lado2()
        c = self.calcular_longitud_lado3()
        return (a+ b > c) and (a+c > b) and (b + c > a)
        
    
    def determinar_tipo_lados(self) -> str:
        """
        Determina el tipo de triángulo según la longitud de sus lados.

        Retorna:
            str: 'Equilátero', 'Isósceles', 'Escaleno' o
            'No identificado'.
        """
      pass
    
    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del triángulo.

        Retorna:
            str: Cadena con los tres puntos del triángulo.
        """
        pass
    
    def __eq__(self, otro: object) -> bool:
        """
        Compara si dos triángulos son iguales.

        Parámetros:
            otro (object): Objeto con el que se va a comparar.

        Retorna:
            bool: True si los triángulos tienen los mismos puntos
            en el mismo orden, False en caso contrario.
        """
        pass

triangulo1 = Triangulo()

punto1 = Punto(2,2)
punto2 = Punto(5,4)
punto3 = Punto(8,1)

triangulo2 =  Triangulo(punto1, punto1, punto1)

while True:
    """
    Menú principal para ejecutar operaciones del triángulo.
    """

    print("MENU")
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
    print("[10] Comparar dos triángulos")

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
            print("¿Es triángulo válido?:", triangulo2.es_triangulo_valido())

        case 8:
            print("Tipo según sus lados:", triangulo2.determinar_tipo_lados())

        case 9:
            print(triangulo1)

        case 10:
            print("¿Los triángulos son iguales?:", triangulo1 == triangulo2)

        case _:
            print("Opción no válida.")