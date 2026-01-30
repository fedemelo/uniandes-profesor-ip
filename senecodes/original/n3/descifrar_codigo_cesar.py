# -*- coding: utf-8 -*-
def descifrar_codigo_cesar(texto_cifrado: str, corrimiento: int)->str:
    """ Descifrar código César
    Parámetros:
      texto_cifrado (str): El texto cifrado que se quiere descifrar. Puede incluir minúsculas, mayúsculas,
                           espacios y otros caracteres especiales. Sólo tendrá letras del alfabeto inglés.
      corrimiento (int): El corrimiento (cantidad de lugares que se corre una letra) que se usó para generar
                         el cifrado, y por ende debe usarse para descrifar el mensaje
    Retorno:
      str: La cadena descifrada, incluyendo espacios y caracteres especiales que tenía la original.
    """
    texto=list(texto_cifrado)
    textofin=[]
    #Las mayúculas en ascii están en el intervalo [65,90]; minúsculas en [97,122].
    for letra in texto: #Lista con todos los caracteres del texto.
        if ord(letra) in range(65,91) or ord(letra) in range(97,123): #Si el caracter es una letra, ya sea mayúscula o minúscula.
            codascii=ord(letra) #Se obtiene su código ascii.
            nuevocod=codascii-corrimiento #Se le resta el corrimiento para descifrar.
            if nuevocod not in range(65,91) and ord(letra) in range(65,91): #Si tras la resta no está en el rango de las mayúsculas siendo mayúscula.
                nuevaletra=chr(nuevocod+26) #Toca ir al final, o sea 26 letras adelante.
            elif nuevocod not in range(97,123) and ord(letra) in range(97,123): #Si tras la resta no está en el rango de las minúsculas siendo minúscula.
                nuevaletra=chr(nuevocod+26) #Toca ir al final, o sea 26 letras adelante.
            elif nuevocod in range(65,91) or nuevocod in range(97,123): #Si tras la resta sigue en el rango de las letras, bien.
                nuevaletra=chr(nuevocod) #La nueva letra es la correspondiente a la resta.
        else:
            nuevaletra=letra
        textofin.append(nuevaletra)
    return "".join(textofin) #Devuelve la lista pero unida como un string.