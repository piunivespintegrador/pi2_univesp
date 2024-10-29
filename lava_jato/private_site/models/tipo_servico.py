from django.db import models

class TipoServico(models.Model):
    tipo_servico = models.CharField(max_length=100)
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo_servico

    class Meta:
        app_label = 'mysql'