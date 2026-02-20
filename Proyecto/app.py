from flask import Flask # Importamos Flask [cite: 646, 673]

app = Flask(__name__) # Inicializamos la aplicación Flask [cite: 647, 676]

# 1. Ruta principal (/) [cite: 647, 679, 680]
@app.route('/')
def home(): # [cite: 648, 682]
    # La tarea pide que muestre el propósito del negocio [cite: 649, 683]
    return '<h1>Bienvenido al Sistema de Reservas - Papangu Tours</h1>'

# 2. Ruta dinámica adaptada a tu negocio (/reserva/<cliente>) [cite: 736, 737]
@app.route('/reserva/<cliente>') # [cite: 739]
def reserva(cliente): # [cite: 740]
    # Devuelve un mensaje coherente usando el parámetro [cite: 741]
    return f'<h2>¡Hola, {cliente}! Tu reserva para el tour en la selva está en proceso.</h2>'

# Ejecutamos el servidor en modo depuración [cite: 651, 652]
if __name__ == '__main__': # [cite: 685]
    app.run(debug=True) # [cite: 688, 689]