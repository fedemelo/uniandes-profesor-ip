def desglose_billetes(monto: int) -> str:
    """
    Recibe un monto entero en pesos colombianos (múltiplo de 1000) y retorna
    un str con la cantidad mínima de billetes de cada denominación necesarios
    para completar dicho monto.
    """
    billetes_100k = monto // 100000
    resto = monto % 100000
    billetes_50k = resto // 50000
    resto %= 50000
    billetes_20k = resto // 20000
    resto %= 20000
    billetes_10k = resto // 10000
    resto %= 10000
    billetes_5k = resto // 5000
    resto %= 5000
    billetes_2k = resto // 2000
    resto %= 2000
    billetes_1k = resto // 1000
    return (f"{billetes_100k} de $100.000, "
            f"{billetes_50k} de $50.000, "
            f"{billetes_20k} de $20.000, "
            f"{billetes_10k} de $10.000, "
            f"{billetes_5k} de $5.000, "
            f"{billetes_2k} de $2.000, "
            f"{billetes_1k} de $1.000")


def distancia_esquina_esfera(radio: float) -> float:
    """
    Recibe el radio de una esfera empacada en el menor cubo que la contiene
    y retorna la distancia desde una esquina del cubo al punto más cercano
    en la superficie de la esfera.
    """
    lado = 2 * radio
    diagonal_cara = (2 * lado ** 2) ** 0.5
    diagonal_espacial = (diagonal_cara ** 2 + lado ** 2) ** 0.5
    distancia = diagonal_espacial / 2 - radio
    return distancia
