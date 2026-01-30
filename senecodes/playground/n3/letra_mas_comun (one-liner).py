from collections import Counter

def letra_mas_comun(cadena: str) -> str:
    return Counter(filter(lambda x: x.isalpha(), sorted(cadena, reverse=1))).most_common(1)[0][0]