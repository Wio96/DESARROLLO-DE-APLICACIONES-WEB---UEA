from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from services.reserva_service import ReservaService
from fpdf import FPDF 

app = Flask(__name__)
app.secret_key = 'papangu_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

service = ReservaService()

@login_manager.user_loader
def load_user(user_id):
    return service.obtener_usuario_por_id(user_id)

# --- RUTAS ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = service.validar_usuario(email, password)
        if usuario:
            login_user(usuario)
            return redirect(url_for('listar_reserva'))
        flash('Correo o contraseña incorrectos', 'danger')
    return render_template('login.html')

@app.route('/reservar')
def crear_reserva():
    return render_template('reserva/crear.html')

@app.route('/reserva/listar')
@login_required
def listar_reserva():
    lista = service.obtener_todas()
    return render_template('reserva/listar.html', reserva=lista)

@app.route('/reserva/eliminar/<int:id_p>')
@login_required
def eliminar(id_p):
    if service.eliminar(id_p):
        flash(f'Reserva #{id_p} eliminada con éxito', 'success')
    else:
        flash('Error al intentar eliminar la reserva', 'danger')
    return redirect(url_for('listar_reserva'))

@app.route('/reserva/editar/<int:id_p>', methods=['GET', 'POST'])
@login_required
def editar_reserva(id_p):
    if request.method == 'POST':
        # Capturamos según los 'name' del formulario HTML
        id_cli = request.form.get('id_cliente')
        id_paq = request.form.get('id_paquete')
        f_viaje = request.form.get('fecha_viaje')
        pasajeros = request.form.get('cantidad_pasajeros')
        est = request.form.get('estado')
        
        if service.actualizar(id_p, id_cli, id_paq, f_viaje, pasajeros, est):
            flash('Reserva de Papangu Tours actualizada', 'success')
        return redirect(url_for('listar_reserva'))

    datos = service.obtener_por_codigo(id_p)
    return render_template('reserva/editar.html', r=datos)

@app.route('/reserva/reporte')
@login_required
def reporte_pdf():
    lista = service.obtener_todas()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "Reporte de Reservas - Papangu Tours", 0, 1, 'C')
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(30, 10, "Codigo", 1)
    pdf.cell(80, 10, "Cliente", 1)
    pdf.cell(50, 10, "Tour", 1)
    pdf.cell(30, 10, "Pasajeros", 1, 1)
    
    pdf.set_font("Arial", '', 10)
    for r in lista:
        pdf.cell(30, 10, str(r['codigo_reserva']), 1)
        pdf.cell(80, 10, str(r['nombre_cliente']), 1)
        pdf.cell(50, 10, str(r['paquete_turistico']), 1)
        pdf.cell(30, 10, str(r['cantidad_pasajeros']), 1, 1)
    
    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=reporte_reservas.pdf'
    return response

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# ESTO SIEMPRE AL FINAL
if __name__ == '__main__':
    app.run(debug=True)