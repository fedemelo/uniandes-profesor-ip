def secuencia_de_fibonacci(fib_1: int, fib_2: int, fib_3: int, fib_4: int) -> str:
    return "Fibofacil" if fib_3 == fib_1 + fib_2 and fib_4 == fib_3 + fib_2 else "Fibofalsa"
