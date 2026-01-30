def analizar_texto(texto: str, caracteres_permitidos: list) -> dict:
    texto += " "
    i: int = 0
    palabra: str = ""
    palabras: dict[str, tuple[int, int, int]] = {}
    hayPalabra: bool = False
    while i < len(texto):
        char: str = texto[i]
        if char in caracteres_permitidos:
            palabra += char
            hayPalabra = True
        elif hayPalabra:
            apariciones, primera, ultima = palabras.get(palabra.lower(),  (0, i-len(palabra), i-len(palabra)))
            apariciones += 1
            ultima = i-len(palabra)
            palabras[palabra.lower()] = apariciones, primera, ultima
            palabra = ""
            hayPalabra = False
        i += 1
    return palabras

print(analizar_texto("Muchos años después frente al pelotón de fusilamiento el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo ", ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']))
# print(analizar_texto("Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo.", ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']))

# eg2: str = "Seis suecos sosos secan sesos sin sal, Secan seis sesos los suecos, Salan seis sesos con sal, secan y salan los sesos, que sacan del secadal."
# cp2: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']
 
# print(analizar_texto(eg2, cp2))