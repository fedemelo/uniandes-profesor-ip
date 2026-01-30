# -*- coding: utf-8 -*-

def calcular_definitivas(estudiantes: list)->list:
    """ Aproximación de Notas
    Parámetros:
      estudiantes (list): Una lista de diccionarios que representan a los estudiantes que han finalizado el
                          curso, con su nota final sin aproximar.  Cada diccionario tiene las siguientes
                          llaves: "nombre": (str) el nombre del estudiante.  "nota": (float), un float que
                          representa la nota sin aproximar del estudiante.
    Retorno:
      list: La función retorna una lista de diccionarios, con tantos diccionarios como estudiantes había en la
            lista inicial, pero con sus notas aproximadas. El orden de los diccionarios debe ser el mismo de la
            lista de entrada. Cada uno de los diccionarios retornados debe tener las llaves: "nombre" (str) y
            "nota" (float).
    """
    notas_aproximadas=[]
    for diccionario_estudiante in estudiantes:
        if diccionario_estudiante["nota"]>=4.5:
            diccionario_estudiante["nota"]=5.0
        elif diccionario_estudiante["nota"]>=3.5 and diccionario_estudiante["nota"]<4.5:
            diccionario_estudiante["nota"]=4.0
        elif diccionario_estudiante["nota"]>=2.5 and diccionario_estudiante["nota"]<3.5:
            diccionario_estudiante["nota"]=3.0
        else:
            diccionario_estudiante["nota"]=1.5
        notas_aproximadas.append(diccionario_estudiante)
    return notas_aproximadas
        