# En este archivo se maneja toda la información
# relacionada con los clientes del sistema.

from abc import ABC, abstractmethod


class Persona(ABC):

    @abstractmethod
    def mostrar_informacion(self):
        pass


class Cliente(Persona):

    def __init__(self, nombre, correo, telefono):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre}"
