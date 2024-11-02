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

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        locale: "pt-br",
        headerToolbar: {
            left: "prev,next today",
            center: "title",
            right: "dayGridMonth,timeGridWeek,timeGridDay"
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
    });

    calendar.render();
});