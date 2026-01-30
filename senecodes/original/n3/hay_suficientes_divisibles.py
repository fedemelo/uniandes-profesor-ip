# -*- coding: utf-8 -*-

def hay_suficientes_divisibles(d: int, numeros: list, n: int)->bool:
    """ Conteo de Divisibles
    Parámetros:
      d (int): El divisor contra el que se evaluarán los números de la lista. El número 'd' será un entero
               positivo.
      numeros (list): Una lista de números enteros positivos. La lista tiene al menos un elemento.
      n (int): La cantidad de números mínima que se espera que cumplan con la condición de ser divisibles
               por 'd'. El número 'n' será un entero mayor o igual a 0.
    Retorno:
      bool: Retorna el valor True si la lista recibida tiene al menos 'n' números que cumplen con ser divisibles
            por el número 'd'. Retorna False de lo contrario.
    """
    count=0
    for num in numeros:
        if num%d==0:
            count+=1
    if count>=n:
        answ=True
    else: 
        answ=False
    return answ

