'''''
Cambios realizados por Luis Fernando 
se añade el caso donde el archivo no sea encontrado
al igual que en caso de que el archivo no contenga 
información el promedio automáticamente sea 0
junto a la validación  de calificaciones entre el 
0 y 10.
'''''

def leer_alumnos(archivo):
    alumnos = []
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if linea:
                if ',' in linea:
                    try:
                        nombre, calificacion = linea.split(',')
                        calificacion = int(calificacion)
                        if 0 <= calificacion <= 10:  # Validar que la calificación esté en el rango 0-10
                            alumnos.append((nombre.strip(), calificacion))
                        else:
                            print(f"Calificación fuera de rango (0-10): {calificacion}")
                    except ValueError:
                        print(f"Error al procesar la línea (no es un número válido): {linea}")
                else:
                    print(f"Línea inválida (sin separador ','): {linea}")
            else:
                print("Línea vacía encontrada, omitiendo...")
    return alumnos

def calcular_promedio(alumnos):
    if not alumnos:
        return 0  # Evita división por cero si no hay alumnos
    total_calificaciones = sum(calificacion for _, calificacion in alumnos)
    return total_calificaciones / len(alumnos)

def alumnos_sin_derecho(alumnos):
    # Filtrar los alumnos con calificación menor o igual a 6
    return [nombre for nombre, calificacion in alumnos if calificacion <= 6]

def bubble_sort(alumnos):
    n = len(alumnos)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if alumnos[j][1] > alumnos[j+1][1]:  # Comparar calificaciones
                alumnos[j], alumnos[j+1] = alumnos[j+1], alumnos[j]

# Archivo de texto
archivo = 'alumnos.txt'

try:
    # Leer alumnos y calificaciones desde el archivo
    alumnos = leer_alumnos(archivo)

    if alumnos:
        # Ordenar los alumnos por calificación usando bubble sort
        bubble_sort(alumnos)

        # Mostrar los alumnos sin derecho a calificación
        sin_derecho = alumnos_sin_derecho(alumnos)
        print("Alumnos sin derecho a calificación:", sin_derecho)

        # Calcular el promedio del grupo
        promedio = calcular_promedio(alumnos)
        print(f"Promedio del grupo: {promedio:.2f}")

        # Mostrar la lista de alumnos con sus calificaciones en orden ascendente
        print("Lista de alumnos y calificaciones en orden ascendente:")
        for nombre, calificacion in alumnos:
            print(f"{nombre}: {calificacion}")
    else:
        print("No se encontraron alumnos válidos en el archivo.")
except FileNotFoundError:
    print(f"Error: El archivo '{archivo}' no fue encontrado.")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
