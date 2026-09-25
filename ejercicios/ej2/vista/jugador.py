# jugador.py
# Dibujo del punto del jugador (con su animacion de muerte).

import pygame

from modelo.constantes import JUGADOR_CX, JUGADOR_CY, JUGADOR_RADIO
from vista.colores import COLOR_JUGADOR, COLOR_ROJO, mezclar_color


def dibujar_jugador(screen, partida):
    # punto azul del jugador; al morir se achica y se va poniendo rojo
    factor = partida.tiempo_muerte / partida.DURACION_MUERTE_JUGADOR
    if factor >= 1.0:
        return
    radio = int(JUGADOR_RADIO * (1.0 - factor))
    if radio < 1:
        return
    color = mezclar_color(COLOR_JUGADOR, COLOR_ROJO, factor)
    pygame.draw.circle(screen, color, (int(JUGADOR_CX), int(JUGADOR_CY)), radio)