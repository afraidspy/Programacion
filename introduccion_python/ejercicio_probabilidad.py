"""
En una urna hay 10 bolas distribuidas de la siguiente manera:
5 bolas rojas
3 bolas azules
2 bolas verdes
Se desea simular 30 extracciones con reemplazo. Esto significa que, después de cada extracción,
la bola se devuelve a la urna antes de realizar la siguiente.
Escribe un programa en Python que:
a) simula las 30 extracciones de bolas
b) cuente cuántas veces se obtiene cada color
c) calcule la probabilidad experimental de obtener una bola roja, una azul y una verde

d) muestre en pantalla los resultados obtenidos;
e) utilice un operador ternario para indicar si el color rojo fue el más frecuente o no.
Para realizar la simulación, utiliza números aleatorios del 1 al 10 con la siguiente correspondencia:
números del 1 al 5: bola roja
números del 6 al 8: bola azul
números del 9 al 10: bola verde
Al final, el programa debe mostrar:
la cantidad de veces que salió cada color;
la probabilidad experimental de cada color;
un mensaje final indicando si el rojo fue o no el color más frecuente.

"""
import random

def sacar_bola():
    
    numero = random.randint(1, 10)
    if numero <= 5: # Esta entre 1 y 5
        return "roja"
    #elif numero >= 6 and numero <= 8:       # Esta entre 6 y 8 entonces es azul
    elif numero <= 8:
        return "azul"
    else:
        return "verde"
    

contador_rojas = 0
contador_verdes = 0
contador_azules = 0
total_experimentos = 30

for i in range (1, total_experimentos + 1):
    resultado = sacar_bola()
    if resultado == "roja":
        contador_rojas +=1
    elif resultado == "verde":
        contador_verdes +=1
    else:
        contador_azules +=1
        

#Calculo de probabilidas
        
prob_rojas =  contador_rojas / total_bolas
prob_verdes = contador_verdes / total_bolas
prob_azules = contador_azules / total_bolas

frecuente = "El rojo es el mas frecuente" if contador_rojas > (contador_verdes and contador_azules) else "El rojo NO es el más frecuente"

print("Prob rojas: ", prob_rojas)
print("Prob verdes: ", prob_verdes)
print("Prob azules: ", prob_azules)
print(frecuente)
    
    
    