class EmpleadoPorComision(object):
    
    def __init__(self,nombre, apellidoPaterno, numSegSocial, ventas, comision):
        self._nombre = nombre  #protected
        self._apellidoPaterno = apellidoPaterno
        self._numSegSocial = numSegSocial
        self._ventas = ventas
        self._comision = comision
        
    def calcularSueldo(self):
        return self._ventas * self._comision
    
    def __str__(self):
        return self._nombre + "-" + str(self._ventas)
    
        