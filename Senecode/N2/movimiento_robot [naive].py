def movimiento_robot(orientacion_actual: str, movimiento: str) -> str:
    """ Movimiento robótico
    Parámetros:
      orientacion_actual (str): La orientación actual del robot
      giro (str): La acción a ejecutar a partir de la orientación inicial del robot. Debe ser un valor de
                  los siguientes: {"L","H","R","."}
    Retorno:
      str: La orientación final del robot, debe ser un valor de los siguientes:  {"W","N","S","E"}
    """
    if orientacion_actual == "N":
        if movimiento == "R":
            answ = "E"
        elif movimiento == "L":
            answ = "W"
        elif movimiento == "H":
            answ = "S"
        else: 
            answ = "N"

    elif orientacion_actual == "S":
        if movimiento == "R":
            answ = "W"
        elif movimiento == "L":
            answ = "E"
        elif movimiento == "H":
            answ = "N"
        else: 
            answ = "S"

    elif orientacion_actual == "E":
        if movimiento == "R":
            answ = "S"
        elif movimiento == "L":
            answ = "N"
        elif movimiento == "H":
            answ = "W"
        else: 
            answ = "E"

    else:
        if movimiento == "R":
            answ = "N"
        elif movimiento == "L":
            answ = "S"
        elif movimiento == "H":
            answ = "E"
        else: 
            answ = "W"

    return answ