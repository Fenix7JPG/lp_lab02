# partida.py
# Estado y reglas de la partida: puntos, oleada, WPM, game over y enemigos.

from modelo.constantes import JUGADOR_CX, JUGADOR_CY
from modelo.palabras import iniciar_oleada

# fases de la partida
FASE_MENU = "menu"
FASE_JUGANDO = "jugando"
FASE_GAME_OVER = "game_over"


class Partida:

    # la animacion de muerte del jugador dura estos milisegundos
    DURACION_MUERTE_JUGADOR = 700

    def __init__(self):
        # estado de la partida: antes eran variables sueltas de main
        self.puntos = 0
        self.oleada = 1
        self.fase = FASE_MENU
        self.tiempo_transcurrido = 0
        self.tiempo_muerte = 0
        self.letras_acertadas = 0
        self.montar_oleada()

    def montar_oleada(self):
        # estado limpio para una oleada nueva
        self.texto = ""
        self.activa = None
        self.palabras_enemigas = iniciar_oleada(self.oleada)

    def reiniciar(self):
        # Jugar / Otra partida: partida desde cero y directo a jugar
        self.puntos = 0
        self.oleada = 1
        self.fase = FASE_JUGANDO
        self.tiempo_transcurrido = 0
        self.tiempo_muerte = 0
        self.letras_acertadas = 0
        self.montar_oleada()

    def ir_al_menu(self):
        # Volver al menu: la proxima partida arrancara desde cero
        self.fase = FASE_MENU

    def registrar_letras(self, cantidad):
        # cuenta las letras correctas tecleadas (alimentan el WPM)
        self.letras_acertadas = self.letras_acertadas + cantidad

    def wpm(self):
        # palabras por minuto: cada 5 letras acertadas valen una palabra
        if self.tiempo_transcurrido <= 0:
            return 0
        minutos = self.tiempo_transcurrido / 60000.0
        return int((self.letras_acertadas / 5.0) / minutos)

    def actualizar(self, dt):
        if self.fase == FASE_GAME_OVER:
            # congelado: el tiempo solo corre para la animacion de muerte
            self.tiempo_muerte = self.tiempo_muerte + dt
            return

        if self.fase != FASE_JUGANDO:
            return

        # avanza un frame de la partida
        self.tiempo_transcurrido = self.tiempo_transcurrido + dt

        # pintar el verde ANTES de soltar la palabra (asi queda congelado)
        for palabra in self.palabras_enemigas:
            completado = ""
            if palabra is self.activa:
                completado = self.texto
            palabra.definir_completado(completado)
            palabra.actualizar(dt)

        # al completar la palabra muere al instante y suma su punto
        if self.activa is not None and self.texto == self.activa.texto:
            self.activa.iniciar_muerte()
            self.puntos = self.puntos + 1
            self.texto = ""
            self.activa = None

        sobrevivientes = []
        for palabra in self.palabras_enemigas:
            if palabra.termino_muerte() == False:
                sobrevivientes.append(palabra)
        self.palabras_enemigas = sobrevivientes

        for palabra in self.palabras_enemigas:
            if palabra.avanzar(dt, JUGADOR_CX, JUGADOR_CY) == True:
                self.fase = FASE_GAME_OVER
                self.texto = ""
                self.activa = None
                break

        if not self.palabras_enemigas:
            self.oleada = self.oleada + 1
            self.montar_oleada()