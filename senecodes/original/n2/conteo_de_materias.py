# -*- coding: utf-8 -*-

def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str)->int:
    """ Materias favoritas
    Parámetros:
      nombre_materia_1 (str): El nombre de la primera de las tres materias
      nombre_materia_2 (str): El nombre de la segunda materia
      nombre_materia_3 (str): El nombre de la tercera materia
    Retorno:
      int: Retorna el número de materias que cumplen con ser del agrado de Pedro.
    """
    count=0
    if "programacion" in nombre_materia_1 \
    or "matematica" in nombre_materia_1\
    or "filosofia" in nombre_materia_1\
    or "literatura" in nombre_materia_1:
        count+=1
    if "programacion" in nombre_materia_2 \
    or "matematica" in nombre_materia_2\
    or "filosofia" in nombre_materia_2\
    or "literatura" in nombre_materia_2:
        count+=1
    if "programacion" in nombre_materia_3 \
    or "matematica" in nombre_materia_3\
    or "filosofia" in nombre_materia_3\
    or "literatura" in nombre_materia_3:
        count+=1
    return count
    

