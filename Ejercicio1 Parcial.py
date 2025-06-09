#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:

    #funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
    #funcion recursiva para listar los superheroes de la lista.
Superheroes = [ "Spiderman", "Wolverine", "Capitan America", "Iron Man", "Thor", "Deadpool", "Batman", "Superman", 
"Robin", "Supergirl", "Batgirl" , "Powergirl", "Starfire", "Raven", "Hulk"]

posicion = int
posicion = -1
primero = 0
ultimo = len(Superheroes) -1
buscado = "Capitan America"
Superheroes.sort()
def Buscar(Superheroes,buscado):    # Funcion de listar y buscar
 
    if (Superheroes != ""):
     print("La Lista es")
     print(Superheroes)
     buscado = "Capitan America"
     posicion = -1
     primero = 0
     ultimo = len(Superheroes)-1
     while (primero <= ultimo) and (posicion == -1):
      medio = (primero + ultimo) // 2
      
      if  (Superheroes[medio] == buscado):
        posicion = medio
      elif buscado < Superheroes[medio]:
        ultimo = medio - 1
      else:
        primero = medio + 1 
     
     return "El capitan America se encuentra en la posicion" ,posicion
     



    else:
     print("la lista esta vacia")

Encontrado = Buscar(Superheroes, buscado)
print(Encontrado)

    


    
