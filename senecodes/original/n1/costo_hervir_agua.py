def costo_hervir_agua(masa_agua: float)->float:
    """ Costo de hervir agua
    Parámetros:
      masa_agua (float): Masa de agua a hervir
    Retorno:
      float: Valor en dólares de hervir la masa de agua dada como parámetro redondeado con 4 decimales
    """
    return round((0.089*((((masa_agua)*(4.186)*(80))/3600)/1000)),4)

