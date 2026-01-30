# Without filter

from itertools import takewhile as tw

def encontrar_primer_par(numeros: list) -> int:
    return None if len(list(tw(lambda x: x%2 != 0, numeros))) == len(numeros) else numeros[len(list(tw(lambda x: x%2 != 0, numeros)))]


# With filter
def encontrar_primer_par(numeros: list) -> int:
    return None if len(numeros) == 0 else next(filter(lambda x: x % 2 == 0, numeros))