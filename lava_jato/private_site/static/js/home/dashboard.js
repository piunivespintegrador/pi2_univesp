const csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

let calendar = null;

function showModelYear() {
    // obtem o ano que adiciona no input do year
    document.getElementById('yearInput').value = calendar.getDate().getFullYear();
    document.getElementById('modelYear').style.display = 'flex';
}

// Função para fechar o modal
function closeModal() {
    document.getElementById('modelYear').style.display = 'none';
}

function alertMessage(message) {
    document.getElementById('modelAlertMessage').innerText = message;
    document.getElementById('modelAlert').style.display = 'flex';
}

// Função para fechar o modal
function closeAlertModal() {
    document.getElementById('modelAlert').style.display = 'none';
}

function changeYear() {
    let year = document.getElementById('yearInput').value;

    // se já estiver o ano, ignora
    if(year == calendar.getDate().getFullYear()) {
        closeModal();
        return;
    }

    // faz a troca do ano se estiver dentro dos limites
    if (year && !isNaN(year) && year >= 1900 && year <= 2100) {
        // Navega para o primeiro dia do ano selecionado
        calendar.gotoDate(year + "-01-01");
        closeModal();
        return;
    }

    alertMessage("Por favor, insira um ano válido entre 1900 e 2100.");
}

function getCalendarServiceEvent(info, successCallback, failureCallback) {
    // Quando a visualização do calendário for carregada
    let data = {
        'start-data': info.start.toISOString(), // Data inicial do intervalo
        'end-data': info.end.toISOString(),     // Data final do intervalo
    }

    console.log('request:', data);

    // Envia os dados via AJAX (usando fetch)
    fetch('/admin/service/calendar_service_event/', {
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

        if(data.warning) {
            alertMessage(data.message);
            failureCallback(data.message);
            return;
        }
        else if(data.success) {
            successCallback(data.events);
            return;
        }

        alertMessage(data.message);
        failureCallback(data.message);
    })
    .catch(error => {
        alertMessage('Erro ao tentar receber informação dos eventos de agendamento dos serviço');
        failureCallback(error);

        console.error('Error:', error);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    const calendarEl = document.getElementById("calendar");

    calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        locale: "pt-br",
        headerToolbar: {
            left: "prev,next today",
            center: "title",
            right: "dayGridMonth,timeGridWeek,timeGridDay,yearSelect"
        },
        customButtons: {
            yearSelect: {
                text: 'select year',
                click: function() {
                    // Abre o modal
                    showModelYear();
                }
            }
        },
        events: function(info, successCallback, failureCallback) {
            // Chama a função separada para buscar os eventos
            getCalendarServiceEvent(info, successCallback, failureCallback);
        },
        eventClick: function(info) {
            // Exibe informações do serviço em um alerta
            alertMessage(
                `Serviço: ${info.event.title}\n` +
                `Início: ${info.event.start.toLocaleString()}\n` +
                `Fim: ${info.event.end ? info.event.end.toLocaleString() : "N/A"}\n` +
                `Descrição: ${info.event.extendedProps.description}`
            );
        }
    });

    calendar.render();
});