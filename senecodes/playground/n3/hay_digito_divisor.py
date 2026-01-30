def hay_digito_divisor(n1: int, n2: int)->bool:
    return bool(list(filter(lambda x: n2 % int(x) == 0, str(n1).replace("0", ""))))