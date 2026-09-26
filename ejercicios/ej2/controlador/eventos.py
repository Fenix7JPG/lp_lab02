# eventos.py
# Traduce los eventos de cada frame a acciones sobre la partida, segun su fase.

import pygame

from controlador import entrada_texto
from modelo.constantes import (BOTON_JUGAR, BOTON_MENU, BOTON_OTRA_PARTIDA,
                              BOTON_SALIR, BOTON_SALIR_FINAL)
from modelo.partida import FASE_GAME_OVER, FASE_JUGANDO, FASE_MENU


def procesar_eventos(partida, eventos):
    # aplica los eventos del frame a la partida; devuelve True si hay que cerrar la ventana
    cerrar_ventana = False

    for evento in eventos:
        if evento.type == pygame.QUIT:
            cerrar_ventana = True

    if partida.fase == FASE_MENU:
        # en el menu solo importan los clics sobre sus dos botones
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if BOTON_JUGAR.collidepoint(evento.pos):
                    partida.reiniciar()
                elif BOTON_SALIR.collidepoint(evento.pos):
                    cerrar_ventana = True

    elif partida.fase == FASE_GAME_OVER:
        # en la derrota, los tres botones deciden el destino
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if BOTON_OTRA_PARTIDA.collidepoint(evento.pos):
                    partida.reiniciar()
                elif BOTON_MENU.collidepoint(evento.pos):
                    partida.ir_al_menu()
                elif BOTON_SALIR_FINAL.collidepoint(evento.pos):
                    cerrar_ventana = True

    if partida.fase == FASE_JUGANDO:
        # la entrada de texto corre tambien en el frame donde arranca la partida
        texto, activa = entrada_texto.actualizar_texto(eventos, partida.palabras_enemigas, partida.texto, partida.activa)
        # las letras nuevas correctas tecleadas cuentan para el WPM
        if len(texto) > len(partida.texto):
            partida.registrar_letras(len(texto) - len(partida.texto))

        # Texto escrito
        partida.texto = texto

        # Palabra objetivo
        partida.activa = activa

    return cerrar_ventana