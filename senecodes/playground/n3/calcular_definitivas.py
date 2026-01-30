def calcular_definitivas(estudiantes: list) -> list:

    def aproximar_nota(estudiante: dict) -> dict:
        if estudiante["nota"] >= 4.5:
            estudiante["nota"] = 5.0
        elif estudiante["nota"] >= 3.5:
            estudiante["nota"] = 4.0
        elif estudiante["nota"] >= 2.5:
            estudiante["nota"] = 3.0
        else:
            estudiante["nota"] = 1.5
        return estudiante

    return list(map(aproximar_nota, estudiantes))