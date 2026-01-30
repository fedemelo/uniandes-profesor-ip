def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int) -> int:
    return round((tamanio_archivo / (velocidad / 8000)) / 60)