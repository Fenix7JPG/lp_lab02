# partida.py
# Estado y reglas de la partida completa: puntos, oleada, game over y enemigos.

from modelo import balas
from modelo.constantes import JUGADOR_CX, JUGADOR_CY
from modelo.palabras import iniciar_oleada


class Partida:

    def __init__(self):
        # estado de la partida: antes eran variables sueltas de main
        self.puntos = 0
        self.oleada = 1
        self.game_over = False
        self.montar_oleada()

    def montar_oleada(self):
        # estado limpio para una oleada nueva
        self.texto = ""
        self.activa = None
        self.balas_jugador = []
        self.palabras_enemigas = iniciar_oleada(self.oleada)

    def reiniciar(self):
        # Enter en la pantalla de game over: partida desde cero
        self.puntos = 0
        self.oleada = 1
        self.game_over = False
        self.montar_oleada()

    def disparar_balas_nuevas(self):
        # cada caracter nuevo escrito dispara una bala hacia la palabra activa
        if self.activa is not None:
            faltan = len(self.texto) - self.activa.balas_disparadas
            nuevas = self.texto[len(self.texto) - faltan:]
            for caracter in nuevas:
                self.balas_jugador = balas.disparar(self.balas_jugador, (JUGADOR_CX, JUGADOR_CY), self.activa, caracter)

    def cancelar_balas_de(self, palabra):
        # quita las balas en vuelo de esa palabra (su progreso se perdio)
        quedan = []
        for bala in self.balas_jugador:
            if bala.objetivo is not palabra:
                quedan.append(bala)
        self.balas_jugador = quedan

    def actualizar(self, dt):
        # avanza un frame completo de la partida (solo se llama sin game over)
        self.disparar_balas_nuevas()

        # pintar el verde ANTES de soltar la palabra (asi queda congelado)
        for palabra in self.palabras_enemigas:
            completado = ""
            if palabra is self.activa:
                completado = self.texto
            palabra.definir_completado(completado)
            palabra.actualizar(dt)

        # soltar la palabra despues de pintar su verde
        if self.activa is not None and self.texto == self.activa.texto:
            self.texto = ""
            self.activa = None

        self.balas_jugador, destruidas = balas.avanzar(self.balas_jugador, dt)
        self.puntos = self.puntos + len(destruidas)

        sobrevivientes = []
        for palabra in self.palabras_enemigas:
            if palabra.termino_muerte() == False:
                sobrevivientes.append(palabra)
        self.palabras_enemigas = sobrevivientes

        for palabra in self.palabras_enemigas:
            if palabra.avanzar(dt, JUGADOR_CX, JUGADOR_CY) == True:
                self.game_over = True
                self.texto = ""
                self.activa = None
                break

        if not self.palabras_enemigas:
            self.oleada = self.oleada + 1
            self.montar_oleada()