# With factorial

from math import factorial

def seno(x: float) -> float:
    return round(sum(map(lambda n: (-1)**n * x**(2*n+1)/factorial(2*n + 1), range(5))), 5)


# Without factorial

from functools import reduce

def seno(x: float) -> float:
    return round(sum(map(lambda n: (-1)**n * x**(2*n+1)/reduce(lambda x, y: x*y, range(1, 2*n + 2)), range(5))), 5)