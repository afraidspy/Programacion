from Equipo import Equipo


class LigaFutbol:
    """
    Representa una liga de fútbol formada por varios equipos.

    Atributos:
        totalEquipos (int): Cantidad total de equipos registrados en la liga.
        equipos (list): Lista de objetos de tipo Equipo.
    """

    def __init__(self):
        """
        Inicializa una liga de fútbol vacía.
        """
        self.__totalEquipos = 0
        self.__equipos = []

    def agregarEquipo(self, equipo):
        """
        Agrega un equipo a la liga si no existe previamente.

        Params:
            equipo (Equipo): Equipo que se desea agregar.
        """
        if not isinstance(equipo, Equipo):
            print("El objeto no es de tipo Equipo")
            return

        if not self.__existeEquipo(equipo):
            self.__equipos.append(equipo)
            self.__totalEquipos += 1
        else:
            print("El equipo ya existe, imposible de agregar")

    def __existeEquipo(self, equipo):
        """
        Verifica si un equipo ya existe en la liga.

        Params:
            equipo (Equipo): Equipo que se desea buscar.

        Returns:
            bool: True si el equipo existe, False en caso contrario.
        """
        for item in self.__equipos:
            if item == equipo:
                return True

        return False

    def obtenerPuntuacionEquipo(self, nombreEquipo):
        """
        Obtiene la puntuación de un equipo por su nombre.

        Params:
            nombreEquipo (str): Nombre del equipo.

        Returns:
            int: Puntos del equipo si se encuentra.
            None: Si el equipo no existe.
        """
        for equipo in self.__equipos:
            if equipo.getNombre().lower() == nombreEquipo.lower():
                return equipo.getPuntos()

        return None

    def obtenerEntrenadores(self):
        """
        Obtiene la lista de entrenadores de todos los equipos.

        Returns:
            list: Lista con los nombres de los entrenadores.
        """
        entrenadores = []

        for equipo in self.__equipos:
            entrenadores.append(equipo.getEntrenador())

        return entrenadores

    def obtenerEntrenadorEquipo(self, nombreEquipo):
        """
        Obtiene el entrenador de un equipo por su nombre.

        Params:
            nombreEquipo (str): Nombre del equipo.

        Returns:
            str: Nombre del entrenador si el equipo existe.
            None: Si el equipo no existe.
        """
        for equipo in self.__equipos:
            if equipo.getNombre().lower() == nombreEquipo.lower():
                return equipo.getEntrenador()

        return None

    def obtenerEstadioEquipo(self, nombreEquipo):
        """
        Obtiene el estadio de un equipo por su nombre.

        Params:
            nombreEquipo (str): Nombre del equipo.

        Returns:
            str: Nombre del estadio si el equipo existe.
            None: Si el equipo no existe.
        """
        for equipo in self.__equipos:
            if equipo.getNombre().lower() == nombreEquipo.lower():
                return equipo.getEstadio()

        return None

    def obtenerEquiposConMayorPuntaje(self):
        """
        Obtiene los equipos con el mayor puntaje de la liga.

        Returns:
            list: Lista de equipos con el mayor puntaje.
        """
        if len(self.__equipos) == 0:
            return []

        mayorPuntaje = self.__equipos[0].getPuntos()

        for equipo in self.__equipos:
            if equipo.getPuntos() > mayorPuntaje:
                mayorPuntaje = equipo.getPuntos()

        equiposMayorPuntaje = []

        for equipo in self.__equipos:
            if equipo.getPuntos() == mayorPuntaje:
                equiposMayorPuntaje.append(equipo)

        return equiposMayorPuntaje

    def obtenerEquiposConMenorPuntaje(self):
        """
        Obtiene los equipos con el menor puntaje de la liga.

        Returns:
            list: Lista de equipos con el menor puntaje.
        """
        if len(self.__equipos) == 0:
            return []

        menorPuntaje = self.__equipos[0].getPuntos()

        for equipo in self.__equipos:
            if equipo.getPuntos() < menorPuntaje:
                menorPuntaje = equipo.getPuntos()

        equiposMenorPuntaje = []

        for equipo in self.__equipos:
            if equipo.getPuntos() == menorPuntaje:
                equiposMenorPuntaje.append(equipo)

        return equiposMenorPuntaje

    def obtenerEquiposPorPuntuacion(self, puntuacion):
        """
        Obtiene los equipos que tienen una puntuación específica.

        Params:
            puntuacion (int): Puntuación que se desea buscar.

        Returns:
            list: Lista de equipos que tienen la puntuación indicada.
        """
        equiposEncontrados = []

        for equipo in self.__equipos:
            if equipo.getPuntos() == puntuacion:
                equiposEncontrados.append(equipo)

        return equiposEncontrados

    def obtenerCantidadEquipos(self):
        """
        Obtiene la cantidad total de equipos registrados.

        Returns:
            int: Total de equipos.
        """
        return self.__totalEquipos

    def obtenerEquipos(self):
        """
        Obtiene todos los equipos registrados en la liga.

        Returns:
            list: Lista de objetos de tipo Equipo.
        """
        return self.__equipos
    
    def eliminarEquipo(self, nombreEquipo:str) -> None:
        
        for i in self.__equipos:
            equipo = i #objeto de la clase Equipo
            
            if equipo.getNombre() ==  nombreEquipo:
                self.__equipos.remove(nombreEquipo)
                self.__total_equipos += -1
        

    def __str__(self):
        """
        Devuelve una representación en texto de la liga.

        Returns:
            str: Información de los equipos de la liga.
        """
        resultado = "Liga de Fútbol\n"
        resultado += "Total de equipos: " + str(self.__totalEquipos) + "\n"

        for equipo in self.__equipos:
            resultado += str(equipo) + "\n"

        return resultado