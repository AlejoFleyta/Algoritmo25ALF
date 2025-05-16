#Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
#verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
#usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
#las siguientes actividades:
#a.determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
#además mostrar el nombre de dichas películas;
#b.mostrar los modelos que quedaron dañados, sin perder información de la pila.
#c. eliminar los modelos de los trajes destruidos mostrando su nombre;
#d.un modelo de traje puede usarse en más de una película y en una película se pueden usar
#más de un modelo de traje, estos deben cargarse por separado;
#e.agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
#f.mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y “Capitan America: Civil War”.

pila = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"},
    {"modelo": "Mark XL", "pelicula": "Iron Man 3", "estado": "Destruido"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Dañado"},
]

def buscar_hulkbuster(pila): 
    peliculas_hulkbuster = []
    for traje in pila:
        if traje["modelo"] == "Mark XLIV":
            peliculas_hulkbuster.append(traje["pelicula"])
            return peliculas_hulkbuster
        return None
def mostraer_dañados(pila):
    trajes_dañados = []
    for traje in pila:
        if traje["estado"] == "Dañado":
            trajes_dañados.append(traje)
        return trajes_dañados

def eliminar_destruidos(pila):
    trajes_destruidos = []
    for traje in pila:
        if traje["estado"] == "Destruido":
            trajes_destruidos.append(traje)
            pila.remove(traje)
    return trajes_destruidos

def agregar_mark_lxxxv(pila):
    nuevo_traje = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Dañado"}
    for traje in pila:
        if traje["modelo"] == nuevo_traje["modelo"] and traje["pelicula"] == nuevo_traje["pelicula"]:
            return "El modelo ya existe en la pelicula"
        pila.append(nuevo_traje)
    return "Modelo agregado correctamente"
def mostrar_trajes_spiderman_civilwar(pila):
    trajes_spiderman_civilwar = []
    for traje in pila:
        if traje["pelicula"] == "Spider" and "Civil War":
            trajes_spiderman_civilwar.append(traje)
        return trajes_spiderman_civilwar 
    
    
    peliculas_hulkbuster = buscar_hulkbuster(pila)
    if peliculas_hulkbuster:
        print("El modelo Mark XLIV (Hulkbuster) fue utilizando en las peliculas:")
        for pelicula in peliiculas_hulkbuster:
            print(f"- {pelicula}")
    else:
        print("El modelo Mark XLIV (Hulkbuster) no fue utilizado en ninguna pelicula.")
    trajes_dañados = mostraer_dañados(pila)
    print("Trajes dañados:")
    for traje in trajes_dañados:
        print(f"- {traje['modelo']} ({traje['pelicula']})")
        trajes_destruidos = eliminar_destruidos(pila)
        print("Trajes destruidos:")
        for traje in trajes_destruidos:
            print(f"- {traje['modelo']} ({traje['pelicula']})")
            agregar_mark_lxxxv(pila)
            print("Modelo Mark LXXXV agregado correctamente.")
        trajes_spiderman_civilwar = mostrar_trajes_spiderman_civilwar(pila)
        print("Trajes utilizados en") 
        for traje in trajes_spiderman_civilwar:
            print(f"- {traje['modelo']} ({traje['pelicula']})")


    
