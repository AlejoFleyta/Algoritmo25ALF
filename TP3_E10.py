#Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#resolver las siguientes actividades:
#a.escribir una función que elimine de la cola todas las notificaciones de Facebook;
#b.escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
#c.utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from collections import deque

class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora  # formato 'HH:MM'
        self.app = app
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.hora} - {self.app}: {self.mensaje}"


class Cola:
    def __init__(self):
        self.items = deque()

    def insertar(self, dato):
        self.items.append(dato)

    def mover_frente(self):
        if not self.vacia():
            return self.items.popleft()
        return None

    def vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)

    def barrido(self):
        for item in list(self.items):
            print(item)
def eliminar_facebook(cola):
    cola_aux = Cola()
    while not cola.vacia():
        dato = cola.mover_frente()
        if dato.app != 'Facebook':
            cola_aux.insertar(dato)
    return cola_aux

def mostrar_twitter_python(cola):
    cola_aux = Cola()
    while not cola.vacia():
        dato = cola.mover_frente()
        if dato.app == 'Twitter' and 'Python' in dato.mensaje:
            print(dato)
        cola_aux.insertar(dato)
    return cola_aux

def notificaciones_en_rango(cola):
    pila = []
    cola_aux = Cola()
    while not cola.vacia():
        dato = cola.mover_frente()
        if '11:43' <= dato.hora <= '15:57':
            pila.append(dato)
        cola_aux.insertar(dato)
    return len(pila), pila, cola_aux

cola = Cola()
cola.insertar(Notificacion('11:55', 'Facebook', 'Nueva publicación'))
cola.insertar(Notificacion('15:00', 'Twitter', 'Curso de Python!'))
cola.insertar(Notificacion('09:30', 'Instagram', 'Nueva historia'))
cola.insertar(Notificacion('08:20', 'Facebook', 'Nuevo evento'))
cola.insertar(Notificacion('16:00', 'Twitter', 'Python es genial'))


cola = eliminar_facebook(cola)
print("\nCola sin Facebook:")
cola.barrido()

print("\nNotificaciones de Twitter con 'Python':")
cola = mostrar_twitter_python(cola)


cantidad, pila, cola = notificaciones_en_rango(cola)
print(f"\nCantidad de notificaciones entre 11:43 y 15:57: {cantidad}")
for n in pila:
    print(n)
