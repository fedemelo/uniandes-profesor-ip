def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int) -> str:
    birth_in_days = _date_to_days(dia_nacio, mes_nacio, anio_nacio)
    current_in_days = _date_to_days(dia_actual, mes_actual, anio_actual)

    total_days = current_in_days - birth_in_days
    years = total_days // 360
    remaining_days = total_days % 360
    months = remaining_days // 30
    days = remaining_days % 30
    return f"{years},{months},{days}"
    
def _date_to_days(day: int, month: int, year: int) -> int:
    return day + month * 30 + year * 360
