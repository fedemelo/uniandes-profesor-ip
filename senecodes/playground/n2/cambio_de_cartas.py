def cambio_de_cartas(carta_mano: dict, opcion_1: dict, opcion_2: dict) -> int:
    sirve = lambda x: carta_mano["numero"] == x["numero"] or carta_mano["palo"] == x["palo"]
    return 1 if sirve(opcion_1) else 2 if sirve(opcion_2) else 0