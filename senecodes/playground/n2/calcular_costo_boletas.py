def calcular_costo_boletas(cantidad_boletas: int, tipo_sala: str, hora_pico: bool, pago_tarjeta_cinema: bool, reserva: bool) -> int:
    basic = 15500 if tipo_sala == "3D" else 11300 if tipo_sala == "2D" else 18800
    basic *= cantidad_boletas
    discount = 0
    if hora_pico:
        discount -= 0.5*basic if tipo_sala == "Dinamix" else 0.25*basic
    else:
        discount += 0.1*basic
        discount += cantidad_boletas*500 if cantidad_boletas > 2 else 0
    discount += 0.05*basic if pago_tarjeta_cinema else 0
    discount -= 2000*cantidad_boletas if reserva else 0
    return round(basic - discount)