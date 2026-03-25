from conexion.conexion import obtener_conexion
from models.reserva import Usuario, Reserva

class ReservaService:
    def validar_usuario(self, email, password):
        db = obtener_conexion()
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE email = %s AND password = %s", (email, password))
            u = cursor.fetchone()
            db.close()
            if u:
                return Usuario(u['id_usuario'], u['nombre'], u['email'], u['password'])
        return None

    def obtener_usuario_por_id(self, user_id):
        db = obtener_conexion()
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
            u = cursor.fetchone()
            db.close()
            if u:
                return Usuario(u['id_usuario'], u['nombre'], u['email'], u['password'])
        return None

    def obtener_todas(self):
        db = obtener_conexion()
        lista_final = []
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reserva")
            lista_final = cursor.fetchall()
            db.close()
        return lista_final
    
    # --- AQUÍ ESTABA EL ERROR DE ESPACIOS ---
    def eliminar(self, codigo):
        db = obtener_conexion()
        if db:
            cursor = db.cursor()
            # Usamos tu nombre de columna 'codigo_reserva'
            sql = "DELETE FROM reserva WHERE codigo_reserva = %s"
            cursor.execute(sql, (codigo,))
            db.commit() 
            db.close()
            return True
        return False
    def obtener_por_codigo(self, codigo):
        db = obtener_conexion()
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reserva WHERE codigo_reserva = %s", (codigo,))
            reserva = cursor.fetchone()
            db.close()
            return reserva
        return None

def actualizar(self, codigo, id_cliente, id_paquete, fecha_viaje, pasajeros, estado):
    db = obtener_conexion()
    if db:
        cursor = db.cursor()
        sql = """UPDATE reserva 
                 SET id_cliente=%s, id_paquete=%s, fecha_viaje=%s, cantidad_pasajeros=%s, estado=%s 
                 WHERE codigo_reserva=%s"""
        cursor.execute(sql, (id_cliente, id_paquete, fecha_viaje, pasajeros, estado, codigo))
        db.commit()
        db.close()
        return True
    return False