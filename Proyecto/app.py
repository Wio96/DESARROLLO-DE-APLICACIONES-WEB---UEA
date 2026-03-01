from flask import Flask, render_template, request, redirect, url_for
from models import GestorDestinos, PaqueteTuristico

app = Flask(__name__)
gestor = GestorDestinos()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reservar')
def reservar():
    return render_template('reservar.html')

@app.route('/admin/inventario')
def gestion_inventario():
    lista = gestor.listar_paquetes()
    return render_template('inventario.html', productos=lista)

@app.route('/admin/nuevo', methods=['POST'])
def nuevo_paquete():
    id_p = request.form.get('id')
    nombre = request.form.get('nombre')
    desc = request.form.get('descripcion')
    precio = request.form.get('precio')
    
    nuevo = PaqueteTuristico(id_p, nombre, desc, precio)
    gestor.agregar_paquete(nuevo)
    return redirect(url_for('gestion_inventario'))

@app.route('/admin/eliminar/<int:id_p>')
def eliminar(id_p):
    gestor.eliminar_paquete(id_p)
    return redirect(url_for('gestion_inventario'))

@app.route('/confirmacion/<cliente>')
def confirmacion(cliente):
    return render_template('confirmacion.html', nombre=cliente)

if __name__ == '__main__':
    app.run(debug=True)