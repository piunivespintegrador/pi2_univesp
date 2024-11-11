const csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

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

    // Validação aqui

    let result = submitForm(new FormData(this));

    if(!result) return;
});

function submitForm(formData)
{
    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    let request_uri = document.getElementById('registerForm').action

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

        return true;
    })
    .catch(error => {
        console.error('Error:', error);
        Fail('Erro ao cadastrar o Tipo Veículo.');
        return false;
    });
}