def invertir_cadena(cadena: str) -> str:
    """
    Invierte una cadena de caracteres.
    """
    cadena_invertida = ""
    i = len(cadena) - 1
    
    while i >= 0:
        cadena_invertida += cadena[i]
        i -= 1
    
    return cadena_invertida


def histograma_caracteres(cadena: str) -> dict:
    """
    Crea un histograma de los caracteres en una cadena.
    
    Args:
        cadena: La cadena a analizar
        
    Returns:
        Un diccionario con cada carácter como llave y su frecuencia como valor
    """
    histograma = {}
    i = 0
    
    while i < len(cadena):
        caracter = cadena[i]
        histograma[caracter] = histograma.get(caracter, 0) + 1
        i += 1
    
    return histograma


def verificar_simetria_vocales(cadena: str) -> bool:
    """
    Verifica si las vocales en una cadena forman un patrón simétrico.
    
    Args:
        cadena: La cadena a analizar
        
    Returns:
        True si las vocales forman un patrón simétrico, False en caso contrario
    """
    i = 0
    j = len(cadena) - 1

    es_simetrico = True
    while i < j and es_simetrico:
        if cadena[i].lower() not in "aeiou":
            i += 1
        elif cadena[j].lower() not in "aeiou":
            j -= 1
        elif cadena[i].lower() != cadena[j].lower():
            es_simetrico = False
        else:
            i += 1
            j -= 1
    
    return es_simetrico
