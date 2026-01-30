
def contar_hormigas(cantidad_inicial: int, meses: int) -> int:
    for _ in range(meses):
        if cantidad_inicial <= 28000:
            cantidad_inicial = cantidad_inicial*1.4-7000
            if cantidad_inicial <= 0:
                return 0
        else:
            cantidad_inicial = cantidad_inicial*1.31-7000
            if cantidad_inicial <= 0:
                return 0
    return cantidad_inicial

print(contar_hormigas(10000, 3))


def contar_hormigas(cantidad_inicial: int, meses: int) -> int:
    for _ in range(meses):
        cantidad_inicial = (lambda x: x*1.4-7000 if x <= 28000 else x*1.31-7000)(cantidad_inicial)
    return cantidad_inicial

print(contar_hormigas(10000, 3))
