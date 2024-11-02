let cliente_id = null;

// Função para abrir o modal e definir o ID do cliente a ser excluído
function confirmDeleteCustomer(id) {
    cliente_id = id;
    document.getElementById('modelConfirmMessage').innerText = "Tem certeza que deseja excluir o cliente " + cliente_id + " ?"
    document.getElementById('modelConfirm').style.display = 'flex';
}

// Função para fechar o modal
function closeModal() {
    document.getElementById('modelConfirm').style.display = 'none';
    cliente_id = null;
}

function alertMessage(message) {
    document.getElementById('modelAlertMessage').innerText = message;
    document.getElementById('modelAlert').style.display = 'flex';
}

// Função para fechar o modal
function closeAlertModal() {
    document.getElementById('modelAlert').style.display = 'none';
}

// Função para excluir o cliente usando AJAX
function deleteCustomer() {
    if (cliente_id) {
        fetch(`/admin/customer/delete_customer/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'  // Inclui o token CSRF para segurança
            },
            body: JSON.stringify({ id: cliente_id })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Remover a linha da tabela
                const row = document.getElementById('cliente-' + cliente_id);
                row.parentNode.removeChild(row);
                alertMessage(data.message);
            } else {
                alertMessage(data.message);
            }
            closeModal();
        })
        .catch(error => {
            console.error('Error:', error);
            alertMessage('Erro ao tentar excluir o cliente ' + cliente_id + '.');
            closeModal();
        });
    }
}