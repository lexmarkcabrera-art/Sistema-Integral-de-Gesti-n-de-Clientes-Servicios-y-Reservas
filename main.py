# =========================================================
# Proyecto: Sistema Integral de Gestión - Software FJ
# Descripción:
# Sistema orientado a objetos SIN base de datos.
# Se implementan:
# - Abstracción
# - Herencia
# - Polimorfismo
# - Encapsulación
# - Manejo avanzado de excepciones
# - Registro de logs
# =========================================================

from modelos.cliente import Cliente
from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from modelos.reserva import Reserva

from datetime import datetime


# =========================================================
# LOGS
# =========================================================

LOG_FILE = "logs/logs.txt"


def registrar_log(mensaje):

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            f"{datetime.now()} -> {mensaje}\n"
        )


# =========================================================
# LISTAS DEL SISTEMA
# =========================================================

clientes = []
servicios = []
reservas = []

print("\n=========== SOFTWARE FJ ===========\n")


# =========================================================
# OPERACIÓN 1
# CLIENTE VÁLIDO
# =========================================================

try:

    c1 = Cliente(
        "Carlos Perez",
        "carlos@gmail.com",
        "123456789"
    )

    clientes.append(c1)

    print(
        "Cliente registrado correctamente"
    )

    registrar_log(
        "Cliente válido registrado"
    )

except Exception as e:

    print("Error:", e)

    registrar_log(
        f"ERROR CLIENTE: {e}"
    )


# =========================================================
# OPERACIÓN 2
# CLIENTE INVÁLIDO
# =========================================================

try:

    c2 = Cliente(
        "Al",
        "correo_mal",
        "abc"
    )

    clientes.append(c2)

except Exception as e:

    print("Error:", e)

    registrar_log(
        f"ERROR CLIENTE INVÁLIDO: {e}"
    )


# =========================================================
# OPERACIÓN 3
# SERVICIO SALA
# =========================================================

try:

    s1 = ReservaSala(
        "Sala Premium",
        50,
        20
    )

    servicios.append(s1)

    print("Servicio Sala creado")

except Exception as e:

    print(e)

    registrar_log(
        f"ERROR SERVICIO: {e}"
    )


# =========================================================
# OPERACIÓN 4
# SERVICIO EQUIPO
# =========================================================

try:

    s2 = AlquilerEquipo(
        "Laptop Gamer",
        80,
        "Computador"
    )

    servicios.append(s2)

    print("Servicio Equipo creado")

except Exception as e:

    print(e)

    registrar_log(
        f"ERROR SERVICIO: {e}"
    )


# =========================================================
# OPERACIÓN 5
# SERVICIO ASESORÍA
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

    registrar_log(
        f"ERROR SERVICIO: {e}"
    )


# =========================================================
# OPERACIÓN 6
# RESERVA EXITOSA
# =========================================================

try:

    r1 = Reserva(
        c1,
        s1,
        3
    )

    reservas.append(r1)

    r1.confirmar()

    r1.procesar_reserva()

    registrar_log(
        "Reserva exitosa"
    )

except Exception as e:

    print(e)

    registrar_log(
        f"ERROR RESERVA: {e}"
    )


# =========================================================
# OPERACIÓN 7
# RESERVA FALLIDA
# =========================================================

try:

    r2 = Reserva(
        "Cliente falso",
        s2,
        2
    )

except Exception as e:

    print("Error:", e)

    registrar_log(
        f"RESERVA FALLIDA: {e}"
    )


# =========================================================
# OPERACIÓN 8
# DURACIÓN INVÁLIDA
# =========================================================

try:

    r3 = Reserva(
        c1,
        s3,
        -1
    )

except Exception as e:

    print("Error:", e)

    registrar_log(
        f"DURACIÓN INVÁLIDA: {e}"
    )


# =========================================================
# OPERACIÓN 9
# CÁLCULO CON IMPUESTOS
# =========================================================

try:

    total = s1.calcular_costo(
        5,
        0.19
    )

    print(
        f"Costo Sala con impuestos: ${total}"
    )

except Exception as e:

    print(e)


# =========================================================
# OPERACIÓN 10
# CÁLCULO CON DESCUENTO
# =========================================================

try:

    total = s2.calcular_costo(
        4,
        0.10
    )

    print(
        f"Costo Equipo con descuento: ${total}"
    )

except Exception as e:

    print(e)


# =========================================================
# TRY / EXCEPT / ELSE / FINALLY
# =========================================================

try:

    numero = int("10")

except ValueError as e:

    registrar_log(
        f"ERROR CONVERSIÓN: {e}"
    )

else:

    print(
        "Conversión realizada correctamente"
    )

finally:

    print(
        "Finalizó el bloque de validación"
    )


# =========================================================
# RESUMEN FINAL
# =========================================================

print("\n=========== RESUMEN ===========")

print(
    f"Clientes registrados: "
    f"{len(clientes)}"
)

print(
    f"Servicios registrados: "
    f"{len(servicios)}"
)

print(
    f"Reservas registradas: "
    f"{len(reservas)}"
)

print("Sistema ejecutado correctamente")

print("Revise el archivo logs.txt")

print("================================")
