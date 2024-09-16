import os
def presionarTecla():
    input("Presione una tecla para continuar...")

def menu(op):
    os.system('cls')
    print("----------Bienvenido----------")
    print("Seleccione una opción")
    print("1- Registrar alumnos")
    print("2- Mostrar listado de alumnos")
    print("3- Buscar alumno por DNI")
    print("4- Ordenar listado de alumnos")
    print("5- Salir")
    op = int(input())
    return op

def leerNota():
    nota = float(input("Ingrese nota: "))
    while not(nota >= 0 and nota <= 10):
        print("Nota no válida...")
        nota = float(input("Ingrese nota: "))
    return nota

def registrarAlumnos():
    listado = []
    dni = 1
    while dni != 0:
        dni = int(input("Ingrese DNI: "))
        if dni != 0:
            nombre = input("Ingrese nombre: ")
            nota = leerNota()
            listado.append([dni, nombre, nota])
    return listado

def mostrarListado(listado):
    print("DNI\tNombre\tNota")
    for i in range(len(listado)):
        print(listado[i][0], "\t", listado[i][1], "\t", listado[i][2])
    presionarTecla()

def buscarAlumno(listado):
    dni = int(input("Ingrese DNI: "))
    for i in range(len(listado)):
        if listado[i][0] == dni:
            print("DNI\tNombre\tNota")
            print(listado[i][0], "\t", listado[i][1], "\t", listado[i][2])
            presionarTecla()
            return
    print("Alumno no encontrado...")
    presionarTecla()

def ordenarListado(listado):
    listado.sort(key = lambda x: x[1])
    mostrarListado(listado)

#Principal
print("Bienvenido al sistema de alumnos")
listado = []
op = 0
while op != 5:
    op = menu(op)
    if op == 1:
        listado = registrarAlumnos()
    elif op == 2:
        mostrarListado(listado)
    elif op == 3:
        buscarAlumno(listado)
    elif op == 4:
        ordenarListado(listado)
    elif op == 5:
        print("Hasta luego...")
    else:
        print("Opción no válida...")         

