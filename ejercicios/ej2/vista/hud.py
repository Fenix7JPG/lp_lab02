# hud.py
# Fuentes del juego, la linea de estado (con WPM) y la pantalla de derrota.

import pygame

from modelo.constantes import (ALTO, ANCHO, BOTON_JUGAR, BOTON_MENU,
                              BOTON_OTRA_PARTIDA, BOTON_SALIR, BOTON_SALIR_FINAL)
from vista.colores import (COLOR_FONDO, COLOR_MARCO, COLOR_PERDISTE,
                          COLOR_TEXTO)

# fuentes de la vista: se crean una sola vez en preparar_fuentes y nunca cambian
FUENTE_HUD = None
FUENTE_FINAL = None

# tamano de las fuentes (el mundo va a 2x)
TAM_FUENTE_HUD = 68
TAM_FUENTE_FINAL = 120

# textos de la interfaz
TITULO_MENU = "WordStrike"
TITULO_DERROTA = "DERROTA"
ETIQUETA_JUGAR = "Jugar"
ETIQUETA_SALIR = "Salir"
ETIQUETA_OTRA_PARTIDA = "Otra partida"
ETIQUETA_VOLVER_MENU = "Volver al menu"


def preparar_fuentes():
    # crea las fuentes del hud y de la pantalla final (una sola vez)
    global FUENTE_HUD, FUENTE_FINAL
    FUENTE_HUD = pygame.font.Font(None, TAM_FUENTE_HUD)
    FUENTE_FINAL = pygame.font.Font(None, TAM_FUENTE_FINAL)


def dibujar_boton(screen, rect, etiqueta):
    # boton simple: fondo oscuro, borde azul y texto centrado
    pygame.draw.rect(screen, COLOR_FONDO, rect)
    pygame.draw.rect(screen, COLOR_MARCO, rect, 6)
    texto = FUENTE_HUD.render(etiqueta, True, COLOR_TEXTO)
    screen.blit(texto, texto.get_rect(center=rect.center))


def dibujar_menu(screen):
    # pantalla de inicio: titulo y botones Jugar/Salir
    titulo = FUENTE_FINAL.render(TITULO_MENU, True, COLOR_TEXTO)
    screen.blit(titulo, titulo.get_rect(center=(ANCHO / 2, 300)))

    dibujar_boton(screen, BOTON_JUGAR, ETIQUETA_JUGAR)
    dibujar_boton(screen, BOTON_SALIR, ETIQUETA_SALIR)


def dibujar_hud(screen, partida):
    # dibuja la linea de oleada, puntos y WPM (usa la fuente interna de la vista)
    texto = FUENTE_HUD.render("Oleada " + str(partida.oleada) + "   Puntos: " + str(partida.puntos) + "   WPM: " + str(partida.wpm()), True, COLOR_TEXTO)
    screen.blit(texto, (16, 12))


def dibujar_game_over(screen, partida):
    # pantalla opaca de derrota con el contenido centrado
    screen.fill(COLOR_FONDO)

    msg1 = FUENTE_FINAL.render(TITULO_DERROTA, True, COLOR_PERDISTE)
    screen.blit(msg1, msg1.get_rect(center=(ANCHO / 2, ALTO / 2 - 240)))
    msg2 = FUENTE_HUD.render("Puntos: " + str(partida.puntos) + "   Oleada: " + str(partida.oleada) + "   WPM: " + str(partida.wpm()), True, COLOR_TEXTO)
    screen.blit(msg2, msg2.get_rect(center=(ANCHO / 2, ALTO / 2 - 120)))

    dibujar_boton(screen, BOTON_OTRA_PARTIDA, ETIQUETA_OTRA_PARTIDA)
    dibujar_boton(screen, BOTON_MENU, ETIQUETA_VOLVER_MENU)
    dibujar_boton(screen, BOTON_SALIR_FINAL, ETIQUETA_SALIR)