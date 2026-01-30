from functools import reduce

def movimiento_robot(orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str) -> str:
    return reduce(lambda a, g: a if g == "." else {0: "W", 1: "N", 2: "E", 3: "S"}[({"W": 0, "N": 1, "E": 2, "S": 3}[a] + (-1 if g == "L" else (1 if g == "R" else 2))) % 4], (orientacion_actual, giro_1, giro_2, giro_3))
