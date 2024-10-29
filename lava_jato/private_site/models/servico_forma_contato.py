from django.db import models

from .servico import Servico
from .forma_contato import FormaContato

class ServicoFormaContato(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    forma_contato = models.ForeignKey(FormaContato, on_delete=models.CASCADE)

    class Meta:
        db_table = 'servico_forma_contato'

    def __str__(self):
        return f"Serviço {self.servico.id} - {self.forma_contato.forma_nome}"