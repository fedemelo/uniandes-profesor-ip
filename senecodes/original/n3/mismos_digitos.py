# -*- coding: utf-8 -*-

def lista_digitos(num:int)->list:
    lista=[]
    for digito in str(num):
        if digito not in lista:
            lista.append(digito)
            lista.sort()
    return lista

def mismos_digitos(a:int, b:int)->bool:
    alist=lista_digitos(a)
    blist=lista_digitos(b)
    return alist==blist
        
        
        

