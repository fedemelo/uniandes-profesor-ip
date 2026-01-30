def encontrar_manzana(barrio: list) -> tuple:

    mas_sospechosos: int = 0
    best_dist: float = float("inf")
    answ = (0, 0)

    for i in range(len(barrio)):
        for j in range(len(barrio[i])):

            cantidad_sospechosos: int = 0
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    no_es_el_central: bool = not (x == 0 and y == 0)
                    se_salio: bool = (i+x < 0) or (i + x >= len(barrio)) or (j+y < 0) or (j+y >= len(barrio[i]))
                    if not se_salio and no_es_el_central:
                        borde: int = barrio[i+x][j+y]
                        cantidad_sospechosos += borde

            if cantidad_sospechosos > mas_sospechosos:
                mas_sospechosos = cantidad_sospechosos
                answ = (i, j)
                best_dist = cartesian_distance(0, 0, i, j)

            elif cantidad_sospechosos == mas_sospechosos:
                dist = cartesian_distance(0, 0, i, j)
                if dist < best_dist:
                    best_dist = dist
                    answ = (i, j)
                elif dist == best_dist:
                    if i < answ[0]:
                        answ = (i, j)
    
    return answ


def cartesian_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x2-x1)**2 + (y2-y1)**2)**(1/2)