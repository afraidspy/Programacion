class Poliza:
    """
    Representa una póliza de seguro.

    Una póliza contiene un número, el nombre del asegurado
    y el monto asegurado.
    """

    def __init__(self, numero: str, asegurado: str, monto: float) -> None:
        """
        Inicializa una póliza de seguro.

        Parámetros:
            numero (str): Número de la póliza.
            asegurado (str): Nombre del asegurado.
            monto (float): Monto asegurado.
        """
        self.__numero = numero
        self.__asegurado = asegurado
        self.__monto = monto

    def get_numero(self) -> str:
        """
        Devuelve el número de la póliza.
        """
        return self.__numero

    def set_numero(self, numero: str) -> None:
        """
        Modifica el número de la póliza.
        """
        self.__numero = numero

    def get_asegurado(self) -> str:
        """
        Devuelve el nombre del asegurado.
        """
        return self.__asegurado

    def set_asegurado(self, asegurado: str) -> None:
        """
        Modifica el nombre del asegurado.
        """
        self.__asegurado = asegurado

    def get_monto(self) -> float:
        """
        Devuelve el monto asegurado.
        """
        return self.__monto

    def set_monto(self, monto: float) -> None:
        """
        Modifica el monto asegurado.
        """
        self.__monto = monto

    def __str__(self) -> str:
        """
        Devuelve una representación en texto de la póliza.
        """
        return (
            f"Número de póliza: {self.__numero}\n"
            f"Asegurado: {self.__asegurado}\n"
            f"Monto asegurado: {self.__monto}"
        )

    def __eq__(self, otra_poliza: object) -> bool:
        """
        Compara dos pólizas.

        Dos pólizas son iguales si tienen el mismo número de póliza.
        """
        if not isinstance(otra_poliza, Poliza):
            return False

        return self.__numero == otra_poliza.__numero