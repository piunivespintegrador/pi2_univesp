let service_id = null;

// Função para abrir o modal e definir o ID do cliente a ser excluído
function confirmDeleteService(id) {
    service_id = id;
    document.getElementById('modelConfirmMessage').innerText = "Tem certeza que deseja excluir o serviço " + service_id + " ?"
    document.getElementById('modelConfirm').style.display = 'flex';
}

// Função para fechar o modal
function closeModal() {
    document.getElementById('modelConfirm').style.display = 'none';
    service_id = null;
}

function alertMessage(message) {
    document.getElementById('modelAlertMessage').innerText = message;
    document.getElementById('modelAlert').style.display = 'flex';
}

// Função para fechar o modal
function closeAlertModal() {
    document.getElementById('modelAlert').style.display = 'none';
}

// Função para excluir o serviço usando AJAX
function deleteService() {
    if (service_id) {
        fetch(`/admin/service/delete_service/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'  // Inclui o token CSRF para segurança
            },
            body: JSON.stringify({ id: service_id })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Remover a linha da tabela
                const row = document.getElementById('service-' + service_id);
                row.parentNode.removeChild(row);
                alertMessage(data.message);
            } else {
                alertMessage(data.message);
            }
            closeModal();
        })
        .catch(error => {
            console.error('Error:', error);
            alertMessage('Erro ao tentar excluir o serviço ' + service_id + '.');
            closeModal();
        });
    }
}