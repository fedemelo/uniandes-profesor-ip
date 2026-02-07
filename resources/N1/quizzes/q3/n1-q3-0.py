def convertir_milisegundos(milisegundos_totales: int) -> str:
    milisegundos_en_una_hora = 1000 * 60 * 60
    horas = milisegundos_totales // milisegundos_en_una_hora
    milisegundos_restantes = milisegundos_totales % milisegundos_en_una_hora

    milisegundos_en_un_minuto = 1000 * 60
    minutos = milisegundos_restantes // milisegundos_en_un_minuto
    milisegundos_restantes = milisegundos_restantes % milisegundos_en_un_minuto

    milisegundos_en_un_segundo = 1000
    segundos = milisegundos_restantes // milisegundos_en_un_segundo
    milisegundos = milisegundos_restantes % milisegundos_en_un_segundo

    return f"{horas} h, {minutos} min, {segundos} s y {milisegundos} ms"

assert convertir_milisegundos(3_723_004) == "1 h, 2 min, 3 s y 4 ms"