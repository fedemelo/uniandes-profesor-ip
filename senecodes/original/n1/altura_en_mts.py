def altura_en_mts(pies: int, pulgadas: int)->float:
    pulg=pies*12+pulgadas
    cm=pulg*2.54
    m=cm/100
    altura=round(m,2)
    return(altura)
    pass

