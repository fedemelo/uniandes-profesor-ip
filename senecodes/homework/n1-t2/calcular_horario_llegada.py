def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int)->str:
    
    departure_in_seconds = _time_to_seconds(hora_salida, minuto_salida, segundo_salida)
    duration_in_seconds = _time_to_seconds(duracion_horas, duracion_minutos, duracion_segundos)
    arrival_in_seconds = departure_in_seconds + duration_in_seconds

    arrival_hours = arrival_in_seconds // (60 * 60)
    hours_in_24h_format = arrival_hours % 24
    remaining_seconds = arrival_in_seconds % (60 * 60)
    arrival_minutes = remaining_seconds // 60
    arrival_seconds = remaining_seconds % 60

    return f"{hours_in_24h_format}:{arrival_minutes}:{arrival_seconds}"


def _time_to_seconds(hours: int, minutes: int, seconds: int) -> int:
    return hours * 3600 + minutes * 60 + seconds