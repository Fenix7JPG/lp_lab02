# visual.py
# Dibujo puro: cada funcion dibuja una cosa, sin decidir nada.

import pygame

from modelo.constantes import (ALTO, ANCHO, COLOR_FONDO, COLOR_JUGADOR,
                              COLOR_PERDISTE, COLOR_TEXTO, COLOR_TEXTO_SUAVE,
                              COLOR_VELO, JUGADOR_CX, JUGADOR_CY, JUGADOR_RADIO)

# colores de dibujo de las palabras enemigas (antes eran de PalabraObjetivo)
COLOR_MARCO = (128, 0, 200)
COLOR_VERDE = (0, 200, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_ROJO = (220, 30, 30)

# tamano inicial del aro decorativo del foco
ESCALA_INICIAL = 2.2

# margen interno entre el borde del marco y el texto
PADDING_MARCO = 10


def mezclar_color(color_a, color_b, factor):
    # mezcla dos colores; factor 0 devuelve color_a y 1 devuelve color_b
    if factor < 0.0:
        factor = 0.0
    if factor > 1.0:
        factor = 1.0

    r_a, g_a, b_a = color_a
    r_b, g_b, b_b = color_b

    r_nuevo = int(r_a + (r_b - r_a) * factor)
    g_nuevo = int(g_a + (g_b - g_a) * factor)
    b_nuevo = int(b_a + (b_b - b_a) * factor)

    return (r_nuevo, g_nuevo, b_nuevo)


def crear_fuentes():
    # devuelve (fuente_hud, fuente_final, fuente_bala)
    return pygame.font.Font(None, 34), pygame.font.Font(None, 60), pygame.font.Font(None, 30)


def crear_ventana():
    # arma la ventana del juego y su reloj; devuelve (screen, clock)
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mecanografia espacial")
    clock = pygame.time.Clock()
    pygame.key.set_repeat(500, 50)
    return screen, clock


def limpiar(screen):
    # pinta el fondo
    screen.fill(COLOR_FONDO)


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

    # fondo negro para tapar lo de atras y borde del color del marco
    pygame.draw.rect(screen, (0, 0, 0), marco)
    pygame.draw.rect(screen, color_marco, marco, 3)

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
        pygame.draw.rect(screen, color_marco, pop, 3)


def dibujar_muerte(palabra, screen):
    # marco que crece y desaparece
    factor = palabra.tiempo_muerte / palabra.DURACION_MUERTE

    centro = palabra.centro()
    marco = pygame.Rect(0, 0, palabra.ancho, palabra.alto)
    marco.center = (int(centro[0]), int(centro[1]))

    crece = int((palabra.ancho * 1.2) * (1.0 - factor))
    pop = marco.inflate(crece, crece)

    pygame.draw.rect(screen, COLOR_MARCO, pop, 3)


def dibujar_jugador(screen):
    # dibuja el punto azul del jugador
    pygame.draw.circle(screen, COLOR_JUGADOR, (int(JUGADOR_CX), int(JUGADOR_CY)), JUGADOR_RADIO)


def dibujar_bala(bala, screen, fuente):
    # la bala se dibuja como su caracter (antes era Bala.dibujar)
    sup = fuente.render(bala.caracter, True, bala.COLOR)
    screen.blit(sup, sup.get_rect(center=(int(bala.x), int(bala.y))))


def dibujar_balas(screen, balas, fuente):
    for bala in balas:
        dibujar_bala(bala, screen, fuente)


def dibujar_hud(screen, fuente_hud, puntos_partida, oleada_actual):
    # dibuja la linea de oleada y puntos
    texto = fuente_hud.render("Oleada " + str(oleada_actual) + "   Puntos: " + str(puntos_partida), True, COLOR_TEXTO)
    screen.blit(texto, (16, 12))


def dibujar_game_over(screen, fuente_final, fuente_hud, puntos_partida, oleada_actual):
    # dibuja la pantalla de derrota
    velo = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    velo.fill(COLOR_VELO)
    screen.blit(velo, (0, 0))

    msg1 = fuente_final.render("PERDISTE", True, COLOR_PERDISTE)
    msg2 = fuente_hud.render("Puntos: " + str(puntos_partida) + "   Oleada: " + str(oleada_actual), True, COLOR_TEXTO)
    msg3 = fuente_hud.render("Enter para reiniciar - ESC para salir", True, COLOR_TEXTO_SUAVE)
    screen.blit(msg1, msg1.get_rect(center=(ANCHO / 2, ALTO / 2 - 50)))
    screen.blit(msg2, msg2.get_rect(center=(ANCHO / 2, ALTO / 2 + 10)))
    screen.blit(msg3, msg3.get_rect(center=(ANCHO / 2, ALTO / 2 + 50)))