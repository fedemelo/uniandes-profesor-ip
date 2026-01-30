def calcular_total_pan_comprado(frescos: int, viejos: int)->int:
    """ Pan del día anterior
    Parámetros:
      frescos (int): Cantidad de panes frescos comprados
      viejos (int): Cantidad de panes del día anterior comprados
    Retorno:
      int: Valor total a pagar por el pan comprado
    """
    return int(frescos*450+viejos*450*0.4)

