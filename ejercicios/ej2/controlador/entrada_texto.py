# entrada_texto.py
# Interpreta las teclas del jugador: devuelve (texto, palabra_activa, palabra_errada).

import pygame


# el matching ignora mayusculas y minusculas
def actualizar_texto(eventos, palabras, texto_actual, palabra_activa):
    texto = texto_actual
    activa = palabra_activa
    palabra_errada = None

    for evento in eventos:
        if evento.type == pygame.TEXTINPUT:
            for caracter in evento.text:
                caracter = caracter.lower()
                if texto == "":
                    for palabra in palabras:
                        if palabra.texto.startswith(caracter):
                            activa = palabra
                            texto = caracter
                            break
                elif len(texto) < len(activa.texto):
                    if caracter == activa.texto[len(texto)]:
                        texto = texto + caracter
                    else:
                        # letra errada: se pierde todo el progreso de la palabra
                        activa.perder_progreso()
                        palabra_errada = activa
                        texto = ""
                        activa = None
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto = texto[:-1]
                if texto == "":
                    activa = None

    return texto, activa, palabra_errada