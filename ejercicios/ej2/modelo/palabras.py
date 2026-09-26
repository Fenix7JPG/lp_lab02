# palabras.py
# Enemigos: naves con etiqueta que se acercan al jugador, mueren con un impacto por caracter.

import math
import random

import pygame

from modelo.constantes import ALTO, ANCHO, PALABRAS


def _posicion_borde():
    # posicion aleatoria en un borde de la ventana
    margen = 60
    lado = random.randint(0, 3)
    if lado == 0:
        return random.randint(margen, ANCHO - margen), margen
    if lado == 1:
        return ANCHO - margen, random.randint(margen, ALTO - margen)
    if lado == 2:
        return random.randint(margen, ANCHO - margen), ALTO - margen
    return margen, random.randint(margen, ALTO - margen)


def _choca_con(palabra, palabras):
    # True si el rect de palabra toca a alguna otra
    rect = palabra.rect()
    for otra in palabras:
        if rect.colliderect(otra.rect()) == True:
            return True
    return False


def peso_de_palabra(texto, oleada):
    # peso de una palabra en el sorteo de la oleada
    # el largo ideal crece con la oleada (3, 4, 5, 6...); afinar aqui
    largo_ideal = 2 + oleada
    # cada letra de distancia al largo ideal resta 3 de peso; afinar aqui
    distancia = abs(len(texto) - largo_ideal)
    # peso minimo 1: ninguna palabra queda fuera del sorteo
    return max(1, 10 - 3 * distancia)


def iniciar_oleada(n):
    # genera y devuelve una lista nueva de enemigos para la oleada n
    nueva = []
    cantidad = min(2 + n, 7)
    velocidad = min(36 + 20 * (n - 1), 180)

    usadas = set()
    for _ in range(cantidad):
        # candidatas: todas las palabras con inicial aun libre en la oleada
        candidatos = []
        for t in PALABRAS:
            if t[0] not in usadas:
                candidatos.append(t)
        if not candidatos:
            break

        # bolsa de sorteo: cada palabra entra tantas veces como su peso,
        # asi las cercanas al largo ideal de la oleada salen mas seguido
        bolsa = []
        for t in candidatos:
            peso = peso_de_palabra(t, n)
            for _ in range(peso):
                bolsa.append(t)

        texto = random.choice(bolsa)
        usadas.add(texto[0])

        pos = _posicion_borde()
        prueba = PalabraObjetivo(texto, pos, velocidad)
        intentos = 0
        while intentos < 20 and _choca_con(prueba, nueva) == True:
            pos = _posicion_borde()
            prueba = PalabraObjetivo(texto, pos, velocidad)
            intentos = intentos + 1
        nueva.append(prueba)

    return nueva


class PalabraObjetivo:

    TAM_FUENTE_BASE = 72
    DURACION_ANIMACION = 350
    DURACION_RAYO = 120
    DURACION_FALLO = 500
    DURACION_MUERTE = 300
    RADIO_TOQUE = 92

    def __init__(self, texto, pos, velocidad):
        self.texto = texto
        self.font = pygame.font.Font(None, self.TAM_FUENTE_BASE)
        self.velocidad = velocidad

        # geometria fija: fuente y texto no cambian
        self.ancho = self.font.size(texto)[0] + 40
        self.alto = self.font.get_height() + 40

        self.completado_valido = ""
        self.muriendo = False
        self.tiempo_muerte = 0

        self.tiempo_animacion = 0
        self.tiempo_rayo = 0
        self.tiempo_fallo = 0

        self.x, self.y = 0, 0
        self.poner_centro(pos[0], pos[1])

    def centro(self):
        return self.x + self.ancho / 2, self.y + self.alto / 2

    def poner_centro(self, cx, cy):
        self.x = cx - self.ancho / 2
        self.y = cy - self.alto / 2

    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def avanzar(self, dt_ms, jugador_cx, jugador_cy):
        # se acerca al jugador; True si lo toca
        if self.muriendo == True:
            return False
        dist = self.velocidad * dt_ms / 1000.0
        px, py = self.centro()
        dx = jugador_cx - px
        dy = jugador_cy - py
        d = math.hypot(dx, dy)
        if d > dist:
            px = px + dx / d * dist
            py = py + dy / d * dist
        else:
            px, py = jugador_cx, jugador_cy
        self.poner_centro(px, py)
        return d <= self.RADIO_TOQUE

    def definir_completado(self, nuevo_completado):
        # fija la parte verde escrita; ignora si muere o ya se completo
        if self.muriendo == True:
            return
        # el verde ya completo se congela (no vuelve a blanco)
        if self.completado_valido == self.texto:
            return
        if self.texto.startswith(nuevo_completado):
            if len(self.completado_valido) == 0 and len(nuevo_completado) > 0:
                # al enfocar la palabra arranca la animacion del aro
                self.tiempo_animacion = self.DURACION_ANIMACION
            self.completado_valido = nuevo_completado

    def disparar_rayo(self):
        # cada letra acertada dispara un rayo breve hacia la palabra
        self.tiempo_rayo = self.DURACION_RAYO

    def perder_progreso(self):
        # una letra errada borra el progreso y dispara el rayo rojo
        self.completado_valido = ""
        self.tiempo_rayo = self.DURACION_RAYO
        self.tiempo_fallo = self.DURACION_FALLO

    def iniciar_muerte(self):
        # activa la animacion de muerte
        if self.muriendo == True:
            return
        self.muriendo = True
        self.tiempo_muerte = self.DURACION_MUERTE

    def termino_muerte(self):
        # True cuando la animacion de muerte termino
        return self.muriendo == True and self.tiempo_muerte == 0

    def actualizar(self, dt):
        # descuenta los tiempos de animaciones
        if self.tiempo_rayo > 0:
            self.tiempo_rayo = max(0, self.tiempo_rayo - dt)
        if self.tiempo_animacion > 0:
            self.tiempo_animacion = max(0, self.tiempo_animacion - dt)
        if self.tiempo_fallo > 0:
            self.tiempo_fallo = max(0, self.tiempo_fallo - dt)
        if self.muriendo == True:
            self.tiempo_muerte = max(0, self.tiempo_muerte - dt)