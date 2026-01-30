def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int)->str:
    """ Hora de llegada de vuelo
    Parámetros:
      hora_salida (int): Hora de salida del vuelo (valor entre 0 y 23)
      minuto_salida (int): Minuto de salida del vuelo (valor entre 0 y 59)
      segundo_salida (int): Segundo de salida del vuelo (valor entre 0 y 59)
      duracion_horas (int): Número de horas que dura el vuelo
      duracion_minutos (int): Número de minutos (adicionales al número de horas) que dura el vuelo
      duracion_segundos (int): Número de segundos (adicionales al número de horas y minutos) que dura el
                               vuelo
    Retorno:
      str: Cadena que indica la hora de llegada del vuelo a su destino, la cadena debe estar con el formato
           “HH:mm:ss”.
    """
    hss=hora_salida*3600
    mss=minuto_salida*60
    ss=segundo_salida+mss+hss
    hds=duracion_horas*3600
    mds=duracion_minutos*60
    ds=duracion_segundos+mds+hds
    lls=ss+ds
    llh=lls//3600
    ps=lls%3600
    llm=ps//60
    lls=ps%60
    rd=llh//24
    h=llh-rd*24
    return str(h)+":"+str(llm)+":"+str(lls)


    
