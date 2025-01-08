import pygame
from controller.controller_contador import ControllerContador
from controller.controller_peatones import ControllerPeatones
from controller.controller_semaforos_peaton import ControllerSemaforosPeaton
from controller.controller_semaforos import ControllerSemaforos
from controller.controller_vehiculos import ControllerVehiculos
from view.calles import Calles


class Principal:
    def __init__(self):
        pygame.init()
        self.view = Calles()
        self.clock = pygame.time.Clock()
        self.c_semaforos = ControllerSemaforos(self.view)
        self.c_semaforos_peaton = ControllerSemaforosPeaton(
            self.view, self.c_semaforos.semaforo_h, self.c_semaforos.semaforo_v
        )
        self.c_contador = ControllerContador(self.view, self.c_semaforos)
        self.c_vehiculos = ControllerVehiculos(
            self.view, self.c_semaforos.semaforo_h, self.c_semaforos.semaforo_v
        )
        self.c_peatones = ControllerPeatones(
            self.view,
            self.c_semaforos_peaton.semaforo_peaton_h_1,
            self.c_semaforos_peaton.semaforo_peaton_h_2,
            self.c_semaforos_peaton.semaforo_peaton_v_1,
            self.c_semaforos_peaton.semaforo_peaton_v_2,
        )
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.c_contador.handle_event(event)

    def update(self):
        self.c_vehiculos.generar_vehiculos()
        self.c_vehiculos.mover()
        self.c_peatones.generar_peatones()
        self.c_peatones.mover()
        self.c_peatones.animar()
        self.c_semaforos_peaton.cambiar_colores()

    def render(self):
        self.view.draw()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()
