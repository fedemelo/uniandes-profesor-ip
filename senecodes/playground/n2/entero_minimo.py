def entero_minimo(l: int, r: int, d: int) -> int:
    return d if d < l or d > r else r//d*d + d