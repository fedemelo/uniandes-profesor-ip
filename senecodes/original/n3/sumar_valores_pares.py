def sumar_valores_pares(numeros: list)->int:
    """ 
        Sumar valores pares
    Parámetros:
      numeros (list): Una lista de números enteros.
    Retorno:
      int: La suma de los números de la lista que sean pares.
    """
    suma_pares=0
    for nums in numeros:
        if nums%2==0:
            suma_pares+=nums
    return suma_pares    
    
            

