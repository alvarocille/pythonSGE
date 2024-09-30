import numpy as np
from config import CASILLA

def mostrar_tablero(tablero):
    for i in range(len(tablero)):
        for j in range (len(tablero[i])):
            print(tablero[i][j], end = "")
        print()

def jugar(turno, tablero):
    print(f"Turno de {turno}. Indique la celda en la que quiere jugar.")
    print("Fila (1-3):")
    fila = int(input()) - 1
    print("Columna (1-3):")
    columna = int(input()) - 1
    if (fila >= 0 and fila <= 2 and columna >= 0 and columna <= 2) and (tablero[fila][columna] == CASILLA):
        tablero[fila][columna] = turno
    else:
        return "error"
    return "ok"

def comprobar_ganador(tablero):
    # Comprobar filas y columnas
    for i in range(3):
        if tablero[i, 0] == tablero[i, 1] == tablero[i, 2] != CASILLA:
            return tablero[i, 0]
        if tablero[0, i] == tablero[1, i] == tablero[2, i] != CASILLA:
            return tablero[0, i]
    
    # Comprobar diagonales
    if tablero[0, 0] == tablero[1, 1] == tablero[2, 2] != CASILLA:
        return tablero[0, 0]
    if tablero[0, 2] == tablero[1, 1] == tablero[2, 0] != CASILLA:
        return tablero[0, 2]

    # Comprobar empate (si no hay más casillas vacías)
    if np.all(tablero != CASILLA):
        return "empate"
    
    return None
