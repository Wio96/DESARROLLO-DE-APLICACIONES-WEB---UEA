import sqlite3

class PaqueteTuristico:
    def __init__(self, id_paquete, nombre_paquete, descripcion, precio_referencial):
        self.id = id_paquete
        self.nombre = nombre_paquete
        self.descripcion = descripcion
        self.precio = precio_referencial

class GestorDestinos:
    def __init__(self, db_path='papangu.db'):
        self.db_path = db_path
        self._inicializar_db()

    def _get_connection(self):
        # Esta conexión generará el archivo .db automáticamente
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _inicializar_db(self):
        with self._get_connection() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS paquetes (
                id_paquete INTEGER PRIMARY KEY,
                nombre_paquete TEXT NOT NULL,
                descripcion TEXT,
                precio_referencial REAL NOT NULL)''')

    # CRUD: Leer (Uso de colecciones: Lista de Diccionarios)
    def listar_paquetes(self):
        with self._get_connection() as conn:
            rows = conn.execute('SELECT * FROM paquetes').fetchall()
            return [dict(r) for r in rows]

    # CRUD: Crear
    def agregar_paquete(self, p):
        with self._get_connection() as conn:
            conn.execute('INSERT INTO paquetes VALUES (?,?,?,?)', 
                         (p.id, p.nombre, p.descripcion, p.precio))

    # CRUD: Eliminar
    def eliminar_paquete(self, id_p):
        with self._get_connection() as conn:
            conn.execute('DELETE FROM paquetes WHERE id_paquete = ?', (id_p,))