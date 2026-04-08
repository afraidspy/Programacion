class Robot:
    """
    Consultar: https://peps.python.org/pep-0257/
    Clase que representa un robot con atributos básicos.

    Esta clase permite ejemplificar conceptos de programación
    orientada a objetos, como abstracción, encapsulamiento
    y documentación.
    """

    def __init__(self) -> None:
        """
        Inicializa un objeto de tipo Robot con valores por defecto.
        """
        print("Entrando al método inicial")

        # Atributo público
        self.nombre = "Wall-e"

        # Atributos encapsulados
        self.__edad = 100
        self.__peso = 200
        self.__num_armas = 3

    def get_edad(self) -> float:
        """
        Devuelve la edad del robot.

        Retorna:
            float: La edad actual del robot.
        """
        return self.__edad

    def get_peso(self) -> float:
        """
        Devuelve el peso del robot.

        Retorna:
            float: El peso actual del robot.
        """
        return self.__peso

    def get_num_armas(self) -> int:
        """
        Devuelve el número de armas del robot.

        Retorna:
            int: La cantidad de armas del robot.
        """
        return self.__num_armas

    def set_edad(self, nueva_edad: float) -> None:
        """
        Modifica la edad del robot.

        Paràmetros:
            nueva_edad (float): Nueva edad del robot.
        """
        self.__edad = nueva_edad

    def set_peso(self, nuevo_peso: float) -> None:
        """
        Modifica el peso del robot.

        Parámetros:
            nuevo_peso (float): Nuevo peso del robot.
        """
        self.__peso = nuevo_peso

    def set_num_armas(self, nuevo_num_armas: int) -> None:
        """
        Modifica el número de armas del robot.

        Parámetros:
            nuevo_num_armas (int): Nueva cantidad de armas.
        """
        self.__num_armas = nuevo_num_armas
        
    def __str__(self) -> str:
        """
        Devuelve una representación en texto del estado del objeto.

        Retorna:
            str: Cadena con los valores actuales del robot.
        """
        return (
            f"Robot(nombre={self.nombre}, edad={self.__edad}, "
            f"peso={self.__peso}, num_armas={self.__num_armas})"
        )
    
    def __eq__(self, otro) -> bool:
        """
        Compara si este robot es igual a otro robot.

        Parámetros:
            otro: Objeto con el que se desea comparar.

        Retorna:
            bool: True si ambos objetos tienen el mismo estado,
            False en caso contrario.
        """
        if not isinstance(otro, Robot):
            return False

        return (
            self.nombre == otro.nombre
            and self.__edad == otro.__edad
            and self.__peso == otro.__peso
            and self.__num_armas == otro.__num_armas
        )



# Crear un objeto de la clase
bunny = Robot()

# Modificar atributos encapsulados mediante métodos
bunny.set_peso(500)
bunny.set_num_armas(10)

# Mostrar información del objeto
print("Peso:", bunny.get_peso())
print("Nombre:", bunny.nombre)
print("Edad:", bunny.get_edad())
print("Número de armas:", bunny.get_num_armas())

print(bunny)
print(bunny.__str__())

robotin =  Robot()

print(bunny.__eq__(bunny))
print(bunny.__eq__(robotin))


print("¿Son iguales?", bunny == robotin)
