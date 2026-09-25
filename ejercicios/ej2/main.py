# main.py
# Punto de entrada: arma la ventana, crea la partida y gira el bucle.

import pygame

from controlador.eventos import procesar_eventos
from modelo.constantes import FPS
from modelo.partida import FASE_GAME_OVER, FASE_MENU, Partida
from vista import enemigos, hud, jugador, rayos, ventana


def main():
    # la ventana la arma la vista; el estado y la fase los lleva el modelo
    screen, clock = ventana.crear_ventana()
    partida = Partida()

    cerrar_ventana = False
    while cerrar_ventana == False:
        dt = clock.tick(FPS)

        cerrar_ventana = procesar_eventos(partida, pygame.event.get())

        partida.actualizar(dt)

        ventana.limpiar(screen)
        if partida.fase == FASE_MENU:
            hud.dibujar_menu(screen)
        elif partida.fase == FASE_GAME_OVER and partida.tiempo_muerte >= partida.DURACION_MUERTE_JUGADOR:
            # termino la animacion de muerte: pantalla opaca con el resumen
            hud.dibujar_game_over(screen, partida)
        else:
            rayos.dibujar_rayos(screen, partida)
            enemigos.dibujar_enemigos(screen, partida.palabras_enemigas)
            jugador.dibujar_jugador(screen, partida)
            hud.dibujar_hud(screen, partida)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()