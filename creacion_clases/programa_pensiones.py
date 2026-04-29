class Pensionado:
    def __init__(self, nombre, edad, salario_base, anios_cotizados):
        self.__nombre = nombre
        self.__edad = edad
        self.__salario_base = salario_base
        self.__anios_cotizados = anios_cotizados
        self.__monto_pension = self.__calcular_pension()

    def __calcular_pension(self):
        decena = self.__anios_cotizados // 10

        match decena:
            case 0:
                return 0
            case 1:
                return self.__salario_base * 0.40
            case 2:
                return self.__salario_base * 0.60
            case _:
                return self.__salario_base * 0.80

    def __str__(self):
        return (
            "Nombre: " + self.__nombre +
            " | Edad: " + str(self.__edad) +
            " | Salario base: " + str(self.__salario_base) +
            " | Anios cotizados: " + str(self.__anios_cotizados) +
            " | Pension: " + str(self.__monto_pension)
        )

    def __eq__(self, otro):
        if type(otro) == Pensionado:
            return self.__nombre.lower() == otro.__nombre.lower()
        return False

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def obtener_salario_base(self):
        return self.__salario_base

    def obtener_anios_cotizados(self):
        return self.__anios_cotizados

    def obtener_monto_pension(self):
        return self.__monto_pension

    def establecer_nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            self.__nombre = nuevo_nombre

    def establecer_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

    def establecer_salario_base(self, nuevo_salario_base):
        if nuevo_salario_base >= 0:
            self.__salario_base = nuevo_salario_base
            self.__monto_pension = self.__calcular_pension()

    def establecer_anios_cotizados(self, nuevos_anios_cotizados):
        if nuevos_anios_cotizados >= 0:
            self.__anios_cotizados = nuevos_anios_cotizados
            self.__monto_pension = self.__calcular_pension()

    def mostrar_datos(self):
        print(self.__str__())


class SistemaPensiones:
    def __init__(self, maximo_pensionados):
        self.__maximo_pensionados = maximo_pensionados
        self.__pensionados = []

    def es_entero_positivo(self, texto):
        return texto.isdigit()

    def es_decimal_positivo(self, texto):
        if texto.count(".") > 1:
            return False

        partes = texto.split(".")

        if len(partes) == 1:
            return partes[0].isdigit()

        if len(partes) == 2:
            parte_entera = partes[0]
            parte_decimal = partes[1]

            if parte_entera == "":
                return False

            if not parte_entera.isdigit():
                return False

            if parte_decimal == "":
                return True

            return parte_decimal.isdigit()

        return False

    def leer_entero_positivo(self, mensaje):
        valor = input(mensaje).strip()

        while not self.es_entero_positivo(valor):
            print("Debes ingresar un numero entero valido.")
            valor = input(mensaje).strip()

        return int(valor)

    def leer_decimal_positivo(self, mensaje):
        valor = input(mensaje).strip()

        while not self.es_decimal_positivo(valor):
            print("Debes ingresar un numero decimal valido.")
            valor = input(mensaje).strip()

        return float(valor)

    def buscar_pensionado(self, nombre):
        for pensionado in self.__pensionados:
            if pensionado.obtener_nombre().lower() == nombre.lower():
                return pensionado
        return None

    def agregar_pensionado(self):
        if len(self.__pensionados) >= self.__maximo_pensionados:
            print("El sistema ya alcanzo el numero maximo de pensionados.\n")
            return

        nombre = input("Ingresa el nombre del pensionado: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacio.\n")
            return

        if self.buscar_pensionado(nombre) is not None:
            print("Ese pensionado ya existe.\n")
            return

        edad = self.leer_entero_positivo("Ingresa la edad: ")
        salario_base = self.leer_decimal_positivo("Ingresa el salario base: ")
        anios_cotizados = self.leer_entero_positivo("Ingresa los anios cotizados: ")

        nuevo_pensionado = Pensionado(nombre, edad, salario_base, anios_cotizados)
        self.__pensionados.append(nuevo_pensionado)

        print("Pensionado agregado correctamente.\n")

    def mostrar_pension_de_un_pensionado(self):
        nombre = input("Ingresa el nombre del pensionado: ").strip()
        pensionado = self.buscar_pensionado(nombre)

        if pensionado is not None:
            print(
                "La pension de " +
                pensionado.obtener_nombre() +
                " es: " +
                str(pensionado.obtener_monto_pension()) +
                "\n"
            )
        else:
            print("Pensionado no encontrado.\n")

    def mostrar_todos_los_pensionados(self):
        if len(self.__pensionados) == 0:
            print("No hay pensionados registrados.\n")
            return

        print("Lista de pensionados:")
        for pensionado in self.__pensionados:
            print(pensionado)
        print()

    def mostrar_pensionado_con_mayor_pension(self):
        if len(self.__pensionados) == 0:
            print("No hay pensionados registrados.\n")
            return

        mayor = self.__pensionados[0]

        for pensionado in self.__pensionados:
            if pensionado.obtener_monto_pension() > mayor.obtener_monto_pension():
                mayor = pensionado

        print(
            "El pensionado con mayor pension es " +
            mayor.obtener_nombre() +
            " con " +
            str(mayor.obtener_monto_pension()) +
            "\n"
        )

    def mostrar_pensionado_con_menor_pension(self):
        if len(self.__pensionados) == 0:
            print("No hay pensionados registrados.\n")
            return

        menor = self.__pensionados[0]

        for pensionado in self.__pensionados:
            if pensionado.obtener_monto_pension() < menor.obtener_monto_pension():
                menor = pensionado

        print(
            "El pensionado con menor pension es " +
            menor.obtener_nombre() +
            " con " +
            str(menor.obtener_monto_pension()) +
            "\n"
        )

    def mostrar_pensionados_por_anios_cotizados(self):
        anios_buscados = self.leer_entero_positivo("Ingresa los anios cotizados a buscar: ")
        encontrados = []

        for pensionado in self.__pensionados:
            if pensionado.obtener_anios_cotizados() == anios_buscados:
                encontrados.append(pensionado)

        if len(encontrados) > 0:
            print("Pensionados con " + str(anios_buscados) + " anios cotizados:")
            for pensionado in encontrados:
                print(pensionado.obtener_nombre())
            print()
        else:
            print("No hay pensionados con esa cantidad de anios cotizados.\n")

    def mostrar_cantidad_pensionados(self):
        print("La cantidad de pensionados registrados es: " + str(len(self.__pensionados)) + "\n")

    def mostrar_datos_de_un_pensionado(self):
        nombre = input("Ingresa el nombre del pensionado: ").strip()
        pensionado = self.buscar_pensionado(nombre)

        if pensionado is not None:
            print(pensionado)
            print()
        else:
            print("Pensionado no encontrado.\n")

    def mostrar_menu(self):
        print("M E N U")
        print("[0] Salir")
        print("[1] Agregar pensionado")
        print("[2] Mostrar la pension de un pensionado")
        print("[3] Mostrar todos los pensionados")
        print("[4] Mostrar pensionado con mayor pension")
        print("[5] Mostrar pensionado con menor pension")
        print("[6] Mostrar pensionados por anios cotizados")
        print("[7] Mostrar cantidad de pensionados")
        print("[8] Mostrar datos de un pensionado")

    def ejecutar(self):
        opcion = -1

        while opcion != 0:
            self.mostrar_menu()
            texto_opcion = input("Selecciona una opcion: ").strip()

            if not texto_opcion.isdigit():
                print("Debes ingresar una opcion valida.\n")
                continue

            opcion = int(texto_opcion)

            match opcion:
                case 0:
                    print("Saliendo del programa.")
                case 1:
                    self.agregar_pensionado()
                case 2:
                    self.mostrar_pension_de_un_pensionado()
                case 3:
                    self.mostrar_todos_los_pensionados()
                case 4:
                    self.mostrar_pensionado_con_mayor_pension()
                case 5:
                    self.mostrar_pensionado_con_menor_pension()
                case 6:
                    self.mostrar_pensionados_por_anios_cotizados()
                case 7:
                    self.mostrar_cantidad_pensionados()
                case 8:
                    self.mostrar_datos_de_un_pensionado()
                case _:
                    print("Opcion no valida.\n")


sistema = SistemaPensiones(10)
sistema.ejecutar()