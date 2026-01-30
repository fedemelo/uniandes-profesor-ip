def area_poligono_regular(num_lados: int, longitud: float)->float:
    import math
    n=float(num_lados)
    s=longitud
    area=(n*(s**2))/(4*((math.tan(math.pi/n))))
    area=round(area,2)
    return(area)

