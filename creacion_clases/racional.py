"""
Nùmero racionales : a / b donde b!= 0
Atributos de clase: a = numerador y b = denominador
Mètodos: suma, restar, multiplicar, dividir, eq, str
"""

class Racional:
    
    def __init__(self, numerador = 1, denominador = 1) -> None:
        self.__numerador = numerador
        if denominador != 0:
            self.__denominador = denominador
        else:
            self.__denominador = 1
            
                
    def get_numerador(self):
        return self.__numerador
    
    def get_denominador(self):
        return self.__denominador

    
    def suma(self, otro:object)-> object:
        """
            racional1 =  a /b --> self
            racional2 = c / d  ---> otro
            suma = (ad + bc)/ bd
            
            1er racional: racional que manda a llamar al método
            2dro racional: objeto que me pasan como parámetro
        """
        #numerador_r = self.get_numerador()* otro.get_denominador() + self.get_denominador()*otro.get_numerador()
        #denominador_r = self.get_denominador() * otro.get_denominador()
        numerador_r   = self.__numerador* otro.__denominador + self.__denominador*otro.__numerador
        denominador_r = self.__denominador * otro.__denominador
    
        nuevo_suma = Racional(numerador_r, denominador_r)
        
        return nuevo_suma
    
    def resta(self, otro:object)-> object:
        """
            racional1 =  a / b --> self
            racional2 = c / d  ---> otro
            resta = (ad - bc)/ bd
        """
        numerador_r   = self.__numerador* otro.__denominador - self.__denominador*otro.__numerador
        denominador_r = self.__denominador * otro.__denominador
        
        return Racional(numerador_r, denominador_r)
    
    def __str__(self)-> str:
        cadena_racional = f"{self.__numerador} / {self.__denominador}"
        return cadena_racional
    
    
    def __eq__(self, otro) -> bool:
        
        #1. Validar si otro es instancia de la clase Racional
        if isinstance(otro, Racional):
        #2. Comparar los atributos : numerador y denominador de ambos objetos
        # 1er racional --> self
        # 2do racional --> otro
            return self.get_numerador() == otro.get_numerador() and self.get_denominador() == otro.get_denominador()
        else:
            return False
    
        


class Complejo:
    pass

racional1 = Racional()
racional2 = Racional(8,0)

# racional1 = 1/1 y racional2 = 8/1
racional_suma = racional1.suma(racional2)
print("Numerador de suma:  ", racional_suma.get_numerador())
print("Denonminador de suma: ", racional_suma.get_denominador())
#racional1 = 1/1 y racional2 = 8/1  (1/1 - 8/ 1)
racional_resta = racional1.resta(racional2)
print("Numerador de resta:  ", racional_resta.get_numerador())
print("Denonminador de resta: ", racional_resta.get_denominador())

racional3 = Complejo()

print(racional1)
print("¿Son iguales?", racional1.__eq__(racional2))
print("¿Son iguales?", racional1 == racional2)
print("¿Son iguales?", racional1 == racional3)