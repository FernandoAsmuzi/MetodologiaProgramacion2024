import os

#PRESIONAR TECLA
def presionarTecla():
    input("Presione una tecla para continuar...")


#MENU DE OPCIONES
def menu():
    print("**********BIENVENIDO**********")
    print(
    "Seleccione una opción: \n1. REGISTRAR MAQUINARIA/HERRAMIENTA \n2. MOSTRAR MAQUINARIA/HERRAMIENTAS DISPONIBLES PARA ALQUILER \
        \n3. ORDENAR HERRAMIENTAS POR PRECIO DE ALQUILER \n4. REALIZAR PRESUPUESTO \n5. ACTUALIZAR PRECIOS \n6. SALIR"
    )
    op = int(input())
    return op


#REGISTRO DE MAQUINARIA
def registrarMaquinaria():
    os.system('cls')
    band = False
    nombre = input("Ingrese el nombre de la maquinaria/herramienta: ")
    while not band:
        os.system('cls')
        tipo = input("Ingrese el tipo de maquinaria/herramienta (solo letra inicial): \n M- Maquina \n H- Herramienta \n P- Máquina pesada \n")
        if(tipo == "M" or tipo == "m"):
            tipo = "Máquina"
            band = True
        elif(tipo == "H" or tipo == "h"):
            tipo = "Herramienta"
            band = True
        elif(tipo == "P" or tipo == "p"):
            tipo = "Máquina pesada"
            band = True
        else:
            print("Tipo inválido")
            presionarTecla()
    precio = float(input("Ingrese el precio de alquiler: ")) 
    band = False
    while not band:
        os.system('cls')
        disponible = input("¿Está disponible para alquiler? (S/N): ")
        if(disponible == "S" or disponible == "s"):
            disponible = True
            band = True
        elif(disponible == "N" or disponible == "n"):
            disponible = False
            band = True
        else:
            print("Opción inválida")
            presionarTecla()
    maquinasHerramientas.append([nombre, tipo, precio, disponible])


#MOSTRAR MAQUINARIA/HERRAMIENTA DISPONIBLE PARA ALQUILER
def mostrarMaquinariaParaAlquiler():
    os.system('cls')
    print("DISPONIBLES PARA ALQUILER: ")
    for i in range(len(maquinasHerramientas)):
        if maquinasHerramientas[i][3]:
            print("**********************************************************")
            print("Nombre: ", maquinasHerramientas[i][0])
            print("Tipo: ", maquinasHerramientas[i][1])
            print("Precio de alquiler: ", maquinasHerramientas[i][2])
    print("**********************************************************")

#MOSTRAR HERRAMIENTAS ORDENADAS
def mostrarHerramientas(lst):
    for i in range(len(lst)):
        if lst[i][1] == "Herramienta":
            print("**********************************************************")
            print("Nombre: ", lst[i][0])
            print("Tipo: ", lst[i][1])
            print("Precio de alquiler: ", lst[i][2])
            print("Disponible: ", lst[i][3])
    print("**********************************************************")
#ORDENAR HERRAMIENTAS POR PRECIO DE ALQUILER
def ordenarPorPrecio(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            tmp = lst[i]
            j = i
            while j >= gap and lst[j - gap][2] > tmp[2]:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = tmp
        gap = gap // 2
    mostrarHerramientas(lst)
    print("HERRAMIENTAS ORDENADAS POR PRECIO DE ALQUILER: ")

#REALIZAR PRESUPUESTO
def realizarPresupuesto():
    mostrarMaquinariaParaAlquiler()
    maquina = input("Ingrese el nombre de la maquinaria/herramienta que desea alquilar: ")
    dias = int(input("Ingrese la cantidad de días que desea alquilar la maquinaria/herramienta: "))
    for i in range(len(maquinasHerramientas)):
        if maquinasHerramientas[i][0] == maquina:
            precio = maquinasHerramientas[i][2] * dias
            print("El precio total por alquilar la maquinaria/herramienta ", maquina, " por ", dias, " días es de: ", precio)
            op = input("¿Desea realizar el alquiler? (S/N): ")
            if(op == "S" or op == "s"):
                maquinasHerramientas[i][3] = False
                print("Alquiler realizado con éxito")
                return
            else:
                print("Alquiler cancelado")
                return
    
    print("Maquinaria/herramienta no encontrada")

#ACTUALIZAR PRECIOS
def actualizarPrecios(lst):
    porcentaje = float(input("Ingrese el porcentaje de aumento: (0.1 - 0.9): "))
    if porcentaje < 0.1 or porcentaje > 0.9:
        print("Porcentaje inválido")
    else:
        for i in range(len(lst)):
            lst[i][2] = lst[i][2] + (lst[i][2] * porcentaje)
        print("Precios actualizados con éxito")
        for i in range(len(lst)):
            print("---------------------------------------------")
            print("Nombre: ", lst[i][0], " Precio: ", lst[i][2], " Disponible: ", lst[i][3])
        print("---------------------------------------------")
        sumar(lst, 0)
        sumar(lst, 1)
    return lst
#SUMAR PRECIOS
def sumar(lst, tipo):
    suma = 0
    for i in range(len(lst)):
        if lst[i][3] and tipo == 0:
            suma += lst[i][2]
        elif not lst[i][3] and tipo == 1:
            suma += lst[i][2]
    if tipo == 0:
        print("La suma actualizada de los precios de productos disponibles es de: ", suma)
    elif tipo == 1:
        print("La suma actualizada de los precios de productos no disponibles es de: ", suma)

# PRINCIPAL
os.system('cls')
maquinasHerramientas = [["Taladro", "Herramienta", 150.0, True], 
                        ["Excavadora", "Máquina pesada", 200.0, False],
                        ["Generador eléctrico", "Máquina", 50.0, True], 
                        ["Sierra circular", "Herramienta", 25.0, True], 
                        ["Cortadora de césped", "Máquina", 30.0, True], 
                        ["Compactadora","Máquina pesada", 150.0, False], 
                        ["Amoladora", "Herramienta", 20.0, True], 
                        ["Pistola de pintura", "Herramienta", 40.0, False], 
                        ["Retroexcavadora", "Máquina pesada", 250.0, True]]

opcion = menu()

while(opcion != 6):
    
    if(opcion == 1):
        registrarMaquinaria()
        presionarTecla()
    elif(opcion == 2):
        mostrarMaquinariaParaAlquiler()
        presionarTecla()
    elif(opcion == 3):
        ordenarPorPrecio(maquinasHerramientas)
        presionarTecla()
    elif(opcion == 4):
        realizarPresupuesto()
        presionarTecla()
    elif(opcion == 5):
        maquinasHerramientas = actualizarPrecios(maquinasHerramientas)
        presionarTecla()
    else:
        print("Opción inválida")
        presionarTecla()
    os.system('cls')
    opcion = menu()

print("Saliendo...")