lista=[7,6,5,4,3,2]
print(len(lista))
#Agregar elementos al final
lista.append("Manzana")
print(lista)
#Agregar en un determinado lugar
lista.insert(1,8)
print(lista)
#Borrar valores por su posicion
del lista[3]
print(lista)
#Borra el valor de la lista
lista.remove(2)
print(lista)
#POP
lista.pop()
print(lista)
#Averigua informacion de elementos
print(lista.index(4))

lista[0]=1
print(lista)

nom,edad,estatura,año,codigo = lista

a=10
b=20
c,d=a,b
print(f"c{c} d{d}")

b,a=a,b
print(f"a{a} b{b}")