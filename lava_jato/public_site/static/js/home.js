// Função para exibir ou ocultar a resposta
function toggleAnswer(faqItem) {
    const answer = faqItem.querySelector('.answer');
    const isVisible = answer.style.display === 'block';
    
    // Oculta todas as respostas
    document.querySelectorAll('.answer').forEach(answer => answer.style.display = 'none');

    // Exibe ou oculta a resposta clicada
    answer.style.display = isVisible ? 'none' : 'block';
}