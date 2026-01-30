def eliminar_vocales(cadena: str) -> str:
    return "".join(filter(lambda x: x not in 'aeiouAEIOU', cadena))
