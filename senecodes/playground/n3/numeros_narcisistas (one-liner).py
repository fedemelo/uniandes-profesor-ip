def numeros_narcisistas(n: int) -> bool:
    return n == sum(map(lambda x: int(x)**len(str(n)), str(n)))