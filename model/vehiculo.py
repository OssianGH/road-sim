import random


class Vehiculo:
    def __init__(self, imagen, x, y, girar=False):
        self.imagen = imagen
        self.x = x
        self.y = y
        self.girar = girar
        self.velocidad = random.randint(4, 8)
        self.velocidad_actual = self.velocidad
        self.girando = False

    def mover_x(self):
        self.x += self.velocidad_actual

    def mover_y(self):
        self.y -= self.velocidad_actual
