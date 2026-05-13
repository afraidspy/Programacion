from EmpleadoPorComision import EmpleadoPorComision

class EmpleadoBase(EmpleadoPorComision):
    
    def __init__(self,nombre, apellidoPaterno, numSegSocial, ventas, comision, sueldoBase):
        super().__init__(nombre, apellidoPaterno, numSegSocial, ventas, comision)
        self.__sueldoBase =  sueldoBase
    
    def calcularSueldo(self):
        return super().calcularSueldo() + self.__sueldoBase
    
    def __str__(self):
        return super().__str__() + " Sueldo base: " + str(self.__sueldoBase)
        


empleado1 =  EmpleadoBase("Pedro","Picapiedra","12", 5, 30, 1000)

print(empleado1)
print(empleado1.calcularSueldo())