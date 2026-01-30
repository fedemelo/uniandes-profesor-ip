# -*- coding: utf-8 -*-

def letra_mas_comun(cadena: str)->str:
    """ Moda en una cadena
    Parámetros:
      cadena (str): La cadena en la que se quiere saber cuál es la letra más común
    Retorno:
      str: La letra más común en la cadena que ingresa como parámetro,  si son dos es la letra alfabéticamente
           posterior.
    """
    lista=[]
    dic={}
    dic2={}
    quitar=[".",","," "] #Lo que voy a quitar de la cadena.
    for thing in quitar:
        lista_cadena=cadena.split(thing) #Me deshago de la cosa que no quiero, porque es el separador de la lista.
        cadena="".join(lista_cadena) #Otra vez creo la cadena uniendo la lista, ahora sin la cosa que quité.
    for letra in cadena:
        lista.append(letra) #Lista con todo caracter de la cadena
        lista.sort() #Lista con letras ordenadas
    for letra in lista:
        dic[letra]=dic.get(letra,0)+1 #Diccionario con parejas letra:apariciones
        dic2[dic[letra]]=letra #Diccionario con parejas apariciones:letra
    greatest=0
    for elemento in dic2.keys():
        if int(elemento)>greatest:
            greatest=elemento
            mas_aparece=dic2[elemento]
    return mas_aparece #Retorna la letra con más apariciones. Como la lista está 
    #ordenada y el ciclo retorna el último, da el alfabéticamente posterior.
        
            
            
        
