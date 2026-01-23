def buscar_par_en_cuadrante(matriz: list, color: str) -> int:
    n = len(matriz)
    mitad_filas = n // 2
    tercio_cols = n // 3
    
    cuadrantes = {
        "rojo": (0, mitad_filas, 0, tercio_cols),
        "verde": (0, mitad_filas, tercio_cols, 2 * tercio_cols),
        "azul": (0, mitad_filas, 2 * tercio_cols, n),
        "amarillo": (mitad_filas, n, 0, tercio_cols),
        "naranja": (mitad_filas, n, tercio_cols, 2 * tercio_cols),
        "morado": (mitad_filas, n, 2 * tercio_cols, n)
    }
    
    if color not in cuadrantes:
        return None
    
    fila_inicio, fila_fin, col_inicio, col_fin = cuadrantes[color]
    
    for i in range(fila_inicio, fila_fin):
        for j in range(col_inicio, col_fin):
            if matriz[i][j] % 2 == 0:
                return matriz[i][j]
    
    return None


def dibujar_t(matriz: list) -> None:
    n = len(matriz)
    col_medio = n // 2
    
    for i in range(n):
        for j in range(n):
            matriz[i][j] = ' '
    
    for j in range(n):
        matriz[0][j] = '-'
    
    for i in range(1, n):
        matriz[i][col_medio] = '|'


def producto_mas_vendido_ciudad(info_ventas: tuple, ciudad: str) -> tuple:
    matriz, productos, ciudades = info_ventas
    
    if ciudad not in ciudades:
        return (None, None)
    
    indice_ciudad = ciudades.index(ciudad)
    max_producto = productos[0]
    max_ventas = matriz[0][indice_ciudad]
    
    for i in range(len(matriz)):
        ventas = matriz[i][indice_ciudad]
        if ventas > max_ventas:
            max_producto = productos[i]
            max_ventas = ventas
    
    return (max_producto, max_ventas)


def primer_introvertido_hablara(salon: list) -> tuple:
    n = len(salon)
    
    for i in range(n):
        for j in range(n):
            if salon[i][j] == 1:
                diag_inf_izq_existe = i + 1 < n and j - 1 >= 0
                diag_inf_der_existe = i + 1 < n and j + 1 < n
                
                if not (diag_inf_izq_existe and diag_inf_der_existe):
                    continue
                
                tiene_extrovertidos_atras = (salon[i + 1][j - 1] == 2 and 
                                             salon[i + 1][j + 1] == 2)
                
                if not tiene_extrovertidos_atras:
                    continue
                
                pos_adelante_existe = i - 1 >= 0
                if pos_adelante_existe:
                    tiene_extrovertido_adelante = salon[i - 1][j] == 2
                else:
                    tiene_extrovertido_adelante = False
                
                if not tiene_extrovertido_adelante:
                    return (i, j)
    
    return (None, None)


def imprimir_ejemplo_matriz_pintada_t() -> None:
    matriz = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
    ]

    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        matriz[i][j] = ' '

    n = len(matriz)
    col_medio = n // 2
    
    for j in range(n):
        matriz[0][j] = '—'
    
    for i in range(1, n):
        matriz[i][col_medio] = '|'

    print("Ejemplo de matriz pintada T:")
    for row in matriz:
        print(''.join(row))
    

if __name__ == "__main__":
    imprimir_ejemplo_matriz_pintada_t()
