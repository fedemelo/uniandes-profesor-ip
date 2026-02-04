def fecha_desde_horas(horas: int) -> str:
    """
    Recibe un número de horas transcurridas desde el 1 de enero a las 00:00
    y retorna una cadena con el formato "dd/mm" de la fecha correspondiente,
    suponiendo que cada mes tiene 30 días.
    """
    dias_completos = horas // 24
    mes = (dias_completos // 30) % 12 + 1
    dia_del_mes = dias_completos % 30 + 1
    return f"{dia_del_mes}/{mes}"


def fecha_desde_segundos(segundos: int) -> str:
    """
    Recibe un número de segundos transcurridos desde el 1 de enero a las 00:00
    y retorna una cadena con el formato "dd/mm" de la fecha correspondiente,
    suponiendo que cada mes tiene 30 días.
    """
    horas = segundos // 3600
    return fecha_desde_horas(horas)
