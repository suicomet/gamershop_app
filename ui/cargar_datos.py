from ui.models import Categoria, Juego


datos = {
    "Aventura": [
        ("Ori and the Blind Forest", "Un pequeño espíritu entrañable se embarca en una misión para salvar el bosque con más ternura que un gato con capa.", 13990),
        ("Uncharted 4: El desenlace del ladrón", "Nathan Drake vuelve a hacer parkour, encontrar tesoros y romper cosas. Porque claro, ¿qué podría salir mal?", 22000),
        ("The Last of Us Parte II Remastered", "Venganza, hongos, lágrimas y más tensión que cuando ves a tu ex con alguien mejor.", 49990),
        ("Horizon Zero Dawn", "Cazadora pelirroja vs dinosaurios robóticos. Pura acción postapocalíptica con vistas increíbles.", 19990)
    ],
    "Terror": [
        ("Phasmophobia", "Caza fantasmas con tus amigos... hasta que todos salgan gritando por el micro.", 12000),
        ("Silent Hill", "Niebla, monstruos y traumas. ¿Qué más se puede pedir en un paseo por el pueblo?", 4990),
        ("Mouthwashing", "Terror psicológico en un mundo tan raro que hasta tu cepillo de dientes da miedo.", 7500),
        ("Silent Hill 2", "El clásico del horror donde ir por una carta lleva a un espiral emocional de proporciones épicas.", 14990)
    ],
    "Free to Play": [
        ("League of Legends", "Te unes por diversión, te quedas por el tilt. El MOBA que todos juegan y todos odian.", 0),
        ("Fortnite", "Construye, dispara, baila… y vuelve a construir. Un caos con estilo y skins.", 0),
        ("Marvel Rivals", "Los héroes de Marvel se agarran a combos en partidas que parecen películas de acción.", 0),
        ("Overwatch 2", "Héroes, estrategia, tiros… y algún que otro grito en el micro.", 0)
    ],
    "Estrategia": [
        ("Age of Empires II", "Cuando lanzar arqueros y aldeanos era más importante que estudiar historia.", 8990),
        ("StarCraft II", "Humanos, alienígenas e insectos galácticos luchando por el control del universo.", 15990),
        ("Total War: Warhammer III", "Un simulador de guerra con dragones, demonios y caos total.", 35990),
        ("Civilization VI", "Fundar un imperio, investigar ciencias... o simplemente conquistar todo con Gandhi.", 19990)
    ],
    "Deportes": [
        ("FIFA 23", "Patea el balón, grita goles, y luego grita aún más cuando te anotan uno en el 90.", 29990),
        ("NBA 2K24", "Dunks, triples y más drama que una final de campeonato.", 34990),
        ("Rocket League", "Fútbol... pero con autos voladores. Porque claro, ¿por qué no?", 0),
        ("Tony Hawk's Pro Skater 1+2", "Vuelve el rey del skate con trucos imposibles y nostalgia pura.", 17990)
    ]
}

# Crea categorías y juegos
for nombre_cat, juegos in datos.items():
    categoria, created = Categoria.objects.get_or_create(nombre=nombre_cat)
    for nombre_juego, descripcion, precio in juegos:
        Juego.objects.get_or_create(
            nombre=nombre_juego,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria
        )

print("✅ Categorías y juegos agregados con éxito.")
