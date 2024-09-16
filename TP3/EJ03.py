import random

def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def generarNumeros(lst):
    for i in range(len(lst)):
        lst[i] = random.randint(1, 100)
    bubbleSort(lst)
    return lst

def fusionarListas(lst1, lst2):
    lst3 = lst1 + lst2
    bubbleSort(lst3)
    return lst3

len1, len2 = random.randint(5, 10), random.randint(5, 10)
lista1 = [0] * len1
lista2 = [0] * len2

lista3 = fusionarListas(generarNumeros(lista1), generarNumeros(lista2))

print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista fusionada: ", lista3)


