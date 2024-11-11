const csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

function moneyFormat(input) {
    let valor = input.value.replace(/\D/g, ''); // Remove qualquer coisa que não seja número
    valor = (valor / 100).toFixed(2) + ''; // Converte para formato decimal
    valor = valor.replace('.', ','); // Substitui o ponto por vírgula
    valor = valor.replace(/(\d)(\d{3})(\d{2}$)/, '$1.$2,$3'); // Adiciona o ponto e a vírgula
    input.value = valor;
}

function removerDisabled(element) {
    const defaultOption = element.querySelector('option[value=""]');

    // Remove o atributo 'disabled' quando o usuário faz uma escolha
    if (defaultOption && element.value !== "") {
        defaultOption.remove();
    }
}

function calculateServiceValue(element) {
    const selectedOption = element.options[element.selectedIndex];
    const selectedPrice = selectedOption.getAttribute('price');;
    const servicePriceInput = document.getElementById('valor-servico');
    servicePriceInput.value = selectedPrice;
    moneyFormat(servicePriceInput)
}

function Reset(message)
{
    document.getElementById('result').textContent = '';
    document.getElementById('result').style.color = '';
}

function Fail(message)
{
    document.getElementById('result').textContent = message;
    document.getElementById('result').style.color = 'red';
}

function Warning(message)
{
    document.getElementById('result').textContent = message;
    document.getElementById('result').style.color = '#eed202';
}

function Success(message)
{
    document.getElementById('result').textContent = message;
    document.getElementById('result').style.color = 'green';
}

document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário

    Reset();

    submitForm(new FormData(this));
});

function submitForm(formData)
{
    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    let request_uri = document.getElementById('registerForm').action

    console.log(data);

    // Envia os dados via AJAX (usando fetch)
    fetch(request_uri, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(data)  // Envia os dados coletados no FormData
    })
    .then(response => response.json())  // Aqui você pode ajustar a resposta de acordo com sua view
    .then(data => {
        // Trate a resposta aqui, por exemplo, mostre uma mensagem de sucesso
        console.info(data);

        if(data.warning)
            Warning(data.message);
        else if(data.success)
            Success(data.message);
        else
            Fail(data.message);
    })
    .catch(error => {
        Fail('Erro ao cadastrar o Tipo Serviço.');

        console.error('Error:', error);
    });
}