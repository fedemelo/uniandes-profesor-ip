
def secuencia(i: int) -> int:
    """ 
    Secuencia 0, 1, 1, 5, 18

    Parámetros:
      i (int): Posición en la secuencia que se quiere calcular
    Retorno:
      int: Número i-esimo de la secuencia
    """
    memo: list[int] = [0, 1, 1]

    memo.extend([None] * (i-2))
    for j in range(3, i+1):
        memo[j] = 3*memo[j-1] + 2*memo[j-2] + memo[j-3]
    return memo[i]


# Pruebas
assert secuencia(0) == 0
assert secuencia(1) == 1
assert secuencia(2) == 1
assert secuencia(3) == 5
assert secuencia(4) == 18
assert secuencia(5) == 65
assert secuencia(6) == 236


