# Procedimental

def encontrar_mejor_puntaje_equipo(salon: list, m: int)->int:
    grupos = [0]*(m+1)
    for fila in range(len(salon)):
        for columna in range(len(salon[fila])):
            grupo = columna // (len(salon) // m)
            grupos[grupo] += salon[fila][columna]
    return max(grupos)

salon = [[1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 2, 1, 1],
         [1, 1, 1, 2, 1, 1],
         [1, 1, 1, 1, 2, 1],
         [1, 1, 1, 1, 1, 1]]

print(encontrar_mejor_puntaje_equipo(salon, 3))

# Pasito a pasito, suave suavecito

def encontrar_mejor_puntaje_equipo(salon: list, m: int)->int:
    # Hay m equipos y queremos contar los ejercicios resueltos por equipo.
    # Para ello, creamos un diccionario con m claves, una por cada equipo.
    # El valor de cada clave es la cantidad de ejercicios resueltos por el equipo.
    equipos = {}
    for i in range(1, m+1):
        equipos["Equipo "+str(i)] = 0
    # El diccionario se ve así: {"Equipo 1": 0, "Equipo 2": 0,...,"Equipo m": 0}

    # N: Número de filas
    N = len(salon)
    M = m

    # Ahora: los estudiantes del grupo k están sentados entre la columna (k-1)*(N/M) y la columna k*(N/M)-1.
    # Eso satisface el enunciado: si k=1 (grupo 1), entonces están sentados entre la columna 0 y la columna N/M-1.
    # Si k=2 (grupo 2), entonces están sentados entre la columna N/M y la columna 2*N/M-1.
    for fila in range(len(salon)):
        for columna in range(len(salon[fila])):
            # Acá reviso, para cada equipo, si la columna en la que está sentado el estudiante pertenece a ese equipo.
            # Miro si está dentro del rango, con la fórmula explicada antes
            for num_equipo in range(1, m+1):
                if (num_equipo-1)*(N/M) <= columna <= num_equipo*(N/M)-1:
                    equipos["Equipo "+str(num_equipo)] += salon[fila][columna]

    # Ahora, el diccionario equipos tiene la cantidad de ejercicios resueltos por cada equipo.
    # Buscamos qué equipo tiene el máximo puntaje.
    maximo = 0
    for equipo in equipos:
        if equipos[equipo] > maximo:
            maximo = equipos[equipo]
    return maximo


salon = [[1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 2, 1, 1],
         [1, 1, 1, 2, 1, 1],
         [1, 1, 1, 1, 2, 1],
         [1, 1, 1, 1, 1, 1]]

print(encontrar_mejor_puntaje_equipo(salon, 3))