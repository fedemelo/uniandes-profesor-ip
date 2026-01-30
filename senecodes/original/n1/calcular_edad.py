def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int)->str:
    an=anio_nacio*360
    mn=mes_nacio*30
    dn=dia_nacio+mn+an
    aa=anio_actual*360
    ma=mes_actual*30
    da=dia_actual+aa+ma
    totaldias=da-dn
    anio=str(totaldias//360)
    resto=totaldias%360
    mes=str(resto//30)
    dia=str(resto%30)
    return anio+","+mes+","+dia
    