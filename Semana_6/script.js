// 1. Selección de elementos del DOM
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');
const btnSubmit = document.getElementById('btnSubmit');
const btnReset = document.getElementById('btnReset');

// 2. Objeto para controlar el estado de cada campo (True = Valido, False = Invalido)
const validaciones = {
    nombre: false,
    email: false,
    edad: false,
    password: false,
    confirmPassword: false
};

// 3. Expresiones Regulares (Regex) para validar formatos
const expresiones = {
    // Nombre: Letras, espacios y acentos. Mínimo 3 caracteres.
    nombre: /^[a-zA-ZÀ-ÿ\s]{3,40}$/, 
    // Email: Formato estándar de correo
    email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    // Password: Mínimo 8 chars, al menos 1 numero y 1 caracter especial
    // Nota: (?=.*[0-9]) busca un numero, (?=.*[!@#...]) busca un símbolo
    password: /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/
};

// 4. Función principal que valida cada campo según su "name" o "id"
const validarFormulario = (e) => {
    switch (e.target.id) {
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre', 'El nombre debe tener al menos 3 letras.');
        break;
        case "email":
            validarCampo(expresiones.email, e.target, 'email', 'El correo no es válido.');
        break;
        case "edad":
            validarEdad(e.target);
        break;
        case "password":
            validarCampo(expresiones.password, e.target, 'password', 'Mínimo 8 caracteres, 1 número y 1 símbolo.');
            validarConfirmacion(); // Si cambio la pass, debo revalidar la confirmación
        break;
        case "confirmPassword":
            validarConfirmacion();
        break;
    }
    // Intentar activar el botón cada vez que se valida un campo
    activarBoton();
};

// 5. Función genérica para validar con Regex (Visuales)
const validarCampo = (expresion, input, campo, mensaje) => {
    if(expresion.test(input.value)){
        // Caso Correcto
        document.getElementById(`error${capitalize(campo)}`).textContent = '';
        input.classList.remove('incorrecto');
        input.classList.add('correcto');
        validaciones[campo] = true;
    } else {
        // Caso Incorrecto
        document.getElementById(`error${capitalize(campo)}`).textContent = mensaje;
        input.classList.add('incorrecto');
        input.classList.remove('correcto');
        validaciones[campo] = false;
    }
};

// 6. Validación específica para Edad (>= 18)
const validarEdad = (input) => {
    const edad = parseInt(input.value);
    if (edad >= 18 && edad <= 100) {
        document.getElementById('errorEdad').textContent = '';
        input.classList.remove('incorrecto');
        input.classList.add('correcto');
        validaciones.edad = true;
    } else {
        document.getElementById('errorEdad').textContent = 'Debes tener al menos 18 años.';
        input.classList.add('incorrecto');
        input.classList.remove('correcto');
        validaciones.edad = false;
    }
};

// 7. Validación específica para Confirmar Contraseña
const validarConfirmacion = () => {
    const inputPass1 = document.getElementById('password');
    const inputPass2 = document.getElementById('confirmPassword');

    if(inputPass1.value !== inputPass2.value || inputPass2.value === "") {
        document.getElementById('errorConfirm').textContent = 'Las contraseñas no coinciden.';
        inputPass2.classList.add('incorrecto');
        inputPass2.classList.remove('correcto');
        validaciones.confirmPassword = false;
    } else {
        document.getElementById('errorConfirm').textContent = '';
        inputPass2.classList.remove('incorrecto');
        inputPass2.classList.add('correcto');
        validaciones.confirmPassword = true;
    }
};

// 8. Función para activar el botón de envío
const activarBoton = () => {
    // Verificamos si TODOS los valores en el objeto "validaciones" son verdaderos
    const formularioValido = Object.values(validaciones).every(valor => valor === true);
    
    if (formularioValido) {
        btnSubmit.disabled = false; // Habilitar
    } else {
        btnSubmit.disabled = true; // Deshabilitar
    }
};

// 9. Reiniciar formulario
btnReset.addEventListener('click', () => {
    formulario.reset();
    // Limpiar clases y mensajes
    inputs.forEach(input => {
        input.classList.remove('correcto');
        input.classList.remove('incorrecto');
    });
    document.querySelectorAll('.error-msg').forEach(msg => msg.textContent = '');
    
    // Reiniciar objeto de validación
    Object.keys(validaciones).forEach(key => validaciones[key] = false);
    activarBoton();
});

// Event Listeners para cada input
inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario); // Al soltar tecla
    input.addEventListener('blur', validarFormulario);  // Al salir del campo
});

// Envio del formulario
formulario.addEventListener('submit', (e) => {
    e.preventDefault(); // Evita que se recargue la página
    if(!btnSubmit.disabled) {
        alert("¡Formulario enviado con éxito!");
        // Aquí iría el código para enviar al servidor
    }
});

// Helper para poner mayúscula la primera letra (para buscar IDs)
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}