# colores.py
# Toda la paleta del juego y la funcion para mezclar colores.

# Onyx: fondo de la pantalla y relleno de los botones
COLOR_FONDO = (18, 22, 25)

# Almond Cream: todo el texto de la interfaz y la parte pendiente de la palabra
COLOR_TEXTO = (234, 224, 213)
COLOR_BLANCO = (234, 224, 213)

# Watermelon: el error (rayo rojo, tinte de fallo) y PERDISTE
COLOR_ROJO = (238, 66, 102)
COLOR_PERDISTE = (238, 66, 102)

# Blue Bell: el jugador, los marcos de las palabras y los bordes de los botones
COLOR_JUGADOR = (40, 146, 215)
COLOR_MARCO = (40, 146, 215)

# Shamrock: el texto ya escrito y el rayo verde
COLOR_VERDE = (16, 150, 72)


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