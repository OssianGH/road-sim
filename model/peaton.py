import random


class Peaton:
    def __init__(self, modelo, imagen, x, y):
        self.modelo = modelo
        self.imagen = imagen
        self.x = x
        self.y = y
        self.velocidad = random.choice([1, 2])
        self.velocidad_actual = self.velocidad
        self.index_sprite = 0

    def mover_x(self):
        self.x += self.velocidad_actual

    def mover_y(self):
        self.y -= self.velocidad_actual
