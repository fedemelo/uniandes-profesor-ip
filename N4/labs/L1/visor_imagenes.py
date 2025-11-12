# -*- coding: utf-8 -*-
"""
Ejemplo Nivel 4: Visor de imágenes

Temas:

* Matrices

@author: Cupi2
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def normalizar_color(color: float) -> float:
    """ Normaliza el color a [0.0, 1.0]
    En ocasiones, los componentes RGB pueden estar en el rango [0, 255]. Esta función normaliza el color a [0.0, 1.0].
    Parámetros:
        color (float) Color a normalizar.
    Retorno:
        float: Color normalizado.
    """
    if color <= 1.0:
        return color
    return color / 255.0


def cargar_imagen(ruta_imagen: str) -> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz (M,N) con la imagen cargada como lista de listas de tuplas.
              Cada tupla contiene los 3 componentes RGB del píxel.
    """
    imagen_array = mpimg.imread(ruta_imagen)
    imagen = []
    for i in range(len(imagen_array)):
        fila = []
        for j in range(len(imagen_array[i])):
            pixel = imagen_array[i][j][:3]  # RGB, ignorar alpha si existe
            pixel_normalizado = (normalizar_color(pixel[0]), 
                                 normalizar_color(pixel[1]), 
                                 normalizar_color(pixel[2]))
            fila.append(pixel_normalizado)
        imagen.append(fila)
    
    return imagen


def visualizar_imagen(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list) Matriz (M,N) como lista de listas de tuplas con la imagen a visualizar.
    """
    plt.close('all')
    plt.imshow(imagen)
    plt.show()


def convertir_negativo(imagen: list) -> list:
    """  Convierte la imagen en negativo.
    El negativo se calcula restando cada componente RGB de 1.0 (el valor máximo).
    Parámetros:
        imagen (list) Matriz (M,N) como lista de listas de tuplas con la imagen a convertir a negativo.
    Retorno:
        list: Nueva matriz con la imagen en negativo.
    """
    imagen_nueva = []
    for i in range(len(imagen)):
        fila_nueva = []
        for j in range(len(imagen[i])):
            pixel_original = imagen[i][j]
            # Calcular el negativo de cada componente
            r_nuevo = 1.0 - pixel_original[0]
            g_nuevo = 1.0 - pixel_original[1]
            b_nuevo = 1.0 - pixel_original[2]
            # Crear nuevo pixel como tupla
            pixel_nuevo = (r_nuevo, g_nuevo, b_nuevo)
            fila_nueva.append(pixel_nuevo)
        imagen_nueva.append(fila_nueva)
    
    return imagen_nueva


def reflejar_imagen(imagen: list) -> list:
    """Refleja la imagen verticalmente.
    Consiste en intercambiar las columnas enteras de la imagen, de las finales a las iniciales.
    Parámetros:
        imagen (list) Matriz (M,N) como lista de listas de tuplas con la imagen a reflejar.
    Retorno:
        list: Nueva matriz con la imagen reflejada.
    """
    return imagen


def binarizar_imagen(imagen: list, umbral: float) -> list:
    """ Binariza la imagen.
    Consiste en llevar cada píxel de una imagen a negro o blanco.
    Para ello se requiere un umbral: si el promedio de los componentes RGB del píxel está por encima o es igual al umbral se lleva a blanco, y si está por debajo se lleva a negro.
    Parámetros:
        imagen (list) Matriz (M,N) como lista de listas de tuplas con la imagen a binarizar.
        umbral (float) Umbral de la binarización (valor entre 0.0 y 1.0).
    Retorno:
        list: Nueva matriz con la imagen binarizada.
    """
    return imagen


def convertir_a_grises(imagen: list) -> list:
    """ Convierte la imagen a escala de grises.
    Para ello promedia los componentes de cada píxel y crea un nuevo color donde cada componente (RGB) tiene el valor de dicho promedio.
    Parámetros:
        imagen (list) Matriz (M,N) como lista de listas de tuplas con la imagen a convertir a grises.
    Retorno:
        list: Nueva matriz con la imagen en escala de grises.
    """
    return imagen


def convolucion_imagen(imagen: list) -> list:
    """ Opera la imagen con una matriz de convolución.
    Aplica una matriz de convolución 3x3 a cada píxel de la imagen, utilizando sus vecinos
    para calcular el nuevo valor de cada componente RGB.
    Parámetros:
        imagen (list) Matriz (M,N) como lista de listas de tuplas con la imagen a convolucionar.
    Retorno:
        list: Nueva matriz con la imagen convolucionada.
    """
    # Matriz de convolución 3x3
    # Opción 1: Afilado (Sharpen) - Resalta detalles y bordes
    convolucion = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    
    # Otras opciones para experimentar:
    # Opción 2: Desenfoque (Blur) - Suaviza la imagen
    # convolucion = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    
    # Opción 3: Detección de bordes - Resalta contornos
    # convolucion = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    
    # Opción 4: Relieve (Emboss) - Efecto de relieve
    # convolucion = [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]
    
    return imagen

