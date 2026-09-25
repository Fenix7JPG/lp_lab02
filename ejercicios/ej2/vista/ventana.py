# ventana.py
# Abre el juego en pantalla completa y limpia el fondo.

import pygame

from modelo.constantes import ALTO, ANCHO
from vista.colores import COLOR_FONDO
from vista.hud import preparar_fuentes


def crear_ventana():
    # abre pantalla completa: el mundo 1920x1080 se escala solo a la pantalla
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN | pygame.SCALED)
    pygame.display.set_caption("Mecanografia espacial")
    clock = pygame.time.Clock()
    pygame.key.set_repeat(500, 50)
    preparar_fuentes()
    return screen, clock


def limpiar(screen):
    # pinta el fondo
    screen.fill(COLOR_FONDO)