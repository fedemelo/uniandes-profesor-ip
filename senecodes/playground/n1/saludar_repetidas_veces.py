def saludar_repetidas_veces(nombre: str, veces: int) -> str:
    return "H%sl%s %s" % ("o" * veces, "a" * (veces//2), nombre)