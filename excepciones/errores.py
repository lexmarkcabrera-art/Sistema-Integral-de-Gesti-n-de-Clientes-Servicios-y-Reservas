# =========================================================
# Archivo: errores.py
# Descripción:
# Aquí se manejan las excepciones personalizadas
# del sistema Software FJ.
# =========================================================


class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass
