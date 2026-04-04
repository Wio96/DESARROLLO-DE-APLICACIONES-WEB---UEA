from conexion.conexion import obtener_conexion
from models.reserva import Usuario, Reserva

class ReservaService:
    def validar_usuario(self, email, password):
        db = obtener_conexion()
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE email = %s AND password = %s", (email, password))
            u = cursor.fetchone()
            cursor.close()
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
            cursor.close()
            db.close()
            if u:
                return Usuario(u['id_usuario'], u['nombre'], u['email'], u['password'])
        return None

    def obtener_todas(self):
        db = obtener_conexion()
        lista_final = []
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reserva ORDER BY codigo_reserva DESC")
            lista_final = cursor.fetchall()
            cursor.close()
            db.close()
        return lista_final

    def crear(self, nombre, email, id_paquete, fecha_viaje, pasajeros, estado):
        db = obtener_conexion()
        if db:
            try:
                cursor = db.cursor()
                
                # PASO 1: Buscar si el cliente ya existe en la tabla 'cliente'
                # Usamos 'correo_electronico' que es tu nombre de columna real
                cursor.execute("SELECT id_cliente FROM cliente WHERE correo_electronico = %s", (email,))
                res = cursor.fetchone()
                
                if res:
                    id_cliente_final = res[0]
                else:
                    # Si no existe, lo creamos con tus nombres de columna exactos
                    sql_cliente = "INSERT INTO cliente (nombre_completo, correo_electronico) VALUES (%s, %s)"
                    cursor.execute(sql_cliente, (nombre, email))
                    id_cliente_final = cursor.lastrowid

                # PASO 2: Insertar la reserva en la tabla 'reserva'
                # Usamos el orden de columnas que me pasaste antes
                sql_reserva = """INSERT INTO reserva (id_cliente, id_paquete, fecha_solicitud, fecha_viaje, cantidad_pasajeros, estado) 
                                 VALUES (%s, %s, NOW(), %s, %s, %s)"""
                
                cursor.execute(sql_reserva, (id_cliente_final, id_paquete, fecha_viaje, pasajeros, estado))
                
                db.commit()
                cursor.close()
                db.close()
                return True
            except Exception as e:
                print(f"Error en creación: {e}")
                return False
        return False

    def obtener_por_codigo(self, codigo):
        db = obtener_conexion()
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reserva WHERE codigo_reserva = %s", (codigo,))
            reserva = cursor.fetchone()
            cursor.close()
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
            cursor.close()
            db.close()
            return True
        return False

    def eliminar(self, codigo):
        db = obtener_conexion()
        if db:
            cursor = db.cursor()
            sql = "DELETE FROM reserva WHERE codigo_reserva = %s"
            cursor.execute(sql, (codigo,))
            db.commit() 
            cursor.close()
            db.close()
            return True
        return False