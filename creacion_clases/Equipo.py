class Equipo:
	
    def __init__(self, nombre, entrenador, estadio, puntos, jugadores):
        """
            Inicializa los datos de un equipo
            Parameters:
            nombre:str  -- nombre del equipo
            entrenador:str-- entrenador del equipo
            estadio:str -- estadio del equipo
            puntos:int -- puntos del equipo
        
        """
        self.__nombre = nombre
        self.__entrenador = entrenador
        self.__estadio = estadio 
        self.__puntos =  puntos
        self.__jugadores = jugadores
    
    def setNombre(self, nombre):
        """
        Establece el nombre del equipo
        Parameters:
        nombre: str -- nombre del equipo
        """
        self.__nombre = nombre

    def setEntrenador(self, entrenador):
        self.__entrenador = entrenador
    
    def setEstadio(self, estadio):
        self.__estadio = estadio
    
    def setPuntos(self, puntos):
        self.__puntos = puntos
        
    def getNombre(self):
        return self.__nombre
    
    def getEntrenador(self):
        return self.__entrenador
    
    def getEstadio(self):
        return self.__estadio
    
    def getPuntos(self):
        return self.__puntos
        
    def __str__(self):
        return "Nombre: " + self.__nombre + "Entrenador: " + self.__entrenador + "Estadio: "+ self.__estadio+ str(self.__puntos)
    
    def __eq__(self, otro):
        return self.__nombre ==  otro.__nombre and self.__entrenador == otro.__entrenador and self.__estadio == otro.__estadio  and self.__puntaje == otro.__puntaje and self.__jugadores == otro.__jugadores
                    
  
equipo1 =  Equipo("Pumas","Efraìn Juàrez","Estadio Olimpico Universitario",10,[])
 
print(equipo1)