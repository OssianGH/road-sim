import random
from model.semaforo_estado import SemaforoEstado
from model.semaforo import Semaforo
from model.vehiculo import Vehiculo
from view.calles import Calles


class ControllerVehiculos:
    def __init__(self, view: Calles, semaforo_h: Semaforo, semaforo_v: Semaforo):
        self.view = view
        self.semaforo_h = semaforo_h
        self.semaforo_v = semaforo_v
        self.tope_interseccion_h = (
            (self.view.ancho - self.view.ancho_calle - self.view.altura_vehiculo) / 2
            - self.view.ancho_vereda
            - 2 * self.view.separacion_linea
        )
        self.tope_interseccion_v = (
            (self.view.altura + self.view.ancho_calle + self.view.altura_vehiculo) / 2
            + self.view.ancho_vereda
            + 2 * self.view.separacion_linea
        )
        self.linea_h_1 = self.view.altura / 2 + self.view.ancho_calle / 4
        self.linea_h_2 = self.view.altura / 2 - self.view.ancho_calle / 4
        self.linea_v_1 = self.view.ancho / 2 + self.view.ancho_calle / 4
        self.linea_v_2 = self.view.ancho / 2 - self.view.ancho_calle / 4
        self.max_vehiculos_h = 4
        self.max_vehiculos_v = 2
        self.distancia_seguridad = 200
        self.vehiculos_h = []
        self.vehiculos_v = []

    def generar_vehiculos(self):
        if (
            random.random() < 0.01
            and self.__numero_vehiculos_h_1() < self.max_vehiculos_h
        ):
            self.__generar_vehiculo_h_1()

        if (
            random.random() < 0.01
            and self.__numero_vehiculos_h_2() < self.max_vehiculos_h
        ):
            self.__generar_vehiculo_h_2()

        if (
            random.random() < 0.01
            and self.__numero_vehiculos_v_1() < self.max_vehiculos_v
        ):
            self.__generar_vehiculo_v_1()

        if (
            random.random() < 0.01
            and self.__numero_vehiculos_v_2() < self.max_vehiculos_v
        ):
            self.__generar_vehiculo_v_2()

    def mover(self):
        self.__mover_h()
        self.__mover_v()

    # Horizontal

    def __generar_vehiculo_h_1(self):
        x = -self.view.altura_vehiculo / 2
        y = self.linea_h_1
        vehiculo = Vehiculo(random.choice(self.view.imagen_vehiculos), x, y)

        self.vehiculos_h.append(vehiculo)
        self.view.vehiculos_h.append((vehiculo.imagen, vehiculo.x, vehiculo.y))

    def __generar_vehiculo_h_2(self):
        x = -self.view.altura_vehiculo / 2
        y = self.linea_h_2
        vehiculo = Vehiculo(
            random.choice(self.view.imagen_vehiculos), x, y, random.random() < 0.4
        )

        self.vehiculos_h.append(vehiculo)
        self.view.vehiculos_h.append((vehiculo.imagen, vehiculo.x, vehiculo.y))

    def __numero_vehiculos_h_1(self):
        return len(
            [vehiculo for vehiculo in self.vehiculos_h if vehiculo.y == self.linea_h_1]
        )

    def __numero_vehiculos_h_2(self):
        return len(
            [vehiculo for vehiculo in self.vehiculos_h if vehiculo.y == self.linea_h_2]
        )

    def __mover_h(self):
        for i in range(len(self.vehiculos_h)):
            vehiculo = self.vehiculos_h[i]

            if self.__girar_h(vehiculo):
                vehiculo.girando = True

                vehiculo.x = self.linea_v_2
                self.vehiculos_v.append(vehiculo)
                self.view.vehiculos_v.append((vehiculo.imagen, vehiculo.x, vehiculo.y))

                self.vehiculos_h.pop(i)
                self.view.vehiculos_h.pop(i)
                break

            if self.__esta_vehiculo_adelante_h(vehiculo):
                vehiculo.velocidad_actual = 0
            elif (
                (
                    self.tope_interseccion_h
                    <= vehiculo.x
                    <= self.tope_interseccion_h + 12
                )
                and not vehiculo.girar
                and self.semaforo_h.estado
                in [SemaforoEstado.ROJO, SemaforoEstado.AMARILLO]
            ):
                vehiculo.velocidad_actual = 0
            elif (
                (
                    self.tope_interseccion_h
                    <= vehiculo.x
                    <= self.tope_interseccion_h + 12
                )
                and vehiculo.girar
                and self.semaforo_h.estado != SemaforoEstado.ESPECIAL
            ):
                vehiculo.velocidad_actual = 0
            else:
                vehiculo.velocidad_actual = vehiculo.velocidad

            vehiculo.mover_x()
            self.view.vehiculos_h[i] = (vehiculo.imagen, vehiculo.x, vehiculo.y)

            if self.__esta_fuera_h(vehiculo):
                self.vehiculos_h.pop(i)
                self.view.vehiculos_h.pop(i)
                break

    def __esta_vehiculo_adelante_h(self, vehiculo):
        for vehiculo_h in self.vehiculos_h:
            if (
                (vehiculo_h != vehiculo)
                and (vehiculo_h.y == vehiculo.y)
                and (vehiculo_h.x > vehiculo.x)
                and (vehiculo_h.x - vehiculo.x < self.distancia_seguridad)
            ):
                return True
        else:
            return False

    def __esta_fuera_h(self, vehiculo):
        return vehiculo.x > self.view.ancho + self.view.altura_vehiculo / 2

    def __girar_h(self, vehiculo):
        return (
            vehiculo.girar
            and not vehiculo.girando
            and self.linea_v_2 <= vehiculo.x <= self.linea_v_2 + 12
        )

    # Vertical

    def __generar_vehiculo_v_1(self):
        x = self.linea_v_1
        y = self.view.altura + self.view.altura_vehiculo / 2
        vehiculo = Vehiculo(
            random.choice(self.view.imagen_vehiculos), x, y, random.random() < 0.4
        )

        self.vehiculos_v.append(vehiculo)
        self.view.vehiculos_v.append((vehiculo.imagen, vehiculo.x, vehiculo.y))

    def __generar_vehiculo_v_2(self):
        x = self.linea_v_2
        y = self.view.altura + self.view.altura_vehiculo / 2
        vehiculo = Vehiculo(random.choice(self.view.imagen_vehiculos), x, y)

        self.vehiculos_v.append(vehiculo)
        self.view.vehiculos_v.append((vehiculo.imagen, vehiculo.x, vehiculo.y))

    def __numero_vehiculos_v_1(self):
        return len(
            [vehiculo for vehiculo in self.vehiculos_v if vehiculo.x == self.linea_v_1]
        )

    def __numero_vehiculos_v_2(self):
        return len(
            [vehiculo for vehiculo in self.vehiculos_v if vehiculo.x == self.linea_v_2]
        )

    def __mover_v(self):
        for i in range(len(self.vehiculos_v)):
            vehiculo = self.vehiculos_v[i]

            if self.__girar_v(vehiculo):
                vehiculo.girando = True

                vehiculo.y = self.linea_h_1
                self.vehiculos_h.append(vehiculo)
                self.view.vehiculos_h.append((vehiculo.imagen, vehiculo.x, vehiculo.y))

                self.vehiculos_v.pop(i)
                self.view.vehiculos_v.pop(i)
                break

            if self.__esta_vehiculo_adelante_v(vehiculo):
                vehiculo.velocidad_actual = 0
            elif (
                (
                    self.tope_interseccion_v - 12
                    <= vehiculo.y
                    <= self.tope_interseccion_v
                )
                and not vehiculo.girar
                and self.semaforo_v.estado
                in [SemaforoEstado.ROJO, SemaforoEstado.AMARILLO]
            ):
                vehiculo.velocidad_actual = 0
            elif (
                (
                    self.tope_interseccion_v - 12
                    <= vehiculo.y
                    <= self.tope_interseccion_v
                )
                and vehiculo.girar
                and self.semaforo_v.estado != SemaforoEstado.ESPECIAL
            ):
                vehiculo.velocidad_actual = 0
            else:
                vehiculo.velocidad_actual = vehiculo.velocidad

            vehiculo.mover_y()
            self.view.vehiculos_v[i] = (vehiculo.imagen, vehiculo.x, vehiculo.y)

            if self.__esta_fuera_v(vehiculo):
                self.vehiculos_v.pop(i)
                self.view.vehiculos_v.pop(i)
                break

    def __esta_vehiculo_adelante_v(self, vehiculo):
        for vehiculo_v in self.vehiculos_v:
            if (
                (vehiculo_v != vehiculo)
                and (vehiculo_v.x == vehiculo.x)
                and (vehiculo_v.y < vehiculo.y)
                and (vehiculo.y - vehiculo_v.y < self.distancia_seguridad)
            ):
                return True
        else:
            return False

    def __esta_fuera_v(self, vehiculo):
        return vehiculo.y < -self.view.altura_vehiculo / 2

    def __girar_v(self, vehiculo):
        return (
            vehiculo.girar
            and not vehiculo.girando
            and self.linea_h_1 - 12 <= vehiculo.y <= self.linea_h_1
        )
