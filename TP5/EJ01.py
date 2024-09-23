from io import open
import os

def presionarTecla():
    input('Presione una tecla para continuar...')

def leerArchivo(path):
    lista = []
    fichero = open(path, 'r', encoding='utf-8')
    lineas = fichero.readlines()
    fichero.close()

    for linea in lineas:
        linea = linea.strip()
        aux = linea.split(';')
        lista.append(aux)

    return lista

def mostrarLibro(libro):
    print('**********************************')
    print(f'ID: {libro[0]}')
    print(f'Titulo: {libro[1]}')
    print(f'Autor: {libro[2]}')
    print(f'Genero: {libro[3]}')
    print(f'Año: {libro[4]}')
    print(f'Precio: {libro[5]}')
    print(f'Estado: {libro[6]}')
    print('**********************************')

def ordenarTitulo(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lst[j][1] > lst[j+1][1]:
                # Intercambiar elementos
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

def buscarPorTitulo(lst):
    if lst == []:
        print('No hay libros cargados')
        return
    else:
        lst = ordenarTitulo(lst)
        titulo = input('Ingrese el titulo del libro: ')

        izq = 0
        der = len(lst) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if lst[medio][1].lower() == titulo.lower():
                mostrarLibro(lst[medio])
                return
            elif lst[medio][1].lower() < titulo.lower():
                izq = medio + 1
            else:
                der = medio - 1
        
    print('Libro no encontrado')

def buscarporGenero(lst):
    if lst == []:
        print('No hay libros cargados')
        return
    else:
        genero = input('Ingrese el genero del libro: ')
        for libro in lst:
            if genero.lower() in libro[3].lower():
                mostrarLibro(libro)
    print('Libro no encontrado')


#principal

path = r'C:\Users\fer_a\OneDrive\Escritorio\ING. INF. 2024\MetodologiaProgramacion2024\TP5\libros.txt'
op = 0
libros = []

while op != 7:
    os.system('cls')
    print('1. Leer archivo')
    print('2. Buscar libro por título')
    print('3. Buscar libro por género')
    print('4. Listar por autor')
    print('5. Listar por precio')
    print('6. Modificar precio')
    print('7. Salir')
    op = int(input('Ingrese una opcion: '))

    if op == 1:
        libros = leerArchivo(path)
        presionarTecla()
    elif op == 2:
        buscarPorTitulo(libros)
        presionarTecla()
    elif op == 3:
        buscarporGenero(libros)
        presionarTecla()
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        pass
    elif op == 7:
        print('Fin del programa')
    else:
        print('Opcion incorrecta')