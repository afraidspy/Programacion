import random # Se manda a llamar a la libreria random

#Se manda a llamar al método randrange con el símbolo de punto
aleatorio = random.randrange(1,4) ## selecciona un numero al azar entre 1 y 4-1 (n,m) -> [n,m-1]
#print(aleatorio)
maquina = 1 # Variable para guardar el tiro de la computadora
if aleatorio == 1:
    maquina = "PIEDRA"
elif aleatorio == 2:
    maquina = "PAPEL"
elif aleatorio == 3:
    maquina = "TIJERA"
else: # Este else es opcional
    print("Opcion no válida")

#Pedir el tiro del usuario
print("ingresa 1 para PIEDRA, ingresa 2 para PAPEL, ingresa 3 para TIJERA")
miopcion = int(input())

if miopcion == 1:
    miopcion = "PIEDRA"
elif miopcion == 2:
    miopcion = "PAPEL"
elif miopcion == 3:
    miopcion = "TIJERA"
else:#Esta si es obligatoria en caso de que el usuairo escriba un número no valido
    print("Opcion no válida")

print("la opcion de la maquina fue: ",maquina)
print("tu opcion fue: ",miopcion)

# Validar las opciones mías contra la maquina para ver los casos
#En los que se pierde
if miopcion == "PIEDRA" and maquina =="PAPEL":
    print("perdiste")
elif miopcion == "PAPEL" and maquina =="TIJERA":
    print("perdiste")
elif miopcion == "TIJERA" and maquina =="PIEDRA":
    print("perdiste")


# Casos para ver cuando se gana
if miopcion == "PAPEL" and maquina =="PIEDRA":
    print("ganaste")
elif miopcion == "TIJERA" and maquina =="PAPEL":
    print("ganaste")
elif miopcion == "PIEDRA" and maquina =="TIJERA":
    print("ganaste")
elif maquina == miopcion:
    print("empate")


print("FIN DEL PROGRAMA C: ")