def sumatoria_k2(n: int) -> float:
    return round(sum(map(lambda k: k/2**k, range(1, n+1))), 2)