// 1. FUNCIONALIDAD: BOTÓN DE ALERTA
const btnAlerta = document.getElementById('btnAlerta');

btnAlerta.addEventListener('click', function() {
    alert("¡Hola! Has interactuado con JavaScript y Bootstrap correctamente.");
});

// 2. FUNCIONALIDAD: VALIDACIÓN DEL FORMULARIO
const formulario = document.getElementById('formularioContacto');

formulario.addEventListener('submit', function(evento) {
    // Evitamos que el formulario se envíe automáticamente
    evento.preventDefault();

    // Obtenemos los valores de los campos
    const nombre = document.getElementById('nombre');
    const email = document.getElementById('email');
    const mensaje = document.getElementById('mensaje');

    // Variables para controlar si hay errores
    let validacionCorrecta = true;

    // --- Validar Nombre ---
    if (nombre.value.trim() === "") {
        mostrarError('errorNombre', 'El nombre es obligatorio.');
        nombre.classList.add('is-invalid'); // Clase de Bootstrap para borde rojo
        validacionCorrecta = false;
    } else {
        ocultarError('errorNombre');
        nombre.classList.remove('is-invalid');
        nombre.classList.add('is-valid'); // Clase de Bootstrap para borde verde
    }

    // --- Validar Email ---
    if (email.value.trim() === "") {
        mostrarError('errorEmail', 'El correo es obligatorio.');
        email.classList.add('is-invalid');
        validacionCorrecta = false;
    } else {
        ocultarError('errorEmail');
        email.classList.remove('is-invalid');
        email.classList.add('is-valid');
    }

    // --- Validar Mensaje ---
    if (mensaje.value.trim() === "") {
        mostrarError('errorMensaje', 'Por favor, escribe un mensaje.');
        mensaje.classList.add('is-invalid');
        validacionCorrecta = false;
    } else {
        ocultarError('errorMensaje');
        mensaje.classList.remove('is-invalid');
        mensaje.classList.add('is-valid');
    }

    // Si todo está correcto, mostramos éxito
    if (validacionCorrecta) {
        alert("¡Formulario enviado con éxito! Nos pondremos en contacto.");
        formulario.reset(); // Limpiar formulario
        // Quitar las clases verdes
        nombre.classList.remove('is-valid');
        email.classList.remove('is-valid');
        mensaje.classList.remove('is-valid');
    }
});

// Funciones auxiliares para reutilizar código
function mostrarError(idElemento, texto) {
    const elemento = document.getElementById(idElemento);
    elemento.textContent = texto;
    elemento.style.display = 'block';
}

function ocultarError(idElemento) {
    const elemento = document.getElementById(idElemento);
    elemento.style.display = 'none';
}