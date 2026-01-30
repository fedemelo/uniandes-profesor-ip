def menor_digito(numero: int)->int:
    return int(min(str(numero if numero>=0 else -numero)))

print(menor_digito(56789))