lista=[1, 2, 3, 4, 5]
print(lista)
e=int(input("que numero desea eliminar:"))
for k in range(len(lista)):
    if lista[k-1]==e:
        lista.pop(k-1)
print(lista)
+-