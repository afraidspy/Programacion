from Equipo import Equipo

class LigaFutbol:
    
    def __init__(self):
        self.__total_equipos = 0
        self.__equipos = []  #Lista de Objetos de tipo Equipo
        
    def agregarEquipo(self, equipo):
        if not(__existeEquipo(equipo)):
            self.__equipos.append(equipo)
            self_total_equipos += 1
        else:
            print("El equipo ya existe, imposible de agregar")
    
    def __existeEquipo(self, equipo:object)-> bool:#Método privado
        for item in self.__equipos:
            if item == equipo:
                return True
        
        return False
        
        
        