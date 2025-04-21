#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:
#a.sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;
#b.determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#c.Utilizar un vector para representar la mochila.

mochila = ['linterna', 'sable de luz', 'agua', 'comida', 'mapa']

def usar_la_fuerza(mochila):
    if not mochila:
        return None, 0 
    objeto = mochila.pop(0)
    if objeto == 'sable de luz':
        return objeto, 1
    else:
        sable, count = usar_la_fuerza(mochila)
        if sable:
            return sable, count + 1
        else:
            return None, count + 1

# bloque principal
sable, count = usar_la_fuerza(mochila)
if sable:
    print(f"Encontré un {sable} después de sacar {count} objetos.")
else:
    print("No encontré un sable de luz en la mochila.")