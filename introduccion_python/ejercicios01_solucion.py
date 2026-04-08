"""
ejercicios01.py

Objetivo:
1) Identificar si un nombre puede usarse como identificador en Python.
2) Proponer correcciones cuando no sea válido.
3) Elegir nombres apropiados para variables a partir de un enunciado.

"""

"Parte 1: Idenfitficadores"

"""
Instrucciones:
- Para cada línea de abajo:
  1) escribe si el identificador es válido (True/False)
  2) si NO es válido, escribe una corrección sugerida en snake_case
  3) si SÍ es válido, la corrección sugerida puede ser el mismo nombre
- Responde escribiendo al lado de cada línea (en el comentario con comillas dobles).
- No cambies los valores.
"""
corazòn = "roto"
id_paciente = 1001 
nombre_completo = "Ana López"
telefono_paciente = "5551234567"  
edad = 20  
segundo_apellido = "García"  
fecha_cita = "Lunes"  
cancelada = "no"  
motivo_cancelacion = "" 
class_a = "A" 
for_3 = 3 
str_texto = "texto" 
list_grupo = "grupo 1"
_total_citas = 12  
TotalCitas = 12  
costo = 500  
nombre_del_medico = "Dra. Pérez" 
cita = "A-103"
hora_cita = "10:30" 
correo_electronico = "ana@example.com" 
pais_origen = "México" 


"Parte 2: Elige identificadores significativos a partir de un enunciado"

"""
Instrucciones:
Lee el enunciado y escribe qué identificador pondrías para cada variable.
Escribe tus respuestas, e inicializalas con un valor apropiado. Puedes incluso inicializarlas en None

Reglas:
- Usa snake_case.
- Evita palabras reservadas.
- Deben ser claros y específicos, es decir significativos

"""

"""
Registro de una cita médica:
Un alumno está registrando información básica de una cita médica.
Quiere guardar:
1) el nombre completo del paciente
2) la edad del paciente
3) el día de la cita (como texto, por ejemplo "Lunes")
4) el número de teléfono del paciente
5) si la cita fue cancelada (sí o no)
6) el motivo de la cancelación (puede quedar vacío si no hubo cancelación)

"""
nombre_paciente = "Pedro"
edad_paciente = 30
dia_cita = "Lunes"
num_telefono = 5577899345
esta_cancela = True
motivo_cancelacion = None



"Enunciado 1: Registro de alumno"
"""
Quiere guardar:
1) nombre completo del alumno
2) matrícula del alumno
3) semestre actual
4) grupo
5) promedio (puede quedar vacío si aún no hay)
6) si tiene beca (sí o no)
"""

nombre_alumno = "Diana Medina Suarez"
matricula = "AA-203"
semestre = "2026-2"
grupo = "Programacion"
promedio = "10.0"
tiene_beca = False

"Enunciado 2: Pedido en cafetería"
"""
Quiere guardar:
1) nombre del cliente
2) producto pedido
3) cantidad
4) tamaño del producto (chico/mediano/grande)
5) si es para llevar (sí o no)
6) nota adicional (puede quedar vacía)
"""
nombre_cliente= "Sergio "
producto = "cafe mediano"
cantidad = 1
tamanio = "mediano"
es_para_llevar = True
nota_adicional = ""

"Enunciado 3: Biblioteca (préstamo de libro)"
"""
Quiere guardar:
1) título del libro
2) autor
3) número de ejemplar
4) fecha de préstamo (texto)
5) fecha de devolución (texto)
6) si fue devuelto (sí o no)
"""
titulo_libro = "Programaciòn en Java"
autor = "Deitel"
numero_ejemplar = 30
fecha_prestamo = "25-02-26"
fecha_devolucion = "26-02-26"
esta_devuelto = False

"Enunciado 4: Reserva de hotel"
"""
Quiere guardar:
1) nombre del huésped
2) número de habitación
3) fecha de entrada (texto)
4) fecha de salida (texto)
5) número de noches
6) si incluye desayuno (sí o no)
"""

nombre_huesped = "Karla Rojas"
num_habitacion = 304
fecha_entrada = "14-02-26"
fecha_salida = "24-02-26"
num_noches =  10
con_desayuno = False

#Imprime los valores de cada variable, así como su tipo de dato.
