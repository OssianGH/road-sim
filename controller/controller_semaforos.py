from model.semaforo_estado import SemaforoEstado
from model.semaforo import Semaforo
from view.calles import Calles


class ControllerSemaforos:
    def __init__(self, vista: Calles):
        self.vista = vista
        self.semaforo_h = Semaforo(SemaforoEstado.ROJO)
        self.semaforo_v = Semaforo(SemaforoEstado.ESPECIAL)
        self.__actualizar_colores()

    def cambiar_colores(self):
        if self.semaforo_h.estado in [SemaforoEstado.ESPECIAL, SemaforoEstado.VERDE]:
            self.semaforo_h.cambiar_estado()
            self.__actualizar_colores_h()
            return

        if self.semaforo_v.estado in [SemaforoEstado.ESPECIAL, SemaforoEstado.VERDE]:
            self.semaforo_v.cambiar_estado()
            self.__actualizar_colores_v()
            return

        self.semaforo_h.cambiar_estado()
        self.semaforo_v.cambiar_estado()
        self.__actualizar_colores()

    def __actualizar_colores_h(self):
        COLOR = {
            SemaforoEstado.ROJO: self.vista.imagen_semaforo_rojo_h,
            SemaforoEstado.AMARILLO: self.vista.imagen_semaforo_amarillo_h,
            SemaforoEstado.VERDE: self.vista.imagen_semaforo_verde_h,
            SemaforoEstado.ESPECIAL: self.vista.imagen_semaforo_verde_viraje_h,
        }

        self.vista.imagen_semaforo_h = COLOR.get(self.semaforo_h.estado)

    def __actualizar_colores_v(self):
        COLOR = {
            SemaforoEstado.ROJO: self.vista.imagen_semaforo_rojo_v,
            SemaforoEstado.AMARILLO: self.vista.imagen_semaforo_amarillo_v,
            SemaforoEstado.VERDE: self.vista.imagen_semaforo_verde_v,
            SemaforoEstado.ESPECIAL: self.vista.imagen_semaforo_verde_viraje_v,
        }

        self.vista.imagen_semaforo_v = COLOR.get(self.semaforo_v.estado)

    def __actualizar_colores(self):
        self.__actualizar_colores_h()
        self.__actualizar_colores_v()
