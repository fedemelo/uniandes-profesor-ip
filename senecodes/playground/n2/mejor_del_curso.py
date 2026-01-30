from functools import reduce

def mejor_del_curso(estudiante1: dict, estudiante2: dict, estudiante3: dict, estudiante4: dict, estudiante5: dict, curso: str)->str:
    e1, e2, e3, e4, e5, c = estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, curso
    return reduce(lambda e,f: e if e[c]>f[c] or (e[c]==f[c] and e["nombre"].lower()<f["nombre"].lower()) else f, [e1,e2,e3,e4,e5])["nombre"]





estudiante1 = {"nombre": "Juan", "matematicas": 8, "historia": 7, "lengua": 9}
estudiante2 = {"nombre": "aedro", "matematicas": 9, "historia": 8, "lengua": 7}
estudiante3 = {"nombre": "Maria", "matematicas": 7, "historia": 9, "lengua": 8}
estudiante4 = {"nombre": "Jose", "matematicas": 8, "historia": 7, "lengua": 9}
estudiante5 = {"nombre": "Luis", "matematicas": 9, "historia": 8, "lengua": 7}

print(mejor_del_curso(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, "matematicas"))