
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
        pass
        
    
    def calcular_longitud_lado1(self) -> float:
        """
        Calcula la longitud del lado formado por punto1 y punto2.

        Retorna:
            float: Distancia entre punto1 y punto2.
        """
        pass
    
    def calcular_longitud_lado2(self) -> float:
        """
        Calcula la longitud del lado formado por punto2 y punto3.

        Retorna:
            float: Distancia entre punto2 y punto3.
        """
        pass
    
    def calcular_longitud_lado3(self) -> float:
        """
        Calcula la longitud del lado formado por punto1 y punto3.

        Retorna:
            float: Distancia entre punto1 y punto3.
        """
        pass
    
    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del triángulo.

        Retorna:
            float: Suma de las longitudes de los tres lados.
        """
        pass
    
    def calcular_semiperimetro(self) -> float:
        """
        Calcula el semiperímetro del triángulo.

        Retorna:
            float: Mitad del perímetro del triángulo.
        """
        pass
    
    def calcular_area(self) -> float:
        """
        Calcula el área del triángulo usando la fórmula de Herón.

        Retorna:
            float: Área del triángulo.
        """
        pass
    
    def es_triangulo_valido(self) -> bool:
        """
        Verifica si los tres lados cumplen la desigualdad triangular.

        Retorna:
            bool: True si los puntos forman un triángulo válido,
            False en caso contrario.
        """
        pass
    
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