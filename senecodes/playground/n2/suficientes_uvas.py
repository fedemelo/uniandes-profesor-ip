def suficientes_uvas(cantidad_ivan: int, cantidad_nicolas: int, cantidad_adriana: int, cantidad_verde: int, cantidad_morada: int, cantidad_negra: int)->str:
    ivan, nico, adri, verdes, moradas, negras = cantidad_ivan, cantidad_nicolas, cantidad_adriana, cantidad_verde, cantidad_morada, cantidad_negra
    uvas_nico = verdes + moradas

    ninguno_puede_comer = verdes < ivan  and  uvas_nico < nico  and  uvas_nico + negras < adri
    todos_pueden_comer = verdes >= ivan  and  uvas_nico-ivan >= nico  and  uvas_nico-nico-ivan + negras >= adri
    ivan_y_alguien = verdes >= ivan  and  (uvas_nico-ivan >= nico  or  uvas_nico-ivan + negras >= adri)
    nico_y_adri = uvas_nico >= nico  and  uvas_nico-nico + negras >= adri

    if ninguno_puede_comer:
        return "al menos somos amigos"
    elif todos_pueden_comer:
        return "felices"
    elif ivan_y_alguien or nico_y_adri:  # Dos pueden comer
        return "casi"
    else:  # Solo uno puede comer
        return "fallamos"