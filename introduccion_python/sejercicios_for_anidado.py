# For anidados
contador = 0
for i in range(3):
    for j in range(2):
        print(i,j)
        contador +=1
        
print("Contador: " , contador)

# Tablas de multiplicar
for i in range (1,11):
    for j in range (1, 11):
        mult =  i * j
        print(f"{i} * {j} = {mult}")
    