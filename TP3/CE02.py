#ordenacion burbuja
def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


lista = [5, 2, 9, 10, 1, 11, 19, 25, 50]

print("Lista sin ordenar: ", lista)

print("Lista ordenada por método burbuja: ", bubbleSort(lista))