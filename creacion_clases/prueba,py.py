from Equipo import Equipo
from liga_futbol import LigaFutbol


def mostrarEquipos(equipos):
    """
    Muestra una lista de equipos.

    Params:
        equipos (list): Lista de objetos de tipo Equipo.
    """
    if len(equipos) == 0:
        print("No hay equipos para mostrar")
    else:
        for equipo in equipos:
            print(equipo)


def main():
    """
    Ejecuta el menú principal del programa.
    """
    liga = LigaFutbol()

    opcion = -1

    while opcion != 0:
        print("\nMENÚ LIGA DE FÚTBOL")
        print("1. Agregar equipo")
        print("2. Obtener puntuación de un equipo")
        print("3. Obtener entrenadores")
        print("4. Obtener entrenador de un equipo")
        print("5. Obtener estadio de un equipo")
        print("6. Obtener equipos con mayor puntaje")
        print("7. Obtener equipos con menor puntaje")
        print("8. Obtener equipos por puntuación")
        print("9. Obtener cantidad de equipos")
        print("10. Mostrar todos los equipos")
        print("0. Salir")

        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                nombre = input("Ingrese el nombre del equipo: ")
                entrenador = input("Ingrese el entrenador: ")
                estadio = input("Ingrese el estadio: ")
                puntos = int(input("Ingrese los puntos: "))

                jugadores = []
                cantidadJugadores = int(input("Ingrese la cantidad de jugadores: "))

                for i in range(cantidadJugadores):
                    jugador = input("Ingrese el nombre del jugador " + str(i + 1) + ": ")
                    jugadores.append(jugador)

                equipo = Equipo(nombre, entrenador, estadio, puntos, jugadores)
                liga.agregarEquipo(equipo)

            case 2:
                nombre = input("Ingrese el nombre del equipo: ")
                puntos = liga.obtenerPuntuacionEquipo(nombre)

                if puntos is None:
                    print("Equipo no encontrado")
                else:
                    print("Puntuación:", puntos)

            case 3:
                entrenadores = liga.obtenerEntrenadores()

                if len(entrenadores) == 0:
                    print("No hay entrenadores registrados")
                else:
                    print("Entrenadores:")
                    for entrenador in entrenadores:
                        print(entrenador)

            case 4:
                nombre = input("Ingrese el nombre del equipo: ")
                entrenador = liga.obtenerEntrenadorEquipo(nombre)

                if entrenador is None:
                    print("Equipo no encontrado")
                else:
                    print("Entrenador:", entrenador)

            case 5:
                nombre = input("Ingrese el nombre del equipo: ")
                estadio = liga.obtenerEstadioEquipo(nombre)

                if estadio is None:
                    print("Equipo no encontrado")
                else:
                    print("Estadio:", estadio)

            case 6:
                equipos = liga.obtenerEquiposConMayorPuntaje()
                print("Equipos con mayor puntaje:")
                mostrarEquipos(equipos)

            case 7:
                equipos = liga.obtenerEquiposConMenorPuntaje()
                print("Equipos con menor puntaje:")
                mostrarEquipos(equipos)

            case 8:
                puntuacion = int(input("Ingrese la puntuación a buscar: "))
                equipos = liga.obtenerEquiposPorPuntuacion(puntuacion)

                print("Equipos con puntuación", puntuacion, ":")
                mostrarEquipos(equipos)

            case 9:
                print("Cantidad de equipos:", liga.obtenerCantidadEquipos())

            case 10:
                print(liga)

            case 0:
                print("Programa finalizado")

            case _:
                print("Opción inválida")


main()