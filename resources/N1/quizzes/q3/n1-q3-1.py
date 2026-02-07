def convertir_segundos(segundos_totales: int) -> str:
    segundos_en_un_dia = 60 * 60 * 24
    dias = segundos_totales // segundos_en_un_dia
    segundos_restantes = segundos_totales % segundos_en_un_dia

    segundos_en_una_hora = 60 * 60
    horas = segundos_restantes // segundos_en_una_hora
    segundos_restantes = segundos_restantes % segundos_en_una_hora

    segundos_en_un_minuto = 60
    minutos = segundos_restantes // segundos_en_un_minuto
    segundos = segundos_restantes % segundos_en_un_minuto

    return f"{dias} día(s), {horas} h, {minutos} min y {segundos} s"

assert convertir_segundos(93_784) == "1 día(s), 2 h, 3 min y 4 s"