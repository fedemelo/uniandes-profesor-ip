import logica


def consola_segundos():
    segundos = int(input("Ingrese el número de segundos transcurridos desde el 1 de enero a las 00:00: "))
    fecha = logica.fecha_desde_segundos(segundos)
    print(f"La fecha correspondiente es {fecha}.")

consola_segundos()