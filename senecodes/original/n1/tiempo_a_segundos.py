def tiempo_a_segundos(dias: int, horas: int, mins: int, seg: int)->int:
    ds=int(dias*86400)
    hs=int(horas*3600)
    ms=int(mins*60)
    segundos=int(seg+ds+hs+ms)
    return segundos