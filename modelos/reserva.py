# Este archivo permite relacionar
# clientes con servicios mediante reservas.

class Reserva:

    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
