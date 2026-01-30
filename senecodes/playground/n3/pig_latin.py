from itertools import takewhile, dropwhile

def traducir_a_pig_latin(texto: str) -> str:
    def trad(palabra: str) -> str:
        es_vocal = lambda x: x in 'aeiou'
        es_consonante = lambda x: x not in 'aeiou'

        if next(filter(es_vocal, palabra), None):  # Tiene vocal:
            if es_vocal(palabra[0]):  # Empieza por vocal
                return palabra+"way"
            return "".join(dropwhile(es_consonante, palabra))+"".join(takewhile(es_consonante, palabra))+"ay"
        return palabra

    return " ".join(map(trad, texto.split()))