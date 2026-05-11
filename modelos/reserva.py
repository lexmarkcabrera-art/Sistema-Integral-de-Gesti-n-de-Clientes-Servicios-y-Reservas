# =========================================================
# Archivo: reserva.py
# Descripción:
# Este archivo permite manejar las reservas
# realizadas por los clientes.
# =========================================================

from excepciones.errores import ReservaError
from modelos.cliente import Cliente
from modelos.servicio import Servicio


class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        # Validaciones de seguridad
        if not isinstance(cliente, Cliente):
            raise ReservaError(
                "Cliente inválido"
            )

        if not isinstance(servicio, Servicio):
            raise ReservaError(
                "Servicio inválido"
            )

        if duracion <= 0:
            raise ReservaError(
                "La duración debe ser mayor que cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar(self):

        self.estado = "Confirmada"

    # Cancelar reserva
    def cancelar(self):

        self.estado = "Cancelada"

    # Procesar reserva
    def procesar_reserva(self):

        costo = self.servicio.calcular_costo(
            self.duracion
        )

        print("\n=========== RESERVA ===========")

        print(
            self.cliente.mostrar_informacion()
        )

        print(
            self.servicio.descripcion()
        )

        print(
            f"Duración: {self.duracion}"
        )

        print(
            f"Costo: ${costo}"
        )

        print(
            f"Estado: {self.estado}"
        )

        print(
            "===============================\n"
        )
