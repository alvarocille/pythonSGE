# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Tres en raya

import numpy as np

CASILLA = '🟨'
TURNOS = ['⭕', '❎']

tablero = np.full((3, 3), CASILLA)

def mostrar_tablero(tablero):
    for i in range(len(tablero)):
        for j in range (len(tablero[i])):
            print(tablero[i][j], end = "")
        print()

print("Bienvenido al juego de tres en raya.")
mostrar_tablero(tablero)

def jugar(turno, tablero):
    print(f"Turno de {turno}. Indique la celda en la que quiere jugar.")
    print("Fila (1-3):")
    fila = int(input()) - 1
    print("Columna (1-3):")
    columna = int(input()) - 1
    if (tablero[fila][columna] == CASILLA):
        tablero[fila][columna] = turno
    else:
        return "error"
    return "ok"

jugando = True
jugador = 0;

while (jugando):
    retorno = jugar(TURNOS[jugador], tablero)
    if (retorno != "error"):
        mostrar_tablero(tablero)
        if (jugador == 0):
            jugador += 1
        else:
            jugador -= 1

