// Função para exibir ou ocultar a resposta
function toggleAnswer(faqItem) {
    const answer = faqItem.querySelector('.answer');
    const isVisible = answer.style.display === 'block';
    
    // Oculta todas as respostas
    document.querySelectorAll('.answer').forEach(answer => answer.style.display = 'none');

    // Exibe ou oculta a resposta clicada
    answer.style.display = isVisible ? 'none' : 'block';
}

let currentIndex = 0;

function showNextImage() {
    const carouselContainer = document.querySelector('.carousel-container');
    const images = document.querySelectorAll('.carousel-image');
    currentIndex = (currentIndex + 1) % images.length;
    const offset = -currentIndex * 100; // Deslocamento de 100% para cada imagem
    carouselContainer.style.transform = `translateX(${offset}%)`;
}

// Mudar a imagem a cada 3 segundos
setInterval(showNextImage, 3000);