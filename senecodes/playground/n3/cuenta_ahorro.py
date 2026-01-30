from itertools import repeat
from math import ceil

def cuenta_ahorro(saldo: float, interes_mes: float, interes_anio: float, meses: int) -> float:
    anios = list(range(1, meses//12+1))
    zip_ = (repeat(saldo), anios)
    anios = list(map(lambda x: x[0]+(x[0]*(interes_mes/100)**(11 if meses >= 11*x[1] else meses%11))*(1 + 1*(interes_anio/100)), zip_))
    mes = saldo*(1+interes_mes/100)**meses
    anios = sum(map(lambda x: x*(interes_anio/100), [mes]*(meses//12) ))
    return ceil((mes+anios)*(1+interes_mes/100)**meses*100)/100

print(cuenta_ahorro(100, 1.0, 5.0, 0))
