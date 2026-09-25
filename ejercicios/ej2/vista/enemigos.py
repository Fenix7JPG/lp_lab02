# enemigos.py
# Dibujo de las palabras enemigas: texto, marco, aro de foco y muerte.

import pygame

from vista.colores import COLOR_BLANCO, COLOR_FONDO, COLOR_MARCO, COLOR_ROJO, COLOR_VERDE, mezclar_color

# tamano inicial del aro decorativo del foco
ESCALA_INICIAL = 2.2

# margen interno entre el borde del marco y el texto
PADDING_MARCO = 20


def dibujar_enemigos(screen, palabras_enemigas):
    # dibuja los marcos con su texto
    for palabra in palabras_enemigas:
        dibujar_palabra(palabra, screen)


def dibujar_palabra(palabra, screen):
    # dibuja el marco con el texto (verde = ya escrito)
    if palabra.muriendo == True:
        dibujar_muerte(palabra, screen)
        return

    color_verde, color_blanco, color_marco = colores_de_palabra_si_fallo(palabra)
    superficie_verde, superficie_blanca = renderizar_texto(palabra, color_verde, color_blanco)
    marco = calcular_marco(palabra, superficie_verde, superficie_blanca)

    # fondo del color de la pantalla para tapar lo de atras y borde del color del marco
    pygame.draw.rect(screen, COLOR_FONDO, marco)
    pygame.draw.rect(screen, color_marco, marco, 6)

    dibujar_aro_foco(palabra, screen, color_marco, marco)

    x_texto = marco.x + PADDING_MARCO
    y_texto = marco.y + PADDING_MARCO
    screen.blit(superficie_verde, (x_texto, y_texto))
    screen.blit(superficie_blanca, (x_texto + superficie_verde.get_width(), y_texto))


def colores_de_palabra_si_fallo(palabra):
    # colores del texto y del marco; se tinen de rojo mientras dura el destello de fallo
    factor_fallo = palabra.tiempo_fallo / palabra.DURACION_FALLO
    color_verde = mezclar_color(COLOR_VERDE, COLOR_ROJO, factor_fallo)
    color_blanco = mezclar_color(COLOR_BLANCO, COLOR_ROJO, factor_fallo)
    color_marco = mezclar_color(COLOR_MARCO, COLOR_ROJO, factor_fallo)
    return color_verde, color_blanco, color_marco


def renderizar_texto(palabra, color_verde, color_blanco):
    # parte verde = lo ya escrito; parte blanca = lo que falta por escribir
    parte_verde = palabra.completado_valido
    parte_blanca = palabra.texto[len(parte_verde):]
    superficie_verde = palabra.font.render(parte_verde, True, color_verde)
    superficie_blanca = palabra.font.render(parte_blanca, True, color_blanco)
    return superficie_verde, superficie_blanca


def calcular_marco(palabra, superficie_verde, superficie_blanca):
    # caja del marco: el texto mas el margen fijo alrededor
    ancho_texto = superficie_verde.get_width() + superficie_blanca.get_width()
    alto_texto = palabra.font.get_height()
    return pygame.Rect(palabra.x, palabra.y, ancho_texto + PADDING_MARCO * 2, alto_texto + PADDING_MARCO * 2)


def dibujar_aro_foco(palabra, screen, color_marco, marco):
    # el aro se achica hacia la palabra con grosor fijo (sin desvanecerse)
    if palabra.tiempo_animacion > 0:
        factor_anim = palabra.tiempo_animacion / palabra.DURACION_ANIMACION
        borde = int(marco.height / 2 + (marco.height * ESCALA_INICIAL) * factor_anim)
        pop = marco.inflate(borde, borde)
        pygame.draw.rect(screen, color_marco, pop, 6)


def dibujar_muerte(palabra, screen):
    # marco que crece y desaparece
    factor = palabra.tiempo_muerte / palabra.DURACION_MUERTE

    centro = palabra.centro()
    marco = pygame.Rect(0, 0, palabra.ancho, palabra.alto)
    marco.center = (int(centro[0]), int(centro[1]))

    crece = int((palabra.ancho * 1.2) * (1.0 - factor))
    pop = marco.inflate(crece, crece)

    pygame.draw.rect(screen, COLOR_MARCO, pop, 6)