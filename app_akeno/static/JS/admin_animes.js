function toggleMenu() {
    const panel = document.querySelector('.panel-derecho');
    panel.classList.toggle('colapsado');
}

function toggleBusqueda() {
    const panel = document.getElementById('busquedaPanel');
    panel.classList.toggle('oculto');
}

function toggleFiltroEtiquetas() {
    const lista = document.getElementById('etiquetasLista');
    lista.classList.toggle('oculto');
}

function toggleModoOscuro() {
    document.body.classList.toggle('modo-oscuro');
}
// admin_animes.js

// al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    // capturo el botón hamburguesa y el panel
    const btnHamb = document.querySelector('.icono.hamburguesa');
    const panel   = document.querySelector('.panel-derecho');
    btnHamb.addEventListener('click', () => {
        panel.classList.toggle('colapsado');
    });
});
