# eventos.py
# Traduce los eventos de cada frame a acciones sobre la partida.

import pygame

from controlador import entrada_texto
from controlador.game_over import decision_game_over


def procesar_eventos(partida, eventos):
    # aplica los eventos del frame a la partida; devuelve True si hay que cerrar la ventana
    cerrar_ventana = False

    for evento in eventos:
        if evento.type == pygame.QUIT:
            cerrar_ventana = True

    if partida.game_over == True:
        decision = decision_game_over(eventos)
        if decision == "salir":
            cerrar_ventana = True
        elif decision == "reiniciar":
            partida.reiniciar()

    if partida.game_over == False:
        # la entrada de texto corre tambien en el frame del reinicio (igual que antes)
        texto, activa, palabra_errada = entrada_texto.actualizar_texto(eventos, partida.palabras_enemigas, partida.texto, partida.activa)
        partida.texto = texto
        partida.activa = activa
        if palabra_errada is not None:
            # las balas ya volando de esa palabra se cancelan (su progreso se perdio)
            partida.cancelar_balas_de(palabra_errada)

    return cerrar_ventana