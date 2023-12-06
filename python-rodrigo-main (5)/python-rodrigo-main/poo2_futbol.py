import random
class jugadores:
    def __init__(self, nombre, dorsal, probabilidad):
        self.nombre=nombre
        self.dorsal=dorsal
        self.probabilidad=probabilidad
    
jugador1=jugadores("alberto","10", random.randint(1,10))
jugador2= jugadores("fernando","5", random.randint(1,10))

probab_programa=random.randint(1,10)

