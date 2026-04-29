class CarteraSeguros:
    """
    Representa una cartera de seguros.

    Esta clase demuestra composición de objetos porque contiene
    una lista de objetos de tipo Poliza.

    Relación:
        Una CarteraSeguros tiene varias Poliza.
    """

    def __init__(self, nombre: str) -> None:
        """
        Inicializa una cartera de seguros.

        Parámetros:
            nombre (str): Nombre de la cartera.
        """
        self.__nombre = nombre
        self.__polizas = []

    def get_nombre(self) -> str:
        """
        Devuelve el nombre de la cartera.
        """
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        """
        Modifica el nombre de la cartera.
        """
        self.__nombre = nombre

    def get_polizas(self) -> list:
        """
        Devuelve la lista de pólizas.

        Retorna:
            list: Lista de objetos Poliza.
        """
        return self.__polizas

    def set_polizas(self, polizas: list) -> None:
        """
        Modifica la lista completa de pólizas.
        """
        self.__polizas = polizas

    def agregar_poliza(self, poliza: Poliza) -> None:
        """
        Agrega una póliza a la lista de pólizas.

        Parámetros:
            poliza (Poliza): Objeto de tipo Poliza que se agregará.
        """
        self.__polizas.append(poliza)

    def eliminar_poliza(self, numero: str) -> bool:
        """
        Elimina una póliza de la cartera usando su número.

        Parámetros:
            numero (str): Número de la póliza que se desea eliminar.

        Retorna:
            bool: True si la póliza fue eliminada, False si no se encontró.
        """
        for poliza in self.__polizas:
            if poliza.get_numero() == numero:
                self.__polizas.remove(poliza)
                return True

        return False

    def buscar_poliza(self, numero: str) -> object:
        """
        Busca una póliza por su número.

        Parámetros:
            numero (str): Número de la póliza que se desea buscar.

        Retorna:
            Poliza | None: La póliza encontrada o None si no existe.
        """
        for poliza in self.__polizas:
            if poliza.get_numero() == numero:
                return poliza

        return None

    def contar_polizas(self) -> int:
        """
        Cuenta cuántas pólizas tiene la cartera.

        Retorna:
            int: Número total de pólizas.
        """
        return len(self.__polizas)

    def calcular_monto_total(self) -> float:
        """
        Calcula la suma de todos los montos asegurados.

        Retorna:
            float: Monto asegurado total.
        """
        total = 0

        for poliza in self.__polizas:
            total += poliza.get_monto()

        return total

    def calcular_monto_promedio(self) -> float:
        """
        Calcula el monto promedio asegurado.

        Retorna:
            float: Promedio de los montos asegurados.
        """
        if len(self.__polizas) == 0:
            return 0

        return self.calcular_monto_total() / len(self.__polizas)

    def obtener_poliza_mayor_monto(self) -> object:
        """
        Obtiene la póliza con el mayor monto asegurado.

        Retorna:
            Poliza | None: La póliza con mayor monto o None si la lista está vacía.
        """
        if len(self.__polizas) == 0:
            return None

        poliza_mayor = self.__polizas[0]

        for poliza in self.__polizas:
            if poliza.get_monto() > poliza_mayor.get_monto():
                poliza_mayor = poliza

        return poliza_mayor

    def filtrar_polizas_por_monto(self, monto_minimo: float) -> list:
        """
        Filtra las pólizas cuyo monto sea mayor o igual al monto mínimo.

        Parámetros:
            monto_minimo (float): Monto mínimo para filtrar.

        Retorna:
            list: Lista de pólizas que cumplen la condición.
        """
        polizas_filtradas = []

        for poliza in self.__polizas:
            if poliza.get_monto() >= monto_minimo:
                polizas_filtradas.append(poliza)

        return polizas_filtradas

    def ordenar_polizas_por_monto(self) -> None:
        """
        Ordena la lista de pólizas de menor a mayor monto asegurado.
        """
        self.__polizas.sort(key=lambda poliza: poliza.get_monto())

    def mostrar_polizas(self) -> None:
        """
        Muestra todas las pólizas de la cartera.
        """
        print(f"Cartera: {self.__nombre}")
        print("-" * 30)

        for poliza in self.__polizas:
            print(poliza)
            print("-" * 30)

    def __str__(self) -> str:
        """
        Devuelve una representación en texto de la cartera.
        """
        return (
            f"Nombre de la cartera: {self.__nombre}\n"
            f"Cantidad de pólizas: {self.contar_polizas()}\n"
            f"Monto total asegurado: {self.calcular_monto_total()}\n"
            f"Monto promedio asegurado: {self.calcular_monto_promedio()}"
        )

    def __eq__(self, otra_cartera: object) -> bool:
        """
        Compara dos carteras de seguros.

        Dos carteras son iguales si tienen el mismo nombre.
        """
        if not isinstance(otra_cartera, CarteraSeguros):
            return False

        return self.__nombre == otra_cartera.__nombre