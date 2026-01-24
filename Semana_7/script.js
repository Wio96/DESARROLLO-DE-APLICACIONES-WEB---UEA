// 1. LOS DATOS (Simulación de Base de Datos)
// El PDF menciona que la lógica obtiene una colección de datos[cite: 1350].
const productos = [
    { nombre: "Laptop Gamer", precio: 1200, descripcion: "Procesador i7, 16GB RAM, RTX 3060." },
    { nombre: "Mouse Inalámbrico", precio: 25, descripcion: "Ergonómico con batería de larga duración." },
    { nombre: "Teclado Mecánico", precio: 80, descripcion: "Luces RGB y switches azules." }
];

// 2. REFERENCIAS AL DOM
const contenedorLista = document.getElementById('lista-productos');
const btnAgregar = document.getElementById('btn-agregar');

// 3. FUNCIÓN DE RENDERIZADO (El "Motor de Plantillas")
function renderizarLista() {
    // Limpiamos el contenedor para evitar duplicados al actualizar
    contenedorLista.innerHTML = '';

    // El PDF indica que la plantilla itera sobre los datos usando bucles [cite: 1354]
    productos.forEach(producto => {
        
        // --- DEFINICIÓN DE LA PLANTILLA ---
        // Usamos Template Literals (``) que funcionan como los marcadores {{ }} mencionados en el PDF [cite: 1194]
        const plantilla = `
            <li class="producto-card">
                <div>
                    <span class="producto-nombre">${producto.nombre}</span>
                    <span class="producto-precio">$${producto.precio}</span>
                </div>
                <p class="producto-desc">${producto.descripcion}</p>
            </li>
        `;
        
        // Inyectamos la plantilla renderizada en el DOM
        contenedorLista.innerHTML += plantilla;
    });
}

// 4. FUNCIONALIDAD PARA AGREGAR (Interacción Dinámica)
// El PDF menciona que la interacción puede reiniciar el ciclo para renderizar nuevas plantillas[cite: 1300].
function agregarProducto() {
    // Datos de ejemplo para el nuevo producto
    const nuevo = {
        nombre: "Monitor 24 pulgadas",
        precio: 180,
        descripcion: "Full HD, 144Hz, ideal para gaming."
    };

    // Agregamos al arreglo de datos
    productos.push(nuevo);

    // Volvemos a renderizar para reflejar los cambios
    renderizarLista();
    
    // Feedback visual
    alert(`Se agregó: ${nuevo.nombre}`);
}

// 5. INICIALIZACIÓN
// Renderizamos la lista apenas carga la página
renderizarLista();

// Escuchamos el evento click
btnAgregar.addEventListener('click', agregarProducto);