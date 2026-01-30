def despacho_buses (personas_bus: int, personas_estacion: int)->bool:
    """ La estación de Transmilenio
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse
      personas_estacion (int): Número de personas esperando el bus en la estación
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """
    if personas_bus>150:
        x=True
    if personas_estacion-(150-personas_bus)>=50:
        x=True
    else:
        if personas_bus + personas_estacion >150:
            x=True
        else:
            x=False
    return x