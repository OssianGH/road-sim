class SemaforoEstado:

    ROJO = 0
    AMARILLO = 1
    VERDE = 2
    ESPECIAL = 3

    TRANSICION = {
        ESPECIAL: VERDE,
        ROJO: ESPECIAL,
        AMARILLO: ROJO,
        VERDE: AMARILLO,
    }
