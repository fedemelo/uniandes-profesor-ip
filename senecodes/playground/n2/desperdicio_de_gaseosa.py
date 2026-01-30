def desperdicio_de_gaseosa(amigo_1: dict, amigo_2: dict, amigo_3: dict, capacidad_boton: float) ->  str:
    a1, a2, a3 = amigo_1, amigo_2, amigo_3
    riega = lambda x: x["capacidad_actual"] + capacidad_boton > x["capacidad_vaso"]
    return a1["nombre"] if riega(a1) else a2["nombre"] if riega(a2) else a3["nombre"] if riega(a3) else None