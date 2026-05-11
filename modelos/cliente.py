# =========================================================
# Archivo: cliente.py
# Descripción:
# En este archivo se maneja toda la información
# relacionada con los clientes del sistema.
# También se aplican validaciones y encapsulación.
# =========================================================

from abc import ABC, abstractmethod
from excepciones.errores import ClienteError


# Clase abstracta Persona
class Persona(ABC):

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase Cliente
class Cliente(Persona):

    def __init__(self, nombre, correo, telefono):

        # Encapsulación de atributos
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        # Validación automática
        self.validar_datos()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    # Método encargado de validar los datos
    def validar_datos(self):

        if len(self.__nombre.strip()) < 3:
            raise ClienteError(
                "El nombre es demasiado corto"
            )

        if "@" not in self.__correo:
            raise ClienteError(
                "Correo inválido"
            )

        if not self.__telefono.isdigit():
            raise ClienteError(
                "El teléfono debe contener solo números"
            )

    # Método sobrescrito
    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo}"
        )
