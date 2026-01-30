def vel_en_caida_libre(altura: float)->float:
    """ Caída libre
    Parámetros:
      altura (float): Altura desde la cual cae el objeto
    Retorno:
      float: Velocidad del objeto al tocar el suelo tras la caída libre, la velocidad debe estar redondeada a dos
             cifras decimales.
    """
    return round(float((((2)*(9.8)*(altura))**(1/2))), 2)


