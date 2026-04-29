class Prueba:
    """
    Clase encargada de ejecutar el programa principal.

    Esta clase contiene el menú interactivo que permite probar
    las operaciones de la clase CarteraSeguros.

    La clase Prueba no representa una entidad actuarial.
    Su propósito es servir como clase de ejecución.
    """

    def __init__(self) -> None:
        """
        Inicializa la clase de prueba.

        Crea una cartera de seguros vacía para trabajar con ella
        durante la ejecución del menú.
        """
        self.__cartera = CarteraSeguros("Cartera de vida individual")

    def mostrar_menu(self) -> None:
        """
        Muestra las opciones disponibles del menú.
        """
        print("\nMENÚ DE CARTERA DE SEGUROS")
        print("[1] Agregar póliza")
        print("[2] Mostrar pólizas")
        print("[3] Buscar póliza")
        print("[4] Eliminar póliza")
        print("[5] Contar pólizas")
        print("[6] Calcular monto total")
        print("[7] Calcular monto promedio")
        print("[8] Mostrar póliza con mayor monto")
        print("[9] Filtrar pólizas por monto mínimo")
        print("[10] Ordenar pólizas por monto")
        print("[11] Mostrar resumen de la cartera")
        print("[0] Salir")

    def ejecutar(self) -> None:
        """
        Ejecuta el menú principal usando match case.

        Este método permite al usuario interactuar con una cartera
        de seguros que contiene una lista de objetos Poliza.
        """
        while True:
            self.mostrar_menu()

            opcion = input("Elige una opción: ")

            match opcion:
                case "1":
                    self.__agregar_poliza()

                case "2":
                    self.__mostrar_polizas()

                case "3":
                    self.__buscar_poliza()

                case "4":
                    self.__eliminar_poliza()

                case "5":
                    self.__contar_polizas()

                case "6":
                    self.__calcular_monto_total()

                case "7":
                    self.__calcular_monto_promedio()

                case "8":
                    self.__mostrar_poliza_mayor_monto()

                case "9":
                    self.__filtrar_polizas_por_monto()

                case "10":
                    self.__ordenar_polizas_por_monto()

                case "11":
                    self.__mostrar_resumen_cartera()

                case "0":
                    print("Se terminó el programa.")
                    break

                case _:
                    print("Opción no válida. Intenta nuevamente.")

    def __agregar_poliza(self) -> None:
        """
        Solicita los datos de una póliza y la agrega a la cartera.
        """
        print("\nAGREGAR PÓLIZA")

        numero = input("Número de póliza: ")
        asegurado = input("Nombre del asegurado: ")
        monto = float(input("Monto asegurado: "))

        poliza = Poliza(numero, asegurado, monto)
        self.__cartera.agregar_poliza(poliza)

        print("Póliza agregada correctamente.")

    def __mostrar_polizas(self) -> None:
        """
        Muestra todas las pólizas registradas en la cartera.
        """
        print("\nMOSTRAR PÓLIZAS")
        self.__cartera.mostrar_polizas()

    def __buscar_poliza(self) -> None:
        """
        Busca una póliza dentro de la cartera usando su número.
        """
        print("\nBUSCAR PÓLIZA")

        numero = input("Número de póliza a buscar: ")
        poliza_encontrada = self.__cartera.buscar_poliza(numero)

        if poliza_encontrada is None:
            print("No se encontró la póliza.")
        else:
            print("Póliza encontrada:")
            print(poliza_encontrada)

    def __eliminar_poliza(self) -> None:
        """
        Elimina una póliza de la cartera usando su número.
        """
        print("\nELIMINAR PÓLIZA")

        numero = input("Número de póliza a eliminar: ")
        eliminada = self.__cartera.eliminar_poliza(numero)

        if eliminada:
            print("Póliza eliminada correctamente.")
        else:
            print("No se encontró la póliza.")

    def __contar_polizas(self) -> None:
        """
        Muestra la cantidad total de pólizas registradas.
        """
        print("\nCONTAR PÓLIZAS")
        print(f"Cantidad de pólizas: {self.__cartera.contar_polizas()}")

    def __calcular_monto_total(self) -> None:
        """
        Muestra el monto total asegurado de la cartera.
        """
        print("\nCALCULAR MONTO TOTAL")
        print(f"Monto total asegurado: {self.__cartera.calcular_monto_total()}")

    def __calcular_monto_promedio(self) -> None:
        """
        Muestra el monto promedio asegurado de la cartera.
        """
        print("\nCALCULAR MONTO PROMEDIO")
        print(f"Monto promedio asegurado: {self.__cartera.calcular_monto_promedio()}")

    def __mostrar_poliza_mayor_monto(self) -> None:
        """
        Muestra la póliza con el mayor monto asegurado.
        """
        print("\nPÓLIZA CON MAYOR MONTO")

        poliza_mayor = self.__cartera.obtener_poliza_mayor_monto()

        if poliza_mayor is None:
            print("No hay pólizas registradas.")
        else:
            print(poliza_mayor)

    def __filtrar_polizas_por_monto(self) -> None:
        """
        Filtra y muestra las pólizas que tienen un monto mayor o igual
        al monto mínimo ingresado por el usuario.
        """
        print("\nFILTRAR PÓLIZAS POR MONTO MÍNIMO")

        monto_minimo = float(input("Monto mínimo: "))
        polizas_filtradas = self.__cartera.filtrar_polizas_por_monto(monto_minimo)

        if len(polizas_filtradas) == 0:
            print("No hay pólizas que cumplan con ese monto mínimo.")
        else:
            print("Pólizas encontradas:")
            print("-" * 30)

            for poliza in polizas_filtradas:
                print(poliza)
                print("-" * 30)

    def __ordenar_polizas_por_monto(self) -> None:
        """
        Ordena las pólizas por monto asegurado y luego las muestra.
        """
        print("\nORDENAR PÓLIZAS POR MONTO")

        self.__cartera.ordenar_polizas_por_monto()
        print("Pólizas ordenadas correctamente.")
        self.__cartera.mostrar_polizas()

    def __mostrar_resumen_cartera(self) -> None:
        """
        Muestra el resumen general de la cartera.
        """
        print("\nRESUMEN DE LA CARTERA")
        print(self.__cartera)