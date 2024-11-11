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
    document.getElementById('result').style.color = 'yellow';
}

function Success(message)
{
    document.getElementById('result').textContent = message;
    document.getElementById('result').style.color = 'green';
}

document.getElementById('schedulingForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário

    Reset();

    // Obtém os valores dos campos datetime-local
    var startDate = new Date(document.getElementById('start-data').value);
    var endDate = new Date(document.getElementById('end-data').value);

    // Verifica se o start é maior ou igual ao end, se for, exibe erro
    /*
    if (startDate >= endDate) {
        Fail('A data de início do serviço não pode ser maior que a data final do serviço!');
        return;
    }
    */

    let result = submitForm(new FormData(this));

    if(!result) return;
});

function submitForm(formData)
{
    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Envia os dados via AJAX (usando fetch)
    fetch(`/admin/scheduling/register_scheduling/`, {
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

        if(data.success)
            Success(data.message);
        else
            Fail(data.message);

        return true;
    })
    .catch(error => {
        console.error('Error:', error);
        Fail('Erro ao cadastrar o Agendamento.');
        return false;
    });
}