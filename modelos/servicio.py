# =========================================================
# Archivo: servicio.py
# Descripción:
# En este archivo se manejan todos los servicios
# que ofrece la empresa Software FJ.
# Aquí se aplica herencia y polimorfismo.
# =========================================================

from abc import ABC, abstractmethod


# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Servicio de reserva de salas
class ReservaSala(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        capacidad
    ):

        super().__init__(
            nombre,
            precio_base
        )

        self.capacidad = capacidad

    # Método con parámetros opcionales
    def calcular_costo(
        self,
        horas=1,
        impuestos=0
    ):

        total = self.precio_base * horas

        if impuestos > 0:
            total += total * impuestos

        return total

    def descripcion(self):

        return (
            f"Sala con capacidad "
            f"para {self.capacidad} personas"
        )


# Servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        tipo_equipo
    ):

        super().__init__(
            nombre,
            precio_base
        )

        self.tipo_equipo = tipo_equipo

    def calcular_costo(
        self,
        dias=1,
        descuento=0
    ):

        total = self.precio_base * dias

        if descuento > 0:
            total -= total * descuento

        return total

    def descripcion(self):

        return (
            f"Alquiler de equipo tipo: "
            f"{self.tipo_equipo}"
        )


# Servicio de asesorías
class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        experto
    ):

        super().__init__(
            nombre,
            precio_base
        )

        self.experto = experto

    def calcular_costo(
        self,
        horas=1,
        urgente=False
    ):

        total = self.precio_base * horas

        if urgente:
            total += 100

        return total

    def descripcion(self):

        return (
            f"Asesoría realizada por: "
            f"{self.experto}"
        )
