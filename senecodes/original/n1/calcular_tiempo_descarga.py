def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int)->int:
    TMb=tamanio_archivo*8000
    ts=TMb/velocidad
    tmin=ts/60
    return round(tmin)



