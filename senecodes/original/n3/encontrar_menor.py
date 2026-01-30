# -*- coding: utf-8 -*-

def encontrar_menor(entrada: list)->int:
    """ Encontrar el elemento menor
    Parámetros:
      entrada (list): La lista
    Retorno:
      int: El número más pequeño en la lista, si es vacía None.
    """
    if entrada==[]:
        menor=None
    else:
        import numpy as np
        menor=np.infty
        for entero in entrada:
            if entero<menor:
                menor=entero
    return menor
        