from django.db import models

from .agendamento import Agendamento
from .cliente import Cliente
from .tipo_servico import TipoServico
from.tipo_veiculo import TipoVeiculo

class Servico(models.Model):
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_servico = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    tipo_veiculo = models.ForeignKey(TipoVeiculo, on_delete=models.CASCADE)
    mensagem = models.TextField(null=True, blank=True)
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Serviço {self.id} para {self.cliente.nome} \
            com agendamento {self.agendamento.id}"
    
    class Meta:
        app_label = 'mysql'