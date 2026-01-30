def calcular_pago_botellas(cant_pequenias: int, cant_grandes: int)->float:
    paga1=cant_pequenias*0.10
    paga2=cant_grandes*0.25
    paga=round(paga1+paga2,2)
    return paga

