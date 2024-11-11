const csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

let type_vehicle_id = null;

// Função para abrir o modal e definir o ID do cliente a ser excluído
function confirmDeleteTypeVehicle(id) {
    type_vehicle_id = id;
    document.getElementById('modelConfirmMessage').innerText = "Tem certeza que deseja excluir o tipo veiculo " + type_vehicle_id + " ?"
    document.getElementById('modelConfirm').style.display = 'flex';
}

// Função para fechar o modal
function closeModal() {
    document.getElementById('modelConfirm').style.display = 'none';
    type_vehicle_id = null;
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
function deleteTypeVehicle() {
    if (type_vehicle_id) {
        fetch(`/admin/type_vehicle/delete_type_vehicle/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token  // Inclui o token CSRF para segurança
            },
            body: JSON.stringify({ id: type_vehicle_id })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Remover a linha da tabela
                const row = document.getElementById('type-vehicle-' + type_vehicle_id);
                row.parentNode.removeChild(row);
                alertMessage(data.message);
            } else {
                alertMessage(data.message);
            }

            closeModal();
        })
        .catch(error => {
            alertMessage('Erro ao tentar excluir o tipo veiculo ' + type_vehicle_id + '.');
            closeModal();

            console.error('Error:', error);
        });
    }
}