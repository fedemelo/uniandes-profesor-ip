import logica


def consola_esfera():
    radio = float(input("Ingrese el radio de la esfera: "))
    distancia = logica.distancia_esquina_esfera(radio)
    print(f"La distancia desde una esquina del cubo al punto mas cercano de la esfera es {distancia}.")

consola_esfera()
