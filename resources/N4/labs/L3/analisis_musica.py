import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cupicharts.csv")


def canciones_por_genero_artista(df: pd.DataFrame, artista: str) -> None:
    # TODO: Implemente la lógica de Pandas aquí.
    # Filtre el DataFrame para quedarse solo con las canciones del artista.
    # Cuente cuántas canciones tiene en cada género y guarde el resultado en 'conteo'.
    conteo = ...

    # Código de Matplotlib — no modifique esta parte
    conteo.plot(
        kind="bar",
        figsize=(10, 6),
        title=f"Distribución de canciones por género - {artista}",
        xlabel="Género",
        ylabel="Cantidad de canciones"
    )
    plt.tight_layout()
    plt.show()


def popularidad_por_genero_explicitidad(df: pd.DataFrame, explicitas: bool) -> None:
    # TODO: Implemente la lógica de Pandas aquí.
    # Filtre el DataFrame según si las canciones son explícitas o no.
    # Agrupe por género, sume la popularidad total de cada género, ordene de mayor
    # a menor y quédese solo con los 20 géneros más populares.
    # Guarde el resultado en 'popularidad'.
    popularidad = ...

    # Código de Matplotlib — no modifique esta parte
    tipo = "explícitas" if explicitas else "no explícitas"
    ax = popularidad.plot(
        kind="barh",
        figsize=(10, 8),
        title=f"Top 20 géneros por popularidad - Canciones {tipo}",
        xlabel="Popularidad total",
        ylabel="Género"
    )
    ax.invert_yaxis()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    canciones_por_genero_artista(df, "Morgan Wallen")
    popularidad_por_genero_explicitidad(df, False)
