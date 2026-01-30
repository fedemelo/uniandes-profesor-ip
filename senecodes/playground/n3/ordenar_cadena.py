# Bonita

def ordenar_cadena(cadena: str)->str:
  alfabeto: dict[str, int] = {chr(i): 0 for i in range(ord('a'), ord('a')+26)}
  for letra in cadena:
    alfabeto[letra] += 1
  answ: str = ""
  for letra, count in alfabeto.items():
    answ += letra*count
  return answ

print(ordenar_cadena("ertyujhgf"))
print(ordenar_cadena("abahjbbzza"))

# Optimizada

def ordenar_cadena(cadena: str)->str:
  letras: list[int] = [0 for i in range(26)]
  for letra in cadena:
    letras[ord(letra)-ord('a')] += 1
  answ: str = ""
  pos = 0
  for count_letra in letras:
    letra: str = chr(pos+ord('a'))
    answ += letra*count_letra
    pos += 1
  return answ

print(ordenar_cadena("ertyujhgf"))
print(ordenar_cadena("abahjbbzza"))

# One-liner

def ordenar_cadena(cadena: str)->str:
    return "".join(sorted(cadena))