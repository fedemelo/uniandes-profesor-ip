def calcular_mediana(a: int, b: int, c: int)->int:
    """ Mediana
    Parámetros:
      a (int): El primer entero del conjunto de datos
      b (int): El segundo entero del conjunto de datos
      c (int): El tercer entero del conjunto de datos
    Retorno:
      int: La mediana de los 3 enteros
    """
    z=max(a,b,c)
    x=min(a,b,c)
    y=(a+b+c)-(z+x)
    return y



