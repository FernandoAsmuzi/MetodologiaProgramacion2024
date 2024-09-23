from io import open

alumnos = {}

with open('/CE/alumnos.txt', 'r', encoding='utf-8') as fichero:
    for i, linea in enumerate(fichero):
        # Dividir la línea en partes usando ';' como separador
        partes = linea.strip().split(';')
        
        # Asumimos que las partes son: nombre, edad, grado, etc.
        if len(partes) >= 3:  # Asegurarse de que hay al menos 3 partes
            alumnos[i] = {
                'nombre': partes[0],
                'edad': partes[1],
                'grado': partes[2]
                # Agregar más campos según sea necesario
            }
        
    print("Contenido leído y guardado en el diccionario correctamente.")
    
    # Imprimir el contenido del diccionario
    print("Contenido del diccionario:")
    for clave, valor in alumnos.items():
        print(f"{clave}: {valor}")