def decir_el_numero(numero: int) -> str:
    """ Decir el número
    Parámetros:
      numero (int): Entero que se quiere decir en voz alta
    Retorno:
      str: Cadena que representa cómo se diría el número en voz alta
    """
    positive_input = abs(numero)

    negative_or_0 = numero - positive_input
    is_negative = _is_nonzero(negative_or_0)
    negative_str = "menos " * is_negative

    millions_count = positive_input // 1_000_000
    remainder = positive_input % 1_000_000
    has_millions = _is_nonzero(millions_count)
    has_many_millions = _is_nonzero(millions_count // 2)
    has_single_million = _and(_not(has_many_millions), has_millions)
    million_str = str(millions_count) * has_millions + " millones" * has_many_millions + " millón" * has_single_million

    thousands_count = remainder // 1_000
    remainder %= 1_000
    has_thousands = _is_nonzero(thousands_count)
    has_many_thousands = _is_nonzero(thousands_count // 2)
    thousand_str = str(thousands_count) * has_many_thousands + " " * has_many_thousands + "mil" * has_thousands

    has_remainder = _is_nonzero(remainder)
    no_remainder_and_nothing_else = _and(
        _not(has_remainder), _not(_or(has_millions, has_thousands)))
    show_remainder = _or(has_remainder, no_remainder_and_nothing_else)

    space_after_million = " " * _and(has_millions,
                                     _or(has_thousands, show_remainder))
    space_after_thousand = " " * _and(has_thousands, show_remainder)

    return negative_str + million_str + space_after_million + thousand_str + space_after_thousand + str(remainder) * show_remainder


def _is_nonzero(count: int) -> int:
    return min(abs(count), 1)


def _not(one_or_zero: int) -> int:
    return (one_or_zero + 1) % 2


def _and(a: int, b: int) -> int:
    return a * b


def _or(a: int, b: int) -> int:
    return min(a + b, 1)


assert decir_el_numero(-0) == '0'
assert decir_el_numero(-1) == 'menos 1'
assert decir_el_numero(-1000) == 'menos mil'
assert decir_el_numero(-1234567) == 'menos 1 millón 234 mil 567'
assert decir_el_numero(-2000) == 'menos 2 mil'
assert decir_el_numero(0) == '0'
assert decir_el_numero(1) == '1'
assert decir_el_numero(1000) == 'mil'
assert decir_el_numero(1000000) == '1 millón'
assert decir_el_numero(1000001) == '1 millón 1'
assert decir_el_numero(1001000) == '1 millón mil'
assert decir_el_numero(1009) == 'mil 9'
assert decir_el_numero(103) == '103'
assert decir_el_numero(123006789) == '123 millones 6 mil 789'
assert decir_el_numero(1234) == 'mil 234'
assert decir_el_numero(2000) == '2 mil'
assert decir_el_numero(2000000) == '2 millones'
assert decir_el_numero(2002000) == '2 millones 2 mil'
assert decir_el_numero(22034) == '22 mil 34'
assert decir_el_numero(500) == '500'
assert decir_el_numero(999999999) == '999 millones 999 mil 999'
