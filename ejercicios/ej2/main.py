# main.py
# Punto de entrada: arma la ventana, crea la partida y gira el bucle.

import pygame

from controlador.eventos import procesar_eventos
from modelo.constantes import FPS
from modelo.partida import Partida
from vista import visual


def main():
    # la ventana la arma la vista; el estado lo lleva el modelo
    screen, clock = visual.crear_ventana()
    fuente_hud, fuente_final, fuente_bala = visual.crear_fuentes()
    partida = Partida()

    cerrar_ventana = False
    while cerrar_ventana == False:
        dt = clock.tick(FPS)

        cerrar_ventana = procesar_eventos(partida, pygame.event.get())

        if partida.game_over == False:
            partida.actualizar(dt)

        visual.limpiar(screen)
        visual.dibujar_enemigos(screen, partida.palabras_enemigas)
        visual.dibujar_balas(screen, partida.balas_jugador, fuente_bala)
        visual.dibujar_jugador(screen)
        visual.dibujar_hud(screen, fuente_hud, partida.puntos, partida.oleada)

        if partida.game_over == True:
            visual.dibujar_game_over(screen, fuente_final, fuente_hud, partida.puntos, partida.oleada)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()