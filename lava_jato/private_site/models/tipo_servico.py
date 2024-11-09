from django.db import models

class TipoServico(models.Model):
    nome_servico = models.CharField(max_length=100)
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'tipo_servico'

    def __str__(self):
        return f"{self.nome_servico}"