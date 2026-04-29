a = [16,23, 3]
b = [ 5, 12,0]
c = a + b

print(c)

l = [3,4,2,5,6,2,0,3,4,2,0]
sub = l[0:3]

sub_2 = l[4:7]

print(sub_2)

sub3 = l[:5]
print(sub3)
sub3 = l[6:]
print(sub3)

print("Tipo de dato de la estructura: ", type(l))


lista = ["Titanic","Avatar"]

lista.append("Toy Story")
lista.append(10)

print(lista)

#lista.extend("Como agua para chocolate")
lista.extend("3")
print(lista)


lista.insert(3, "Cenicienta")
lista.remove("Avatar")
print(lista)
# Uso de pop
elemento =  lista.pop(2)
print(elemento)
print(lista)

cuantos = lista.count("3")
print("Cuantos: ", cuantos)

lista.pop()
lista.pop()
print(lista)
lista.sort()
print(lista)

lista.reverse()

lista_copia = lista.copy()
print(lista)
print(lista_copia)

lista.clear()

print(lista)



