# =========================================================
# Proyecto: Sistema Integral de Gestión - Software FJ
# Descripción:
# Sistema orientado a objetos SIN base de datos.
# Aquí se realizan todas las pruebas del sistema.
# =========================================================

from modelos.cliente import Cliente
from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from modelos.reserva import Reserva


# Listas principales
clientes = []
servicios = []
reservas = []

print("\n=========== SOFTWARE FJ ===========\n")


# =========================================================
# REGISTRO DE CLIENTE VÁLIDO
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

except Exception as e:

    print("Error:", e)


# =========================================================
# REGISTRO DE CLIENTE INVÁLIDO
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


# =========================================================
# CREACIÓN DE SERVICIOS
# =========================================================

s1 = ReservaSala(
    "Sala Premium",
    50,
    20
)

s2 = AlquilerEquipo(
    "Laptop Gamer",
    80,
    "Computador"
)

s3 = AsesoriaEspecializada(
    "Asesoría Python",
    100,
    "Ingeniero Senior"
)

servicios.append(s1)
servicios.append(s2)
servicios.append(s3)


# =========================================================
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

except Exception as e:

    print("Error:", e)


# =========================================================
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


# =========================================================
# CÁLCULO DE COSTOS
# =========================================================

print(
    f"Costo Sala con impuestos: "
    f"${s1.calcular_costo(5, 0.19)}"
)

print(
    f"Costo Equipo con descuento: "
    f"${s2.calcular_costo(4, 0.10)}"
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

print(
    "Sistema ejecutado correctamente"
)

print("================================")
