def es_primo(numero: int) -> bool:
    return not bool(sum(map(lambda x: 1 if numero % x == 0 else 0, range(2, numero))))

# Implementación más natural con filter (Senecode no permite su uso)
def es_primo(numero: int) -> bool:
    return bool(filter(lambda x: numero % x == 0, range(2, numero)))