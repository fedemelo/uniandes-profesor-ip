def puntaje_contrasena(contrasena: str) -> int:
    numero_digitos = (contrasena.count('0') + 
                      contrasena.count('1') + 
                      contrasena.count('2') + 
                      contrasena.count('3') + 
                      contrasena.count('4') + 
                      contrasena.count('5') + 
                      contrasena.count('6') + 
                      contrasena.count('7') + 
                      contrasena.count('8') + 
                      contrasena.count('9'))

    if (len(contrasena) < 8
        or ' ' in contrasena
        or numero_digitos == len(contrasena)
        or contrasena == 'password'
        or contrasena == 'admin'):
        return 0

    puntaje = len(contrasena)
    if contrasena.upper() != contrasena:
        puntaje += 3
    if contrasena.lower() != contrasena:
        puntaje += 5
    if numero_digitos > 0:
        puntaje += 7
    return puntaje


def mejor_contrasena(
    contrasena1: str, 
    contrasena2: str,
    contrasena3: str, 
    contrasena4: str
) -> str:
    num_mejor_contrasena = 1
    mejor_contrasena = contrasena1
    mejor_puntaje = puntaje_contrasena(contrasena1)

    puntaje2 = puntaje_contrasena(contrasena2)
    if puntaje2 > mejor_puntaje:
        num_mejor_contrasena = 2
        mejor_contrasena = contrasena2
        mejor_puntaje = puntaje2

    puntaje3 = puntaje_contrasena(contrasena3)
    if puntaje3 > mejor_puntaje:
        num_mejor_contrasena = 3
        mejor_contrasena = contrasena3
        mejor_puntaje = puntaje3

    puntaje4 = puntaje_contrasena(contrasena4)
    if puntaje4 > mejor_puntaje:
        num_mejor_contrasena = 4
        mejor_contrasena = contrasena4
        mejor_puntaje = puntaje4

    return f'La contraseña más segura es la contraseña {num_mejor_contrasena}, su valor es {mejor_contrasena} y tiene un puntaje de {mejor_puntaje}.'


assert puntaje_contrasena('1234567') == 0
assert puntaje_contrasena('12345678') == 0
assert puntaje_contrasena('mi clave') == 0
assert puntaje_contrasena('password') == 0
assert puntaje_contrasena('abcdefgh') == 11
assert puntaje_contrasena('PASSWORD') == 13
assert puntaje_contrasena('ABCDEFGH') == 13
assert puntaje_contrasena('Abcdefgh') == 16
assert puntaje_contrasena('1234567a') == 18
assert puntaje_contrasena('admin123') == 18
assert puntaje_contrasena('password1') == 19
