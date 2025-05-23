#20. Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro),que resuelva las siguientes actividades:
#a.agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos sonlos siguientes:
#I.automóviles (tarifa $47);
#II.camionetas (tarifa $59);
#III.camiones (tarifa $71);
#IV.colectivos (tarifa $64).
#b.realizar la atención de las cabinas, considerando las tarifas del punto anterior.
#c.determinar qué cabina recaudó mayor cantidad de pesos ($).
#d.determinar cuántos vehículos de cada tipo se atendieron en cada cola.

from collections import deque
import random

I = 'automoviles'
II = 'camionetas'
III = 'camiones'
IV = 'colectivos'

class Vehiculo:
    def __init__(self, tipo, tarifa):
        self.tipo = tipo
        self.tarifa = tarifa

    def __str__(self):
        return f"Vehiculo tipo: {self.tipo}, tarifa: {self.tarifa}"

class Cabina:
    def __init__(self):
        self.cola = deque()
        self.recaudacion = 0
        self.contador = {I: 0, II: 0, III: 0, IV: 0}

    def agregar_vehiculo(self, vehiculo):
        self.cola.append(vehiculo)
        self.contador[vehiculo.tipo] += 1
        self.recaudacion += vehiculo.tarifa

    def atender_vehiculo(self):
        if self.cola:
            return self.cola.popleft()
        return None

    def cabina_recaudacion(self):
        return self.recaudacion

    def vehiculos_atendidos(self):
        return self.contador

    def cabina_vacia(self):
        return len(self.cola) == 0

    def cabina_tamanio(self):
        return len(self.cola)

    def generar_vehiculo(self):
        tipos = [I, II, III, IV]
        tarifas = [47, 59, 71, 64]
        tipo = random.choice(tipos)
        tarifa = tarifas[tipos.index(tipo)]
        return Vehiculo(tipo, tarifa)

def agregar_vehiculos(cabina, cantidad):
    for _ in range(cantidad):
        vehiculo = cabina.generar_vehiculo()
        cabina.agregar_vehiculo(vehiculo)

def atender_cabinas(cabinas):
    for i, cabina in enumerate(cabinas):
        while not cabina.cabina_vacia():
            vehiculo = cabina.atender_vehiculo()
            print(f"Atendiendo {vehiculo} en la cabina {i+1}")

def cabina_mayor_recaudacion(cabinas):
    mayor_recaudacion = 0
    indice_mayor = -1
    for i, cabina in enumerate(cabinas):
        if cabina.cabina_recaudacion() > mayor_recaudacion:
            mayor_recaudacion = cabina.cabina_recaudacion()
            indice_mayor = i
    return indice_mayor, mayor_recaudacion

def vehiculos_totales_atendidos(cabinas):
    total_vehiculos = {I: 0, II: 0, III: 0, IV: 0}
    for cabina in cabinas:
        vehiculos = cabina.vehiculos_atendidos()
        for tipo, cantidad in vehiculos.items():
            total_vehiculos[tipo] += cantidad
    return total_vehiculos


cabinas = [Cabina() for _ in range(3)]
for cabina in cabinas:
    agregar_vehiculos(cabina, 30)

atender_cabinas(cabinas)

indice_mayor, recaudacion_mayor = cabina_mayor_recaudacion(cabinas)
print(f"\nLa cabina con mayor recaudación es la cabina {indice_mayor + 1} con ${recaudacion_mayor}")

for i, cabina in enumerate(cabinas):
    print(f"Vehículos atendidos en la cabina {i+1}: {cabina.vehiculos_atendidos()}")


