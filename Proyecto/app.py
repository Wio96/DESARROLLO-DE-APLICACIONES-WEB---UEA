from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Página principal del portal de reservas
    return render_template('index.html')

@app.route('/reservar')
def reservar():
    # Aquí irá el formulario para la base de datos después
    return render_template('reservar.html')

@app.route('/confirmacion/<cliente>')
def confirmacion(cliente):
    # Ruta dinámica que recibe el nombre del cliente
    return render_template('confirmacion.html', nombre=cliente)

if __name__ == '__main__':
    app.run(debug=True)