from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reservar')
def reservar():
    return render_template('reservar.html')

@app.route('/confirmacion/<cliente>')
def confirmacion(cliente):
    # Esta ruta servirá para mostrar el éxito de la inserción después
    return render_template('confirmacion.html', nombre=cliente)

if __name__ == '__main__':
    app.run(debug=True)