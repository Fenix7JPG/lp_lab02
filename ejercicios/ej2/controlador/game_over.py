# game_over.py
# Teclas de la pantalla de game over: Enter reinicia, ESC sale.

import pygame


def decision_game_over(eventos):
    # devuelve "reiniciar" (Enter), "salir" (ESC) o None
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                return "reiniciar"
            if evento.key == pygame.K_ESCAPE:
                return "salir"
    return None