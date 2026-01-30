def serie_recomendada(series: list) -> dict:

    puntaje_max = 0

    def calificar_serie(serie: dict, puntaje_max=puntaje_max) -> tuple:
        puntaje = 0
        if serie["Pais"] in ("Corea del Sur", "Japón", "China"):
            puntaje += 1
        elif serie["Pais"] == "Colombia":
            puntaje -= 1
        if "Acción" in serie["Generos"] or "Terror" in serie["Generos"]:
            puntaje -= 1
        if "Romance" in serie["Generos"] or "Comedia" in serie["Generos"] or "Drama" in serie["Generos"]:
            puntaje += 1
        if serie["Numero de capitulos"] <= 16:
            puntaje += 1
        elif serie["Numero de capitulos"] > 30:
            puntaje -= 1

        if puntaje > puntaje_max:
            puntaje_max = puntaje
            return serie

       
        return False

    return next(filter(calificar_serie, series))

l = [{'Titulo': 'Anatomía de Grey', 'Pais': 'Corea del Sur', 'Numero de capitulos': 3, 'Generos': ['Comedia', 'Terror', 'Animación']}, 
     {'Titulo': 'Itaewon class', 'Pais': 'China', 'Numero de capitulos': 16, 'Generos': ['Acción', 'Drama', 'Terror']}]
print(serie_recomendada(l))
