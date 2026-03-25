from flask_login import UserMixin

# Clase para el Usuario (Requerida para el Login)
class Usuario(UserMixin):
    def __init__(self, id_usuario, nombre, email, password):
        self.id = id_usuario  # Flask-Login usa 'id' por defecto
        self.nombre = nombre
        self.email = email
        self.password = password

# Clase para la Reserva (Requerida para el CRUD)
class Reserva:
    def __init__(self, id_reserva, nombre_cliente, paquete, fecha, pasajeros):
        self.id_reserva = id_reserva
        self.nombre_cliente = nombre_cliente
        self.paquete = paquete
        self.fecha = fecha
        self.pasajeros = pasajeros