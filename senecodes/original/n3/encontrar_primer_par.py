# -*- coding: utf-8 -*-

def encontrar_primer_par(numeros: list)->int:
    """ Primer par
    Parámetros:
      numeros (list): La lista de números a revisar
    Retorno:
      int: El primer número par en la lista. Si en la lista no hay números pares, se debe retornar None
    """
    par=None
    for num in numeros:
        if num%2==0:
            par=num
            break
    return par
        

