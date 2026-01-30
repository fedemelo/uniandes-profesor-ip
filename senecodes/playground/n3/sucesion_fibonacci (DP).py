def sucesion_fibonacci(cantidad_numeros: int) -> str:
    if cantidad_numeros == 1:
        return "0"
    if cantidad_numeros == 2:
        return "0,1"
   
    memo: list = [0, 1]
    answ: str = "0,1"
    for i in range(2, cantidad_numeros):
        num: int = memo[i-2]+memo[i-1]
        memo.append(num)
        answ += ","+str(num)
    return answ