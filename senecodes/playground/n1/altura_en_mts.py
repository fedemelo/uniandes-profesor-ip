def altura_en_mts(pies: int, pulgadas: int)->float:
    return round(pies * 0.3048 + pulgadas * 0.0254, 2)