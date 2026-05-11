# En este archivo se manejan
# las excepciones personalizadas del sistema.

class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass
