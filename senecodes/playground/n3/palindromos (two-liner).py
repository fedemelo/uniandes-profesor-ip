from re import sub

def palindromos(cadena: str)->bool:
    remove_accents = lambda x: sub(r"á", "a", sub(r"é", "e", sub(r"í", "i", sub(r"ó", "o", sub(r"[úü]", "u", x)))))
    return sub(r"[,. ]", "", remove_accents(cadena.lower())) == sub(r"[,. ]", "", remove_accents(cadena.lower()))[::-1]