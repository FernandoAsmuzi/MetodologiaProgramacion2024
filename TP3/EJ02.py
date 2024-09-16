def insertionSort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [15,8,4,16,9]
print("Lista sin ordenar: ", lista)

print("Lista ordenada con método de inserción: ", insertionSort(lista))
print("Lista ordenada con método de burbuja: ", bubbleSort(lista))