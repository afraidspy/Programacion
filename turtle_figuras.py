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
