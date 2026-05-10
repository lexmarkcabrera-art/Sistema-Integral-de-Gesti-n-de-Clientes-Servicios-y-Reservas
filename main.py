# =========================================================
# Proyecto: Sistema Integral de Gestión - Software FJ
# Autor: ChatGPT
# Descripción:
# Sistema orientado a objetos SIN base de datos.
# Maneja clientes, servicios y reservas utilizando:
# - Abstracción
# - Herencia
# - Polimorfismo
# - Encapsulación
# - Sobrecarga de métodos
# - Manejo avanzado de excepciones
# - Registro de logs
# =========================================================

from abc import ABC, abstractmethod
from datetime import datetime


# =========================================================
# LOGS
# =========================================================

LOG_FILE = "logs.txt"


def registrar_log(mensaje):
    with open(LOG_FILE, "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} -> {mensaje}\n")


# =========================================================
# EXCEPCIONES PERSONALIZADAS
# =========================================================

class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass


# =========================================================
# CLASE ABSTRACTA PERSONA
# =========================================================

class Persona(ABC):

    @abstractmethod
    def mostrar_informacion(self):
        pass


# =========================================================
# CLASE CLIENTE
# =========================================================

class Cliente(Persona):

    def __init__(self, nombre, correo, telefono):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    # Encapsulación
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar_datos(self):

        try:
            if len(self.__nombre.strip()) < 3:
                raise ClienteError("El nombre es demasiado corto")

            if "@" not in self.__correo:
                raise ClienteError("Correo inválido")

            if not self.__telefono.isdigit():
                raise ClienteError("El teléfono debe contener solo números")

        except ClienteError as e:
            registrar_log(f"ERROR CLIENTE: {e}")
            raise

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo}"


# =========================================================
# CLASE ABSTRACTA SERVICIO
# =========================================================

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


# =========================================================
# SERVICIO: RESERVA DE SALAS
# =========================================================

class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas=1, impuestos=0):

        total = self.precio_base * horas

        if impuestos > 0:
            total += total * impuestos

        return total

    def descripcion(self):
        return f"Sala con capacidad para {self.capacidad} personas"


# =========================================================
# SERVICIO: ALQUILER DE EQUIPOS
# =========================================================

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, tipo_equipo):
        super().__init__(nombre, precio_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias=1, descuento=0):

        total = self.precio_base * dias

        if descuento > 0:
            total -= total * descuento

        return total

    def descripcion(self):
        return f"Alquiler de equipo tipo: {self.tipo_equipo}"


# =========================================================
# SERVICIO: ASESORÍAS
# =========================================================

class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, experto):
        super().__init__(nombre, precio_base)
        self.experto = experto

    def calcular_costo(self, horas=1, urgente=False):

        total = self.precio_base * horas

        if urgente:
            total += 100

        return total

    def descripcion(self):
        return f"Asesoría realizada por: {self.experto}"


# =========================================================
# CLASE RESERVA
# =========================================================

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        try:
            if not isinstance(cliente, Cliente):
                raise ReservaError("Cliente inválido")

            if not isinstance(servicio, Servicio):
                raise ReservaError("Servicio inválido")

            if duracion <= 0:
                raise ReservaError("La duración debe ser mayor que cero")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "Pendiente"

        except ReservaError as e:
            registrar_log(f"ERROR RESERVA: {e}")
            raise

    def confirmar(self):
        self.estado = "Confirmada"
        registrar_log(
            f"Reserva confirmada para {self.cliente.nombre}"
        )

    def cancelar(self):
        self.estado = "Cancelada"
        registrar_log(
            f"Reserva cancelada para {self.cliente.nombre}"
        )

    def procesar_reserva(self):

        try:

            costo = self.servicio.calcular_costo(self.duracion)

            print("\n===================================")
            print("RESERVA PROCESADA")
            print("===================================")
            print(self.cliente.mostrar_informacion())
            print(self.servicio.descripcion())
            print(f"Duración: {self.duracion}")
            print(f"Costo Total: ${costo}")
            print(f"Estado: {self.estado}")
            print("===================================\n")

            registrar_log(
                f"Reserva procesada correctamente para {self.cliente.nombre}"
            )

        except Exception as e:

            registrar_log(f"ERROR PROCESANDO RESERVA: {e}")

            raise ReservaError(
                "No fue posible procesar la reserva"
            ) from e


# =========================================================
# SISTEMA PRINCIPAL
# =========================================================

clientes = []
servicios = []
reservas = []

print("\n=========== SOFTWARE FJ ===========\n")


# =========================================================
# OPERACIÓN 1 - CLIENTE VÁLIDO
# =========================================================

try:
    c1 = Cliente("Carlos Perez", "carlos@gmail.com", "123456789")
    clientes.append(c1)
    print("Cliente registrado correctamente")

except Exception as e:
    print(e)


# =========================================================
# OPERACIÓN 2 - CLIENTE INVÁLIDO
# =========================================================

try:
    c2 = Cliente("Al", "correo_mal", "abc")
    clientes.append(c2)

except Exception as e:
    print("Error:", e)


# =========================================================
# OPERACIÓN 3 - SERVICIO SALA
# =========================================================

try:
    s1 = ReservaSala("Sala Premium", 50, 20)
    servicios.append(s1)
    print("Servicio Sala creado")

except Exception as e:
    print(e)


# =========================================================
# OPERACIÓN 4 - SERVICIO EQUIPO
# =========================================================

try:
    s2 = AlquilerEquipo("Laptop Gamer", 80, "Computador")
    servicios.append(s2)
    print("Servicio Equipo creado")

except Exception as e:
    print(e)


# =========================================================
# OPERACIÓN 5 - SERVICIO ASESORÍA
# =========================================================

try:
    s3 = AsesoriaEspecializada(
        "Asesoría Python",
        100,
        "Ingeniero Senior"
    )

    servicios.append(s3)

    print("Servicio Asesoría creado")

except Exception as e:
    print(e)


# =========================================================
# OPERACIÓN 6 - RESERVA EXITOSA
# =========================================================

try:

    r1 = Reserva(c1, s1, 3)

    reservas.append(r1)

    r1.confirmar()

    r1.procesar_reserva()

except Exception as e:
    print(e)


# =========================================================
# OPERACIÓN 7 - RESERVA FALLIDA
# =========================================================

try:

    r2 = Reserva("Cliente falso", s2, 2)

    reservas.append(r2)

except Exception as e:
    print("Error:", e)


# =========================================================
# OPERACIÓN 8 - RESERVA CON DURACIÓN INVÁLIDA
# =========================================================

try:

    r3 = Reserva(c1, s3, -1)

    reservas.append(r3)

except Exception as e:
    print("Error:", e)


# =========================================================
# OPERACIÓN 9 - CÁLCULO CON IMPUESTOS
# =========================================================

try:

    total = s1.calcular_costo(5, 0.19)

    print(f"Costo Sala con impuestos: ${total}")

except Exception as e:
    print(e)


# =========================================================
# OPERACIÓN 10 - CÁLCULO CON DESCUENTO
# =========================================================

try:

    total = s2.calcular_costo(4, 0.10)

    print(f"Costo Equipo con descuento: ${total}")

except Exception as e:
    print(e)


# =========================================================
# TRY / EXCEPT / ELSE / FINALLY
# =========================================================

try:

    numero = int("10")

except ValueError as e:

    registrar_log(f"ERROR CONVERSIÓN: {e}")

else:

    print("Conversión realizada correctamente")

finally:

    print("Finalizó el bloque de validación")


# =========================================================
# RESUMEN FINAL
# =========================================================

print("\n=========== RESUMEN ===========")
print(f"Clientes registrados: {len(clientes)}")
print(f"Servicios registrados: {len(servicios)}")
print(f"Reservas registradas: {len(reservas)}")
print("Sistema ejecutado correctamente")
print("Revise el archivo logs.txt")
print("================================")
