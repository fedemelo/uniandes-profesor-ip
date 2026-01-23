#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import modulo as mod

##### Funciones auxiliares:

def mostrar_cancion(cancion: dict) -> None:
    """
    Muestra la información de una canción en Cupicharts.

    Parámetros:
        cancion (dict): Diccionario con la información de la canción.
    """
    if cancion is not None and cancion != {}:
        print("\n")
        print("#" * 50)
        
        print((
            "Título: {}\n"
            "Fecha en el top: {}\n"
            "Artista: {}\n"
            "Posición máxima: {}\n"
            "Semanas en el top: {}\n"
            "Álbum: {}\n"
            "Fecha de lanzamiento: {}\n"
            "Popularidad: {}\n"
            "Explícita: {}\n"
            "Número de oyentes: {}\n"
            "Número de reproducciones: {}\n"
            "Duración: {}\n"
        ).format(
            cancion["title"], cancion["chart_week"],
            cancion["performer"], cancion["peak_pos"],
            cancion["wks_on_chart"], cancion["album_name"],
            cancion["release_date"], cancion["popularity"],
            cancion["explicit"], cancion["listeners"],
            cancion["play_count"], cancion["duration_s"]
        ))
        print("#" * 50)
    else:
        print("Error: Diccionario de canción inválido.")

##### Fin de funciones auxiliares


##### Funciones del menú:

def ejecutar_cargar_cupicharts() -> None:
    """Función que ejecuta la carga del archivo CSV."""
    print("Cargar archivo CSV de canciones")
    print("Ingrese la ruta al archivo CSV (ej: ./cupicharts.csv):")
    ruta = input("> ")
    
    try:
        datos = mod.cargar_cupicharts(ruta)
        print("\nDatos cargados exitosamente!")
        print(f"Géneros encontrados: {len(datos)}")
        for genero, canciones in datos.items():
            print(f"  - {genero}: {len(canciones)} canción(es)")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta}'")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")


def ejecutar_cancion_mas_popular() -> None:
    """Función que ejecuta la búsqueda de la canción más popular por género."""
    print("Buscar canción más popular por género")
    print("Ingrese la ruta al archivo CSV (ej: ./cupicharts.csv):")
    ruta = input("> ")
    
    try:
        datos = mod.cargar_cupicharts(ruta)
        print("\nGéneros disponibles:")
        generos = list(datos.keys())
        for i, genero in enumerate(generos, 1):
            print(f"  {i}. {genero}")
        
        genero_buscar = input("\nIngrese el nombre del género: ").strip().lower()
        resultado = mod.cancion_mas_popular_por_genero(datos, genero_buscar)
        
        if resultado is None:
            print(f"No se encontró el género '{genero_buscar}' en los datos cargados.")
        else:
            print(f"\nLa canción más popular del género '{genero_buscar}' es: {resultado}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta}'")
    except Exception as e:
        print(f"Error: {e}")


def mostrar_menu_principal() -> None:
    """Muestra el menú principal de la aplicación."""
    print("\nMenú de opciones:")
    print("1. Cargar archivo CSV de canciones")
    print("2. Buscar canción más popular por género")
    print("3. Salir")


def iniciar_aplicacion() -> None:
    """
    Función principal de la aplicación.
    """
    ejecutando = True
    print("#" * 50)
    print("¡Bienvenido a la aplicación de Cupicharts!")
    print("#" * 50)
    
    while ejecutando:
        mostrar_menu_principal()
        opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
        
        if opcion_elegida == "1":
            ejecutar_cargar_cupicharts()
        elif opcion_elegida == "2":
            ejecutar_cancion_mas_popular()
        elif opcion_elegida == "3":
            print("\n¡Gracias por usar la aplicación de Cupicharts!")
            ejecutando = False
        else:
            print("Opción inválida. Por favor inténtelo de nuevo.")
        
        if ejecutando:
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    iniciar_aplicacion()
