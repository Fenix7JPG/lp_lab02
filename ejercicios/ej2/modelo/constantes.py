# constantes.py
# Valores del mundo que comparten las capas: tamano, jugador, botones y palabras.

import pygame

# el mundo del juego: pantalla completa lo muestra tal cual
ANCHO = 1920
ALTO = 1080

FPS = 60

JUGADOR_CX = ANCHO / 2
JUGADOR_CY = ALTO / 2
JUGADOR_RADIO = 44

# rectangulos de los botones: la vista los dibuja y el controlador los clickea
# (coordenadas del mundo 2x; el controlador multiplica la posicion del clic)
BOTON_JUGAR = pygame.Rect(ANCHO / 2 - 240, 500, 480, 120)
BOTON_SALIR = pygame.Rect(ANCHO / 2 - 240, 660, 480, 120)
BOTON_OTRA_PARTIDA = pygame.Rect(ANCHO / 2 - 240, 520, 480, 110)
BOTON_MENU = pygame.Rect(ANCHO / 2 - 190, 650, 380, 110)
BOTON_SALIR_FINAL = pygame.Rect(ANCHO / 2 - 240, 780, 480, 110)

# todas las palabras posibles del juego
PALABRAS = [            "abanico", "abeja", "aceite", "aceituna", "acordeon", "aguja",
            "ajedrez", "alce", "alfiler", "almohada", "alza", "amapola",
            "amarillo", "ancho", "ancla", "anillo", "antena", "anzuelo",
            "apio", "arana", "arbol", "arco", "ardilla", "arena",
            "arma", "armario", "armonica", "arpa", "arroz", "asiento",
            "atun", "auto", "avion", "avioneta", "azucar", "azul",
            "bahia", "balanza", "balcon", "balon", "bambu", "banana",
            "banano", "bandeja", "barba", "barco", "barril", "bateria",
            "baul", "bolsa", "bombilla", "borcegui", "bordado", "bosque",
            "bota", "bote", "botella", "boton", "brisa", "brocha",
            "brujula", "bufanda", "buho", "buitre", "burbuja", "buzon",
            "caballo", "cable", "cabra", "cacerola", "cactus", "cadena",
            "caja", "cajuela", "calabaza", "calcetin", "caldera", "cama",
            "camino", "camion", "camioneta", "camisa", "camiseta", "campana",
            "canal", "canasta", "cancha", "canela", "canguro", "canoa",
            "cantaro", "capucha", "cara", "caracol", "carburo", "carcasa",
            "cargador", "carne", "carpeta", "carreta", "cartera", "cartucho",
            "cascabel", "cascada", "cascaron", "casco", "castillo", "castor",
            "caverna", "cebolla", "cebra", "ceja", "ceniza", "cereal",
            "cerro", "cetro", "chicle", "chimenea", "chubasco", "cielo",
            "ciervo", "cigarrillo", "cincel", "cinta", "cinturon", "ciruela",
            "cisne", "cisterna", "citara", "ciudad", "clavel", "clavo",
            "coco", "codo", "cofre", "colcha", "colegio", "colina",
            "color", "cometa", "conejo", "contrasena", "copa", "corazon",
            "corbata", "corcho", "cordon", "corneta", "corona", "corral",
            "correa", "cortina", "costa", "cuadro", "cuchara", "cuchillo",
            "cuello", "cuerda", "cuerno", "cueva", "culebra", "dado",
            "dardo", "dedal", "dedo", "delfin", "delta", "dia",
            "diablo", "diamante", "diente", "dificil", "disco", "domino",
            "dona", "dormilon", "dulce", "duna", "eco", "elefante",
            "embudo", "empanada", "enchufe", "eneldo", "ensalada", "erizo",
            "escalera", "escoba", "escudo", "esferico", "espejo", "espinaca",
            "esponja", "esquina", "establo", "estatua", "estilo", "estrella",
            "estufa", "falda", "faldon", "farol", "fecha", "felino",
            "flauta", "flecha", "flor", "florero", "foca", "fogata",
            "fondo", "forma", "frijol", "fruta", "fuente", "funda",
            "galleta", "gancho", "garua", "gato", "gema", "gol",
            "goma", "guitarra", "gusano", "hacha", "hada", "harina",
            "helado", "hierro", "higo", "hilo", "hinojo", "hoja",
            "hombre", "hormiga", "horno", "hueso", "huevo", "humo",
            "huracan", "idioma", "iguana", "iman", "isla", "jabali",
            "jabon", "jaguar", "jamon", "jardin", "jarron", "jaula",
            "jefe", "jirafa", "joya", "juego", "jugo", "juguete",
            "koala", "labio", "ladera", "ladrillo", "lagarto", "lago",
            "laguna", "lana", "lancha", "lanza", "lapiz", "lava",
            "lavanda", "leccion", "leche", "leopardo", "libro", "licor",
            "lienzo", "ligero", "lima", "limon", "lino", "linterna",
            "lirio", "llama", "llave", "llegada", "lluvia", "lobo",
            "loma", "lucero", "lucha", "luna", "lupa", "luz",
            "machete", "madera", "madrugada", "maiz", "manantial", "mandarina",
            "mango", "manzana", "mapa", "maquina", "mar", "maraton",
            "marco", "marea", "margen", "mariposa", "marisco", "martillo",
            "mascara", "masilla", "mata", "mate", "mayo", "mecha",
            "medalla", "medicina", "melocoton", "melodia", "melon", "menta",
            "mermelada", "mesa", "metal", "metro", "miel", "mieles",
            "molde", "molino", "moneda", "mono", "monte", "muralla",
            "murcielago", "muro", "musgo", "musica", "naipe", "naranja",
            "nariz", "navaja", "neblina", "nectar", "niebla", "nieve",
            "nivel", "nogal", "nube", "nueces", "nuez", "numero",
            "oboe", "ocaso", "oceano", "ola", "olivo", "olmo",
            "opera", "organo", "orilla", "orquidea", "oso", "oveja",
            "oxido", "pajaro", "palabra", "palacio", "palma", "palmera",
            "palo", "pan", "panel", "pantalon", "pantano", "papiro",
            "paraiso", "parque", "parte", "paso", "pastel", "pata",
            "patio", "pato", "pavoreal", "pecho", "pedazo", "peine",
            "pelo", "pelota", "pera", "percha", "perdiz", "perla",
            "pescado", "peso", "pez", "piano", "picante", "piedra",
            "piel", "pimienta", "pincel", "pino", "pintura", "pinza",
            "pipa", "pistola", "pizarra", "plancha", "planeta", "plata",
            "plato", "playa", "pluma", "poblado", "policia", "pomelo",
            "poste", "pozo", "pradera", "precio", "premio", "pueblo",
            "puente", "puerta", "puerto", "pulga", "pulpo", "puma",
            "punto", "quebrada", "queso", "quiosco", "radio", "raiz",
            "rama", "rana", "rapido", "raqueta", "raton", "rayo",
            "realeza", "recuerdo", "regla", "reina", "reino", "reloj",
            "remo", "reno", "rescoldo", "rio", "roble", "roca",
            "rodilla", "ropero", "rosa", "rueda", "ruta", "sabana",
            "salchicha", "salero", "salmon", "sandia", "sarten", "sauce",
            "sello", "selva", "semaforo", "semilla", "sendero", "serpiente",
            "sierra", "silla", "sillon", "sitio", "sol", "sombrero",
            "sonaja", "sonido", "sopa", "soplete", "suave", "submarino",
            "sur", "tabla", "taladro", "tallo", "tambor", "tango",
            "tanque", "tapa", "tapete", "tarro", "taxi", "taza",
            "teatro", "techo", "tecla", "tejado", "tela", "telefono",
            "tenaza", "tenis", "terreno", "tetera", "tierra", "tijeras",
            "timbre", "tinta", "toalla", "tobogan", "tomate", "topo",
            "tormenta", "torneo", "toronja", "torre", "tortuga", "tranvia",
            "trazo", "trebol", "tren", "tribu", "triciclo", "trigo",
            "trofeo", "trombon", "trompeta", "tronco", "tuberia", "tulipan",
            "tumba", "tunel", "turbina", "uva", "vagon", "valle",
            "vapor", "vaso", "vecino", "vela", "velero", "ventana",
            "ventisca", "verano", "verde", "veredicto", "vertedero", "vestido",
            "via", "viaje", "victoria", "vidrio", "viento", "vinagre",
            "violeta", "violin", "yate", "yema", "yugo", "zanahoria",
            "zapato", "zarza", "zorro", "zorzal", "zumo"]
