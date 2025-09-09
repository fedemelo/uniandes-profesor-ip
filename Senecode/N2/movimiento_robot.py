def movimiento_robot(orientacion_actual: str, movimiento: str) -> str:
    """ Movimiento robótico
    Parámetros:
      orientacion_actual (str): La orientación actual del robot
      giro (str): La acción a ejecutar a partir de la orientación inicial del robot. Debe ser un valor de
                  los siguientes: {"L","H","R","."}
    Retorno:
      str: La orientación final del robot, debe ser un valor de los siguientes:  {"W","N","S","E"}
    """
    sequence = "NESW"
    index = sequence.find(orientacion_actual)
    
    if movimiento == "R":
        index = (index + 1) % 4
    elif movimiento == "L":
        index = (index - 1) % 4
    elif movimiento == "H":
        index = (index + 2) % 4
    
    return sequence[index]