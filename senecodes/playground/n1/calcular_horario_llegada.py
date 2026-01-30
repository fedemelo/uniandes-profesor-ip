def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int)->str:
    h, m, s = hora_salida + duracion_horas, minuto_salida + duracion_minutos, segundo_salida + duracion_segundos
    return "%i:%i:%i" % ((h + m//60) % 24, (m + s//60) % 60, s%60)