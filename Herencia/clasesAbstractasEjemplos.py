# HERENCIA

"""

La herencia es un proceso mediante el cual se puede crear una clase inferior(hija) 
que hereda de una clase superior(padre), compartiendo sus métodos y atributos. Además de ello, 
una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

Se puede crear una clase hija con tan solo pasar como parámetro la clase de la que queremos heredar.

"""

# Definimos una clase
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass

print(Perro.__bases__)
print(Animal.__subclasses__())


"""

¿ para que la herencia? Dado que una clase hija hereda los atributos y métodos de la padre, 
nos puede ser muy útil cuando tengamos clases que se parecen entre sí pero tienen ciertas 
particularidades. En este caso en vez de definir un montón de clases para cada animal, podemos 
tomar los elementos comunes y crear una clase Animal de la que hereden el resto.



"""


# Métodos
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, especie, edad):
        self._especie = especie #_ indica que es protected
        self._edad = edad

    @abstractmethod
    def hablar(self):
        # Método vacío
        pass
    @abstractmethod
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
        
      
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")
        
        
        
perro = Perro('mamífero', 10)
perro.describeme()
perro.moverse()

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")


mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.hablar()
mi_vaca.hablar()
mi_vaca.describeme()
mi_abeja.describeme()
mi_abeja.picar()

#animalito =  Animal()
# Otro ejemplo
 
class Persona(object):
    """Clase que representa una Persona"""

    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo

    def hablar(self, mensaje):
        return mensaje

    def getGenero(self):
        genero = ('Masculino','Femenino')
        if self._sexo == "M":
            return genero[0]
        elif self._sexo == "F":
            return genero[1]
        else:
            return "Desconocido"
        

class Supervisor(Persona):

    def __init__(self, cedula, nombre, apellido, sexo, rol,salario):
        """Constructor de clase Supervisor"""

        # Invoca al constructor de clase Persona
        ##Persona.__init__(self, cedula, nombre, apellido, sexo)
        super().__init__(cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.__rol = rol
        self.__salario =salario
        

    def consulta_salario(self):
        return 'su salario es '+ str(self.__salario)
    
#cedula, nombre, apellido, sexo, rol,salario):
f=Supervisor(1234,"fernando","ortega","M","supervisor",10000)


print(f.getGenero())






















