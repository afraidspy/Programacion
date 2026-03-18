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



def main(contador_ganador, contador_perdidos, contador_empate):
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
        ganador = determinar_ganador(opcion_maquina , opcion_usuario).strip()
        print("Ganador: ", ganador)
        if ganador == "Ganaste":
            contador_ganador += 1
        elif ganador == "Perdiste":
            contador_perdidos += 1
        else:
            contador_empate +=1
            
        print(ganador)
        print("fin del programa")
    return (contador_ganador, contador_perdidos, contador_empate)
        
#Aquí empieza la ejecución principal del programa
contador_total_juegos = 0
contador_ganador = 0
contador_perdidos = 0
contador_empate = 0
 
while True:
    opcion = input("¿Quieres jugar?: ").strip().upper()#Si o No
    
    if opcion == "SI":
        contador_total_juegos += 1
        a,b,c = main(contador_ganador, contador_perdidos, contador_empate)
        contador_ganador = a
        contador_perdidos = b
        contador_empate = c
        
    elif opcion == "NO":
        print("Ganados: ",contador_ganador)
        print("Perdidos", contador_perdidos)
        print("Empate:",contador_empate)
        break
    else:
        print("Opción NO válida")

print("Fin del programa")
print("Total juegos jugados: ", contador_total_juegos)
print("Total juegos ganados: ",contador_ganador)
print("Total juegos perdidos: ",contador_perdidos)
print("Total juegos empate: ",contador_empate)


#Investigar que es el paso por valor y paso por referencia en PYTHON
        
    
    
    