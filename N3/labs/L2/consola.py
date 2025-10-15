import modulo as mod


def ejecutar_invertir_cadena() -> None:
    print("Inversor de cadenas de caracteres")
    cad = input("Por favor ingrese la cadena: ")
    inversa = mod.invertir_cadena(cad)
    print("La cadena invertida es:", inversa)


def ejecutar_histograma_caracteres() -> None:
    print("Generador de histograma de caracteres")
    cad = input("Por favor ingrese la cadena: ")
    histograma = mod.histograma_caracteres(cad)
    print("El histograma de caracteres es:", histograma)


def ejecutar_verificar_simetria_vocales() -> None:
    print("Verificador de simetría de vocales")
    cad = input("Por favor digite la cadena: ")
    es_simetrico = mod.verificar_simetria_vocales(cad)
    if es_simetrico:
        print("Las vocales en la cadena", cad, "sí forman un patrón simétrico")
    else:
        print("Las vocales en la cadena", cad, "no forman un patrón simétrico")


def mostrar_menu() -> None:
    print("\n\nOPCIONES")
    print("1. Invertir cadena")
    print("2. Histograma de caracteres")
    print("3. Verificar simetría de vocales")
    print("4. Salir")


def iniciar_aplicacion() -> None:
    """
    Esta función mantiene el programa funcionando hasta que el usuario seleccione la opción para salir.
    La función primero debe mostrar el menú de opciones usando la función mostrar_menu().
    A continuación, debe solicitarle al usuario una opción.
    Según lo que haya seleccionado el usuario, debe llamar a una de las funciones cuyo nombre inicia con ejecutar_
    Si el usuario seleccionó la opción de Salir, la función debe terminar su ejecución para que el programa pueda terminar.
    Si el usuario seleccionó cualquier otra opción, después de ejecutar la opción seleccionada se debe volver
    a mostrar el menú de opciones y se debe repetir el proceso.
    """

    continuar = True

    while continuar:
        mostrar_menu()
        opcion = int(input("Ingrese la opción que desea ejecutar: "))

        if opcion == 1:
            ejecutar_invertir_cadena()
        elif opcion == 2:
            ejecutar_histograma_caracteres()
        elif opcion == 3:
            ejecutar_verificar_simetria_vocales()
        elif opcion == 4:
            continuar = False
        else:
            print("La opción elegida no es válida, intente nuevamente.")


iniciar_aplicacion()
