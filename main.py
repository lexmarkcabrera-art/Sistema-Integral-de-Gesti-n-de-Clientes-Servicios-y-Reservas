# Archivo principal del sistema.
# Aquí se ejecutan las pruebas
# del proyecto Software FJ.

from modelos.cliente import Cliente
from modelos.servicio import ReservaSala
from modelos.reserva import Reserva


cliente1 = Cliente(
    "Carlos",
    "carlos@gmail.com",
    "123456"
)

servicio1 = ReservaSala(
    "Sala VIP",
    100
)

reserva1 = Reserva(
    cliente1,
    servicio1
)

print(cliente1.mostrar_informacion())
print(servicio1.calcular_costo())
