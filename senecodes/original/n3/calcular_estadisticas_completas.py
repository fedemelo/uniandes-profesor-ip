# -*- coding: utf-8 -*-

def nombres_tareas(estudiantes_tareas: dict)->list:
    i=0
    lista_nombres_tareas=[]
    lista_dicts_tareas=list(estudiantes_tareas.values())
    while i<len(lista_dicts_tareas):
        for nombre_tarea in list(lista_dicts_tareas[i].keys()):
            if nombre_tarea not in lista_nombres_tareas:
                lista_nombres_tareas.append(nombre_tarea)
        i+=1
    return lista_nombres_tareas

def calcular_estadisticas_tarea(estudiantes_tareas: dict, nombre_tarea: str)->dict:
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
        
def calcular_estadisticas_completas(estudiantes_tareas: dict)->dict:
    answ={}
    i=0
    lista_nombres_tareas=nombres_tareas(estudiantes_tareas)
    while i<len(lista_nombres_tareas):
        estadisticas_tarea=calcular_estadisticas_tarea(estudiantes_tareas,lista_nombres_tareas[i])
        answ[lista_nombres_tareas[i]]=estadisticas_tarea
        i+=1
    return answ

dic={"Roberto": {"Tarea 1": 80, "Tarea 2" : 90}, "Maria": {"Tarea 4": 85, "Tarea 3" : 95}}
    
calcular_estadisticas_completas(dic)