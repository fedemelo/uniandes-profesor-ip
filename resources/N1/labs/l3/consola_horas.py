import logica


def consola_horas():
    horas = int(input("Ingrese el número de horas transcurridas desde el 1 de enero a las 00:00: "))
    fecha = logica.fecha_desde_horas(horas)
    print(f"La fecha correspondiente es {fecha}.")

consola_horas()