from punto import Punto

class Triangulo:
    
    def __init__(self, punto1:object = Punto(2,5), punto2: object = Punto(6,1), punto3: object = Punto(4,2)):
        self.__punto1 = punto1
        self.__punto2 = punto2
        self.__punto3 = punto3
        
    
    def calcular_longitud_lado1(self)->float:
        distancia = self.__punto1.distancia(self.__punto2)
        return distancia
    
    def calcular_longitud_lado2(self) -> float:
        return self.__punto2.distancia(self.__punto3)
    
    def calcular_longitud_lado3(self)->float:
        return self.__punto1.distancia(self.__punto3)
        
    

punto1 = Punto(1,2)
punto2 = Punto(6,3)
punto3 = Punto() # Se va a crear por defecto el punto (1,1)

triangulo1 =  Triangulo(punto1, punto2, punto3)
triangulo2 =  Triangulo()

print("Longitud del lado1: ", triangulo1.calcular_longitud_lado1())
print("Longitud del lado2: ", triangulo1.calcular_longitud_lado2())
print("Longitud del lado3: ", triangulo1.calcular_longitud_lado3())
