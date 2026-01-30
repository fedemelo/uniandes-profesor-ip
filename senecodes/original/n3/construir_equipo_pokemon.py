# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:18:06 2020

@author: FMelo
"""

def construir_equipo_pokemon(cantidad: int, lista_pkmn: list)->list:
    """ Ash y la liga Kalos
    Parámetros:
      cantidad (int): La cantidad de Pokémon que usará cada entrenador en la batalla final. Es un entero
                      entre 3 y 6.
      lista_pkmn (list): Una lista compuesta de diccionarios. Los diccionarios representan cada uno de los
                         Pokémon elegibles por Ash. Cada diccionario tiene las siguientes llaves: "nombre":
                         (str) el nombre del Pokémon; se garantiza que no hay nombres repetidos en los
                         diccionarios de la lista. "vida": (int),  "ataque": (int),  "defensa": (int),
                         "ataque_especial": (int), "defensa_especial": (int) , "velocidad": (int) Cada uno
                         de estos valores enteros representa la estadística respectiva del Pokémon.
    Retorno:
      list: La función retorna None si es imposible generar un equipo de Pokémon seudolegendarios para la
            batalla. De lo contrario, retorna una lista con los nombres de los Pokémon a utilizar en la batalla.
    """
    seudolegendarios=0 #Contador de seudolegendarios
    sepuede=False #Centinela
    i=0 #Índice
    answ=[] #Lista de respuesta
    lista_cualidades=["vida","ataque","defensa","ataque_especial","defensa_especial","velocidad"] #Lista cualidades
    suma_ya=False #Centinela 2 (para saber si acabar la suma o seguir sumando)
    suma=0 #Suma para saber si seudolegendario
    i2=0 #Índice 2
    while i<len(lista_pkmn) and sepuede==False: #Recorrido parcial: hay suficientes seudolegendarios
        while i2<len(lista_cualidades) and suma_ya==False: #Recorrido parcial 2: suma de habilidades para saber si es seudolegendario
            suma+=lista_pkmn[i][lista_cualidades[i2]] #Suma cualidad por cualidad, que están en lista_cualidades
            if suma>=600: #Si la suma llega a 600, para
                suma_ya=True 
            i2+=1
        suma=0 #Reinicia la suma para el próximo Pokémon.
        if suma_ya==True: #Si la suma dio 600
            seudolegendarios+=1 #Se añade 1 a la cuenta de seudolegendarios
            answ.append(lista_pkmn[i]["nombre"]) #Se suma el nombre de ese pokemon a la lista respuesta
        suma_ya=False #Reinicia el centinela de la suma para el próximo Pokémon.
        i2=0 #Reinicia el índice 2
        if seudolegendarios==cantidad: #Si se cumplió la cantidad de seudolegendarios, entonces True y acaba el ciclo grande
            sepuede=True
        i+=1 
    if sepuede==False: #Si no se cumplio la cantidad después del ciclo, se devuelve None.
        answ=None
    return answ