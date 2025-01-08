import pygame
from controller.controller_semaforos import ControllerSemaforos
from model.contador import Contador
from view.calles import Calles


class ControllerContador:
    def __init__(self, vista: Calles, c_semaforos: ControllerSemaforos):
        self.vista = vista
        self.c_semaforos = c_semaforos
        self.contador = Contador()
        self.counter_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.counter_event, 1000)

    def handle_event(self, event):
        if event.type == self.counter_event:
            self.contador.incrementar()

            if self.contador.valor in [7, 17]:
                self.c_semaforos.cambiar_colores()
            elif self.contador.valor == 24:
                self.c_semaforos.cambiar_colores()
                self.contador.resetear()

            if self.contador.valor < 7:
                self.vista.valor_contador = str(self.contador.valor)
            elif self.contador.valor < 17:
                self.vista.valor_contador = str(self.contador.valor - 7)
            else:
                self.vista.valor_contador = str(self.contador.valor - 17)
