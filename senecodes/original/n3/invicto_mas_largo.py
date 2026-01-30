# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:15:02 2020

@author: FMelo
"""

def invicto_mas_largo(goles_diccionarios: list, goles_adversario: list)->int:
    """ Invictos
    Parámetros:
      goles_diccionarios (list): Los goles anotados por Diccionarios F.C en cada una de las fechas. Se
                                 garantiza que cada elemento de la lista es un entero no negativo.
      goles_adversario (list): Los goles anotados por los adversarios de Diccionarios F.C en cada una de las
                               fechas. Se garantiza que cada elemento de la lista es un entero no negativo.
    Retorno:
      int: Retorna la cantidad máxima de fechas consecutivas en que el equipo Diccionarios F.C no perdió
           durante la temporada anterior.
    """
    rachas_sin_perdida=[] #Lista donde se almacenarántodas las rachas sin perder.
    count_no_perdidos=0 #Cuenta de partidos consecutivos no perdidos.
    i=0 #Índice
    while i<len(goles_diccionarios): #Recorrido total
        if goles_diccionarios[i]>=goles_adversario[i]: #Si no perdió
            count_no_perdidos+=1 #Se suma uno a la cuenta de no perdidos
        elif goles_diccionarios[i]<goles_adversario[i]: #Si perdió
            rachas_sin_perdida.append(count_no_perdidos) #Se pone la cuenta en la lista
            count_no_perdidos=0 #Se reinicia la cuenta
        i+=1 
    rachas_sin_perdida.append(count_no_perdidos) #Se añade a la lista la última cuenta.
    answ=max(rachas_sin_perdida) #La recha más larga en la lista el la respuesta.
    return answ