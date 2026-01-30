def picas_y_fijas(numero_secreto: int, intento: int) -> dict:
    fijas = sum(map(lambda x: 1 if x[0] == x[1] else 0, zip(str(numero_secreto), str(intento))))
    picas = sum(map(lambda x: x in str(numero_secreto), str(intento))) - fijas
    return {"FIJAS": fijas, "PICAS": picas}