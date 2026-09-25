# Ej 2 - Mecanografia espacial

Juego de mecanografia con pygame: un punto azul (el jugador) en el centro
y palabras-enemigo que se acercan desde los bordes. Destruyes una palabra
escribiendola completa.

## Mecanicas

- El primer caracter correcto activa una palabra y dispara un rayo laser
  verde breve (nucleo con halo tenue) que parpadea entre su color y uno
  mas claro; del jugador a su centro. Si se escribe rapido, el rayo se ve
  continuo parpadeando. Cada letra acertada repite el disparo y pinta la
  letra en verde.
- Al completar la palabra, muere al instante (su marco crece y desaparece)
  y suma un punto.
- Una letra errada dispara un rayo rojo breve hacia la palabra (mismo
  destello corto que el verde) y borra su progreso (el texto vuelve a
  blanco).
- El HUD muestra la oleada, los puntos y el WPM: cada 5 letras acertadas
  valen una palabra, dividido entre los minutos jugados (0 al empezar).
- Al abrir el juego hay un menu con el titulo y dos botones: Jugar y
  Salir (clic del mouse).
- Si un enemigo toca al jugador, pierdes. En la pantalla de derrota hay
  tres botones: Otra partida, Volver al menu y Salir (clic del mouse).
- Cada oleada suma cantidad de enemigos (hasta 7) y velocidad. El largo de
  palabra no tiene tope: todas las palabras del pool pueden salir en
  cualquier oleada, pero el sorteo es por peso segun el largo ideal de la
  oleada (crece con n), asi las oleadas altas inclinan hacia palabras mas
  largas. La dificultad de fondo la define el pool elegido.

## Configuración del entorno

    py -3.12 -m venv .venv
    .venv\Scripts\activate
    pip install pygame

## Ejecutar

    python main.py

## Paleta (Watermelon, Almond Cream, Onyx, Blue Bell y Shamrock)

- Onyx (#121619): fondo de la pantalla, velo de la derrota y relleno de
  los botones.
- Almond Cream (#eae0d5): todo el texto (HUD, menu, botones) y la parte de
  la palabra que falta por escribir.
- Watermelon (#ee4266): el error (rayo rojo y tinte de fallo) y PERDISTE.
- Blue Bell (#2892d7): el punto del jugador, los marcos de las palabras,
  el aro de foco, el marco de muerte y los bordes de los botones.
- Shamrock (#109648): el texto ya escrito y el rayo verde, que parpadea
  entre Shamrock y su mezcla con Almond Cream.

## Pantalla completa

- El juego abre en PANTALLA COMPLETA: set_mode((ANCHO, ALTO),
  FULLSCREEN | SCALED). El mundo 1920x1080 se escala solo a la pantalla del
  sistema (SDL lo hace en GPU, sin costo por frame, y mapea el mouse solo:
  los botones se clickean sin conversiones).
- Los valores absolutos (fuentes 72/68/120, RADIO_TOQUE 92, JUGADOR_RADIO
  44, velocidad de enemigos min(36+20*(n-1), 180), botones, PADDING_MARCO
  20, bordes 6, rayo 18/4) estan en coordenadas del mundo 1920x1080.
- En pantallas de otra resolucion, SCALED ajusta el mundo manteniendo la
  proporcion (barras si el aspecto difiere).

## Derrota: animacion de muerte y pantalla opaca

- Al morir, la partida entra en FASE_GAME_OVER pero el resumen NO aparece
  todavia: durante DURACION_MUERTE_JUGADOR (700 ms, en partida.py) la
  escena queda congelada y el jugador se achica hasta desaparecer
  mientras se va poniendo rojo (dibujar_jugador con mezclar_color).
- El tiempo de la animacion lo acumula partida.tiempo_muerte: main llama
  actualizar SIEMPRE y actualizar decide que avanzar por fase (menu:
  nada, jugando: todo el juego, derrota: solo el timer de la animacion).
- Pasados los 700 ms, main dibuja solo hud.dibujar_game_over: fondo
  opaco Onyx y todo el contenido centrado (PERDISTE, estadisticas y los
  3 botones). COLOR_VELO salio de la paleta (sin usos).

## Estructura (patron MVC)

    main.py                        crea la partida y gira el bucle
    modelo/constantes.py           valores del mundo que comparten las capas: tamano,
                                   jugador, botones y palabras
    modelo/palabras.py             enemigos (PalabraObjetivo), oleadas y sorteo por peso
    modelo/partida.py              estado y fases (menu/jugando/derrota), puntos, WPM
    vista/colores.py               TODA la paleta (los colores son de la vista) y mezclar_color
    vista/ventana.py               crear_ventana y limpiar el fondo
    vista/rayos.py                 rayos laser verde/rojo
    vista/enemigos.py              dibujo de las palabras enemigas
    vista/jugador.py               dibujo del punto del jugador
    vista/hud.py                   fuentes, textos, menu, hud (con WPM) y pantalla de derrota
    controlador/entrada_texto.py   interpreta las teclas escritas
    controlador/eventos.py         traduce los eventos de cada frame a acciones

El modelo lleva el estado y las reglas y no dibuja; la vista arma la ventana
y dibuja a partir de ese estado; el controlador traduce los eventos a
llamadas de la partida; main solo orquesta el bucle.
