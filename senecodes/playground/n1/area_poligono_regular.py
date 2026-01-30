from math import pi, tan

def area_poligono_regular(num_lados: int, longitud: float)->float:
    return round(num_lados * longitud ** 2 / (4 * tan(pi / num_lados)), 2)