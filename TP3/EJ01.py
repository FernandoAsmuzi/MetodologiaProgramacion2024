def selectionSort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista


lista = [29,10,14,37,13]
print("Lista sin ordenar: ", lista)

print("Lista ordenada con método de selección: ", selectionSort(lista))