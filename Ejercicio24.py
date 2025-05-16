#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#a.determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b.determinar los personajes que participaron en más de 5 películas de la saga, además indicar 
# la cantidad de películas en la que aparece;
#c.determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d.mostrar todos los personajes cuyos nombre empiezan con C, D y G.

pila = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Hawkeye", "peliculas": 6},
    {"nombre": "Loki", "peliculas": 5},
    {"nombre": "Shang-Chi", "peliculas": 1},
    {"nombre": "Moon Knight", "peliculas": 0},
    {"nombre": "Rocket Raccoon", "peliculas": 4},
    {"nombre": "Groot", "peliculas": 3},
]


def posicion_personaje(pila, nombre):
    for i, personaje in enumerate(reversed(pila), 1):
        if personaje["nombre"] == nombre:
            return i
    return -1


def personajes_mas_de_5_peliculas(pila):
    personajes = []
    for personaje in pila:
        if personaje["peliculas"] > 5:
            personajes.append((personaje["nombre"], personaje["peliculas"]))
    return personajes


def peliculas_viuda_negra(pila):
    for personaje in pila:
        if personaje["nombre"] == "Black Widow":
            return personaje["peliculas"]
    return 0


def personajes_iniciales(pila, letras):
    personajes = []
    for personaje in pila:
        if personaje["nombre"][0] in letras:
            personajes.append(personaje["nombre"])
    return personajes


print("Posición de Rocket Raccoon:", posicion_personaje(pila, "Rocket Raccoon"))
print("Posición de Groot:", posicion_personaje(pila, "Groot"))

print("\nPersonajes con más de 5 películas:")
for nombre, cant in personajes_mas_de_5_peliculas(pila):
    print(f"- {nombre} ({cant})")

print("\nPelículas de la Viuda Negra:", peliculas_viuda_negra(pila))

print("\nPersonajes que empiezan con C, D y G:")
for nombre in personajes_iniciales(pila, ['C', 'D', 'G']):
    print(f"- {nombre}")