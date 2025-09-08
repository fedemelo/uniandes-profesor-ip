def verificar_nit(NIT: int, digito: int) -> bool:
    """ Verificar NIT
    Parámetros:
      NIT (int): NIT de una empresa, sin dígito de verificación
      digito (int): Dígito de verificación
    Retorno:
      bool: Retorna True si el NIT es correcto. De lo contrario, retorna False
    """
    
    digit_9 = NIT // 100_000_000
    cropped_nit = NIT - digit_9 * 100_000_000
    digit_8 = cropped_nit // 10_000_000
    cropped_nit = cropped_nit - digit_8 * 10_000_000
    digit_7 = cropped_nit // 1_000_000
    cropped_nit = cropped_nit - digit_7 * 1_000_000
    digit_6 = cropped_nit // 100_000
    cropped_nit = cropped_nit - digit_6 * 100_000
    digit_5 = cropped_nit // 10_000
    cropped_nit = cropped_nit - digit_5 * 10_000
    digit_4 = cropped_nit // 1_000
    cropped_nit = cropped_nit - digit_4 * 1_000
    hundred = cropped_nit // 100
    cropped_nit = cropped_nit - hundred * 100
    ten = cropped_nit // 10
    unit = cropped_nit - ten * 10
    
    sum_ = (digit_9 * 41 + 
            digit_8 * 37 +
            digit_7 * 29 + 
            digit_6 * 23 +
            digit_5 * 19 +
            digit_4 * 17 +
            hundred * 13 +
            ten * 7 +
            unit * 3)
  
    remainder = sum_ % 11
    return digito == (remainder if remainder <= 1 else 11 - remainder)