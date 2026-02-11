import logica


def consola_billetes():
    monto = int(input("Ingrese el monto en pesos colombianos: "))
    desglose = logica.desglose_billetes(monto)
    print(f"Desglose: {desglose}")

consola_billetes()
