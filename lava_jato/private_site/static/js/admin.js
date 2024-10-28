function toggleMenu() {
    const sidebar = document.getElementById("sidebar");
    const mainContent = document.getElementById("main-content");

    // Alterna a classe 'collapsed' no menu e conteúdo principal
    sidebar.classList.toggle("collapsed");
    mainContent.classList.toggle("collapsed");
}

document.addEventListener("DOMContentLoaded", function() {
    const toggleButtonSVG = document.getElementById("toggle-btn-svg");
    const toggleButton = document.getElementById("toggle-btn");
    const sidebar = document.getElementById("sidebar");

    const arrow_left = toggleButtonSVG.getAttribute("arrow-left");
    const arrow_right = toggleButtonSVG.getAttribute("arrow-right");

    toggleButton.addEventListener("click", function() {
        sidebar.classList.toggle("active");

        // Alterna a direção da seta
        if (sidebar.classList.contains("active")) 
        {
            toggleButtonSVG.src = arrow_right; // seta apontando para a direita
        } else 
        {
            toggleButtonSVG.src = arrow_left; // seta apontando para a esquerda
        }
    });
});