# Actividad 1: Palíndromos

def palindromos(n1, n2, n3, n4):
    return {
        n1: str(n1) == str(n1)[::-1],
        n2: str(n2) == str(n2)[::-1],
        n3: str(n3) == str(n3)[::-1],
        n4: str(n4) == str(n4)[::-1],
    }


# Actividad 2: Competencia de videojuegos

def contar_consonantes(nickname):
    vocales = nickname.count("a") + nickname.count("e") + nickname.count("i") + nickname.count("o") + nickname.count("u")
    return len(nickname) - vocales


def mejor_jugador(j1, j2):
    if j1["puntaje"] > j2["puntaje"]:
        return j1
    if j2["puntaje"] > j1["puntaje"]:
        return j2
    c1 = contar_consonantes(j1["nickname"])
    c2 = contar_consonantes(j2["nickname"])
    if c1 > c2:
        return j1
    if c2 > c1:
        return j2
    if j1["experiencia"] < j2["experiencia"]:
        return j1
    return j2


def campeon(j1, j2, j3, j4):
    ganador = mejor_jugador(j1, j2)
    ganador = mejor_jugador(ganador, j3)
    ganador = mejor_jugador(ganador, j4)
    return ganador["nickname"]


# Actividad 3: Sistema de códigos de productos

def digitos_ascendentes(codigo: str) -> bool:
    digitos = ""
    if codigo[0].isdigit():
        digitos += codigo[0]
    if codigo[1].isdigit():
        digitos += codigo[1]
    if codigo[2].isdigit():
        digitos += codigo[2]
    if codigo[3].isdigit():
        digitos += codigo[3]

    if len(digitos) <= 1:
        return True
    if len(digitos) == 2:
        return digitos[0] < digitos[1]
    if len(digitos) == 3:
        return digitos[0] < digitos[1] and digitos[1] < digitos[2]
    return digitos[0] < digitos[1] and digitos[1] < digitos[2] and digitos[2] < digitos[3]


def es_valido(codigo: str) -> bool:
    return len(codigo) == 4 and codigo == codigo.lower() and digitos_ascendentes(codigo)


def validar_codigos(c1: str, c2: str, c3: str, c4: str) -> dict:
    return {
        c1: es_valido(c1),
        c2: es_valido(c2),
        c3: es_valido(c3),
        c4: es_valido(c4),
    }
