def buscar_iguales_consecutivos(lista: list[int]) -> int:
    # En este ejercicio toca recorrerlo al revés para poder hacerlo como recorrido parcial
    i = len(lista) - 1  
    encontrado = False  # Uso centinela! recorrido parcial
    while i > 0 and not encontrado:  # > 0 y no >= 0 porque vamos a comparar con el anterior
        if lista[i] == lista[i - 1]:
            encontrado = True
        i -= 1

    respuesta = -1
    if encontrado:
        # Cuando el centinela para el ciclo, igual se resta uno más. Entonces 
        # toca esa i y la siguiente, que es i + 1
        respuesta = i + (i + 1)
    return respuesta


def contar_apariciones_sublista(lista: list[int], sublista: list[int]) -> int:
    conteo = 0
    i = 0  # Recorre la lista grande
    j = 0  # Recorre la sublista
    while i < len(lista):
        if lista[i] == sublista[j]:
            j += 1
            if j == len(sublista):
                conteo += 1
                j = 0
        else:
            # Acá, uno se acaba de dar cuenta que la sublista que estaba revisando no está contenida
            # entonces retrocede en la lista grande lo que alcanzó a avanzar comparando con la sublista
            # para poder volver empezar a comparar en la siguiente posición en la siguiente iteración.
            i -= j  
            j = 0
        i += 1
    return conteo


def mejor_estudiante_por_materia(estudiantes: list[dict], materia: str) -> str:
    mejor = estudiantes[0]
    i = 1
    while i < len(estudiantes):
        estudiante = estudiantes[i]
        # Desempato: o la nota es mayor, o la nota es igual pero el nombre es mayor
        if estudiante[materia] > mejor[materia] or (estudiante[materia] == mejor[materia] and estudiante["nombre"] > mejor["nombre"]):
            mejor = estudiante
        i += 1
    return mejor["codigo"]
