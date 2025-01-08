from model.semaforo_estado import SemaforoEstado


class Semaforo:
    def __init__(self, estado_inicial):
        self.estado = estado_inicial

    def cambiar_estado(self):
        self.estado = SemaforoEstado.TRANSICION.get(self.estado)
