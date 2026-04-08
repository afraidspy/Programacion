"""
turtle
Es una biblioteca para hacer dibujos con una “tortuga”
que se mueve en pantalla.
"""

import turtle
"""
pen = turtle.Turtle()

pen.forward(100) # Avanza 100 unidades
pen.left(90) #Gira  90 grados
pen.forward(100)# Avanza 100 unidades
turtle.done() #terminar y dejar la ventana abierta
"""
## Ejercicio
"""screen = turtle.Screen()
screen.title("Cuadrados")
pen = turtle.Turtle()
pen.color("black", "yellow")
pen.speed(5)

def dibuja_cuadrado(tam):
    count = 0
    pen.begin_fill()
    while count < 4:
        pen.forward(tam)
        pen.left(90)
        count += 1
    pen.end_fill()

total = 0  # Inicializa el contador en 0
while total < 5:  # Repite mientras total sea menor que 5
    dibuja_cuadrado(50)  # Dibuja un cuadrado de lado 50
    pen.penup()  # Levanta el lápiz para moverse sin dibujar
    pen.forward(70)  # Avanza 70 unidades para dejar espacio entre cada cuadrado
    pen.pendown()  # Baja el lápiz para volver a dibujar
    total += 1  # Aumenta el contador en 1
turtle.done()
"""
"""
Dibuja 8 figuras:
cuadrado si el número es par
triángulo si es impar
"""

import turtle

# Crea la ventana donde aparecerán los dibujos
screen = turtle.Screen()
screen.setup(width=1000, height=400)  # Define el tamaño de la ventana
screen.title("Figuras pares e impares")  # Define el título de la ventana

# Crea la tortuga que dibujará las figuras
pen = turtle.Turtle()
pen.speed(5)  # Define la velocidad del dibujo

# Función para dibujar un cuadrado
def dibuja_cuadrado(size):
    count = 0  # Contador para repetir 4 veces
    while count < 4:  # Un cuadrado tiene 4 lados
        pen.forward(size)  # Dibuja un lado
        pen.left(90)  # Gira 90 grados a la izquierda
        count += 1  # Aumenta el contador

# Función para dibujar un triángulo
def dibuja_triangulo(size):
    count = 0  # Contador para repetir 3 veces
    while count < 3:  # Un triángulo tiene 3 lados
        pen.forward(size)  # Dibuja un lado
        pen.left(120)  # Gira 120 grados a la izquierda
        count += 1  # Aumenta el contador

# Levanta el lápiz para mover la tortuga sin dibujar
pen.penup()

# Mueve la tortuga hacia la parte izquierda de la ventana
# Esto ayuda a que las 8 figuras quepan en la pantalla
pen.goto(-420, 0)

# Vuelve a bajar el lápiz para empezar a dibujar
pen.pendown()

total = 1  # Empieza a contar desde 1

# Repite hasta dibujar 8 figuras
while total <= 8:
    # Si el número es par, dibuja un cuadrado
    if total % 2 == 0:
        dibuja_cuadrado(50)
    else:
        # Si el número es impar, dibuja un triángulo
        dibuja_triangulo(50)

    # Se mueve a la derecha solo si no es la última figura
    if total < 8:
        pen.penup()  # Levanta el lápiz para no dibujar al moverse
        pen.forward(80)  # Avanza para dejar espacio entre figuras
        pen.pendown()  # Baja el lápiz para dibujar la siguiente figura

    total += 1  # Aumenta el contador

# Mantiene la ventana abierta
turtle.done()


