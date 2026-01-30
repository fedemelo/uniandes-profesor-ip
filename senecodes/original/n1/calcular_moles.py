def calcular_moles(presion:float,volumen:float,temp_celsius:float)->float:
    Vmetros=volumen/1000
    Tkelvin=temp_celsius+273.15
    n=(presion*Vmetros)/(8.314*Tkelvin)
    no=round(n,2)
    return(no)
