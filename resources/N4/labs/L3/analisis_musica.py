import pandas as pd
import matplotlib.pyplot as plt


def cargar_datos(archivo: str) -> pd.DataFrame:
    return pd.read_csv(archivo)


def canciones_por_genero_artista(df: pd.DataFrame, artista: str) -> None:
    df_artista = df[df["performer"] == artista]
    conteo = df_artista["genre"].value_counts()
    
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
    df_filtrado = df[df["explicit"] == explicitas]
    popularidad = df_filtrado.groupby("genre")["popularity"].sum()
    popularidad = popularidad.sort_values(ascending=False).head(20)
    
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
    df = cargar_datos("cupicharts.csv")
    # canciones_por_genero_artista(df, "Morgan Wallen")
    popularidad_por_genero_explicitidad(df, False)

