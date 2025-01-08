import random
from model.semaforo_peaton import SemaforoPeaton
from model.peaton import Peaton
from view.calles import Calles


class ControllerPeatones:

    def __init__(
        self,
        view: Calles,
        semaforo_h_1: SemaforoPeaton,
        semaforo_h_2: SemaforoPeaton,
        semaforo_v_1: SemaforoPeaton,
        semaforo_v_2: SemaforoPeaton,
    ):
        self.view = view
        self.semaforo_h_1 = semaforo_h_1
        self.semaforo_h_2 = semaforo_h_2
        self.semaforo_v_1 = semaforo_v_1
        self.semaforo_v_2 = semaforo_v_2
        self.separacion = 12
        self.tope_interseccion_h = (
            self.view.ancho - self.view.ancho_calle - 3 * self.view.ancho_vereda
        ) / 2
        self.tope_interseccion_v = (
            self.view.altura + self.view.ancho_calle + 3 * self.view.ancho_vereda
        ) / 2
        self.linea_h_1_1 = (
            self.view.altura + self.view.ancho_calle + self.view.ancho_vereda
        ) / 2 - self.separacion
        self.linea_h_1_2 = (
            self.view.altura + self.view.ancho_calle + self.view.ancho_vereda
        ) / 2 + self.separacion
        self.linea_h_2_1 = (
            self.view.altura - self.view.ancho_calle - self.view.ancho_vereda
        ) / 2 - self.separacion
        self.linea_h_2_2 = (
            self.view.altura - self.view.ancho_calle - self.view.ancho_vereda
        ) / 2 + self.separacion
        self.linea_v_1_1 = (
            self.view.ancho + self.view.ancho_calle + self.view.ancho_vereda
        ) / 2 - self.separacion
        self.linea_v_1_2 = (
            self.view.ancho + self.view.ancho_calle + self.view.ancho_vereda
        ) / 2 + self.separacion
        self.linea_v_2_1 = (
            self.view.ancho - self.view.ancho_calle - self.view.ancho_vereda
        ) / 2 - self.separacion
        self.linea_v_2_2 = (
            self.view.ancho - self.view.ancho_calle - self.view.ancho_vereda
        ) / 2 + self.separacion
        self.max_peatones_h = 8
        self.max_peatones_v = 6
        self.distancia_seguridad = 50
        self.peatones_h = []
        self.peatones_v = []
        self.frame_count = 0
        self.velocidad_animacion = 9

    def generar_peatones(self):
        if (
            random.random() < 0.01
            and self.__numero_peatones_h_1_1() < self.max_peatones_h
        ):
            self.__generar_peaton_h_1_1()

        if (
            random.random() < 0.01
            and self.__numero_peatones_h_1_2() < self.max_peatones_h
        ):
            self.__generar_peaton_h_1_2()

        if (
            random.random() < 0.01
            and self.__numero_peatones_h_2_1() < self.max_peatones_h
        ):
            self.__generar_peaton_h_2_1()

        if (
            random.random() < 0.01
            and self.__numero_peatones_h_2_2() < self.max_peatones_h
        ):
            self.__generar_peaton_h_2_2()

        if (
            random.random() < 0.01
            and self.__numero_peatones_v_1_1() < self.max_peatones_v
        ):
            self.__generar_peaton_v_1_1()

        if (
            random.random() < 0.01
            and self.__numero_peatones_v_1_2() < self.max_peatones_v
        ):
            self.__generar_peaton_v_1_2()

        if (
            random.random() < 0.01
            and self.__numero_peatones_v_2_1() < self.max_peatones_v
        ):
            self.__generar_peaton_v_2_1()

        if (
            random.random() < 0.01
            and self.__numero_peatones_v_2_2() < self.max_peatones_v
        ):
            self.__generar_peaton_v_2_2()

    def mover(self):
        self.__mover_h()
        self.__mover_v()

    def animar(self):
        self.frame_count += 1

        if self.frame_count % self.velocidad_animacion != 0:
            return

        self.__animar_h()
        self.__animar_v()

    # Horizontal

    def __generar_peaton_h_1_1(self):
        modelo = random.choice(list(range(len(self.view.imagen_peatones_h))))
        imagen = self.view.imagen_peatones_h[modelo][0]
        ancho = imagen.get_width()

        x = -ancho
        y = self.linea_h_1_1
        peaton = Peaton(modelo, imagen, x, y)

        self.peatones_h.append(peaton)
        self.view.peatones_h.append((peaton.imagen, peaton.x, peaton.y))

    def __generar_peaton_h_1_2(self):
        modelo = random.choice(list(range(len(self.view.imagen_peatones_h))))
        imagen = self.view.imagen_peatones_h[modelo][0]
        ancho = imagen.get_width()

        x = -ancho
        y = self.linea_h_1_2
        peaton = Peaton(modelo, imagen, x, y)

        self.peatones_h.append(peaton)
        self.view.peatones_h.append((peaton.imagen, peaton.x, peaton.y))

    def __generar_peaton_h_2_1(self):
        modelo = random.choice(list(range(len(self.view.imagen_peatones_h))))
        imagen = self.view.imagen_peatones_h[modelo][0]
        ancho = imagen.get_width()

        x = -ancho
        y = self.linea_h_2_1
        peaton = Peaton(modelo, imagen, x, y)

        self.peatones_h.append(peaton)
        self.view.peatones_h.append((peaton.imagen, peaton.x, peaton.y))

    def __generar_peaton_h_2_2(self):
        modelo = random.choice(list(range(len(self.view.imagen_peatones_h))))
        imagen = self.view.imagen_peatones_h[modelo][0]
        ancho = imagen.get_width()

        x = -ancho
        y = self.linea_h_2_2
        peaton = Peaton(modelo, imagen, x, y)

        self.peatones_h.append(peaton)
        self.view.peatones_h.append((peaton.imagen, peaton.x, peaton.y))

    def __numero_peatones_h_1_1(self):
        return len(
            [peaton for peaton in self.peatones_h if peaton.y == self.linea_h_1_1]
        )

    def __numero_peatones_h_1_2(self):
        return len(
            [peaton for peaton in self.peatones_h if peaton.y == self.linea_h_1_2]
        )

    def __numero_peatones_h_2_1(self):
        return len(
            [peaton for peaton in self.peatones_h if peaton.y == self.linea_h_2_1]
        )

    def __numero_peatones_h_2_2(self):
        return len(
            [peaton for peaton in self.peatones_h if peaton.y == self.linea_h_2_2]
        )

    def __mover_h(self):
        for i in range(len(self.peatones_h)):
            peaton = self.peatones_h[i]

            if self.__esta_peaton_adelante_h(peaton):
                peaton.velocidad_actual = 0
            elif (
                (self.tope_interseccion_h <= peaton.x <= self.tope_interseccion_h + 5)
                and peaton.y in [self.linea_h_1_1, self.linea_h_1_2]
                and not self.semaforo_h_1.verde
            ):
                peaton.velocidad_actual = 0
            elif (
                (self.tope_interseccion_h <= peaton.x <= self.tope_interseccion_h + 5)
                and peaton.y in [self.linea_h_2_1, self.linea_h_2_2]
                and not self.semaforo_h_2.verde
            ):
                peaton.velocidad_actual = 0
            else:
                peaton.velocidad_actual = peaton.velocidad

            peaton.mover_x()
            self.view.peatones_h[i] = (peaton.imagen, peaton.x, peaton.y)

            if self.__esta_fuera_h(peaton):
                self.peatones_h.pop(i)
                self.view.peatones_h.pop(i)
                break

    def __animar_h(self):
        for i in range(len(self.peatones_h)):
            peaton = self.peatones_h[i]

            if peaton.velocidad_actual > 0:
                peaton.index_sprite = (peaton.index_sprite + 1) % len(
                    self.view.imagen_peatones_h[peaton.modelo]
                )
                peaton.imagen = self.view.imagen_peatones_h[peaton.modelo][
                    peaton.index_sprite
                ]
            else:
                peaton.index_sprite = (peaton.index_sprite + 1) % len(
                    self.view.imagen_peatones_parado_h[peaton.modelo]
                )
                peaton.imagen = self.view.imagen_peatones_parado_h[peaton.modelo][
                    peaton.index_sprite
                ]

    def __esta_peaton_adelante_h(self, peaton):
        for peaton_h in self.peatones_h:
            if (
                (peaton_h != peaton)
                and (peaton_h.y == peaton.y)
                and (peaton_h.x > peaton.x)
                and (peaton_h.x - peaton.x < self.distancia_seguridad)
            ):
                return True
        else:
            return False

    def __esta_fuera_h(self, peaton):
        return peaton.x > self.view.ancho

    # Vertical

    def __generar_peaton_v_1_1(self):
        modelo = random.choice(list(range(len(self.view.imagen_peatones_v))))
        imagen = self.view.imagen_peatones_v[modelo][0]
        altura = imagen.get_height()

        x = self.linea_v_1_1
        y = self.view.altura + altura
        peaton = Peaton(modelo, imagen, x, y)

        self.peatones_v.append(peaton)
        self.view.peatones_v.append((peaton.imagen, peaton.x, peaton.y))

    def __generar_peaton_v_1_2(self):
        modelo = random.choice(list(range(len(self.view.imagen_peatones_v))))
        imagen = self.view.imagen_peatones_v[modelo][0]
        altura = imagen.get_height()

        x = self.linea_v_1_2
        y = self.view.altura + altura
        peaton = Peaton(modelo, imagen, x, y)

        self.peatones_v.append(peaton)
        self.view.peatones_v.append((peaton.imagen, peaton.x, peaton.y))

    def __generar_peaton_v_2_1(self):
        modelo = random.choice(list(range(len(self.view.imagen_peatones_v))))
        imagen = self.view.imagen_peatones_v[modelo][0]
        altura = imagen.get_height()

        x = self.linea_v_2_1
        y = self.view.altura + altura
        peaton = Peaton(modelo, imagen, x, y)

        self.peatones_v.append(peaton)
        self.view.peatones_v.append((peaton.imagen, peaton.x, peaton.y))

    def __generar_peaton_v_2_2(self):
        modelo = random.choice(list(range(len(self.view.imagen_peatones_v))))
        imagen = self.view.imagen_peatones_v[modelo][0]
        altura = imagen.get_height()

        x = self.linea_v_2_2
        y = self.view.altura + altura
        peaton = Peaton(modelo, imagen, x, y)

        self.peatones_v.append(peaton)
        self.view.peatones_v.append((peaton.imagen, peaton.x, peaton.y))

    def __numero_peatones_v_1_1(self):
        return len(
            [peaton for peaton in self.peatones_v if peaton.x == self.linea_v_1_1]
        )

    def __numero_peatones_v_1_2(self):
        return len(
            [peaton for peaton in self.peatones_v if peaton.x == self.linea_v_1_2]
        )

    def __numero_peatones_v_2_1(self):
        return len(
            [peaton for peaton in self.peatones_v if peaton.x == self.linea_v_2_1]
        )

    def __numero_peatones_v_2_2(self):
        return len(
            [peaton for peaton in self.peatones_v if peaton.x == self.linea_v_2_2]
        )

    def __mover_v(self):
        for i in range(len(self.peatones_v)):
            peaton = self.peatones_v[i]

            if self.__esta_peaton_adelante_v(peaton):
                peaton.velocidad_actual = 0
            elif (
                (self.tope_interseccion_v <= peaton.y <= self.tope_interseccion_v + 5)
                and peaton.x in [self.linea_v_2_1, self.linea_v_2_2]
                and not self.semaforo_v_2.verde
            ):
                peaton.velocidad_actual = 0
            elif (
                (self.tope_interseccion_v <= peaton.y <= self.tope_interseccion_v + 5)
                and peaton.x in [self.linea_v_1_1, self.linea_v_1_2]
                and not self.semaforo_v_1.verde
            ):
                peaton.velocidad_actual = 0
            else:
                peaton.velocidad_actual = peaton.velocidad

            peaton.mover_y()
            self.view.peatones_v[i] = (peaton.imagen, peaton.x, peaton.y)

            if self.__esta_fuera_v(peaton):
                self.peatones_v.pop(i)
                self.view.peatones_v.pop(i)
                break

    def __animar_v(self):
        for i in range(len(self.peatones_v)):
            peaton = self.peatones_v[i]

            if peaton.velocidad_actual > 0:
                peaton.index_sprite = (peaton.index_sprite + 1) % len(
                    self.view.imagen_peatones_v[peaton.modelo]
                )
                peaton.imagen = self.view.imagen_peatones_v[peaton.modelo][
                    peaton.index_sprite
                ]
            else:
                peaton.index_sprite = (peaton.index_sprite + 1) % len(
                    self.view.imagen_peatones_parado_v[peaton.modelo]
                )
                peaton.imagen = self.view.imagen_peatones_parado_v[peaton.modelo][
                    peaton.index_sprite
                ]

    def __esta_peaton_adelante_v(self, peaton):
        for peaton_v in self.peatones_v:
            if (
                (peaton_v != peaton)
                and (peaton_v.x == peaton.x)
                and (peaton_v.y < peaton.y)
                and (peaton.y - peaton_v.y < self.distancia_seguridad)
            ):
                return True
        else:
            return False

    def __esta_fuera_v(self, peaton):
        return peaton.y < 0
