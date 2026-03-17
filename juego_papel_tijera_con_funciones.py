import random

def convertir_opcion_a_cadena(numero):
    """
        Convierte el número en una opción correspondiente
        al juego
        PIEDRA - 1
        PAPEL -  2
        TIJERA - 3
    """
    if numero == 1:
        return "PIEDRA"
    elif numero == 2:
        return "PAPEL"
    elif numero == 3:
        return "TIJERA"
    else:
        return None

def obtener_opcion_maquina():
    """
        Genera un número aleatorio y regresa la opción de la máquina
    """
    #Se manda a llamar al método randrange con el símbolo de punto
    aleatorio = random.randrange(1,4) ## selecciona un numero al azar entre 1 y 4-1 (n,m) -> [n,m-1]
    #En caso de que aleatorio no sea un número válido nos va a regresa None
    return convertir_opcion_a_cadena(aleatorio)

def obtener_opcion_usuario():
    """
        Solicitar al usuario que escriba una opción y la función
        va a regresar la cadena asociada a ese número
    """
    #Pedir el tiro del usuario
    print("ingresa 1 para PIEDRA, ingresa 2 para PAPEL, ingresa 3 para TIJERA")
    miopcion = int(input())
    return convertir_opcion_a_cadena(miopcion)

def determinar_ganador(opcion_compu, opcion_usuario):
    """
        Determinar quién es el ganador del juego o
        si hay empate
    """
    if opcion_compu == opcion_usuario:
        return "empate"
    elif opcion_usuario == "PIEDRA" and opcion_compu =="TIJERA":
        return "Ganaste"
    elif opcion_usuario == "PAPEL" and opcion_compu == "PIEDRA":
        return "Ganaste"
    elif opcion_usuario == "TIJERA" and opcion_compu == "PAPEL":
        return "Ganaste"
    else:
        return "Perdiste"
    

def main():
    """
        Aquí se mandan a llamar a las funciones anteriores
        para ejecutar el juego
    """
    opcion_maquina = obtener_opcion_maquina()
    opcion_usuario = obtener_opcion_usuario()
    
    if opcion_usuario is None:
        print("Opción NO válida")
    else:
        print("La opción de la máquina es: ")
        print(opcion_maquina)
        print("La opción de usuario es: ")
        print(opcion_usuario)
        ganador = determinar_ganador(opcion_maquina , opcion_usuario)
        print(ganador)
        print("fin del programa")
        
#Aquí empieza la ejecución principal del programa
while True:
    desea_jugar =  input("¿Quieres jugar piedra papel o tijera?").strip().upper()
    if desea_jugar == "SI":
        main()
    elif desea_jugar == "NO":
        break
    else:
        print("Opción no válida")


        
    
    
    