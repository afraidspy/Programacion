class Robot:
    
    def __init__(self):# Mètodo constructor : Inicializa el estado del objeto
        ## Self
        ## referencia al objeto actual dentro de una clase
        """
            Constructor de la clase
        """
        print("Entrando al metodo inicial")
        #guarda el valor del nombre dentro del objeto
        self.nombre = "Wall-e" #atributo publico
        self.__edad = 100  #atribtuo privado __
        self.__peso = 200
        self.__num_armas = 3
        """
        Encapsulamiento: encapsulamiento se ve cuando los datos internos
        del robot no se manipulan directamente, sino a través de métodos
        de acceso y modificación. 
        Los atributos con __ inidcan que que no deberían tocarse
        directamente desde fuera de la clase.
        La idea es proteger el estado interno del objeto.
        """
    
    ##########################
    # Métodos de acceso     ###
    ##########################
    
    def get_edad(self) -> float:
        return self.__edad
    
    def get_peso(self) -> float:
        return self.__peso
    
    def get_num_armas(self) -> float:
        return self.__num_armas
    
    ##################################
    # Métodos modificadores
    #################################
    
    def set_peso(self, nuevo_peso:float):
        self.__peso = nuevo_peso
    
    def set_edad(self, nueva_edad:float):
        self.__edad = nueva_edad
    
    def set_num_armas(self, nuevo_num_armas):
        self.__num_armas =  nuevo_num_armas
        
#Aqui termina la clase    
bunny = Robot() #Esta línea crea un objeto de la clase y manda a llamar al mètodo init
"""
La abstracción, se refiere a solo mostrar lo importante y
ocultar los detalles internos de funcionamiento.

Desde fuera, nosotros solo sabemos que el robot:
se le puede cambiar el peso
se le puede cambiar el numero de armas
La clase ofrece una forma sencilla de usar el objeto Robot,
por ejemplo con get_peso() o set_peso(),
sin que el usuario necesite entender cómo está implementado internamente.
"""
bunny.set_peso(500)
bunny.set_num_armas(10)
print("Peso: ",bunny.get_peso())
print("Nombre:  ", bunny.nombre)
print("Edad: ", bunny.get_edad())
print("Num armas: ", bunny.get_num_armas())

print(bunny.nombre)
bunny.nombre = "Robotin"
print(bunny.nombre)
#bunny.__edad = 900
#print(bunny.__edad) -- visibilidad privada
