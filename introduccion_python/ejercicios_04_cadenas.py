"""
Programación
Ejercicios prácticos para poder repasar funciones que trabajen con cadenas
"""
# 8. Pide al usuario una palabra y cuenta cuántas veces aparece la letra "a".
frase = input("Escribe palabra: ")
cuantos = frase.count("ap") #regresa un int
print("Cuantas repeticiones de ap hay: " , cuantos)

# 9. Pide al usuario una frase y reemplaza todas las letras "a" por "@".
frase = input("Escribe palabra: ")
otra_frase = frase.replace("a","@") #regresa un int
print("Remplaezo es: " , otra_frase)

# 10. Pide al usuario una frase y elimina los espacios al inicio y al final.
frase = input("Escribe palabra: ").strip()
print("Palabra sin espacios es: " , frase)

# 11. Pide al usuario una frase y cuenta cuántas palabras tiene.

# 12. Pide al usuario una frase y muestra cada palabra en una línea diferente.
frase = input("Escribe la frase: ")
palabras = frase.split("a")
print("Palabras de la frase: ")
print(palabras)


# 13. Pide al usuario una palabra y verifica si empieza con una letra específica.

# 14. Pide al usuario una palabra y verifica si termina con una letra específica.

# 15. Pide al usuario una frase y cuenta cuántas vocales contiene en total.

# 16. Pide al usuario una frase y cuenta cuántas veces aparece una palabra específica.

# 17. Pide al usuario una palabra y verifica si es un palíndromo.

# 18. Pide al usuario un nombre completo y muestra sus iniciales.

# 19. Pide al usuario un correo electrónico y valida de forma básica si contiene "@" y ".".

# 20. Pide al usuario una frase y muestra:
# - la cantidad de caracteres
# - la cantidad de palabras
# - la frase en mayúsculas
# - la frase en minúsculas
# - la frase al revés