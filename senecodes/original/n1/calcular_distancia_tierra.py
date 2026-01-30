def calcular_distancia_tierra(t1: float, g1: float, t2: float, g2: float)->float:
    """ Distancia entre dos puntos en la Tierra
    Parámetros:
      t1 (float): Latitud del primer punto en la Tierra
      g1 (float): Longitud del primero punto en la Tierra
      t2 (float): Latitud del segundo punto en la Tierra
      g2 (float): Longitud del segundo punto en la Tierra
    Retorno:
      float: Distancia entre dos puntos en la Tierra a dos cifras decimales.
    """
    import math
    return round(((6371.01)*(math.acos(((math.sin(math.radians(t1)))*(math.sin(math.radians(t2))))+((math.cos(math.radians(t1)))*(math.cos(math.radians(t2)))*(math.cos(math.radians(g1-g2))))))),2)