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

document.addEventListener("DOMContentLoaded", function() {
    const calendarEl = document.getElementById("calendar");

    // Mock data para os agendamentos
    const schedules = [
        {
            title: "Reunião com cliente",
            start: "2024-11-05T10:00:00",
            end: "2024-11-05T11:30:00",
            description: "Discussão de projeto com cliente."
        },
        {
            title: "Serviço de Manutenção",
            start: "2024-11-10T14:00:00",
            end: "2024-11-10T15:30:00",
            description: "Manutenção preventiva no escritório."
        },
        {
            title: "Consultoria Técnica",
            start: "2024-11-15T09:00:00",
            end: "2024-11-15T10:00:00",
            description: "Consultoria técnica sobre novos sistemas."
        }
    ];

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
        events: schedules,
        eventClick: function(info) {
            // Exibe informações do serviço em um alerta
            alert(
                `Serviço: ${info.event.title}\n` +
                `Início: ${info.event.start.toLocaleString()}\n` +
                `Fim: ${info.event.end ? info.event.end.toLocaleString() : "N/A"}\n` +
                `Descrição: ${info.event.extendedProps.description}`
            );
        },
        dateClick: function(info) {
            console.log('Clicou na data: ' + info.dateStr);
        },
    });

    calendar.render();
});