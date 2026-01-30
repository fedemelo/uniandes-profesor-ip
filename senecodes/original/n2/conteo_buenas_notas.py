# -*- coding: utf-8 -*-

def conteo_buenas_notas(notas: dict)->int:
    """ Materias Excepcionales
    Parámetros:
      notas (dict): Diccionario con las notas del estudiante
    Retorno:
      int: Número de materias excepcionales
    """
    pass
    count=0
    if notas["Matematica"]>4:
        count+=1
    if notas["Ingles"]>4:
        count+=1
    if notas["Sociales"]>4:
        count+=1
    if notas["Ciencias"]>4:
        count+=1
    if notas["Deportes"]>4:
        count+=1
    return count
        
    