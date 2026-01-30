def descifrar_codigo_cesar(texto_cifrado: str, corrimiento: int)->str:
    cte = lambda x : ord("A") if x.isupper() else ord("a")
    return "".join(map(lambda x: chr((ord(x)-cte(x)-corrimiento) % 26 + cte(x)) if x.isalpha() else x, texto_cifrado))

# print(descifrar_codigo_cesar("SJYBTWPX PJJU YMJ BTWQI WZSSNSL", 5))  # NETWORKS KEEP THE WORLD RUNNING

# print(descifrar_codigo_cesar('sjybtwpx pjju ymj btwqi wzssnsl', 5))  # networks keep the world running