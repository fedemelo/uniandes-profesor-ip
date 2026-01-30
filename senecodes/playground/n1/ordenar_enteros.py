def ordenar_enteros(a: int, b: int, c: int) -> str:
    return "%i,%i,%i" % tuple(sorted([a, b, c], reverse=1))