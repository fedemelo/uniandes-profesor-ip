def es_bisiesto(anio: int) -> bool:
    return anio % 400 == 0 if anio % 100 == 0 else anio % 4 == 0