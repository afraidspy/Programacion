# Pedir al usuario nombre completo
# Nota: Solo se calcula para personas con un nombre
nombre_completo =  input("Escribe nombre completo: ")
#Pedir fecha de nacimiento en el formato dd/mm/aa
#Conversión de el nombre a mayusculas
nombre_completo = nombre_completo.upper()
print("Tu nombre completo es: " + nombre_completo)
fecha_nacimiento = input("Escribe la fecha de nacimiento dd/mm/aaaa: ")

#Encontrar el primer espacio
primer_espacio =  nombre_completo.find(" ")
print("Indice del primer espacio en blanco ", primer_espacio)
#Substraer los dos primeros carácteres del ap paterno
paterno_caracteres = nombre_completo[primer_espacio:primer_espacio + 3]

paterno_caracteres =  paterno_caracteres.strip()

print("Subcadena de apellido paterno: ", paterno_caracteres)
print("Longitud de la subcadena:  ", len(paterno_caracteres))
#Substraer el primer carácter del ap materno
subcadena = nombre_completo[primer_espacio:].strip()
segundo_blanco = subcadena.find(" ")
print("Subcadena: ", subcadena)
print("Indice segundo blanco: ", segundo_blanco)
apellido_materno = subcadena[segundo_blanco: ].strip()
print("Apellido materno: ", apellido_materno)
# Substraer primer caracter del apellido materno
primer_caracter_ap_materno = apellido_materno[0]
#Substraer el primer carácter del nombre
primer_caracter_nombre = nombre_completo[0]
print("primer caracter del nombre " + primer_caracter_nombre)
#Substraer día, mes y anio de la fecha de nacimiento
dia = fecha_nacimiento[0:2]
mes = fecha_nacimiento[3:5]
anio = fecha_nacimiento[8:]

print("Dia " + dia)
print("Mes " + mes)
print("Anio " + anio)


#Concatenar los valores para regresar el RFC

rfc = paterno_caracteres + primer_caracter_ap_materno + primer_caracter_nombre + anio + mes+ dia

print("RFC es: " + rfc)
                        
