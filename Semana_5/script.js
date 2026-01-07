// 1. Selección de elementos del DOM [cite: 158, 192]
const inputUrl = document.getElementById('imgUrl');
const btnAgregar = document.getElementById('btnAgregar');
const btnEliminar = document.getElementById('btnEliminar');
const galeria = document.getElementById('galeria');

// 2. Función para agregar una nueva imagen
function agregarImagen() {
    const url = inputUrl.value.trim(); // Obtener el valor del input

    if (url === "") {
        alert("Por favor, escribe una URL válida.");
        return;
    }

    // Crear elemento dinámicamente [cite: 256, 257]
    const nuevaImagen = document.createElement('img');
    nuevaImagen.src = url; // Asignar atributo src [cite: 225]
    nuevaImagen.alt = "Imagen de galería";

    // Agregar evento de click a la NUEVA imagen para poder seleccionarla [cite: 333]
    nuevaImagen.addEventListener('click', function() {
        seleccionarImagen(nuevaImagen);
    });

    // Agregar la imagen al contenedor (DOM) [cite: 262]
    galeria.appendChild(nuevaImagen);

    // Limpiar el input
    inputUrl.value = "";
}

// 3. Función para seleccionar una imagen (Solo una a la vez)
function seleccionarImagen(imagenClickeada) {
    // Primero, quitamos la clase 'seleccionada' de TODAS las imágenes
    const imagenes = document.querySelectorAll('.gallery-grid img'); // [cite: 194]
    imagenes.forEach(img => {
        img.classList.remove('seleccionada'); // [cite: 227]
    });

    // Luego, se la agregamos solo a la que hicimos click
    imagenClickeada.classList.add('seleccionada');
}

// 4. Función para eliminar la imagen seleccionada
function eliminarImagen() {
    // Buscar la imagen que tenga la clase 'seleccionada' [cite: 190]
    const imagenSeleccionada = document.querySelector('.seleccionada');

    if (imagenSeleccionada) {
        imagenSeleccionada.remove(); // Eliminar del DOM [cite: 296]
    } else {
        alert("Primero selecciona una imagen haciendo clic sobre ella.");
    }
}

// 5. Asignación de Eventos Principales [cite: 309, 310]
btnAgregar.addEventListener('click', agregarImagen);
btnEliminar.addEventListener('click', eliminarImagen);

// Requisito Extra: Permitir agregar presionando "Enter" en el teclado [cite: 346]
inputUrl.addEventListener('keydown', (event) => {
    if (event.key === "Enter") {
        agregarImagen();
    }
});