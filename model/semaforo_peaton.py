from model.semaforo_estado import SemaforoEstado


class SemaforoPeaton:
    def __init__(self, verde):
        self.verde = verde

    def poner_verde(self):
        self.verde = True

    def poner_rojo(self):
        self.verde = False
