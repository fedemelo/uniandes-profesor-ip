import modulo as mod


def ejecutar_sumar_posiciones_iguales() -> None:
    """Función que recibe los datos y ejecuta la función de sumar posiciones de elementos iguales."""
    print("Sumador de posiciones de elementos iguales consecutivos")
    print("Ingrese los números separados por comas (ej: 1,2,3,3,4,5):")
    entrada = input("> ")
    
    lista = convertir_entrada_a_lista(entrada)
    suma = mod.sumar_posiciones_iguales_consecutivos(lista)
    
    if suma == -1:
        print("No se encontraron elementos consecutivos iguales")
    else:
        print(f"La suma de las posiciones de los últimos elementos consecutivos iguales es: {suma}")


def ejecutar_mejor_estudiante() -> None:
    """Función que recibe la materia y ejecuta la función de mejor estudiante por materia."""
    print("Buscador del mejor estudiante por materia")
    
    estudiantes = [
        {"codigo": "202012345", "nombre": "Ana García", "IP": 4.5, "calculo": 3.8, 
         "escritura": 4.2, "constitucion": 4.0},
        {"codigo": "202098765", "nombre": "Carlos López", "IP": 4.5, "calculo": 4.1, 
         "escritura": 3.9, "constitucion": 4.3},
        {"codigo": "202055555", "nombre": "Beatriz Ruiz", "IP": 4.2, "calculo": 4.5, 
         "escritura": 4.0, "constitucion": 3.7},
        {"codigo": "202011111", "nombre": "Diego Martínez", "IP": 3.8, "calculo": 4.2, 
         "escritura": 4.5, "constitucion": 4.1},
        {"codigo": "202022222", "nombre": "Elena Rodríguez", "IP": 4.0, "calculo": 3.9, 
         "escritura": 4.3, "constitucion": 4.5}
    ]
    
    materia = input("Ingrese el nombre de la materia: ")
    codigo_mejor = mod.mejor_estudiante_por_materia(estudiantes, materia)
    print(f"El mejor estudiante en {materia} es: {codigo_mejor}")


def ejecutar_contar_apariciones() -> None:
    """Función que recibe los datos y ejecuta la función de contar apariciones de sublista."""
    print("Contador de apariciones de sublista")
    print("Ingrese los números de la lista principal separados por comas:")
    entrada_principal = input("> ")
    print("Ingrese los números de la sublista separados por comas:")
    entrada_sublista = input("> ")
    
    lista_principal = convertir_entrada_a_lista(entrada_principal)
    sublista = convertir_entrada_a_lista(entrada_sublista)
    
    cantidad = mod.contar_apariciones(lista_principal, sublista)
    print(f"La sublista aparece {cantidad} veces en la lista principal")


def convertir_entrada_a_lista(entrada: str) -> list:
    """Función auxiliar que convierte una entrada de números separados por comas en una lista de enteros."""
    lista = []
    numeros = entrada.replace(' ', '').split(',')
    for num in numeros:
        lista.append(int(num.strip()))
    return lista


def mostrar_menu() -> None:
    print("\n\nOPCIONES")
    print("1. Sumar posiciones de elementos iguales consecutivos")
    print("2. Mejor estudiante por materia")
    print("3. Contar apariciones de sublista")
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
            ejecutar_sumar_posiciones_iguales()
        elif opcion == 2:
            ejecutar_mejor_estudiante()
        elif opcion == 3:
            ejecutar_contar_apariciones()
        elif opcion == 4:
            continuar = False
        else:
            print("La opción elegida no es válida, intente nuevamente.")


iniciar_aplicacion()
