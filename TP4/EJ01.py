import random

def sort(lista):
    lista.sort()
    return lista

def quicksort(lst,start,stop):
    if stop - start > 0:        
        pivot, left, right = lst[start], start, stop        
        while left <= right:            
            while lst[left] < pivot:                
                left += 1            
            while lst[right] > pivot:                
                right -= 1            
            if left <= right:                
                lst[left], lst[right] = lst[right], lst[left]                
                left += 1                
                right -= 1        
        quicksort(lst, start, right)        
        quicksort(lst, left, stop)    
    return lst

def shell(lista):
    n = len(lista)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = temp
        intervalo //= 2
    return lista

def cargarLista():
    n = int (input("Ingrese la cantidad de elementos de la lista: "))
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 100))
    print("Lista: ", lista)
    return lista


#PRINCIPAL
lista = cargarLista()
op = int(input("Seleccione metodo de ordenación: \n1. Sort\n2. QuickSort\n3. Shell\n4. Salir\n"))

if (op == 1):
    print("Sort")
    print("Lista ordenada: ", sort(lista))
elif (op == 2):
    print("QuickSort")
    print("Lista ordenada: ", quicksort(lista, 0, len(lista)-1))
elif (op == 3):
    print("Shell")
    print("Lista ordenada: ", shell(lista))
else:  
    print("Saliendo...")