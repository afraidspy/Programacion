class Equipo:
    """
    Representa un equipo de fútbol.

    Atributos:
        nombre (str): Nombre del equipo.
        entrenador (str): Nombre del entrenador.
        estadio (str): Nombre del estadio.
        puntos (int): Puntos del equipo.
        jugadores (list): Lista de jugadores del equipo.
    """

    def __init__(self, nombre, entrenador, estadio, puntos, jugadores):
        """
        Inicializa un equipo de fútbol.

        Params:
            nombre (str): Nombre del equipo.
            entrenador (str): Nombre del entrenador.
            estadio (str): Nombre del estadio.
            puntos (int): Puntos del equipo.
            jugadores (list): Lista de jugadores del equipo.
        """
        self.__nombre = nombre
        self.__entrenador = entrenador
        self.__estadio = estadio
        self.__puntos = puntos
        self.__jugadores = jugadores

    def setNombre(self, nombre):
        """
        Establece el nombre del equipo.

        Params:
            nombre (str): Nuevo nombre del equipo.
        """
        self.__nombre = nombre

    def setEntrenador(self, entrenador):
        """
        Establece el entrenador del equipo.

        Params:
            entrenador (str): Nuevo entrenador del equipo.
        """
        self.__entrenador = entrenador

    def setEstadio(self, estadio):
        """
        Establece el estadio del equipo.

        Params:
            estadio (str): Nuevo estadio del equipo.
        """
        self.__estadio = estadio

    def setPuntos(self, puntos):
        """
        Establece los puntos del equipo.

        Params:
            puntos (int): Nuevos puntos del equipo.
        """
        self.__puntos = puntos

    def setJugadores(self, jugadores):
        """
        Establece la lista de jugadores del equipo.

        Params:
            jugadores (list): Nueva lista de jugadores.
        """
        self.__jugadores = jugadores

    def getNombre(self):
        """
        Obtiene el nombre del equipo.

        Returns:
            str: Nombre del equipo.
        """
        return self.__nombre

    def getEntrenador(self):
        """
        Obtiene el entrenador del equipo.

        Returns:
            str: Nombre del entrenador.
        """
        return self.__entrenador

    def getEstadio(self):
        """
        Obtiene el estadio del equipo.

        Returns:
            str: Nombre del estadio.
        """
        return self.__estadio

    def getPuntos(self):
        """
        Obtiene los puntos del equipo.

        Returns:
            int: Puntos del equipo.
        """
        return self.__puntos

    def getJugadores(self):
        """
        Obtiene la lista de jugadores del equipo.

        Returns:
            list: Lista de jugadores del equipo.
        """
        return self.__jugadores

    def __str__(self):
        """
        Devuelve una representación en texto del equipo.

        Returns:
            str: Información del equipo.
        """
        return (
            "Nombre: " + self.__nombre +
            ", Entrenador: " + self.__entrenador +
            ", Estadio: " + self.__estadio +
            ", Puntos: " + str(self.__puntos) +
            ", Jugadores: " + str(self.__jugadores)
        )

    def __eq__(self, otro):
        """
        Compara dos equipos.

        Params:
            otro (object): Objeto que se va a comparar con el equipo actual.

        Returns:
            bool: True si ambos objetos son de tipo Equipo y tienen los mismos datos.
                  False en caso contrario.
        """
        if not isinstance(otro, Equipo):
            return False

        return (
            self.__nombre == otro.__nombre and
            self.__entrenador == otro.__entrenador and
            self.__estadio == otro.__estadio and
            self.__puntos == otro.__puntos and
            self.__jugadores == otro.__jugadores
        )
  
equipo1 =  Equipo("Pumas","Efraìn Juàrez","Estadio Olimpico Universitario",10,[])
 
print(equipo1)