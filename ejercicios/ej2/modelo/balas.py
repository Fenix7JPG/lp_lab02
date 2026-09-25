# balas.py
# Balas del jugador: la bala es el caracter tecleado viajando a la palabra.

import math


class Bala:

    VELOCIDAD = 520.0
    COLOR = (255, 220, 80)

    def __init__(self, x, y, objetivo, caracter):
        self.x = x
        self.y = y
        self.objetivo = objetivo
        self.caracter = caracter

    def avanzar(self, dt_ms):
        # vuela hacia su objetivo; True al llegar
        cx, cy = self.objetivo.centro()
        dist = self.VELOCIDAD * dt_ms / 1000.0
        dx = cx - self.x
        dy = cy - self.y
        d = math.hypot(dx, dy)
        if d <= dist:
            self.x = cx
            self.y = cy
            return True
        self.x = self.x + dx / d * dist
        self.y = self.y + dy / d * dist
        return False


def disparar(balas, origen, objetivo, caracter):
    # devuelve la lista de balas con una bala nueva
    objetivo.registrar_disparo()
    nueva = []
    for bala in balas:
        nueva.append(bala)
    nueva.append(Bala(origen[0], origen[1], objetivo, caracter))
    return nueva


def avanzar(balas, dt_ms):
    # avanza las balas; devuelve (balas_vivas, palabras_destruidas)
    vivas = []
    destruidas = []
    for bala in balas:
        if bala.avanzar(dt_ms) == True:
            if bala.objetivo.recibir_impacto() == True:
                destruidas.append(bala.objetivo)
        else:
            vivas.append(bala)
    return vivas, destruidas