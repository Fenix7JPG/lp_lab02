# Ej 2 - Mecanografia espacial

Juego de mecanografia con pygame: un punto azul (el jugador) en el centro
y palabras-enemigo que se acercan desde los bordes. Destruyes una palabra
escribiendola completa.

## Mecanicas

- El primer caracter correcto activa una palabra; cada caracter correcto
  dispara una bala (la letra viaja hasta la palabra).
- Cada bala que llega causa un impacto; la palabra muere al recibir un
  impacto por cada letra (su marco crece y desaparece).
- Una letra errada borra todo el progreso de esa palabra (verde, balas
  disparadas e impactos) y cancela sus balas en vuelo; al reescribirla,
  cada letra vuelve a disparar.
- Si un enemigo toca al jugador, pierdes: Enter reinicia, ESC sale.
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

## Estructura (patron MVC)

    main.py                        arma la ventana, crea la partida y gira el bucle
    modelo/constantes.py           valores: ventana, colores, jugador, palabras
    modelo/palabras.py             enemigos (PalabraObjetivo), oleadas y sorteo por peso
    modelo/balas.py                balas-caracter y sus impactos
    modelo/partida.py              estado de la partida (puntos, oleada, game over)
    vista/visual.py                ventana, fuentes y dibujo de lo que se ve en pantalla
    controlador/entrada_texto.py   interpreta las teclas escritas
    controlador/game_over.py       teclas de la pantalla de derrota
    controlador/eventos.py         traduce los eventos de cada frame a acciones

El modelo lleva el estado y las reglas y no dibuja; la vista arma la ventana
y dibuja a partir de ese estado; el controlador traduce los eventos a
llamadas de la partida; main solo orquesta el bucle.
