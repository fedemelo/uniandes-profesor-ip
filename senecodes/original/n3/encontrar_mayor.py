# -*- coding: utf-8 -*-

def encontrar_mayor(entrada: list)->int:
    """ Encontrar el elemento mayor
    Parámetros:
      entrada (list): La lista de números que se desea buscar
    Retorno:
      int: El número más grande en la lista, si está vacía -1.
    """
    if entrada==[]:
        greatest=-1
    else:
        import numpy as np
        greatest=-np.infty
        for num in entrada:
            if num>greatest:
                greatest=num
    return greatest
