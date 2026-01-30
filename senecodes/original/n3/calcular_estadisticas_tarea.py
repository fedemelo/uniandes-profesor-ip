# -*- coding: utf-8 -*-

def calcular_estadisticas_tarea(estudiantes_tareas: dict, nombre_tarea: str)->dict:
    """ Estadisticas de las tareas
    Parámetros:
      estudiantes_tareas (dict): Un diccionario de diccionarios con la información de los estudiantes y sus
                                 tareas.
      nombre_tarea (str): El nombre de la tarea para la que se quiere calcular las estadísticas
    Retorno:
      dict: Un diccionario con las llaves "mayor", "mejor", "menor", "peor", "promedio", "cantidad" y "total"
            que representan: la mayor nota,  el nombre del estudiante con la mejor nota, la peor nota, el nombre
            del estudiante con la peor nota, el promedio, la cantidad de estudiantes que hicieron la tarea y el
            valor total que resulta de sumar todas las notas obtenidas en esa tarea.
    """
    answ={"mayor": 0, "mejor": None, "menor": 100, "peor": None,
          "promedio": 0, "cantidad": None, "total": None}
    i=0
    suma=0
    count=0
    lista_estudiantes=list(estudiantes_tareas.keys()) #[Roberto,...]
    lista_dicts_tareas=list(estudiantes_tareas.values()) #[{"Tarea 1":80,...},{}...]
    while i<len(estudiantes_tareas):
        if nombre_tarea in list(lista_dicts_tareas[i].keys()):
            count+=1
            if lista_dicts_tareas[i][nombre_tarea]>answ["mayor"]:
                answ["mayor"]=lista_dicts_tareas[i][nombre_tarea]
                answ["mejor"]=lista_estudiantes[i]
            if lista_dicts_tareas[i][nombre_tarea]<answ["menor"]:
                answ["menor"]=lista_dicts_tareas[i][nombre_tarea]
                answ["peor"]=lista_estudiantes[i]
            suma+=lista_dicts_tareas[i][nombre_tarea]
            answ["total"]=suma
            answ["cantidad"]=count
            answ["promedio"]=suma/count
        i+=1
    return answ

dic={"Roberto": {"Tarea 1": 80, "Tarea 2" : 90}, "Maria": {"Tarea 1": 85, "Tarea 2" : 95}}

calcular_estadisticas_tarea(dic,"Tarea 1") 