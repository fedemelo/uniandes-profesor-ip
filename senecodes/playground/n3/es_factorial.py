from math import factorial

def es_factorial(n: int) -> int:
    return (lambda x: 0 if x == [] else x[0])([x for x in range(1, int((n+10)**(1/2))) if factorial(x) == n])