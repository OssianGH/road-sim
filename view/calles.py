import pygame
import os


class Calles:
    def __init__(self):
        self.ancho = 1600
        self.altura = 900
        self.ancho_calle = 208
        self.color_calle = (54, 89, 133)
        self.desfasaje_vereda = 12
        self.lineas_peatonales = 6
        self.ancho_peatonal = 20
        self.ancho_linea = 8
        self.altura_linea = 20
        self.separacion_linea = 12
        self.color_linea = (169, 192, 208)
        self.separacion_contador = 24
        self.color_contador = (255, 255, 255)
        self.size_contador = 50
        self.imagen_vehiculos_dir = r".\assets\car"
        self.imagen_peatones_dir = r".\assets\pedestrian"
        self.imagen_peatones_parado_dir = r".\assets\pedestrian_idle"
        self.vehiculos_h = []
        self.vehiculos_v = []
        self.peatones_h = []
        self.peatones_v = []
        self.imagen_vehiculos = []
        self.imagen_peatones_h = []
        self.imagen_peatones_v = []
        self.imagen_peatones_parado_h = []
        self.imagen_peatones_parado_v = []
        self.superficie = pygame.display.set_mode((self.ancho, self.altura))
        self.cargar_imagen_vehiculos()
        self.cargar_imagen_flechas()
        self.cargar_imagen_veredas()
        self.cargar_imagen_semaforos()
        self.cargar_imagen_semaforos_peatones()
        self.cargar_imagen_peatones()
        self.cargar_otras_imagenes()
        self.valor_contador = 0
        pygame.display.set_caption("Gestión de tráfico")

    def cargar_imagen_vehiculos(self):
        for file in os.listdir(self.imagen_vehiculos_dir):
            imagen_vehiculo = pygame.image.load(
                os.path.join(self.imagen_vehiculos_dir, file)
            )
            self.imagen_vehiculos.append(imagen_vehiculo)

        self.ancho_vehiculo, self.altura_vehiculo = self.imagen_vehiculos[0].get_size()

    def cargar_imagen_peatones(self):
        for folder in os.listdir(self.imagen_peatones_dir):
            folder_path = os.path.join(self.imagen_peatones_dir, folder)

            sprites = [
                pygame.image.load(os.path.join(folder_path, file))
                for file in sorted(os.listdir(folder_path))
            ]

            self.imagen_peatones_h.append(sprites)
            self.imagen_peatones_v.append(
                [pygame.transform.rotate(imagen, 90.0) for imagen in sprites]
            )

        for folder in os.listdir(self.imagen_peatones_parado_dir):
            folder_path = os.path.join(self.imagen_peatones_parado_dir, folder)

            sprites = [
                pygame.image.load(os.path.join(folder_path, file))
                for file in sorted(os.listdir(folder_path))
            ]

            self.imagen_peatones_parado_h.append(sprites)
            self.imagen_peatones_parado_v.append(
                [pygame.transform.rotate(imagen, 90.0) for imagen in sprites]
            )

    def cargar_imagen_flechas(self):
        self.imagen_flecha_recta_v = pygame.image.load(r".\assets\arrow\straight.png")
        self.imagen_flecha_recta_h = pygame.transform.rotate(
            self.imagen_flecha_recta_v, -90.0
        )

        self.imagen_flecha_giro_v = pygame.image.load(
            r".\assets\arrow\straight_right.png"
        )
        self.imagen_flecha_giro_h = pygame.transform.flip(
            pygame.transform.rotate(self.imagen_flecha_giro_v, -90.0), False, True
        )

        self.ancho_flecha, self.altura_flecha = self.imagen_flecha_giro_v.get_size()

    def cargar_imagen_veredas(self):
        self.imagen_vereda_v_1 = pygame.image.load(r".\assets\sidewalk\sidewalk.png")
        self.imagen_vereda_v_2 = pygame.transform.flip(
            self.imagen_vereda_v_1, False, True
        )
        self.imagen_vereda_v_3 = pygame.transform.flip(
            self.imagen_vereda_v_2, True, False
        )
        self.imagen_vereda_v_4 = pygame.transform.flip(
            self.imagen_vereda_v_3, False, True
        )

        self.imagen_vereda_h_1 = pygame.transform.rotate(self.imagen_vereda_v_1, 90.0)
        self.imagen_vereda_h_2 = pygame.transform.flip(
            self.imagen_vereda_h_1, False, True
        )
        self.imagen_vereda_h_3 = pygame.transform.flip(
            self.imagen_vereda_h_2, True, False
        )
        self.imagen_vereda_h_4 = pygame.transform.flip(
            self.imagen_vereda_h_3, False, True
        )

        self.imagen_vereda_esquina_4 = pygame.image.load(
            r".\assets\sidewalk\sidewalk_corner.png"
        )
        self.imagen_vereda_esquina_3 = pygame.transform.rotate(
            self.imagen_vereda_esquina_4, 90.0
        )
        self.imagen_vereda_esquina_2 = pygame.transform.rotate(
            self.imagen_vereda_esquina_3, 90.0
        )
        self.imagen_vereda_esquina_1 = pygame.transform.rotate(
            self.imagen_vereda_esquina_2, 90.0
        )

        self.ancho_vereda, self.altura_vereda = self.imagen_vereda_v_1.get_size()

    def cargar_imagen_semaforos(self):
        self.imagen_semaforo_rojo_v = pygame.image.load(
            r".\assets\traffic_light\red.png"
        )
        self.imagen_semaforo_amarillo_v = pygame.image.load(
            r".\assets\traffic_light\yellow.png"
        )
        self.imagen_semaforo_verde_v = pygame.image.load(
            r".\assets\traffic_light\green.png"
        )
        self.imagen_semaforo_verde_viraje_v = pygame.image.load(
            r".\assets\traffic_light\green_turn.png"
        )

        self.imagen_semaforo_rojo_h = pygame.transform.rotate(
            self.imagen_semaforo_rojo_v, -90.0
        )
        self.imagen_semaforo_amarillo_h = pygame.transform.rotate(
            self.imagen_semaforo_amarillo_v, -90.0
        )
        self.imagen_semaforo_verde_h = pygame.transform.rotate(
            self.imagen_semaforo_verde_v, -90.0
        )
        self.imagen_semaforo_verde_viraje_h = pygame.transform.rotate(
            self.imagen_semaforo_verde_viraje_v, -90.0
        )

        self.imagen_semaforo_rojo_v = pygame.transform.flip(
            self.imagen_semaforo_rojo_v, True, False
        )
        self.imagen_semaforo_amarillo_v = pygame.transform.flip(
            self.imagen_semaforo_amarillo_v, True, False
        )
        self.imagen_semaforo_verde_v = pygame.transform.flip(
            self.imagen_semaforo_verde_v, True, False
        )
        self.imagen_semaforo_verde_viraje_v = pygame.transform.flip(
            self.imagen_semaforo_verde_viraje_v, True, False
        )

        self.ancho_semaforo, self.altura_semaforo = (
            self.imagen_semaforo_rojo_v.get_size()
        )

    def cargar_imagen_semaforos_peatones(self):
        self.imagen_semaforo_rojo_peatones_v = pygame.image.load(
            r".\assets\traffic_light\pedestrian_red.png"
        )
        self.imagen_semaforo_verde_peatones_v = pygame.image.load(
            r".\assets\traffic_light\pedestrian_green.png"
        )

        self.imagen_semaforo_rojo_peatones_h = pygame.transform.rotate(
            self.imagen_semaforo_rojo_peatones_v, -90.0
        )
        self.imagen_semaforo_verde_peatones_h = pygame.transform.rotate(
            self.imagen_semaforo_verde_peatones_v, -90.0
        )

        self.ancho_semaforo_peatones, self.altura_semaforo_peatones = (
            self.imagen_semaforo_rojo_peatones_v.get_size()
        )

    def cargar_otras_imagenes(self):
        self.imagen_alcantarilla_v = pygame.image.load(r".\assets\other\sewer.png")
        self.imagen_alcantarilla_h = pygame.transform.rotate(
            self.imagen_alcantarilla_v, 270.0
        )

        self.imagen_grieta_1 = pygame.image.load(r".\assets\other\crack_1.png")
        self.imagen_grieta_2 = pygame.image.load(r".\assets\other\crack_2.png")

    def dibujar_fondo(self):
        self.superficie.fill((55, 195, 78))

    def dibujar_calles(self):
        pygame.draw.rect(
            self.superficie,
            self.color_calle,
            (
                0,
                (self.altura - self.ancho_calle) / 2 - self.ancho_vereda,
                self.ancho,
                self.ancho_calle + 2 * self.ancho_vereda,
            ),
        )
        pygame.draw.rect(
            self.superficie,
            self.color_calle,
            (
                (self.ancho - self.ancho_calle) / 2 - self.ancho_vereda,
                0,
                self.ancho_calle + 2 * self.ancho_vereda,
                self.altura,
            ),
        )

    def dibujar_detalles(self):
        self.superficie.blit(
            self.imagen_alcantarilla_v,
            (
                (self.ancho - self.ancho_calle) / 2,
                206,
            ),
        )

        self.superficie.blit(
            self.imagen_alcantarilla_h,
            (
                992,
                (self.altura - self.ancho_calle) / 2,
            ),
        )

        height = self.imagen_grieta_2.get_height()
        self.superficie.blit(
            self.imagen_grieta_2,
            (200, (self.altura - height) / 2 + self.ancho_calle / 4),
        )

        height = self.imagen_grieta_1.get_height()
        self.superficie.blit(
            self.imagen_grieta_1,
            (1201, (self.altura - height) / 2 - self.ancho_calle / 4),
        )

    def dibujar_flechas(self):
        self.superficie.blit(
            self.imagen_flecha_recta_v,
            (
                (self.ancho - self.ancho_flecha) / 2 - self.ancho_calle / 4,
                (self.altura + self.ancho_calle) / 2
                + self.ancho_vereda
                + self.separacion_linea,
            ),
        )
        self.superficie.blit(
            self.imagen_flecha_giro_v,
            (
                (self.ancho - self.ancho_flecha) / 2 + self.ancho_calle / 4,
                (self.altura + self.ancho_calle) / 2
                + self.ancho_vereda
                + self.separacion_linea,
            ),
        )
        self.superficie.blit(
            self.imagen_flecha_recta_v,
            (
                (self.ancho - self.ancho_flecha) / 2 - self.ancho_calle / 4,
                (self.altura - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.altura_flecha
                - self.separacion_linea,
            ),
        )
        self.superficie.blit(
            self.imagen_flecha_recta_v,
            (
                (self.ancho - self.ancho_flecha) / 2 + self.ancho_calle / 4,
                (self.altura - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.altura_flecha
                - self.separacion_linea,
            ),
        )

        self.superficie.blit(
            self.imagen_flecha_recta_h,
            (
                (self.ancho - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.altura_flecha
                - self.separacion_linea,
                (self.altura - self.ancho_flecha) / 2 + self.ancho_calle / 4,
            ),
        )
        self.superficie.blit(
            self.imagen_flecha_giro_h,
            (
                (self.ancho - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.altura_flecha
                - self.separacion_linea,
                (self.altura - self.ancho_flecha) / 2 - self.ancho_calle / 4,
            ),
        )
        self.superficie.blit(
            self.imagen_flecha_recta_h,
            (
                (self.ancho + self.ancho_calle) / 2
                + self.ancho_vereda
                + self.separacion_linea,
                (self.altura - self.ancho_flecha) / 2 + self.ancho_calle / 4,
            ),
        )
        self.superficie.blit(
            self.imagen_flecha_recta_h,
            (
                (self.ancho + self.ancho_calle) / 2
                + self.ancho_vereda
                + self.separacion_linea,
                (self.altura - self.ancho_flecha) / 2 - self.ancho_calle / 4,
            ),
        )

    def dibujar_veredas(self):
        self.superficie.blit(
            self.imagen_vereda_esquina_1,
            (
                (self.ancho - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.desfasaje_vereda,
                (self.altura + self.ancho_calle) / 2,
            ),
        )
        self.superficie.blit(
            self.imagen_vereda_esquina_2,
            (
                (self.ancho - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.desfasaje_vereda,
                (self.altura - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.desfasaje_vereda,
            ),
        )
        self.superficie.blit(
            self.imagen_vereda_esquina_3,
            (
                (self.ancho + self.ancho_calle) / 2,
                (self.altura - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.desfasaje_vereda,
            ),
        )
        self.superficie.blit(
            self.imagen_vereda_esquina_4,
            (
                (self.ancho + self.ancho_calle) / 2,
                (self.altura + self.ancho_calle) / 2,
            ),
        )

        for y in range(
            (self.altura + self.ancho_calle) // 2
            + self.ancho_vereda
            + self.desfasaje_vereda,
            self.altura,
            self.altura_vereda,
        ):
            self.superficie.blit(
                self.imagen_vereda_v_1,
                (
                    (self.ancho + self.ancho_calle) / 2,
                    y,
                ),
            )
        for y in range(
            (self.altura - self.ancho_calle) // 2
            - self.ancho_vereda
            - self.altura_vereda
            - self.desfasaje_vereda,
            -self.altura_vereda,
            -self.altura_vereda,
        ):
            self.superficie.blit(
                self.imagen_vereda_v_2,
                (
                    (self.ancho + self.ancho_calle) / 2,
                    y,
                ),
            )
        for y in range(
            (self.altura - self.ancho_calle) // 2
            - self.ancho_vereda
            - self.altura_vereda
            - self.desfasaje_vereda,
            -self.altura_vereda,
            -self.altura_vereda,
        ):
            self.superficie.blit(
                self.imagen_vereda_v_3,
                (
                    (self.ancho - self.ancho_calle) / 2 - self.ancho_vereda,
                    y,
                ),
            )
        for y in range(
            (self.altura + self.ancho_calle) // 2
            + self.ancho_vereda
            + self.desfasaje_vereda,
            self.altura,
            self.altura_vereda,
        ):
            self.superficie.blit(
                self.imagen_vereda_v_4,
                (
                    (self.ancho - self.ancho_calle) / 2 - self.ancho_vereda,
                    y,
                ),
            )

        for x in range(
            (self.ancho + self.ancho_calle) // 2
            + self.ancho_vereda
            + self.desfasaje_vereda,
            self.ancho,
            self.altura_vereda,
        ):
            self.superficie.blit(
                self.imagen_vereda_h_1,
                (x, (self.altura - self.ancho_calle) / 2 - self.ancho_vereda),
            )
        for x in range(
            (self.ancho + self.ancho_calle) // 2
            + self.ancho_vereda
            + self.desfasaje_vereda,
            self.ancho,
            self.altura_vereda,
        ):
            self.superficie.blit(
                self.imagen_vereda_h_2, (x, (self.altura + self.ancho_calle) / 2)
            )
        for x in range(
            (self.ancho - self.ancho_calle) // 2
            - self.ancho_vereda
            - self.altura_vereda
            - self.desfasaje_vereda,
            -self.altura_vereda,
            -self.altura_vereda,
        ):
            self.superficie.blit(
                self.imagen_vereda_h_3,
                (
                    x,
                    (self.altura + self.ancho_calle) / 2,
                ),
            )

        for x in range(
            (self.ancho - self.ancho_calle) // 2
            - self.ancho_vereda
            - self.altura_vereda
            - self.desfasaje_vereda,
            -self.altura_vereda,
            -self.altura_vereda,
        ):
            self.superficie.blit(
                self.imagen_vereda_h_4,
                (
                    x,
                    (self.altura - self.ancho_calle) / 2 - self.ancho_vereda,
                ),
            )

    def dibujar_peatonales(self):
        for x in range(self.lineas_peatonales // 2):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho - self.separacion_linea) / 2
                    - (self.ancho_peatonal + self.separacion_linea) * x
                    - self.ancho_peatonal,
                    (self.altura - self.ancho_calle) / 2 - self.ancho_vereda,
                    self.ancho_peatonal,
                    self.ancho_vereda,
                ),
            )
        for x in range(self.lineas_peatonales // 2):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho + self.separacion_linea) / 2
                    + (self.ancho_peatonal + self.separacion_linea) * x,
                    (self.altura - self.ancho_calle) / 2 - self.ancho_vereda,
                    self.ancho_peatonal,
                    self.ancho_vereda,
                ),
            )

        for x in range(self.lineas_peatonales // 2):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho - self.separacion_linea) / 2
                    - (self.ancho_peatonal + self.separacion_linea) * x
                    - self.ancho_peatonal,
                    (self.altura + self.ancho_calle) / 2,
                    self.ancho_peatonal,
                    self.ancho_vereda,
                ),
            )
        for x in range(self.lineas_peatonales // 2):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho + self.separacion_linea) / 2
                    + (self.ancho_peatonal + self.separacion_linea) * x,
                    (self.altura + self.ancho_calle) / 2,
                    self.ancho_peatonal,
                    self.ancho_vereda,
                ),
            )

        for y in range(self.lineas_peatonales // 2):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho - self.ancho_calle) / 2 - self.ancho_vereda,
                    (self.altura - self.separacion_linea) / 2
                    - (self.ancho_peatonal + self.separacion_linea) * y
                    - self.ancho_peatonal,
                    self.ancho_vereda,
                    self.ancho_peatonal,
                ),
            )
        for y in range(self.lineas_peatonales // 2):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho - self.ancho_calle) / 2 - self.ancho_vereda,
                    (self.altura + self.separacion_linea) / 2
                    + (self.ancho_peatonal + self.separacion_linea) * y,
                    self.ancho_vereda,
                    self.ancho_peatonal,
                ),
            )

        for y in range(self.lineas_peatonales // 2):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho + self.ancho_calle) / 2,
                    (self.altura - self.separacion_linea) / 2
                    - (self.ancho_peatonal + self.separacion_linea) * y
                    - self.ancho_peatonal,
                    self.ancho_vereda,
                    self.ancho_peatonal,
                ),
            )
        for y in range(self.lineas_peatonales // 2):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho + self.ancho_calle) / 2,
                    (self.altura + self.separacion_linea) / 2
                    + (self.ancho_peatonal + self.separacion_linea) * y,
                    self.ancho_vereda,
                    self.ancho_peatonal,
                ),
            )

    def dibujar_lineas(self):
        for x in range(
            (self.ancho - self.ancho_calle) // 2
            - self.ancho_vereda
            - self.separacion_linea,
            0,
            -(self.altura_linea + self.separacion_linea),
        ):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    x - self.altura_linea,
                    (self.altura - self.ancho_linea) / 2,
                    self.altura_linea,
                    self.ancho_linea,
                ),
            )
        for x in range(
            (self.ancho + self.ancho_calle) // 2
            + self.ancho_vereda
            + self.separacion_linea,
            self.ancho,
            self.altura_linea + self.separacion_linea,
        ):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    x,
                    (self.altura - self.ancho_linea) / 2,
                    self.altura_linea,
                    self.ancho_linea,
                ),
            )
        for y in range(
            (self.altura - self.ancho_calle) // 2
            - self.ancho_vereda
            - self.separacion_linea,
            0,
            -(self.altura_linea + self.separacion_linea),
        ):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho - self.ancho_linea) / 2,
                    y - self.altura_linea,
                    self.ancho_linea,
                    self.altura_linea,
                ),
            )
        for y in range(
            (self.altura + self.ancho_calle) // 2
            + self.ancho_vereda
            + self.separacion_linea,
            self.altura,
            self.altura_linea + self.separacion_linea,
        ):
            pygame.draw.rect(
                self.superficie,
                self.color_linea,
                (
                    (self.ancho - self.ancho_linea) / 2,
                    y,
                    self.ancho_linea,
                    self.altura_linea,
                ),
            )

    def dibujar_semaforo_h(self):
        self.superficie.blit(
            self.imagen_semaforo_h,
            (
                (self.ancho - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.separacion_linea
                - self.altura_semaforo,
                (self.altura + self.ancho_calle) / 2 + self.ancho_vereda,
            ),
        )

    def dibujar_semaforo_v(self):
        self.superficie.blit(
            self.imagen_semaforo_v,
            (
                (self.ancho + self.ancho_calle) / 2 + self.ancho_vereda,
                (self.altura + self.ancho_calle) / 2
                + self.ancho_vereda
                + self.separacion_linea,
            ),
        )

    def dibujar_semaforo_peatones_h_1(self):
        self.superficie.blit(
            self.imagen_semaforo_peatones_h_1,
            (
                (self.ancho - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.separacion_linea
                - self.altura_semaforo_peatones
                - self.altura_semaforo
                - 4,
                (self.altura + self.ancho_calle) / 2 + self.ancho_vereda + 4,
            ),
        )

    def dibujar_semaforo_peatones_h_2(self):
        self.superficie.blit(
            self.imagen_semaforo_peatones_h_2,
            (
                (self.ancho - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.separacion_linea
                - self.altura_semaforo_peatones,
                (self.altura - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.ancho_semaforo_peatones
                - 4,
            ),
        )

    def dibujar_semaforo_peatones_v_1(self):
        self.superficie.blit(
            self.imagen_semaforo_peatones_v_1,
            (
                (self.ancho + self.ancho_calle) / 2 + self.ancho_vereda + 4,
                (self.altura + self.ancho_calle) / 2
                + self.ancho_vereda
                + self.separacion_linea
                + self.altura_semaforo
                + 4,
            ),
        )

    def dibujar_semaforo_peatones_v_2(self):
        self.superficie.blit(
            self.imagen_semaforo_peatones_v_2,
            (
                (self.ancho - self.ancho_calle) / 2
                - self.ancho_vereda
                - self.ancho_semaforo_peatones
                - 4,
                (self.altura + self.ancho_calle) / 2
                + self.ancho_vereda
                + self.ancho_semaforo
                + 4,
            ),
        )

    def dibujar_valor_contador(self):
        font = pygame.font.Font(None, self.size_contador)
        text_surface = font.render(str(self.valor_contador), True, self.color_contador)
        self.superficie.blit(
            text_surface, (self.separacion_contador, self.separacion_contador)
        )

    def dibujar_vehiculo_h(self, imagen, x, y):
        self.superficie.blit(
            pygame.transform.rotate(imagen, -90.0),
            (x - self.altura_vehiculo / 2, y - self.ancho_vehiculo / 2),
        )

    def dibujar_vehiculo_v(self, imagen, x, y):
        self.superficie.blit(
            imagen, (x - self.ancho_vehiculo / 2, y - self.altura_vehiculo / 2)
        )

    def dibujar_peaton_h(self, imagen, x, y):
        altura = imagen.get_height()

        self.superficie.blit(imagen, (x, y - altura))

    def dibujar_peaton_v(self, imagen, x, y):
        altura, ancho = imagen.get_size()

        self.superficie.blit(imagen, (x - altura, y - ancho))

    def dibujar_vehiculos_h(self):
        for vehiculo in self.vehiculos_h:
            self.dibujar_vehiculo_h(vehiculo[0], vehiculo[1], vehiculo[2])

    def dibujar_vehiculos_v(self):
        for vehiculo in self.vehiculos_v:
            self.dibujar_vehiculo_v(vehiculo[0], vehiculo[1], vehiculo[2])

    def dibujar_peatones_h(self):
        for peaton in self.peatones_h:
            self.dibujar_peaton_h(peaton[0], peaton[1], peaton[2])

    def dibujar_peatones_v(self):
        for peaton in self.peatones_v:
            self.dibujar_peaton_v(peaton[0], peaton[1], peaton[2])

    def draw(self):
        self.dibujar_fondo()
        self.dibujar_calles()
        self.dibujar_detalles()
        self.dibujar_veredas()
        self.dibujar_flechas()
        self.dibujar_peatonales()
        self.dibujar_lineas()
        self.dibujar_peatones_h()
        self.dibujar_peatones_v()
        self.dibujar_vehiculos_h()
        self.dibujar_vehiculos_v()
        self.dibujar_semaforo_h()
        self.dibujar_semaforo_v()
        self.dibujar_semaforo_peatones_h_1()
        self.dibujar_semaforo_peatones_h_2()
        self.dibujar_semaforo_peatones_v_1()
        self.dibujar_semaforo_peatones_v_2()
        self.dibujar_valor_contador()
        pygame.display.flip()
