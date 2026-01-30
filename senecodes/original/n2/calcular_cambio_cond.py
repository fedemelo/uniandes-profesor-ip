def calcular_cambio(cambio:int)->str:
    A=0
    B=0
    C=0
    D=0
    if cambio>=500:
        while cambio-500>=0:
            cambio=cambio-500
            A=A+1
    if cambio>=200:
        while cambio-200>=0:
            cambio=cambio-200
            B=B+1
    if cambio>=100:
        while cambio-100>=0:
            cambio=cambio-100
            C=C+1
    if cambio>=50:
        while cambio-50>=0:
            cambio=cambio-50
            D=D+1
    A=str(A)
    B=str(B)
    C=str(C)
    D=str(D)
    return A+","+B+","+C+","+D

