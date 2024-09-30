# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Tres en raya

import numpy as np
from metodos import jugar, mostrar_tablero, comprobar_ganador
from config import CASILLA, TURNOS

tablero = np.full((3, 3), CASILLA)
jugando = True
jugador = 0;

print("Bienvenidos al 3 en raya o tic-tac-toe. ¡Poneos competitivos y a jugar!")
mostrar_tablero(tablero)

while (jugando):
    retorno = jugar(TURNOS[jugador], tablero)
    if (retorno != "error"):
        mostrar_tablero(tablero)
        resultado = comprobar_ganador(tablero)
        if resultado:
            if resultado == "empate":
                print("¡Habéis empatado!")
            else:
                print(f"¡El ganador es {resultado}!")
            jugando = False
        else:
            jugador = (jugador + 1) % 2  # Alternar entre 0 y 1

