# Ejercicio 4 - TP03 - Metodología de la programación

def selectionSort(participantes, op):
    for i in range(len(participantes)):
        aux = i
        for posAnteriores in range(i+1, len(participantes)):
            if op == 1:
                if participantes[aux][2] > participantes[posAnteriores][2]:
                    aux = posAnteriores
            else:
                if participantes[aux][2] < participantes[posAnteriores][2]:
                    aux = posAnteriores
        participantes[i], participantes[aux] = participantes[aux], participantes[i]
    return participantes


def ordenarParticipantes(participantes):
    op = int(input("Ordenar por poder: 1-Ascendente 2-Descendente: "))
    if op == 1:
        participantes = selectionSort(participantes, op)
        print(participantes)
    else:
        participantes = selectionSort(participantes, op)
        print(participantes)
    
#     c. Ordenar la lista de participantes en forma descendente por Transformación mostrando solamente
# los participantes que nivel de poder superior a 9000 utilizando el método de inserción.

def filtroParticipantes(participantes):
    listaFuertes=[]
    for i in range(len(participantes)):
        if participantes[i][2]>9000:
            listaFuertes.append(participantes[i])
    return listaFuertes         


def ordenarPorTransformaciones(listaFuertes):
    for i in range(1, len(listaFuertes)):
        elemento_actual = listaFuertes[i]
        posicion_anterior = i - 1
        while posicion_anterior >= 0 and elemento_actual[1] > listaFuertes[posicion_anterior][1]:
            listaFuertes[posicion_anterior + 1] = listaFuertes[posicion_anterior]
            posicion_anterior -= 1
        listaFuertes[posicion_anterior + 1] = elemento_actual
    return listaFuertes      


def mostrarPorTransformacion(listaFuertes):
    print("---se va a ordenar la lista de participantes por transformacion---")
    listaTransformaciones=ordenarPorTransformaciones(listaFuertes)
    print(listaTransformaciones)





# Principal

participantes = [["Goku","Kaioken", 10001], ["Vegeta","Super Saiyajin", 8900], ["Gohan", "Beast",12000],
["Piccolo", "Namekiano",7000], ["Freezer","Black", 9500]]

ordenarParticipantes(participantes)
listaFuertes=filtroParticipantes(participantes)
mostrarPorTransformacion(listaFuertes)
