# rayos.py
# Los rayos laser del jugador: verde parpadeante al acertar, rojo al errar.

import pygame

from modelo.constantes import JUGADOR_CX, JUGADOR_CY
from vista.colores import COLOR_FONDO, COLOR_ROJO, COLOR_VERDE, COLOR_BLANCO, mezclar_color

# verde mas claro para el parpadeo del rayo
VERDE_CLARO = mezclar_color(COLOR_VERDE, COLOR_BLANCO, 0.5)

# medio periodo del parpadeo del rayo verde (milisegundos)
PARPADEO_RAYO = 60


def color_del_rayo_verde():
    # el rayo verde parpadea: alterna entre su color y uno mas claro
    if (pygame.time.get_ticks() // PARPADEO_RAYO) % 2 == 0:
        return COLOR_VERDE
    return VERDE_CLARO


def trazar_rayo_laser(screen, desde, hasta, color):
    # halo de laser: linea gruesa tenue (el color mezclado con el fondo)
    # debajo, y el nucleo del color puro encima
    halo = mezclar_color(color, COLOR_FONDO, 0.5)
    x1 = int(desde[0])
    y1 = int(desde[1])
    x2 = int(hasta[0])
    y2 = int(hasta[1])

    pygame.draw.line(screen, halo, (x1, y1), (x2, y2), 18)
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 10)


def dibujar_rayos(screen, partida):
    # rayo laser breve que PARPADEA: verde (alternando con un verde mas
    # claro) hacia la palabra activa o la que acaba de completarse, rojo
    # hacia la que se erro; ambos duran DURACION_RAYO
    for palabra in partida.palabras_enemigas:
        if palabra.tiempo_rayo > 0:
            if palabra is partida.activa or palabra.muriendo == True:
                color = color_del_rayo_verde()
            else:
                color = COLOR_ROJO
            trazar_rayo_laser(screen, (JUGADOR_CX, JUGADOR_CY), palabra.centro(), color)