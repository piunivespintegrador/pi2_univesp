from django.db import models

from .agendamento import Agendamento
from .cliente import Cliente
from .tipo_servico import TipoServico
from .tipo_veiculo import TipoVeiculo

class Servico(models.Model):
    agendamento = models.ForeignKey(Agendamento, null=True, on_delete=models.SET_NULL)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo_servico = models.ForeignKey(TipoServico, on_delete=models.PROTECT)
    tipo_veiculo = models.ForeignKey(TipoVeiculo, on_delete=models.PROTECT)
    mensagem = models.TextField(null=True, blank=True)
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'servico'

    def __str__(self):
        return f"Serviço {self.id} para {self.cliente.nome} com agendamento {self.agendamento.id} \
            Tipo do Serviço {self.tipo_servico.valor_servico} - Nome do Veículo {self.tipo_veiculo.id}"