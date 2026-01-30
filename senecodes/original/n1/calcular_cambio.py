def calcular_cambio(cambio:int)->str:
    A=int(cambio/500)
    resA = cambio % 500
    B=int(resA/200)
    resB = resA % 200
    C=int(resB/100)
    resC = resB % 100
    D=int(resC/50)
    A=str(A)
    B=str(B)
    C=str(C)
    D=str(D)
    return A+","+B+","+C+","+D
