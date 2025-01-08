from model.semaforo_estado import SemaforoEstado
from model.semaforo import Semaforo
from model.semaforo_peaton import SemaforoPeaton
from view.calles import Calles


class ControllerSemaforosPeaton:
    def __init__(self, vista: Calles, semaforo_h: Semaforo, semaforo_v: Semaforo):
        self.vista = vista
        self.semaforo_h = semaforo_h
        self.semaforo_v = semaforo_v
        self.semaforo_peaton_h_1 = SemaforoPeaton(False)
        self.semaforo_peaton_h_2 = SemaforoPeaton(False)
        self.semaforo_peaton_v_1 = SemaforoPeaton(False)
        self.semaforo_peaton_v_2 = SemaforoPeaton(True)
        self.__actualizar_colores()

    def cambiar_colores(self):
        if self.semaforo_v.estado == SemaforoEstado.ESPECIAL:
            self.semaforo_peaton_v_2.poner_verde()
        elif self.semaforo_v.estado == SemaforoEstado.AMARILLO:
            self.semaforo_peaton_v_2.poner_rojo()
            self.semaforo_peaton_v_1.poner_rojo()
        elif self.semaforo_v.estado == SemaforoEstado.VERDE:
            self.semaforo_peaton_v_1.poner_verde()

        if self.semaforo_h.estado == SemaforoEstado.ESPECIAL:
            self.semaforo_peaton_h_1.poner_verde()
        elif self.semaforo_h.estado == SemaforoEstado.AMARILLO:
            self.semaforo_peaton_h_1.poner_rojo()
            self.semaforo_peaton_h_2.poner_rojo()
        elif self.semaforo_h.estado == SemaforoEstado.VERDE:
            self.semaforo_peaton_h_2.poner_verde()

        self.__actualizar_colores()

    def __actualizar_colores_h_1(self):
        if self.semaforo_peaton_h_1.verde:
            self.vista.imagen_semaforo_peatones_h_1 = (
                self.vista.imagen_semaforo_verde_peatones_h
            )
            return

        self.vista.imagen_semaforo_peatones_h_1 = (
            self.vista.imagen_semaforo_rojo_peatones_h
        )

    def __actualizar_colores_h_2(self):
        if self.semaforo_peaton_h_2.verde:
            self.vista.imagen_semaforo_peatones_h_2 = (
                self.vista.imagen_semaforo_verde_peatones_h
            )
            return

        self.vista.imagen_semaforo_peatones_h_2 = (
            self.vista.imagen_semaforo_rojo_peatones_h
        )

    def __actualizar_colores_v_1(self):
        if self.semaforo_peaton_v_1.verde:
            self.vista.imagen_semaforo_peatones_v_1 = (
                self.vista.imagen_semaforo_verde_peatones_v
            )
            return

        self.vista.imagen_semaforo_peatones_v_1 = (
            self.vista.imagen_semaforo_rojo_peatones_v
        )

    def __actualizar_colores_v_2(self):
        if self.semaforo_peaton_v_2.verde:
            self.vista.imagen_semaforo_peatones_v_2 = (
                self.vista.imagen_semaforo_verde_peatones_v
            )
            return

        self.vista.imagen_semaforo_peatones_v_2 = (
            self.vista.imagen_semaforo_rojo_peatones_v
        )

    def __actualizar_colores(self):
        self.__actualizar_colores_h_1()
        self.__actualizar_colores_h_2()
        self.__actualizar_colores_v_1()
        self.__actualizar_colores_v_2()
